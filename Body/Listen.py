import speech_recognition as sr
from googletrans import Translator


def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 5)

    try:
        # print("Recognizing...")
        query = r.recognize_google(audio, language="bn" or "en" or "hi")

    except:
        return ""

    query = str(query).lower()
    return query


# 2 - Translation

def TranslationBnToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text

    if len(data) < 3:
        pass
    else:
        print(f"You : {data}.")
    return data


# 3 - Connect

def MicExecution():
    query = Listen()
    data = TranslationBnToEng(query)
    return data


# MicExecution()
