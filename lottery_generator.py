# ## Write a program that asks the user how many “quick picks” they wish to generate. The program then
# generates that many lines of output. Each line consists of six random numbers between 1 and 45.
# Each line should not contain any repeated number. Each line of numbers should be displayed in
# ascending order.
# Your code should produce output that matches the sample output (except the numbers are random):
# How many quick picks? 5
# 9 10 11 32 38 44
# 2 9 12 14 28 30
# 5 10 16 22 35 42
# 1 2 16 22 37 40
# 1 17 20 23 25 27

import random

def main():
    quick_pick = int(input("How many quick picks would you like?"))

    count = 0
    while count < quick_pick:
        lottery_picks = lottery_pick_gen()
        print(sorted(lottery_picks))
        count += 1

def lottery_pick_gen():

    picks = []

    while len(picks) < 6:
        num = random.randint(1,45)
        if num not in picks:
            picks.append(num)
    return picks

main()

#mon = 8-6 = 9
#tue = 12:30-9:30 = 8
#wen = 0
#thur = 10:30-21:30 = 10
#fri = 0
#sat = 5
#sun = 7-6 =10
#42