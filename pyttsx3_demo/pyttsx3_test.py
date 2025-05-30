import pyttsx3
import os

# 엔진 초기화
engine = pyttsx3.init()

# 속도/볼륨 설정
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# 저장할 텍스트
text = "안녕하세요. 이것은 pyttsx3 데모 음성 파일입니다."

# 저장 경로 지정 (현재 디렉토리 내부)
output_path = os.path.join(os.getcwd(), "output.wav")

# 음성을 wav 파일로 저장
engine.save_to_file(text, output_path)

# 작업 완료 대기
engine.runAndWait()

print(f"✅ 파일 저장 완료: {output_path}")
