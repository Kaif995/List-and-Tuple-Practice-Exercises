#palindromeExample :- num=[1,2,1]
num=[]
num.append(input("Enter your first Number :"))
num.append(input("Enter your second Number :"))
num.append(input("Enter your third Number :"))
copy_num=num.copy()
copy_num.reverse()

if(copy_num==num):
    print("This is Palindrome")
else:
    print("Not a Palindrome")
