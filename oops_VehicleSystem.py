from datetime import date
import time
from sqlite_utils import DbOperations
dta=DbOperations()
dta.create_vehicle_table()
dta.create_starproject_table()
class StarProtectVehicleSystem:
     def __init__(self):
          self.dict1={}
          self.dict2={}
          self.dict1[1]=["Baibhav","12-12-2001","21-10-2012","abc123@"]
          self.dict1[2]=["Akshat","11-02-2000","29-06-2010","cvv13@"]
          self.dict1[3]=["Manikant","25-01-2001","21-01-2012","a223@"]
          self.dict1[4]=["Ashish","15-08-2000","12-02-2013","ab1232@"]
          self.id=5
          self.dict2[1]=[["P11","V11","2-wheeler","Baibhav","E11","Ch11","9876543211","Third Party", "1000","21-02-18","2023-04-12"]]
          self.dict2[2]=[["P12","V12","4-wheeler","Akshat","E12","Ch12","9832117654","Full insurance","2500","21-02-21","2022-01-02"]]
          count=1
          print("ok")
          for i in self.dict1.keys():
               lst=[]
               lst.append(count)
               count+=1
               dta.insert_trainee_data(lst+self.dict1[i])
          for i in self.dict2.keys():
               for j in self.dict2[i]:
                    lst=[]
                    for k in j:
                         lst.append(k)
                    # print(lst)
                    lst.append(i)
                    print(lst)
                    dta.insert_starProject(lst)
              

     def show_login_menu(self):
          print("Welcome to Star Protect Vehicle System")
          print("1. Admin Login")
          print("2. Underwriter Login")
          choice = input("Enter your choice: ")
          if choice == "1":
               print("Admin login successful.")
          elif choice == "2":
               self.underwriter_login()
          else:
               print("Invalid choice. Please enter 1 or 2.")
     
     def underwriter_login(self):
          print("Please enter the id and password")
          id1=int(input())
          pas=input()
          f=1
          for i in self.dict1.keys():
               if(i==id1):
                    if(self.dict1[i][3]==pas):
                         f=2
                         print("User login successful.")
          
          if(f==1):
               print("Please enter a valid id and password")

     def show_admin_menu(self):
          while True:
               print("\nAdmin Menu:")
               print("1. UnderWriter Registration")
               print("2. Search Underwriter by Id")
               print("3. Update UnderWriter password")
               print("4. Delete UnderWriter by Id")
               print("5. View All Underwriter")
               print("6. View All Vehicle specific to underwriter Id")
               print("7. Exit")
               choice = input("Enter your choice: ")
               if choice == "1":
                    self.register_underwriter()
               elif choice == "2":
                    self.search_underwriter_by_id()
               elif choice == "3":
                    self.update_underwriter_password()
               elif choice == "4":
                    self.delete_underwriter_by_id()
               elif choice == "5":
                    self.view_all_underwriters()
               elif choice == "6":
                    self.view_all_vehicles_for_underwriter()
               elif choice == "7":
                    print("Exiting program...")
                    break
               else:
                    print("Invalid choice. Please enter a number between 1 and 7.")

     
     def register_underwriter(self):
          name = input("Enter the name: ")
          dob = input("Enter the date of birth: ")
          doj = input("Enter the date of joining: ")
          password = input("Enter the password: ")
          lst=[]
          lst.append(name)
          lst.append(dob)
          lst.append(doj)
          lst.append(password)
          self.dict1[self.id]=lst
          self.id+=1
          dta.insert_underwriter_data([self.id-1,name,dob,doj,password])

     
     def search_underwriter_by_id(self):
          print("1. View all UnderWriters")
          print("2. View UnderWriters by id")
          n1=int(input())
          if(n1==2):
               n=int(input())
               f=1
               for i in self.dict1.keys():
                    if(i==n):
                         f=2
                         print("Here are the details:")
                         for j in self.dict1[i]:
                              print(j)
               if(f==1):
                    print("please enter a valid id")
          else:
               for i in self.dict1.keys():
                    print("id:",i)
                    print("Here are the details:")
                    for j in self.dict1[i]:
                              print(j)
          d.xyz(id)

     def update_underwriter_password(self):
          print("Enter the id:")
          n=int(input())
          f=1
          for i in self.dict1.keys():
               if(i==n):
                    f=2
                    print("please enter the new password")
                    np=input()
                    self.dict1[i][3]=np
          if(f==1):
               print("Please enter a valid id")
     
     def delete_underwriter_by_id(self):
          print("Enter the id")
          n=int(input())
          f=1
          for i in self.dict1.keys():
               if(i==n):
                    f=2
                    break
                    
          if(f==1):
               print("Please enter a valid id")
          else:
               del self.dict1[n]

     def view_all_underwriters(self):
          print("Here are all the underwriters")
          for i in self.dict1.keys():
                    print("id:",i)
                    print("Here are the details:")
                    for j in self.dict1[i]:
                              print(j)
     def view_all_vehicles_for_underwriter(self):
          print("Enter the user id")
          n=int(input())
          f=1
          for i in self.dict2.keys():
               if(i==n):
                    print("Here are all the details") 
                    f=2
                    for j in  self.dict2[i]:
                         for k in j:
                              print(k)
          if(f==1):
               print("Please enter a valid id")

          
     def vehicle_details(self):
          print("Do you want to see your vehicle details?")
          print("1. Yes")
          print("2. No")
          n=int(input())
          if(n==1):
               print("Please enter the userid and password")
               n1=int(input())
               password=input()
               f=1
               for i in self.dict1.keys():
                    if(i==n1 and self.dict1[i][3]==password):
                         f=2
                         self.vehicle_menu(n1)
               if(f==1):
                    print("please enter a valid password and user id")
     
     def vehicle_menu(self,n1):
          print("\n Vehicle Menu:")
          print("1. Create a new vehicle Insurance")
          print("2. Renewal of Policy")
          print("3. Changing of policy")
          print("4. View of Policy")
          print("5 view by policy no")
          print("6 count of vehicles by an underwriter")
          print("7 Expired Vehicles")
          print("8 delete data based on underwriter id")

          choice=int(input())
          if(choice==1):
               self.new_insurance(n1)
          elif(choice==2):
               self.renewal(n1)
          elif(choice==3):
               self.change(n1)
          elif(choice==4):
               self.view(n1)
          elif(choice==5):
               self.sql_p(n1)
          elif(choice==6):
               self.sql_no(n1)
          elif (choice==7):
               self.expired(n1)
          else:
               self.del_values(n1)


          
     def new_insurance(self,n1):
          print("Enter all the details of the new policy")
          a=input()
          b=input()
          c=input()
          d=input()
          e=input()
          f=input()
          g=input()
          h=input()
          i=input()
          k=input()
          l=input()
          lst=[]
          lst.append(a)
          lst.append(b)
          lst.append(c)
          lst.append(d)
          lst.append(e)
          lst.append(f)
          lst.append(g) 
          lst.append(h) 
          lst.append(i) 
          lst.append(k) 
          lst.append(l)
         
          self.dict2[n1].append(lst) 
          lst.append(n1)
          print(lst)
          dta.insert_starProject(lst)
     def renewal(self,n1):
          print("enter the policy id")
          p_id=input()
          f=1
          for i in self.dict2[n1]:
               if(i[0]==p_id):
                    str=i[10]
                    lst1=str.split("-")
                    today ="2024-02-10"
                    lst2=today.split("-")
                    if(int(lst2[0])>int(lst1[2])):
                         lst2[0]="25"
                         lst2.reverse()
                         str3="-".join(lst2)
                         i[10]=str3
                         print("Updated")
                    else:
                         print("no need to update")
                            

          
     def change(self,n1):
          print("enter the policy id")
          s=input()
          dta.finding_using_policy_no(s)
          f=1;
          for i in self.dict2.keys():
               if(i==n1):
                    for j in self.dict2[i]:
                         if(j[0]==s and j[8]=="Third Party"):
                              print("There is no provision to update a 3rd party to full insurance")
                         elif(j[0]==s and j[8]=="Full Insurance"):
                              print("Press U to change from Full Insurance to Third Party")
                              q=input()
                              if(q=='U'):
                                   f=2
                                   j[8]="Third party"
                                   print("update done")
     def view(self,n1):
          print("1. For all vehicle details")
          print("2. Enter the vehicle id ")
          print("3. Enter the policy id")

          ch=int(input())
          if(ch==1):
               print("here are the details")
               count=1
               for i in self.dict2[n1]:
                    print(count)
                    for j in i:
                         print(j)
          elif(ch==2):
               print("enter vehicle id")
               v_id=input()
               for i in self.dict2[n1]:
                    if(i[1]==v_id):
                         for j in i:
                              print(j)
          else:
               print("enter policy id")
               p_id=input()
               for i in self.dict2[n1]:
                    if(i[0]==p_id):
                         for j in i:
                              print(j)
     def sql_p(self,n1):
          print("enter policy no")
          n=input()
          dta.finding_using_policy_no(n)
     
     def sql_no(self,n1):
          dta.no_vechs_details()
     
     def expired(self,n1):
          dta.date_exp()
     def del_values(self,n1):
          dta.del_data()

if __name__=="__main__":
     s1=StarProtectVehicleSystem()
     s1.show_login_menu()
     s1.show_admin_menu()
     s1.vehicle_details()
