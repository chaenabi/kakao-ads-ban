import pyautogui as auto
import time
from threading import Thread
from pynput import keyboard

def ban(x, y):
    auto.moveTo(x - 80, y - 10)
    auto.click()
    xx, yy = auto.locateCenterOnScreen('ban.png', grayscale=False, confidence=.5)
    auto.moveTo(xx, yy)
    auto.click()
    auto.moveTo(xx - 40, yy, duration=0.2)
    auto.click()
    xx, yy = auto.locateCenterOnScreen('confirm.png', grayscale=False, confidence=.5)
    auto.moveTo(xx, yy)
    auto.click()

def remove_link(x, y):
    auto.moveTo(x, y)
    auto.rightClick()
    auto.moveTo(x+10, y+235)
    auto.moveTo(x+130, y+235, duration=0.2)
    auto.click()

    x, y = auto.locateCenterOnScreen('confirm.png', grayscale=False, confidence=.5)
    auto.moveTo(x, y)
    auto.click()

def exit_program():
    def on_press(key):
        if str(key) == 'Key.esc':
            main.status = 'pause'
            user_input = input('프로그램이 중지되었습니다. 재가동하시겠습니까? (y/n) ')

            while user_input != 'y' and user_input != 'n':
                user_input = input('올바르지 않은 입력입니다. y 혹은 n 를 입력해주세요.')

            if user_input == 'y':
                print('프로그램 재가동')
                main.status = 'run'
            elif user_input == 'n':
                print('프로그램이 종료됩니다.')
                main.status = 'exit'
                exit()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def execution():
    point = auto.locateCenterOnScreen('link.png', grayscale=False, confidence=.5)
    if point:
        x, y = point
        ban(x, y)
        remove_link(x, y)

def main():
    main.status = 'run'
    print('프로그램 가동됨')
    while True:
        execution()
        time.sleep(2)
        while main.status == 'pause':
            time.sleep(2)

        if main.status == 'exit':
            break

Thread(target=main).start()
Thread(target=exit_program).start()