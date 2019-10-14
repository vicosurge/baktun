x = 1872000
leap = 0
years = 0
while x >= 0:
	if leap == 4:
		x -= 366
		leap = 0
		years += 1
		print(years,leap,x)
	else:
		x -= 365
		leap += 1
		years += 1
print(years,years-3115,(years-3115)+leap,leap,x)