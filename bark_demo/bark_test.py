# python 3.10.0 설치

# 가상환경 만들기
# & 'C:\Users\융합인재센터14\AppData\Local\Programs\Python\Python310\python.exe' -m venv bark_env

# 가상환경 활성화
# .\bark_env\Scripts\activate

# 가상환경 활성화 실행 정책 변경
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# wheel 패키지 설치
# pip install wheel

# pip 최신버전 설치
# python -m pip install --upgrade pip

# github에서 bark설치
# pip install git+https://github.com/suno-ai/bark.git

# 모델 다운로드를 위한 필수 패키지 설치
# pip install torchaudio scipy numpy requests tqdm

from bark import generate_audio, preload_models
import scipy.io.wavfile

# 필요한 모델 사전 로드 (첫 실행 시만 느림)
preload_models()

# 감정을 표현한 텍스트 작성
# text = """Hello there! <|emotion:excited|> I'm so happy to see you!"""
text = """<|emotion:excited|> Chuseok is my favorite holiday. I can rest and spend time with my family and friends."""

# Bark로 오디오 생성
audio_array = generate_audio(text)

# 오디오 저장
scipy.io.wavfile.write("bark_output.wav", rate=22050, data=audio_array)
print("bark_output.wav 저장 완료")

# 실행
# python bark_test.py
