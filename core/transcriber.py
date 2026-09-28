import whisper
import os 

whisper_model = os.getenv("WHISPER_MODEL","small")

_model = None

def load_model():
    global _model

    if _model is None:
        print(f"Loading Model...")
        _model = whisper.load_model(whisper_model)
        print("Whisper model loaded successfully")
    
    return _model
