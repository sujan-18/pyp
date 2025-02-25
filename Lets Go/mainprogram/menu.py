#This file is only for login purpose
from mainprogram.Intro_decoration import decoration
from mainprogram.admin_menu import admin_menu

decoration()
def menu():
    choice= input('Enter your choice from above menu:')
    while True:
        if choice=="1":
            from mainprogram.admin_login import admin_login
            result = admin_login()
            if result:
                print("admin menu accesesed")
                admin_menu()
            else:
                print("failed failed failed failed failed")
        elif choice=="2":
            print("manager menu")
        elif choice=="3":
            print("chef menu")
        elif choice=="4":
            print("customer menu")
        elif choice=="5":
            print('Program exit!............')
            exit()
        else:
            print("Enter valid menu from above list.")
            menu()




