from function.manage_staff import manage_staff
from function.update_profile import update_profile
from function.view_feedback import view_feedback
from function.view_report import view_sales_report
from mainprogram.Intro_decoration import decoration


def admin_menu():
    print("-"*77)
    print('+-'*12 + "WELCOME TO OUR ADMINISTRATOR PAGE" + '+-'*12)
    print("-"*77)
    print("Here are some role of Administrator:")
    print("1. Manage Staff\n2. View Sales report\n3. View Feedback\n4. Update own profile\n5. Back to menu")
    while True:
        choice=int(input("Enter your choice from admin role:"))
        if choice==1:
            manage_staff()
        elif choice==2:
            view_sales_report()
        elif choice==3:
            view_feedback()
        elif choice==4:
            update_profile()
        elif choice==5:
            from mainprogram.menu import menu
            decoration()
            menu()
        else:
            print("Your Choice Is Out Of Range!!")


