import random
start = input('請決定隨機數字範圍開始值:')
start = int(start)
end = input('請決定隨機數字範圍結束值:')
end = int(end)
r = random.randint(start , end)
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
