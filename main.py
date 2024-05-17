import pyautogui
import time
import pandas as pd

"""
library configuration to make a pause (in seconds) between
automation commands important to run commands efficiently,
without running over each other during processing
"""
pyautogui.PAUSE = 0.5

"""
pyautogui.click -> command to click the mouse
pyautogui.write -> command to write text
pyautogui.press -> command to press a keyboard key
pyautogui.scroll -> command to scroll with middle mouse button
pyautogui.hotkey -> command to press a set of keys (ctrl+c, ctrl+v, alt+tab)
pyautogui.drag -> command to drag the mouse selecting
pyautogui.moveTo -> command to move the mouse without selecting
"""

# open the browser (Chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# enter the system website
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

"""
need for a longer break to give time to
load the website and continue logging in
"""
time.sleep(3)

# log in to the system
pyautogui.click(x=-1367, y=410)  # click on the email box position
pyautogui.write("victorzucchetti@hotmail.com")  # entering email
pyautogui.press("tab")  # moves to the password field
pyautogui.write("strong password")  # entering password
pyautogui.press("tab")  # go to login button
pyautogui.press("enter")  # logging in

time.sleep(3)

# importing the product database to register in the system

table = pd.read_csv("produtos.csv")

# register products
for line in table.index:  # for each line/index number in the table, do it:
    pyautogui.click(x=-1422, y=292)  # click on the product code field
    pyautogui.write(str(table.loc[line, "codigo"]))
    """
    get the product code from the table and write it
    in the field; str transforms information into string
    """
    pyautogui.press("tab")  # pass to next field
    # repeating for the other fields
    pyautogui.write(str(table.loc[line, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "custo"]))
    pyautogui.press("tab")
    if not pd.isna(table.loc[line, "obs"]):
        """
        verify if there are information on 'obs'
        column, if not, do not fill the field
        """
        pyautogui.write(str(table.loc[line, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
