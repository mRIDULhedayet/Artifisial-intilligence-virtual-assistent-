from Body.Listen import MicExecution
from NeuralNetwork.NN import ReplyNN
# from NeuralNetwork.Qus import QuestionsAnswer


print(">> Starting : Wait For Some Seconds.")
from Body.Speak import Speak
from Featuers.Clap import Tester
from Featuers.Weakup import WakeupDetected
# from main import MainTaskExe
from Featuers.Open import OpenExe

print(">> Starting : Wait For Few Seconds More")


def MainExecution():
    Speak(" Hello Sir!")
    Speak(" I am your Personal Assistant Miki. How can I help you?")

    while True:
        Data = MicExecution()
        Data = str(Data).replace(".", "")

        # ValueReturn = MainTaskExe(Data)

        #  if ValueReturn is True:
        #    pass

        if len(Data) < 3:
            pass

       # elif "about" in Data:
         #   reply = QuestionsAnswer(Data)
         #   Speak(reply)

        else:
            Reply = ReplyNN(Data)
            Speak(Reply)
        TaskExe = str(Data).lower()
        OpenExe(Query=TaskExe)


# def MainTaskExe(Query):
# Task = str(Query).lower()
#  TaskNew = str(Query).lower()
#  if "open" in Query:
#      value = OpenExe(TaskNew)
#    return value


def SoundDetect():
    query: str = Tester() or WakeupDetected()

    if "True-Mic" in query:
        print("")
        print(">> SOUND DETECTED ! >>")
        print("")
        MainExecution()

    else:
        pass
