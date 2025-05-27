# 🔊 coqui-demo
Python 기반으로 Coqui TTS를 테스트하고 있음음

## ✅ 사용 기술
- Python 3.10  
- [Coqui TTS](https://github.com/coqui-ai/TTS)  
- 사용 모델: `tts_models/en/ljspeech/vits--neon`  
- 음성 합성 시 `espeak-ng` 백엔드 사용

## 🚀 실행 방법
1. Python 3.10 가상환경 생성
2. 필요한 패키지 설치:
    1) 가상환경 만들기
    `& 'C:\Users\융합인재센터14\AppData\Local\Programs\Python\Python310\python.exe' -m venv coqui_env`
    2) 가상환경 활성화
    `.\coqui_env\Scripts\activate`
    3) 가상환경 활성화 실행 정책 변경
    `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`
    4) wheel 패키지 설치
    `pip install wheel`
    5) pip 최신버전 설치
    `python -m pip install --upgrade pip`
    6) Coqui TTS 설치
    `pip install TTS`
    7) 음성 생성 모델 실행에 필요한 패키지 설치 (espeak-ng 기반 모델의 경우)
    `espeak-ng 설치 -> https://github.com/espeak-ng/espeak-ng/releases (MSI 설치 후 환경변수 등록 필요)`
    8) 설치 확인 명령어
    `espeak-ng --version`
3. 테스트 코드 실행
`python coqui_test.py`