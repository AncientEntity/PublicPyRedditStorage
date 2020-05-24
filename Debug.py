import datetime

def Log(message):
    print("[" + str(datetime.datetime.utcnow()) + "] " +message)
