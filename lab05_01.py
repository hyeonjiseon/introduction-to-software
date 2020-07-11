print("1단\t\t2단\t\t3단")
for x in range(1,10):
    print("1*"+str(x)+"="+str(x)+"\t\t2*"+str(x)+"="+str(2*x)+"\t\t3*"+str(x)+"="+str(3*x))
print()
print("4단\t\t5단\t\t6단")
for x in range(1,10):
    print("4*"+str(x)+"="+str(4*x)+"\t\t5*"+str(x)+"="+str(5*x)+"\t\t6*"+str(x)+"="+str(6*x))
print()
print("7단\t\t8단\t\t9단")
for x in range(1,10):
    print("7*"+str(x)+"="+str(7*x)+"\t\t8*"+str(x)+"="+str(8*x)+"\t\t9*"+str(x)+"="+str(9*x))
print()


#다른 방법
for n in range(1,8,3):
    print(str(n)+"단\t\t"+str(n+1)+"단\t\t"+str(n+2)+"단")
    for x in range(1,10):
        print(str(n)+"*"+str(x)+"="+str(n*x)+"\t\t"+str(n+1)+"*"+str(x)+"="+str((n+1)*x)+"\t\t"+str(n+2)+"*"+str(x)+"="+str((n+2)*x))
    print()
