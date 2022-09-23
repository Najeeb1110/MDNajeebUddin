#This How We can Define Grater Value Using Def Function 
def letter (a,b,c):
    if a>b and a>c:
        return a
    elif b>c :
        return b
    else :
        return c
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
print(letter(a,b,c))