import whisper
import os 

whisper_model = os.getenv("WHISPER_MODEL","small")

_modle = None

def load_model():
    pass