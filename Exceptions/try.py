try :
    n = int(input())
except :
    print(" error occured only integer values are allowed")
else :
    print(" No error has occured")
finally :
    print("program has finished its execution")
    
n2 = "abcd"
if not type(n2) is int:
   # raise TypeError("ONLY INTEGER VALUES ARE ALLOWED") #raise keyword thorws an error 
    raise Exception("THIS SI GENERIC EXCEPTION")