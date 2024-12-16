from settings import Settings
from utils.utils import *

import datetime
import time

def main():
    s = Settings()
    print(dict(s))
    driver = set_driver(s)
    keiro_setsubi(driver)
    kippu_select(driver)
    login(driver, s)
    kiyaku(driver)
    zaseki(driver)
    yoyaku(driver)
    t_delta = datetime.timedelta(hours=9)  # 9時間
    JST = datetime.timezone(t_delta, 'JST')
    print(datetime.datetime.now(JST))
    print("Enterを押して終了")
    while True:
        if keyboard.is_pressed("enter"):
            break


if __name__ == "__main__":
    main()

