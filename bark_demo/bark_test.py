from bark import generate_audio, preload_models
import scipy.io.wavfile

# 필요한 모델 사전 로드 (첫 실행 시만 느림)
preload_models()

# 감정을 표현한 텍스트 작성
text = """Hello there! <|emotion:excited|> I'm so happy to see you!"""

# Bark로 오디오 생성
audio_array = generate_audio(text)

# 오디오 저장
scipy.io.wavfile.write("bark_output.wav", rate=22050, data=audio_array)
print("bark_output.wav 저장 완료")