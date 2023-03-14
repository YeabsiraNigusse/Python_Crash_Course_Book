user_Number = int(input("enter a number: "))
sum = 0
while user_Number >0:
    if user_Number % 2 == 0:
        # print("even number",user_Number)
        sum += user_Number
    # print(user_Number)
    user_Number-=1
print("total sum of even number", sum)