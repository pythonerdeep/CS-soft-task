import re
value = []
items=[x for x in input("enter the password:- ").split(',')]
print(items)
for p in items:
    print("length is ",len(p))
    if len(p)<4 or len(p)>6:
        continue
    if not re.search("[a-z]",p):
        print(" a-z characters  not in the password")
        continue
    elif not re.search("[0-9]",p):
        print("0-9 letters are not in password")
        continue
    elif not re.search("[A-Z]",p):
        print("A-Z alphabets are not in password")
        continue
    elif re.search(r"\s",p):
        print("space are not allowed")
        continue
    else:
        value.append(p)
print(",".join(value))