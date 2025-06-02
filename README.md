# 🗣️ TTS-Demo (Text-to-Speech Demo)

이 프로젝트는 감정을 표현할 수 있는 다양한 TTS(Text-to-Speech) 모델을 Python으로 실행하고 비교 실험하기 위한 데모 프로젝트입니다.  
각 폴더는 개별 TTS 엔진을 활용한 실습 코드와 실행 샘플을 포함합니다.

---

## 📁 폴더 구성

| 폴더명 | 설명 |
|--------|------|
| `bark_clone_demo/` | Bark 모델 클론 후 감정 음성 생성 실험용 버전 |
| `bark_demo/`       | Bark 모델을 활용한 기본 TTS 실습 |
| `coqui_demo/`      | Coqui TTS 오픈소스 기반 실습 |
| `edge_demo/`       | Microsoft Edge TTS API 기반 윈도우 전용 TTS |
| `gtts_demo/`       | Google Text-to-Speech (gTTS) API 기반 실습 |
| `pyttsx3_demo/`    | pyttsx3 기반 로컬 TTS (인터넷 연결 없이 작동) |

---

## 🔧 사용 기술

| 폴더명             | 사용 기술 / 라이브러리               | 특징 요약 |
|--------------------|---------------------------------------|------------|
| `gtts_demo/`       | [gTTS](https://pypi.org/project/gTTS/) | Google TTS API 기반의 간단한 온라인 음성 합성 |
| `pyttsx3_demo/`    | [pyttsx3](https://pypi.org/project/pyttsx3/) | 인터넷 없이 로컬에서 작동, 빠른 응답 속도 |
| `edge_demo/`       | Microsoft Edge TTS (WinRT API)         | 윈도우 내장 음성 엔진 사용, 다양한 목소리 제공 |
| `coqui_demo/`      | [Coqui TTS](https://github.com/coqui-ai/TTS) | 다양한 사전 학습 모델 제공, 커스터마이징 가능 |
| `bark_demo/`       | [Bark by Suno](https://github.com/suno-ai/bark) | 감정 표현에 특화된 고성능 TTS, 영어 중심 |
| `bark_clone_demo/` | Bark 전체 저장소를 클론하여 로컬에서 테스트 | 로컬 실행 최적화 및 고급 설정 가능 |
---

## 🎯 목적

- 다양한 TTS 엔진의 **음질**, **감정 표현력**, **속도**, **설치 난이도** 비교
- **감정 기반 응답 시스템** 개발 실험 (예: 동화 낭독, 인터랙티브 콘텐츠 등과 연계)
- **로컬 및 온라인 API 기반 모델** 모두 실습

---

## 🧪 비교 요약

| 엔진 (폴더 기준)     | 감정 표현            | 멀티언어 지원       | 설치 난이도 | 특이사항                                     |
|----------------------|----------------------|----------------------|--------------|----------------------------------------------|
| **gTTS (`gtts_demo`)**           | ❌                   | ✅                   | ★☆☆☆☆       | 온라인 Google API 기반, 간편함                   |
| **pyttsx3 (`pyttsx3_demo`)**     | ❌                   | ⚠️ 제한적            | ★☆☆☆☆       | 로컬 기반, 인터넷 불필요, 속도 빠름              |
| **Edge TTS (`edge_demo`)**       | ⚠️ 기본 톤 설정 가능 | ✅                   | ★☆☆☆☆       | Windows 한정, 다양한 목소리 선택 가능            |
| **Coqui TTS (`coqui_demo`)**     | ⚠️ 일부 지원         | ✅                   | ★★★☆☆       | 다양한 사전 학습 모델, 고품질 출력 가능         |
| **Bark (`bark_demo`)**           | ✅✅✅                | ⚠️ 제한적            | ★★★★☆       | 감정 풍부, 자연스러운 발음, 영어 중심            |
| **Bark Clone (`bark_clone_demo`)** | ✅✅✅                | ⚠️ 제한적            | ★★★★☆       | Bark 전체 저장소 직접 클론, 고급 커스터마이징 가능 |
---

## 📝 향후 계획

- **한국어 TTS 품질 비교**
- **감정 인식 + TTS 연동 실험**
- **음성 인터페이스 구축을 위한 통합 시스템 설계**