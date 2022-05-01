#Program To Show The Implementation Of Nested Ifs And The Syntax For Writing Single Statements Inside If
a=input()
b=input()
if (a==1):
    if (b==1) : print("This Is Ek")
    elif (b==2) : print("Ek Aur Do")
    else: print("Kuch Toh Alag Likh Do")
elif (a==2):
      if (b==1) :
         print("Do Aur Ek")
      elif (b==2) : 
         print("This Is Do")
      else: 
         print("Try Dobara")
else:
    print("Alag Ka Matlab Hai Different")
        