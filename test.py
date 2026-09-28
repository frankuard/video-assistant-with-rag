from utils.audio_processor import process_input
from core.transcriber import transcribe_all

source = "https://www.youtube.com/watch?v=RU5u7aQTIrU"


chunks = process_input(source)

transcript = transcribe_all(chunks)

print(transcript)
