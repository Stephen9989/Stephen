import time
from datetime import datetime

def run_bot():
    print("🚀 Trading bot started...")
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] Bot running smoothly...")
        time.sleep(5)

if __name__ == "__main__":
    run_bot()
