import sys
import keyboard
import pyautogui
from pywhatkit import misc
import webbrowser
from time import sleep
import wikipedia
import random


def OpenExe(Query):
    Query = str(Query).lower()

    if "visit" in Query:
        Nameofweb = Query.replace("visit", "")
        link = f"https://www.{Nameofweb}.com"
        webbrowser.open(link)
        return True

    if "hello" in Query:
        Query.replace("hello", "")
        random.choice(Query)
        return True

    elif "Search" in Query:
        misc.search(Query)
        return True

    elif 'wikipedia' in Query:
        Query = Query.replace("wikipedia", "")
        while True:
            Reply = wikipedia.summary(Query, sentences=2, auto_suggest=False)
            return Reply

    elif "open" in Query:
        Nameoftheapp = Query.replace("open", "")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(.5)
        return True

    elif "start" in Query:
        Nameoftheapp = Query.replace("open", "")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(.5)
        return True

    elif "launch" in Query:
        Nameoftheapp = Query.replace("open", "")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(.5)
        return True

    elif "bye" in Query:
        Query.replace("bye", "")
        random.choice(Query)
        sleep(1)
        sys.exit(Query)

    else:
        pass

#OpenExe("Open Google")
