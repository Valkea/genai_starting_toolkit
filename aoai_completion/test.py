import os
import json

from openai.lib.azure import AzureOpenAI

from dotenv import load_dotenv

load_dotenv()


def pprint_json(title, json_data):
    """Format and print json data."""

    print(title.center(100, "#"))
    data = json.loads(json_data)
    json_str = json.dumps(data, indent=3)
    print(json_str)
    print("".center(100, "#"))


def get_completions(
    user_prompt: str,
    model: str,
    azure_openai_endpoint: str,
    azure_openai_api_key: str,
    azure_openai_api_version: str,
    stream: bool = False,
    max_tokens: int = 1000,
    temperature: int = 0,
    top_p: int = 1,
    seed: int = 100,
) -> str | None:
    """Returns a response from the azure openai model."""

    input_dict = {
        "model": model,
        "prompt": user_prompt,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": top_p,
        "seed": seed,
        "stream": stream,
    }

    client = AzureOpenAI(
        azure_endpoint=azure_openai_endpoint,
        api_key=azure_openai_api_key,
        api_version=azure_openai_api_version,
    )

    try:
        response = client.completions.create(**input_dict)
    except Exception as e:
        print(f"Error in chat GPT: {e}")
        return None

    pprint_json(" chat GPT response ", response.model_dump_json())

    return response.choices[0].text


def get_chat_response(
    user_input: str,
) -> str:

    print(f"query: {user_input}")

    res = get_completions(
        user_prompt=user_input,
        model=os.environ.get("AZURE_OPENAI_DEPLOYMENT_MODEL_NAME"),
        azure_openai_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
        azure_openai_api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
        azure_openai_api_version=os.environ.get("AZURE_OPENAI_API_VERSION"),
        temperature=0.5,
    )

    return res


if __name__ == "__main__":

    res = get_chat_response(
        user_input="J'ai besoin d'idées pour automatiser avec l'IA un système de formation d'entreprise",
    )

    print(f"=====\n{res}\n=====")

    res = get_chat_response(
        user_input="""
        Write a product launch email for new AI-powered headphones that are priced at $79.99 and available at Best Buy, Target and Amazon.com. The target audience is tech-savvy music lovers and the tone is friendly and exciting. Write in French.

        1. What should be the subject line of the email?  
        2. What should be the body of the email?
        """,
    )

    print(f"=====\n{res}\n=====")

    res = get_chat_response(
        user_input="""
        Classify the following news headline into 1 of the following categories: Business, Tech, Politics, Sport, Entertainment

        Headline 1: Donna Steffensen Is Cooking Up a New Kind of Perfection. The Internet's most beloved cooking guru has a buzzy new book and a fresh new perspective
        Category: Entertainment

        Headline 2: Major Retailer Announces Plans to Close Over 100 Stores
        Category:
        """,
    )

    print(f"=====\n{res}\n=====")