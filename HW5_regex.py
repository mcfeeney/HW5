import re

nums= []
fname= open("regex_sum_35654.txt", "r")
for line in fname:
	y = re.findall('[0-9]+',line)
	
	for num in y:
		nums.append(int(num))

# print (nums)
sums= sum(nums)
print (sums)

