import datetime

class Greeting:
    def __init__(self):
        pass
    
    def grtng(self):
        a = datetime.datetime.now()

        if (a.hour >= 0 and a.hour < 6):
            return "Good night"
        elif (a.hour >= 6 and a.hour < 12):
            return "Good morning"
        elif (a.hour >= 12 and a.hour < 18):
            return "Good day"
        else:
            return "Good evening"
                   
    def getName(self):
        print("Как к вам можно обратиться? Представьтесь: ")
        name = input()
        return name
    
    