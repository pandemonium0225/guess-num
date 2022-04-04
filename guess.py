import random

r = random.randint(1,100)
while True:
	guess_num = 0
	num = int(input('請猜數字: '))
	if num == r:
		print("你猜中了!!!")
		break
	elif num > r:
		print("不對喔!!! 比答案大")
	elif num < r:
		print("不對喔!!! 比答案小")