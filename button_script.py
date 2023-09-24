import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from PIL import Image, ImageDraw
import adafruit_ssd1306
import time

# Creates the i2c interface
i2c = busio.I2C(board.SCL, board.SDA)

# Creates the SSD1306 OLED class
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Input pins:
button_A = DigitalInOut(board.D5)
button_A.direction = Direction.INPUT
button_A.pull = Pull.UP

button_B = DigitalInOut(board.D6)
button_B.direction = Direction.INPUT
button_B.pull = Pull.UP

button_L = DigitalInOut(board.D27)
button_L.direction = Direction.INPUT
button_L.pull = Pull.UP

button_R = DigitalInOut(board.D23)
button_R.direction = Direction.INPUT
button_R.pull = Pull.UP

button_U = DigitalInOut(board.D17)
button_U.direction = Direction.INPUT
button_U.pull = Pull.UP

button_D = DigitalInOut(board.D22)
button_D.direction = Direction.INPUT
button_D.pull = Pull.UP

button_C = DigitalInOut(board.D4)
button_C.direction = Direction.INPUT
button_C.pull = Pull.UP

# Clear display
disp.fill(0)
disp.show()

# Test buttons and joystick


# if button_A.value:
#     print("Button A pressed and released")
# if button_B.value:
#     print("Button B pressed and released")
# if button_L.value:
#     print("Button L pressed and released")
# if button_R.value:
#     print("Button R pressed and released")
# if button_U.value:
#     print("Button U pressed and released")
# if button_D.value:
#     print("Button D pressed and released")
# if button_C.value:
#     print("Button C pressed and released")

try:
    while True:
        if not button_A.value:
            print("Button A input received")
            time.sleep(0.2)
        if not button_B.value:
            print("Button B input received")
            time.sleep(0.2)
        if not button_L.value:
            print("Button L input received")
            time.sleep(0.2)
        if not button_R.value:
            print("Button R input received")
            time.sleep(0.2)
        if not button_U.value:
            print("Button U input received")
            time.sleep(0.2)
        if not button_D.value:
            print("Button D input received")
            time.sleep(0.2)
        if not button_C.value:
            print("Button C input received")
            time.sleep(0.2)
except KeyboardInterrupt:
    pass
