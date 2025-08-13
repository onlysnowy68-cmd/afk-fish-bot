import time
import random

def afk_fish():
    print("🎣 Bot AFK Fishing mulai...")
    while True:
        # Simulasi lempar pancing
        print("Lempar pancing...")
        time.sleep(random.uniform(2, 5))  # tunggu beberapa detik

        # Simulasi tarik ikan
        print("Tarik ikan!")
        time.sleep(random.uniform(1, 3))  # jeda sebelum lempar lagi

if __name__ == "__main__":
    afk_fish()
