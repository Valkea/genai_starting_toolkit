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
    messages: list,
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
        "messages": messages,
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
        response = client.chat.completions.create(**input_dict)
    except Exception as e:
        print(f"Error in chat GPT: {e}")
        return None

    pprint_json(" chat GPT response ", response.model_dump_json())

    return response.choices[0].message.content


def get_chat_response(
    user_input: str,
    system_prompt: str,
    history: list = [],
) -> str:

    print(f"query: {user_input}")

    user_request = {
        "role": "user",
        "content": f"Answer the following question in less than 200 characters: {user_input}",
    }

    if len(history) == 0:
        history.append({"role": "system", "content": f"{system_prompt}"})

    history.append(user_request)

    pprint_json(" chat history ", json.dumps(history))

    res = get_completions(
        messages=history,
        model=os.environ.get("AZURE_OPENAI_DEPLOYMENT_MODEL_NAME"),
        azure_openai_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
        azure_openai_api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
        azure_openai_api_version=os.environ.get("AZURE_OPENAI_API_VERSION"),
    )

    history[-1]["content"] = user_input
    assistant_answer = {
        "role": "assistant",
        "content": res,
    }
    history.append(assistant_answer)

    return res


if __name__ == "__main__":

    system_prompt = """
    - You are a marketing writing assistant. 
    - You help come up with creative content ideas and content like marketing emails, blog posts, tweets, ad copy and product descriptions. 
    - You write in a friendly yet professional tone but can tailor your writing style that best works for a user-specified audience. 
    - If you do not know the answer to a question, respond by saying 'I do not know the answer to your question.'
    """

    # system_prompt="""
    # •	You are an IRS chatbot whose primary goal is to help users with filing their tax returns for the 2022 year.
    # •	Provide concise replies that are polite and professional.
    # •	Answer questions truthfully based on official government information, with consideration to context provided below on changes for 2022 that can affect tax refund.
    # •	Do not answer questions that are not related to United States tax procedures and respond with "I can only help with any tax-related questions you may have.".
    # •	If you do not know the answer to a question, respond by saying “I do not know the answer to your question. You may be able to find your answer at www.irs.gov/faqs”

    # Changes for 2022 that can affect tax refund:
    # •	Changes in the number of dependents, employment or self-employment income and divorce, among other factors, may affect your tax-filing status and refund. No additional stimulus payments. Unlike 2020 and 2021, there were no new stimulus payments for 2022 so taxpayers should not expect to get an additional payment.
    # •	Some tax credits return to 2019 levels.  This means that taxpayers will likely receive a significantly smaller refund compared with the previous tax year. Changes include amounts for the Child Tax Credit (CTC), the Earned Income Tax Credit (EITC) and the Child and Dependent Care Credit will revert to pre-COVID levels.
    # •	For 2022, the CTC is worth $2,000 for each qualifying child. A child must be under age 17 at the end of 2022 to be a qualifying child.For the EITC, eligible taxpayers with no children will get $560 for the 2022 tax year.The Child and Dependent Care Credit returns to a maximum of $2,100 in 2022.
    # •	No above-the-line charitable deductions. During COVID, taxpayers were able to take up to a $600 charitable donation tax deduction on their tax returns. However, for tax year 2022, taxpayers who don’t itemize and who take the standard deduction, won’t be able to deduct their charitable contributions.
    # •	More people may be eligible for the Premium Tax Credit. For tax year 2022, taxpayers may qualify for temporarily expanded eligibility for the premium tax credit.
    # •	Eligibility rules changed to claim a tax credit for clean vehicles. Review the changes under the Inflation Reduction Act of 2022 to qualify for a Clean Vehicle Credit.
    # """

    res = get_chat_response(
        user_input="J'ai besoin d'idées pour automatiser avec l'IA yun système de formation d'entreprise",
        system_prompt=system_prompt,
    )

    print(f"=====\n{res}\n=====")

    res = get_chat_response(
        user_input="Peux tu développer ?",
        system_prompt=system_prompt,
    )

    print(f"=====\n{res}\n=====")

    res = get_chat_response(
        user_input="Liste moi 5 autres idées",
        system_prompt=system_prompt,
    )

    print(f"=====\n{res}\n=====")
