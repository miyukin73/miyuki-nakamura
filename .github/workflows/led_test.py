#led_test.py
import led_class
from time import sleep

#インスタンス生成
LED=led_class.Led()

try:
    while True:
        LED.led_on()
        sleep(0.5)
        LED.led_off()
        sleep(0.5)

except KeyboardInterrupt:
    pass

cleanup()
