
flag=0
while flag==0:
    a=input("enter number of lines to generate")
    for i in range(0,a):
        for j in range(0,i+1):
            print("*"),
        print "\n"
    b=(input("Do you wish to quit: (0/1)"))
    if(b==1):
        flag=1
    else:
        continue
