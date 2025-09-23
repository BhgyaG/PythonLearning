fruits=("apple","banana","orange","mango")
print(len(fruits))
user=input("enter a fruit name:")
if user in fruits:
    print("yes,it exists")
else:
    print("not found")