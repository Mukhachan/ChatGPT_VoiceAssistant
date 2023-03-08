import speech_recognition as sr
import openai
from gtts import gTTS
import os


openai.api_key = "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"

model_engine = "text-davinci-003"

# задаем макс кол-во слов
max_tokens = 128

def speak(text):
    print(text)
    # создаем объект gTTS с входным текстом
    audio = gTTS(text=text, lang='ru', slow=False)

    # сохраняем аудиофайл во временный файл
    audio_file = 'speech.mp3'
    audio.save(audio_file)

    # воспроизводим аудиофайл через системный плеер
    os.system('mpg123 ' + audio_file)

    # удаляем временный файл
    os.remove(audio_file)


def chat_with_gpt(prompt):
    completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=2048,
    temperature=0.5,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    
    return speak(completion.choices[0].text)


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
            chat_with_gpt(text)
            recognize()

    except sr.UnknownValueError:
        print("Не удалось распознать речь")
    except sr.RequestError as e:
        print("Ошибка запроса веб-службы: {0}".format(e))

if __name__ == '__main__':
    # Вызов функции распознавания
    recognize()

