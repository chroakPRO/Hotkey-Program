"""

IMPORTS

"""
import keyboard
import win32gui
import win32api
from typing import Dict, List
from prettytable import PrettyTable
import datetime
import os
from string import ascii_lowercase

"""

Macro Program Class.

"""

class HotkeyConf:
    
    def __init__(self):
        self.binds: Dict[str, str] = {}
        self.txtbinds: List[str] = []
        self.txtaction: List[str] = []
        self.highestindex: int = 2

    def add_keybinding(self, value: str, key: str) -> bool:
        self.binds.update(value, key)
        return True
    
    def record_bind(self) -> str:
        # Record events until 'esc' is pressed.
        temp = []
        print("Recording keys.. press 'ESC' when done")
        recorded = keyboard.record(until='esc', suppress=False, trigger_on_release=False)
        count = 0
        for i in recorded:
            if count  > 1:
                if i.event_type == "up":
                        temp.append(i.name)
            else: count += 1

        return "+".join(temp)
          
    def mute(self):
        WM_APPCOMMAND = 0x319
        APPCOMMAND_MICROPHONE_VOLUME_MUTE = 0x180000

        hwnd_active = win32gui.GetForegroundWindow()
        win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE)

    def shutdown(self):
        print("Shutdown worked.")
        #s.system("date")
        #os.system("shutdown -l -t 0")


    def placeholder(self):
        pass

    def add_binds(self, bind: str, func: object) -> bool:
        keyboard.add_hotkey(bind, func)
        

        #return keyboard.add_hotkey("CTRL+ALT+A", self.shutdown)

    def view_keybinds(self) :

        table = PrettyTable()
        table.field_names = ["ID", "Bind", "Action", "Time"]
        for j, i in enumerate(self.txtbinds):
            table.add_row([j, str(i), self.txtaction[j], datetime.datetime.now().strftime("%d/%m/%Y")])
            
        return table


"""

GLOBAL OBJECTS.

"""

main_object = HotkeyConf()
def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')
    

"""

Functioning classes and functions/methods.

"""

def view_controller(): 
    print(123)
    if len(main_object.txtbinds) <= 0:
        print("There have been no enteries into the system")
    else:
        clearConsole()
        p_table = main_object.view_keybinds()
        print(p_table)
        print("Press 'ESC' to go back.")

def edit_controller():
    print("You can always show the keybindings by using option 1 at the main menu.")
    user_input = int(input("Choose... a number to edit: "))
    if type(user_input) == int:
        if user_input == 0:
            new_binding = main_object.record_bind()
            txt_parsed = new_binding
            if 



            main_object.txtbinds[0] = new_binding
        elif user_input == 1:
            new_binding = main_object.record_bind()
            main_object.txtbinds[1] = new_binding
            # This dosen't actually change the keybind, need to add add_binds(object, function)   
        elif user_input == 2:
            menu = False
        else: print("Else statement, under input validation.")
    else: print(888)

            
def main():

    menu = True  
    while menu:
        #main_object.mute()
        #binding = main_object.record_bind()
        #x = main_object.add_binds("CTR¨00L+SHIFT+L")
        clearConsole()
        print("This is mysteriesly a locked vault of goblin gadgets.")
        print("Peak Inside.... and wait for the lights.")
        print("Pick one of these options")
        print("\t [0] View Keybinds\n", "\t [1] Change Keybinds\n", "\t [2] Exit\n")
        user_input = int(input("Choose... a number: "))
        if type(user_input) == int:
            if user_input == 0:
                view_controller()
            elif user_input == 1:
                edit_controller()
            elif user_input == 2:
                #menu = False
                exit(2)
            else:
                print("Else statement, under input validation.")
        else:
            print(2)


        if len(main_object.txtbinds) > main_object.highestindex + 1:
            print("To many actions.")
        else:
            for j, i in enumerate(main_object.txtbinds):
                #test = new_dict[j]
                #print(test, type(test))
                #function 0= main_object.
                #main_object.add_binds(i, function)

                if j == 0:
                    function = main_object.mute
                    main_object.add_binds(i, function)
                elif j == 1:
                    function = main_object.shutdown
                    main_object.add_binds(i, function)
                elif j == 2:
                    function = main_object.shutdown
                    main_object.add_binds(i, function)
                else: print("Something went wrong")
            keyboard.wait('ESC')

if __name__ == '__main__':
    # Default values.
    main_object.txtbinds.append("CTRL+ALT+I")
    main_object.txtaction.append("mute")

    main_object.txtbinds.append("CTRL+ALT+O")
    main_object.txtaction.append("Macro")

    main_object.txtbinds.append("CTRL+ALT+P")
    main_object.txtaction.append("shutdown")
    main()