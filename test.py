
def almost_pal(str):
	score = 0
	str2 = str[::-1]
	for i in range(len(str)):
		if str2[i] != str[i]:
			score = score + 1
	return score

str = '{"z08":{"00":{"duration":0},"01":{"duration":60},"02":{"duration":60},"03":{"duration":60},"04":{"duration":60},"05":{"duration":60},"06":{"duration":0}}}'
print(len(str))
