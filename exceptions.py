a=input("please enter the name : ")

if(len(a)>5):
    raise ValueError(f"name {a} is less than 5 characters")
print(a)