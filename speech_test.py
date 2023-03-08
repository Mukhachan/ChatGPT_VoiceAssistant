import speech_recognition as sr

# Функция для распознавания голоса
def recognize():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Я слушаю...")
            audio = r.listen(source)
            text = r.recognize_google(audio, language="ru")
            print("Вы сказали: \n", text)        
            
        if 'робин' in text:
            print('Отправляю запрос ChatGPT')
            text = text.replace('робин', '', 1)

        if 'ты меня слышишь' in text:
            print("Слышу")

    except sr.UnknownValueError:
        print("Не удалось распознать речь")
    except sr.RequestError as e:
        print("Ошибка запроса веб-службы: {0}".format(e))

if __name__ == '__main__':
    # Вызов функции распознавания
    recognize()

