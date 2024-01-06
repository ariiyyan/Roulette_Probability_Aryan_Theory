import random
userNum = int(input("what is the number you looking for to loose constantly? "))
flag = True
arrayRepeat = []
count = 0
while flag:
    count += 1
    num = random.randint(0, 100)
    print(num)
    if num % 2 == 0 and num != 0 and num != 100:
        arrayRepeat.append(num)
        if len(arrayRepeat) == userNum:
            flag = False
    else:
        arrayRepeat = []

chance = 0
chance = (1/count)*100
print(f" {count} many time played happen and the numbers of Roulette are {arrayRepeat}  ")
print(f" chance of loose on {userNum} repeatedly is = {chance} percent")