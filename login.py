import csv
from forgetpass import for_pwd


def email_val(email):
    email_starts = ("A",'B','C','D', 'E', 'F', 'G','H', 'I', 'J', 'K', 'L', 
                'M', 'N', 'O','P','Q','R','S','T','U','V','W','X', 'Y','Z',
                'a','b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',' m'
                ,'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x','y','z')
    mails=["gmail","ymail","Outlook","Zoho","Yandex"]
    sp_char=["@","."]
    e,s,n,sp=0,0,0,0
    user=email.split('@')[0] #keshavan
    user2=email.split("@")[1] #@gmail.com
    user3=user2.split('.')[0] #@gmail
    if email.endswith(".com") or email.endswith(".in"):
    
        if email.startswith(email_starts):
                s+=1
        if len(user)>4:
            n=len(user)        
        if len(user3)>4:
                   e=len(user2)
                   
        for i in email:
            if i in sp_char:
                sp+=1        
        if e>=1 and s>=1 and sp>=2 and n>=1 and e+sp+n-s== len(email):
            
            return True
        else:
            
            return False
                   
                     
    

def password_val(pwd):
    ecape_ch= ('~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', 
             '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', 
             '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/')
    digit= ('1','2','3','4','5','6','7','8','9','0')
    lower_case= ('a','b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l',' m',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x','y','z')
    upper_case= ("A",'B','C','D', 'E', 'F', 'G','H', 'I', 'J', 'K', 'L', 
                'M', 'N', 'O','P','Q','R','S','T','U','V','W','X', 'Y','Z')
    c,d,l,u=0,0,0,0

    for j in pwd:  
             if j in ecape_ch:
                 c+=1
             if j in digit:
                 d+=1
             if j in lower_case:
                 l+=1
             if j in upper_case:
                 u+=1
    if (c>=1 and d>=1 and l>=1 and u>=1 and c+d+l+u == len(pwd)):
        
        return True
    else:
        return False
        


def reg():
    email= input("Enter the Email id: ")
    

    if email_val(email):
        password = input("Enter the password : ")
        if password_val(password):
                with open('user.csv','a',newline='') as file:
                    
                    file.writelines(email +","+ password)
                    file.write('\n')
                    file.close()
                    print("Registration sucessfully")
                return True
        else:
                print("Password Not Valiadte")
    else:
           print("Email Not Valiadte")             
           


def login():
    email=input("Enter the Email id: ")
    if email_val(email):
        password = input("Enter the password : ")
        if password_val(password):
            
            with open("user.csv",'r',newline='') as file:
                reader=csv.reader(file)
                
                for i in reader:
                   if email == i[0] and password ==  i[1]:
                       print("Sucessfully Login")
                       print(i[0],i[1])
                       return True
                       
                
                else:
                    print("invalid USER")
                    print("please Register")
                    reg()
        else:
              print("invalid password")          
    else:
         print("invalid email")           
           

 
if __name__=="__main__":
    
    print("""please select one option :
              
              1.login
              2.Registration
              3.Forgot Password
          
          """)
    option=int(input("Enter your option: "))
    if option==1:
        login()
    elif option==2:
        reg()
    elif option==3:
        for_pwd()
    else:
        print("invalid option")

