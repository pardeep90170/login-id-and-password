class User:
    def __init__(self,name,id,password):
        self.id=id
        self.name=name
        self.password=password 
        self.followers=0
        self.following=0
        
    def matched(self,user):
        return self.id == user.id and self.password == user.password 
      
    def follow(self,user):
        self.followers+=1
        self.following+=1
    
#singup function 
def signup():
    name=input("Enter your name:")
    id=input("Enter your Email_id:")
    password=input("Enter your password:")
    user=User(name,id,password)
    print("Signup To sucessfully..")
    list.append(user)
    
# login function
def login_id():
    id=input("Enter your Email_id:")
    password=input("Enter your password:")
    user=User("",id,password)
    if user.matched(list[0]):
        print("Login sucessfully..")
        print("Open To Dashboard..")
    else:
        print("Invalid Login_id")
        
# def follow():
    name=input("Enter your name to follow:")
    user=User(name,"","")
    user.follow()
    

# follow function
list=[]
while True:
    print("press 1 for signup..\npress 2 for login..\npress 3 for exit..")
    ch =input("Enter your choice:")
    if ch == '1':
        print("Welcome to signup page..")
        signup()
    elif ch == '2':
        login_id()
    elif ch == '3':
        exit()
    else :
        print("Invalid Choice.....")
