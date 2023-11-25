drive = input('你有開過車嗎')
if drive != '有' and drive != '沒有':
	print('不要亂打')
age = input('你的年齡')
age = int(age)
if drive == '有':
	if age >= 18:
		print('棒棒')
	else:
		print('what???')
elif drive == '沒有':
	if age >= 18:
		print('哈哈')
	else:
		print('good~')
