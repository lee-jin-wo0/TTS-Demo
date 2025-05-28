import os
import sys
import scipy.io.wavfile

# 현재 디렉토리를 기준으로 bark 루트 모듈 경로 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
bark_root = os.path.join(current_dir, "bark")
sys.path.append(bark_root)

# bark 내부 함수 불러오기
from bark import SAMPLE_RATE, generate_audio

# 텍스트 입력
text_prompt = (
    "한글은 백성을 위한 글입니다. "
    "모든 사람이 쉽게 읽고 쓸 수 있도록 만들었습니다. "
    "지금 이 순간에도 우리는 함께 배우고, 나누며, 더 나은 세상을 만들어가고 있습니다. "
    "이제 여러분이 한글의 가치를 전해 주세요."
)

# 음성 생성
audio_array = generate_audio(text_prompt)

# 출력 경로 및 저장
output_path = os.path.join(current_dir, "bark_output.wav")
scipy.io.wavfile.write(output_path, SAMPLE_RATE, audio_array)

print(f"✅ 생성 완료: {output_path}")

