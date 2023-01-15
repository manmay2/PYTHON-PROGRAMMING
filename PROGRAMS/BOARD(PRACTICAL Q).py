                                # BOARD QUESTIONS....GIVEN BY SCHOOL PRACTISE....
# 1. READ A TEXT FILE LINE BY LINE AND DISPLAY EACH WORD SEPARATED BY #.
def func1():
    str1=''
    with open("b1.txt",'w') as f1:
        inp1=input("Enter the text: ")
        f1.write(inp1)
    with open("b1.txt") as f2:
        k=len(f2.read().split())-1
        for i in range(k+1):
            if(i!=k):
                str1=str1+f2.read().split()[i]+'#'
                ct+=1
            elif(k==i):
                str1+=str1+f2.read().split()
    return str1


# 2. READ A TXT FILE AND DISPLAY THE NO. OF VOWELS,CONSONANT,UPPERCASE,LOWERCASE CHARACTERS.

def func2():
    v='aeiouAEIOU'
    vo=0
    co=0
    lo=0
    up=0
    with open("b1.txt") as f3:    
        
        def check(p):
            if(p in v):
                vo+=1
            else:
                co+=1
        for i in f3.read():
            if i.isupper():
                up+=1
                check(i)
            elif(i.islower()):
                lo+=1
                check(i)
    return vo,co,up,lo


# 3. REMOVE ALL THE LINES THAT CONTAIN THE CHARACTER 'a/A' IN A FILE AND WRITE IT TO ANOTHER FILE.
            # will do it soon....


# 4. CREATE A BINARY FILE WITH NAME, ROLL . SEARCH FOR A GIVEN ROLL AND DISPLAY THE NAME IF NOT FOUND APPROPRIATATE MESSAGE.
def func4():
    import pickle
    with open("b1.dat",'wb') as f4:
        n=int(input("Enter the range: "))
        d=dict()
        for i in range(n):
            d['Name']=input("Enter the name: ")
            d['Roll']=int(input("Enter the Roll number: "))
            pickle.dump(d,f4)
    with open("b1.dat",'rb') as f5:
        f=0
        try:
            r=int(input("Enter the roll number to be searched for: "))
            while True:
                D=pickle.load(f5)
                for i in D:
                    if(D['Roll']==r):
                        print("Name is: ",D['Name'])
                        f=1
                        break
        except EOFError:
            if(f==0):
                return "Name not found! Please try inputting a valid Roll no."



# 5. CREATE A BINARY FILE WITH ROLL,NAME AND MARKS. INPUT A ROLL AND UPDATE THE MARKS VIA UPDATING THE FILE.
def func5():
    import pickle
    with open("b2.dat",'wb') as f6:
        n=int(input("Enter the range: "))
        d=dict()
        for i in range(n):
            d['Name']=input("Enter the name: ")
            d['Roll']=int(input("Enter the Roll number: "))
            d['Marks']=float(input("Enter the Marks: "))
            pickle.dump(d,f6)
    print("FILE BEFORE UPDATING")
    with open("b2.dat",'rb') as f11:
        try:
            while True:
                d=pickle.load(f11)
                print(d)
        except EOFError:
            f11.close()
    with open("b2.dat",'rb') as f7:
        f=0
        try:
            r=int(input("Enter the roll number to be searched for: "))
            while True:
                D=pickle.load(f7)
                for i in D:
                    if(D['Roll']==r):
                        D['Marks']=float(input("Enter the updated marks: "))
                        f=1
        except EOFError:
            if(f==0):
                return "Roll not found! Please try inputting a valid Roll no."
    print("FILE AFTER UPDATING...............")
    with open("b2.dat",'rb') as f12:
        try:
            while True:
                d22=pickle.load(f12)
                print(d22)
        except EOFError:
            f11.close()

# 6. WRITE A RANDOM NO. GENERATOR THAT  GENERATES RANDOM NO. B/W 1 AND 6(SIMULATES A DICE).
def rand_func6():
    ans=True
    from random import randint
    while ans:
        d=randint(1,6)
        return d
        if(d==6):
            continue
        elif(input("Wish to continue: ").lower()=='yes' or input("Wish to continue: ").lower()=='y'):
            ans=True
        else:
            break

#7. WRITE A PYTHON PROGRAM TO IMPLEMENT A STACK.
def func6():
    def push(li,n):
        item=int(input("Enter the item to be pushed into the stack: "))
        if(len(li)==n):
            return "OVERFLOW"
        else:
            li.append(item)
    def pop(li):
        if(li==[]):
            return "UNDERFLOW"
        else:
            return li.pop()
    def peek(li):
        if li==[]:
            return "STACK EMPTY"
        else:
            return "TOPMOST ELEMENT IS: ",li[len(li)-1]

    def display(li):
        if li!=[]:
            for i in range(li-1,-1,-1):
                return i
        else:
            return "STACK IS ALREADY EMPTY!!!!..."
    li=list()
    print("WELCOME TO THE STACK OPERATION!!!!")
    print("1. PUSH")
    print("2. POP")
    print("3. PEEK")
    print("4. DISPLAY")
    ch=int(input("Enter your choices: "))
    n=int(input("PLEASE ! ENTER THE RANGE OF THE STACK!: "))
    if(ch==1):
        push(li,n)
    elif(ch==2):
        print(pop(li))
    elif(ch==3):
        print(peek(li))
    elif(ch==4):
        print(display(li))
