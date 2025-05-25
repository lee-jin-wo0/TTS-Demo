# 🎤 bark-demo
Python 기반으로 Bark를 가상환경에서 테스트하고 있음.

## ✅ 사용 기술
- Python 3.10
- [Bark by Suno](https://github.com/suno-ai/bark) (텍스트 기반 감정 음성 생성)

## 🚀 실행 방법
1. Python 3.10 가상환경 생성
2. 필요한 패키지 설치:
    1) 가상환경 만들기
    `& 'C:\Users\융합인재센터14\AppData\Local\Programs\Python\Python310\python.exe' -m venv bark_env`
    2) 가상환경 활성화
    `.\bark_env\Scripts\activate`
    3) 가상환경 활성화 실행 정책 변경
    `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`
    4) wheel 패키지 설치
    `pip install wheel`
    5) pip 최신버전 설치
    `python -m pip install --upgrade pip`
    6) github에서 bark설치
    `pip install git+https://github.com/suno-ai/bark.git`
    7) 모델 다운로드를 위한 필수 패키지 설치
    `pip install torchaudio scipy numpy requests tqdm`
3. 실행
    `bark_test.py`