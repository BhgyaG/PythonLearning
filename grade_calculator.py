marks=int(input("enter marks:"))
if marks>=90:
    print("grade 1")
elif marks>=75:
    print("grade 2")
elif marks>=50 and marks<75: #we dont need to write marks<75 here in this line i just wrote for my undersatanding
    print("grade 3")
else:
    print("fail")
