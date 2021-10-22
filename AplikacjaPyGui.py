from selenium import webdriver
import time
import keyboard
import pyautogui
import random
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
print("podaj ile razy chcesz wysłać wiadomość")
i=input()
i=int(i)
print("podaj treść wiadomości")
t=input()
driver = webdriver.Firefox()
driver.maximize_window
time.sleep(2)
driver.get("<facebook>")
time.sleep(2)
driver.find_element_by_id("email").click()
keyboard.write('<email>')
time.sleep(2)
driver.find_element_by_id("pass").click()
keyboard.write('<password>')
time.sleep(2)
driver.find_element_by_id("loginbutton").click()
time.sleep(2)
pyautogui.moveTo(1200, 310)
pyautogui.doubleClick()
pyautogui.doubleClick()
time.sleep(5)
while i>0 :
    keyboard.write(t)
    x = random.randint(1,3)
    time.sleep(x)
    keyboard.press_and_release('enter')
    i=i-1






