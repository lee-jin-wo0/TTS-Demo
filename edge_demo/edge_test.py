import edge_tts
import asyncio

# 텍스트와 저장할 파일명
TEXT = "안녕하세요. 이것은 Microsoft Edge TTS 데모입니다."
VOICE = "ko-KR-SunHiNeural"  # 한국어 여성 음성
OUTPUT_FILE = "edge_output.mp3"

async def tts():
    communicate = edge_tts.Communicate(text=TEXT, voice=VOICE)
    await communicate.save(OUTPUT_FILE)

# 실행
asyncio.run(tts())
