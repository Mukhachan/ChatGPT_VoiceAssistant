import speech_recognition as sr
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


# Функция для распознавания голоса
def recognize():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Я слушаю...")
            audio = r.listen(source)
            text = r.recognize_google(audio, language="ru")
            print("Вы сказали: \n", text)        
            
        if 'робин' in text.lower():
            print('Отправляю запрос ChatGPT')
            text = text.replace('робин', '', 1)
            print(chat_with_gpt(text))
            recognize()

    except sr.UnknownValueError:
        print("Не удалось распознать речь")
    except sr.RequestError as e:
        print("Ошибка запроса веб-службы: {0}".format(e))

if __name__ == '__main__':
    # Вызов функции распознавания
    recognize()

