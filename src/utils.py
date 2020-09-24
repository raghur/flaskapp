import socket
import os

def gethostname():
    return socket.gethostname()

def getlocaladdress():
    return socket.gethostbyname(socket.gethostname())

def getEnvVar():
    return ("MESSAGE", os.getenv("MESSAGE", "NOT_SET"))
