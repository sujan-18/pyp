
staff_file_path="Data/manage_staff.txt"
def manage_staff():
   print("-"*77)
   print('+-'*12 + "WELCOME TO OUR STAFF MANAGE PAGE" + '+-'*12)
   print("-"*77)
   print( "1. Add staff"  )
   print( "2. Edit staff" )
   print( "3. Delete staff")
   print( "4. Back to role of Admin")

   while True:
      choice=int(input( "Enter your choice (EX:1,2,3): "))

      if choice==1:
         f=open(staff_file_path,"a+")
         add=input( "Enter the name of staff: ").capitalize()
         f.write("\n" + add)
         print("successfully added" )
         #manage_staff()
      if choice==2:
         f=open(staff_file_path,"w+")
         add=input("Enter the name of staff: ").capitalize()
         f.write(add)
         print("successfully edited")

         #manage_staff()
      if choice==3:
         f=open(staff_file_path,"r+")
         name=f.readlines()
         add=input("Enter the name of staff you want to delete: ").capitalize()
         for line in name:
            if add in line:
               del line
               print("successfully deleted" )
               #manage_staff()
            else:
               print("Name is not in list...!!" )
               #manage_staff()
         
      if choice==4:
         from mainprogram.admin_menu import admin_menu
         admin_menu()
         
