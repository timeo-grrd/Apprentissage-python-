num = 5
a=6
b=7
age= 25
temp = 30
user_role ="admin"
# print("postive"  if num > 0  else "negative")
# result = "EVEN" if num % 2 == 0 else "ODD" 
max_num= a if a>b else b
min_num= a if a<b else b
status = "adult" if age >= 18 else "child"
weather= "hot" if temp > 25 else "warm"
access_level = "full access" if user_role == "admin" else "not full access"
print(access_level)