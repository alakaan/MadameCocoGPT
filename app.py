from utils import load_json
from utils import get_response_from_model
import streamlit as st

config = load_json('config.json')

# Код для удаления кнопки Deploy
st.markdown(
    r"""
    <style>
    .stDeployButton {
            visibility: hidden;
        }
    </style>
    """, unsafe_allow_html=True
)

st.sidebar.image('madame_coco_pink.jpg')

grid = [col for col in st.sidebar.columns(2)]

# with grid[0]:
#    st.image('uralitech_logo_ru.png')

st.sidebar.text("  ")

# полная чистка истории
def clear():
	if hasattr(st.session_state, 'messages'):
		del st.session_state.messages

# чистка ранних сообщений
def clear_first_messages(keep):
    del st.session_state.messages[0:-keep*2]



# Чат
with st.chat_message("assistant", avatar="🤖"):
    st.write(f'Добро пожаловать!')

if "messages" not in st.session_state:
    st.session_state.messages = []

# сохранение аватаров в чате
for message in st.session_state.messages:
    if message["role"] == "user":
        avatar = "🧑‍🎨"
    else:
        avatar = "🤖"

    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# ввод запроса пользователя
if prompt := st.chat_input("Введите запрос"):

    # добавляем запрос пользователя в историю
    st.session_state.messages.append({"role": "user",
                                      "content": prompt})

    # вывод запроса пользователя
    with st.chat_message("user", avatar="🧑‍🎨"):
        st.markdown(prompt)

    # вывод ответа системы

    with st.chat_message("assistant", avatar="🤖"):
        response = st.write_stream(get_response_from_model(config = config,
                                             user_input=prompt) )


    # добавление ответа в историю сообщений
    st.session_state.messages.append({"role": "assistant",
                                      "content": response})


st.sidebar.divider()

grid = [col for col in st.sidebar.columns(2)]
with grid[1]:
     container = st.container()
     container.button('Очистить чат', on_click=clear, use_container_width=True)



