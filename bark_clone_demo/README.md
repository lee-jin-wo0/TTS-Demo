# 🎤 bark-clone-demo
Python 기반으로 Bark를 suno.ai github에서 clone하여 가상환경에서 테스트하고 있음.

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
    6) Github에서 Bark 저장소를 클론하여 로컬 실행 환경 구성  
    `git clone https://github.com/suno-ai/bark.git bark`
    7) 클론한 후 `bark` 디렉토리에 진입:   
    `cd bark` -> `pip install -e .`
    8) 모델 다운로드를 위한 필수 패키지 설치  
    `pip install torchaudio scipy numpy requests tqdm`
3. 실행 스크립트 작성  
    `bark_clone_demo` 폴더 하위에 `__main__.py` 파일 생성하여 코드 작성성
4. 실행 명령어  
    프로젝트 루트(`tts-demo`) 디렉토리에서 아래 명령어로 실행:
    `python -m bark_clone_demo`

> ⚠️ 참고:  
> - `__main__.py`가 `bark_clone_demo` 폴더에 있어야 `-m` 실행이 가능  
> - 상대 경로 import 오류를 피하기 위해 `sys.path.append()`로 `bark/bark` 디렉토리를 경로에 추가함  
> - 모델 로딩 오류 시 PyTorch `weights_only=False` 옵션 경고 주의. 반드시 신뢰된 모델만 사용할 것