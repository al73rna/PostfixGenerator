import math

in_str = "5 + ((10 + 42) * 874) - 3"
print("YOUR INFIX EXPRESSION IS : ",in_str)
print("_________________________________________")
print("")
s = []
so = ""
for i in in_str :
    
    if i.isnumeric():
        so+=i+''
    elif i == '(':
        s.append(i)
    elif i == ')':
        while len(s)!=1 and s[-1]!='(':
            tmp = s.pop()
            if tmp!=')' and tmp!='(':
                so+=tmp
        s.pop()

    elif (i == '+'):
        so+=','
        if len(s)==0 :
            s.append(i)
        elif s[-1] == '-' or s[-1] == '+'or s[-1]=='(' or s[-1]==')' :
            s.append(i)
        elif s[-1] == '/' or s[-1] == '*' :
            while s[-1] == '/' or s[-1] == '*':
                so+=s.pop()
                if (len(s)==0):
                    break
            s.append(i)

    elif (i == '-'):
        
        so+=','
        if len(s)==0 :
            s.append(i)
        elif s[-1] == '-' or s[-1] == '+'or s[-1]=='(' or s[-1]==')' :
            s.append(i)
        elif s[-1] == '/' or s[-1] == '*' :
            while s[-1] == '/' or s[-1] == '*':
                so+=s.pop()
                if (len(s)==0):
                    break
            s.append(i)


    elif (i == '*'):
        so+=','
        if len(s)==0 :
            s.append(i)
        elif s[-1] == '-' or s[-1] == '+'or s[-1] == '/' or s[-1] == '*'or s[-1]=='(' or s[-1]==')' :
            s.append(i)

    elif (i == '/'):
        so+=','
        if len(s)==0 :
            s.append(i)
        elif s[-1] == '-' or s[-1] == '+'or s[-1] == '/' or s[-1] == '*'or s[-1]=='(' or s[-1]==')' :
            s.append(i)

   


while len(s)!= 0:
     so  += s.pop()

#so=so.replace('(','')
print("POST FIX NOTATION IS ---- > ",so)


s=[]
tx = so
tt= ""
for i in tx:
    #print(s)
    if i.isnumeric() :
        tt+=i
    else:
        if tt.isnumeric():
            s.append(int(tt))
        tt=''
    if i == '+':
        tmp = s.pop()+s.pop()
        s.append(tmp)
    if i == '-':
        t1=s.pop()
        tmp = s.pop()-t1
        s.append(tmp)
    if i == '*':
        tmp = s.pop()*s.pop()
        s.append(tmp)
    if i == '/':
        t2=s.pop()
        tmp = s.pop()/t2
        s.append(tmp)

print("RESULT IS : ------------- > ",tmp)
