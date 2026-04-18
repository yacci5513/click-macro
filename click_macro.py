#!/usr/bin/env python3
"""같은 화면 위치를 반복 클릭하는 매크로. Ctrl+C로 정지."""
import argparse
import random
import sys
import time

try:
    import pyautogui
except ImportError:
    sys.exit("pyautogui 미설치입니다. 설치: pip3 install pyautogui")


def main() -> None:
    ap = argparse.ArgumentParser(description="반복 클릭 매크로")
    ap.add_argument("--x", type=int, help="X 좌표 (생략 시 warmup 후 현재 마우스 위치)")
    ap.add_argument("--y", type=int, help="Y 좌표 (생략 시 warmup 후 현재 마우스 위치)")
    ap.add_argument("--interval", type=float, default=60.0,
                    help="클릭 간격(초). --interval-max와 같이 쓰면 최소값. 기본 60초")
    ap.add_argument("--interval-max", type=float, default=None,
                    help="지정 시 --interval ~ --interval-max 사이 랜덤 간격 적용")
    ap.add_argument("--warmup", type=float, default=3.0,
                    help="좌표 미지정 시 시작 전 대기 초. 기본 3초")
    ap.add_argument("--button", choices=["left", "right", "middle"], default="left")
    ap.add_argument("--clicks", type=int, default=1,
                    help="한 회차에 연속 클릭할 횟수. 2면 더블클릭처럼 동작. 기본 1")
    ap.add_argument("--click-interval", type=float, default=0.1,
                    help="--clicks가 2 이상일 때 클릭 사이 간격(초). 기본 0.1")
    args = ap.parse_args()

    if args.clicks < 1:
        sys.exit("--clicks는 1 이상이어야 합니다.")

    if args.interval_max is not None and args.interval_max < args.interval:
        sys.exit(f"--interval-max({args.interval_max})는 --interval({args.interval})보다 크거나 같아야 합니다.")

    pyautogui.FAILSAFE = True

    if args.x is None or args.y is None:
        print(f"{args.warmup}초 후 현재 마우스 위치를 기준으로 시작합니다. 커서를 옮겨두세요.")
        time.sleep(args.warmup)
        x, y = pyautogui.position()
    else:
        x, y = args.x, args.y

    if args.interval_max is not None:
        interval_desc = f"{args.interval}~{args.interval_max}s (랜덤)"
    else:
        interval_desc = f"{args.interval}s"
    clicks_desc = f"{args.clicks}회{' 연속' if args.clicks > 1 else ''}"
    print(f"클릭 위치: ({x}, {y}) | 간격: {interval_desc} | 버튼: {args.button} | 1회차당 {clicks_desc}")
    print("정지: Ctrl+C  |  긴급 정지: 마우스를 화면 좌상단 구석으로 이동 (FAILSAFE)")

    count = 0
    try:
        while True:
            pyautogui.click(x=x, y=y, button=args.button,
                            clicks=args.clicks, interval=args.click_interval)
            count += 1
            if args.interval_max is not None:
                wait = random.uniform(args.interval, args.interval_max)
            else:
                wait = args.interval
            print(f"  클릭 #{count} @ {time.strftime('%H:%M:%S')} (다음까지 {wait:.1f}s)")
            time.sleep(wait)
    except KeyboardInterrupt:
        print(f"\n총 {count}회 클릭 후 종료.")
    except pyautogui.FailSafeException:
        print(f"\nFAILSAFE 작동. 총 {count}회 클릭 후 종료.")


if __name__ == "__main__":
    main()
