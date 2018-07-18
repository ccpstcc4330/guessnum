import random

r = random.randint(1,100)
count = 0
while True:
	count += 1 # count = count + 1
	n = input('請猜一個數字:')
	n = int(n)
	if n == r:
		print('終於猜對了!')
		break
	elif n > r:
		print('比答案大')
	elif n < r:
		print('比答案小')
	print('這是你猜的第', count, ' 次')
