# click-macro

같은 화면 위치를 일정 간격으로 반복 클릭하는 간단한 macOS/Linux/Windows용 매크로.

## 요구 사항

- Python 3.8+
- [pyautogui](https://pyautogui.readthedocs.io/)

```bash
pip3 install pyautogui
```

macOS의 경우 *시스템 설정 → 개인정보 보호 및 보안 → 손쉬운 사용(Accessibility)* 에서 스크립트를 실행하는 터미널(Terminal.app / iTerm2 등)에 권한을 부여해야 클릭이 동작합니다.

## 사용법

```bash
# 3초 후 현재 마우스 위치를 기준으로 60초마다 반복 클릭 (기본값)
python3 click_macro.py

# 간격 10초
python3 click_macro.py --interval 10

# 좌표 직접 지정
python3 click_macro.py --x 500 --y 300 --interval 30

# 우클릭
python3 click_macro.py --interval 5 --button right
```

### 옵션

| 옵션 | 기본값 | 설명 |
|------|-------|------|
| `--x`, `--y` | 현재 커서 위치 | 클릭할 화면 좌표 |
| `--interval` | `60.0` | 클릭 사이 대기 시간(초) |
| `--warmup` | `3.0` | 좌표 미지정 시 시작 전 대기 시간(초) |
| `--button` | `left` | 마우스 버튼 (`left` / `right` / `middle`) |

## 정지 방법

- **Ctrl+C** — 터미널에서 중단
- **FAILSAFE** — 마우스를 화면 좌상단 구석으로 빠르게 이동하면 자동 종료

## 라이선스

MIT
