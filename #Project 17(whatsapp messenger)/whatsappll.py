import pywhatkit
import pyautogui

name = input("whom do you want to send message : \n a for Dagar\n b for Ritul \n c for poonam: ")
if name=='a':
    a = int(input('How many word he/she has spoken in hindi: '))
    fine = a * 5
    pywhatkit.sendwhatmsg_instantly("+91 9817456365", f"You have spoken {a} words, You have got file of ruppes : {fine}")
    pyautogui.click(x=1282, y=1723)
    pyautogui.keyDown('Enter')
elif name=='b':
    a = int(input('How many word he/she has spoken in hindi: '))
    fine = a * 5
    pywhatkit.sendwhatmsg_instantly("+91 9518185226", f"You have spoken {a} words, You have got file of ruppes : {fine}")
    pyautogui.rightClick(x=1282, y=1723)
    pyautogui.keyDown('Enter')
else:
    print("sorry others are pending😕😕😕") 