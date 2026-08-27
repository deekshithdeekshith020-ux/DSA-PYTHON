s = "No lemon, no melon!"
left=0
right=len(s)-1
while(left<right):
    
    if not s[left].isalnum():
        left+=1
        
    elif not s[right].isalnum():
        right-=1
        
    elif(s[left].lower()==s[right].lower()):
        left+=1
        right-=1
            
    elif(s[left].lower()!=s[right].lower()):
        print("false")
        break  
else:
    print("true")     

         

##if not s[left].isalnum(): this checks wheather the given element is num and charecter      