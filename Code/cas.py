#TO USE THIS CODE YOU MUST INSTALL THE LIBRARY PYAUTOGUI:
#!pip install pyautogui

##import, functions and definition
import pyautogui as auto
import time as tm

auto.PAUSE = .5

def maxsr():
	auto.keyDown("win")
	auto.press("up")
	auto.keyUp("win")

def splitsr():
	auto.keyDown("win")
	auto.press("right")
	auto.keyUp("win")

def minsr():
	auto.keyDown("alt")
	auto.keyDown("space")
	auto.press("n")
	auto.keyUp("alt")
	auto.keyUp("space")


#open edge
auto.press("win")
auto.write("edge") #change to the browser you are used to
auto.press("enter")
tm.sleep(.3)
maxsr()

#open vscode
auto.press("win")
auto.write("vscode") #change to the IDE you user to code
auto.press("enter")
tm.sleep(.5)

#split screen
splitsr()
tm.sleep(.5)
auto.press("enter")

#open spotify
auto.press("win")
auto.write("spotify")
auto.press("enter")
tm.sleep(10)
auto.press("space")
minsr()
