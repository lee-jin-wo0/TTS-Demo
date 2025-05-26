from gtts import gTTS
import os

# 변환할 텍스트 입력
text = "안녕하세요. 저는 구글 텍스트 투 스피치입니다."
# 언어 설정: 한국어 = 'ko', 영어 = 'en'
tts = gTTS(text=text, lang='ko')

# 더 긴 문장 혹은 다른 언어도 가능
# text = "Hello, I am using Google Text to Speech in Python."
# tts = gTTS(text=text, lang='en')

# mp3 파일로 저장
tts.save("output.mp3")

# 저장된 mp3 파일 자동 실행 (운영체제에 따라 선택)
os_name = os.name
if os_name == "nt":  # Windows
    os.system("start output.mp3")
elif os_name == "posix":  # macOS or Linux
    os.system("afplay output.mp3")  # macOS인 경우
    # os.system("mpg123 output.mp3")  # Linux인 경우 mpg123 설치 필요