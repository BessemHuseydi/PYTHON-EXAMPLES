import time
import pygame

def basit_zamanlayici(dakika, alarm_dosyasi):
    sure = dakika * 60
    while sure:
        mins, secs = divmod(sure, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(0.1)
        sure -= 1

    print("Zaman doldu! Alarm çalıyor...")
    pygame.mixer.init()
    pygame.mixer.music.load(alarm_dosyasi)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():  # Alarmın bitmesini bekle
        pygame.time.Clock().tick(10)

def main():
    dakika = input("Zamanlayıcı için süre (dakika cinsinden): ")
    alarm_dosyasi = 'alarm.mp3'  # Alarm ses dosyasının yolu

    try:
        dakika = int(dakika)
        basit_zamanlayici(dakika, alarm_dosyasi)
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    main()
