# 该实例演示了数字猜谜游戏
import random

number = random.randrange(1, 100)
guess = -1
print("数字猜谜游戏!")
print(number)
while guess != number:
    guess = int(input("请输入你猜的数字："))

    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")
# 阿萨大手大aa
