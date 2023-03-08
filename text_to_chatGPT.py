import openai


openai.api_key = "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"
model_engine = "text-davinci-003"

# задаем макс кол-во слов
max_tokens = 128


def chat_with_gpt(prompt):
    completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    temperature=0.5,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return completion.choices[0].text

while True:
    print(chat_with_gpt(input()),'\n')