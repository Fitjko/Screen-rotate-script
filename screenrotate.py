from time import sleep
import pyautogui

pyautogui.click(x=100,y=300,button='right',)
x, y = pyautogui.locateCenterOnScreen("display.png",confidence=0.9)

# Function for moving and clicking improved readability
def moveToAndClick (a,b):
    pyautogui.moveTo(a, b)
    pyautogui.click()

moveToAndClick(x, y)

sleep(1)

z, w = pyautogui.locateCenterOnScreen("landscape_but.png",confidence=0.9)

moveToAndClick(z, w)

m, n = pyautogui.locateCenterOnScreen("portrait_but.png",confidence=0.9)

moveToAndClick(m, n)

sleep(1)

# Manually found pixels of keep changes button on inverted screen and clicking on it afterwards
pyautogui.moveTo(x=700, y=980)
pyautogui.click()












    


