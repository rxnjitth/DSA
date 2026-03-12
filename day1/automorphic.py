num = int(input("enter the number"))

s = num * num

m = len(str(num))

if s % (10 **m) == num :
    print("automorphic number")
else:
    print("not an automorphic number")