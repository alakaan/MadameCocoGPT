from openai import OpenAI
import json

def load_json(file_name):
    with open(file_name) as f:
        config = json.load(f)
    return config


def get_response_from_model(user_input,config):
    client = OpenAI(
        api_key=config["openai_api_key"],
        base_url=config["openai_api_base"],
    )

    chat = client.chat.completions.create(model="Qwen/Qwen3-8B",
                                         messages= [{"role": "user", "content": user_input}],
                                         temperature=0.2,
                                         stream = True)

    print("Completion result:", chat)

    return chat

