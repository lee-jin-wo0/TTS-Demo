from TTS.api import TTS
import os

tts = TTS(model_name="tts_models/en/ljspeech/vits--neon", progress_bar=True, gpu=False)

text = "Hello! I'm now working with espeak-ng backend properly installed."
output_path = "output.wav"
tts.tts_to_file(text=text, file_path=output_path)

os.system(f'start {output_path}')
