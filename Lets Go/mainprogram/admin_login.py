#import admin_menu

login_path='Data/login.txt'
def admin_login():
    attempt=3
    while attempt > 0:
        name=input("Enter your name: ").lower()
        user_name=input('Enter your user_name: ').lower()
        password=input('Enter your password: ').lower()
        file=open(login_path,'r')
        for path in file:
            role,user,pwd=path.strip().split(',')
            if user_name==user and password==pwd: 
                print(f"Welcome, {name}..! Your role is {role}.")
                return True
            return False
        attempt=attempt-1
        print(f"Invalid username and password!!..\nNow you have {attempt} attempt left")
        if attempt==0   :
           print("To many wrong attempt!!!Page Exiting..... " )
           # decoration()
    exit()

'''result = admin_login()
print(result)
if result:
    print("login success")
else:
    print("failed")'''


