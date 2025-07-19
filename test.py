import pyautogui as pg
import time
import pymsgbox

pg.FAILSAFE = True
screenWidth, screenHeight = pg.size()

# coordinates
titleBurgerX, titleBurgerY = (2450, 1422)               # title hamburger icon
skipX, skipY = (1204, 1450)
rolls = 8


currentMouseX, currentMouseY = pg.position()


def delete_user_data():
    pg.click(1262, 1083)       # move to delete user data and click it
    time.sleep(0.5)
    pg.click(1458, 1026)                      # then confirm
    time.sleep(0.5)
    pg.click()
    time.sleep(2)
    pg.move(-100, 0)        # Close
    pg.click()

def terms_of_consent():
    touX, touY = (1564, 718)
    ppX, ppY = (1561, 868)
    pg.click(touX, touY)                   # view ToU
    time.sleep(2)
    with pg.hold('ctrl'):
        pg.press('w')           # close browser window
    time.sleep(1)
    pg.hotkey('alt', 'tab')          # return to Uma
    time.sleep(1)
    pg.click(ppX, ppY)                      # view PP
    time.sleep(2)
    with pg.hold('ctrl'):
        pg.press('w')  # close browser window
    time.sleep(1)
    pg.hotkey('alt', 'tab')          # return to Uma
    time.sleep(1)
    pg.click(1477, 1130)             # I Agree

def country():
    changeX, changeY = (1541, 829)
    okX, okY = (1481, 1105)
    confirmX, confirmY = (1449, 1013)
    pg.click(changeX, changeY)
    time.sleep(0.5)
    pg.click(okX, okY)
    time.sleep(0.5)
    pg.click(confirmX, confirmY)

def age_confirm():
    textX, textY = (1298, 834)
    age = '200301'
    okX, okY = (1470, 1032)
    pg.click(textX, textY)
    time.sleep(0.5)
    pg.write(age)
    time.sleep(0.5)
    pg.click(1470, 1032)

def trainer_reg():
    pg.click(1325, 741)      # text box
    pg.write('Alice')
    pg.press('enter')
    pg.sleep(0.5)
    pg.click(1283, 1034)     # register
    time.sleep(2)
    pg.click(1453, 1021)     # OK

def present():
    pg.click(1072, 1114)     # click on presents
    time.sleep(2)
    pg.click(915, 1414)      # collect all
    time.sleep(1.5)
    pg.click(723, 1423)      # close
    time.sleep(1.5)
    pg.click(565, 1414)      # close again

def check_for_good():
    # sakura bakushin o
    # tokai teio
    # silence suzuka
    # eishin flash

    # need event for purely kitasan black
    # also fine motion super creek at least is good
    return True

def scout():
    pg.click(1065, 1465)     # scout icon
    time.sleep(2)
    for x in range(0, 3):
        pg.click(1136, 952)  # move banner to right
        time.sleep(0.5)
    # now on kita black banner

    pg.click(976, 1235)      # click 10x scout
    time.sleep(0.5)
    pg.click(914, 1031)      # confirm
    time.sleep(3)

    # all in loop
    for x in range (0, rolls):
        for y in range(0, 10):
            pg.click(skipX, skipY)           # skip cards (10 max SSR cards)
        time.sleep(1)
        if x != rolls-1:                            # not last scout
            pg.click(903, 1437)         # scout again
            time.sleep(0.5)
            pg.click(915, 1022)         # confirm
        time.sleep(3)

    pg.click(576, 1433)         # Back

def bridge():
    # delete user data from title screen
    pg.click(titleBurgerX, titleBurgerY)
    time.sleep(2)
    delete_user_data()

    # back at the title screen
    time.sleep(3)
    pg.click()               # minor warning
    time.sleep(3)
    pg.click()               # tap to start
    time.sleep(3)

    terms_of_consent()
    time.sleep(1)

    country()
    time.sleep(1)

    age_confirm()
    time.sleep(4.5)

    # skip tutorial
    pg.click(1452, 1021)
    pg.sleep(0.5)

    trainer_reg()

    time.sleep(4)
    # first banners
    for x in range(0, 60):
        pg.click(skipX, skipY)       # last reward
        time.sleep(0.25)

    # now at home screen
    present()
    time.sleep(2.5)

    scout()
    time.sleep(7)


    # now at home screen
    pg.click(425, 1459)          # Enhance
    time.sleep(1)
    pg.click(900, 1024)          # Support
    time.sleep(0.75)
    pg.click(552, 1179)          # List
    time.sleep(0.75)
    pg.moveTo(258, 923)           # go off-screen
    time.sleep(1)
    input()
    if check_for_good():                          # scans for good cards
        pymsgbox.alert(text='Found more than 3 Good cards', title='GOOD', button='OK')
        return True
    else:
        return False


def brain():
    while not bridge():         # < 3 good cards
        pg.click(2000, 1281)        # to title screen
        time.sleep(5)

pg.hotkey('alt', 'tab')
time.sleep(1)
brain()

# print(currentMouseX, currentMouseY)

# remember to alt+tab at the start bc you're running this