for i in range(5):
    print(i)

for i in range(1, 5):
    print(i)    

for i in range(0, 10, 5):
    print(i)  

# সংখ্যার যোগফল

total = 0
for i in range(1, 101):
    total += i
print("The sum of numbers from 1 to 101 is:", total)  

# ans 5050 
# 
# break ও continue     
for i in range(15):
    if i == 10:
        break
    print(i)
    0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

for i in range(15):
    if i == 5:
        continue
    print(i)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 0
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14

# enumerate—সাথে নম্বর

for index, fruit in enumerate(['apple', 'banana', 'cherry']):
    print(index, fruit)

# 0 apple
# 1 banana
# 2 cherry
