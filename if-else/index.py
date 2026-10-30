number = 28

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")   


    # একাধিক শর্ত     
age = 25
has_id = True
if age >= 18 and has_id:
    print("You are eligible to vote.")

    # এক লাইনে
result = "Positive" if number > 0 else "Negative or Zero"
print(result)