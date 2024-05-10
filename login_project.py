class User:
  def __init__(self,name,id,password):
      self.name=name
      self.id=id
      self.password=password
      self.followers=0
      self.following=0
    
  def matched(self,user):
    return self.id == user.id and self.password==user.password
    
  def follow(self,user):
    self.followers +=1
    user.following +=1
    
# singup function 
def singup():
        name=input("Enter your first name and last name:")
        id=input("Enter your Email_id:")
        password=input("Enter your Password:")
        user1=User(name,id,password)
        user_list.append(new_user)
        print("Singup successfully...")  
        
# login_id function
def login_id():
    id=input("Enter your Email_id:")
    password=input("Enter your Password:")
    user=User("",id,password)
    
#   matching function
    user.matched(user1)
    if user1.matched(user):
        print("login successfully...")
        print("open the dashboard..")
    else:
        print("invalid login_id")
        return login_id()
 
# profile function
def follow_by():
    name = input("Enter the name to follow: ")
    user3 = User(name,"","")
    user1.follow(user3)

    print(f"{user1.name}")
    print("Following:", user1.following)
    print("Followers:", user1.followers)

    print(f"{user3.name}")
    print("Following:", user3.following)
    print("Followers:", user3.followers)
          
# singup page
user_list=[] 
print("Welcome to sigup..")
name=input("Enter your first name and last name:")
id=input("Enter your Email_id:")
password=input("Enter your Password:")
user1=User(name,id,password)

#store in user list
new_user=User(name,id,password)
user_list.append(user1)

# singup or lgin new account create
while (True):
    print("press 1 for signup , press 2 for login , press 3 for exit.")
    ch=input("Enter your choice:")
    if ch == '1':   
        singup()
    elif ch == '2': 
        login_id()
        break
    elif ch == '3':
        exit()
    else:
        print("Invalid choice.....")
     
#profile function
while True:
    print("press 1 for follow , press 2 for exit profile:")
    ch=input("Enter your choice:")
    if ch == '1':
        follow_by()
    elif ch == '2':
        exit()
    else:
        print("Wrong choice......")
    