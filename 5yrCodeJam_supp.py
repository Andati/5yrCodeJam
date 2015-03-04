
"""5yrCodeJam.py: Solves the supplementary problem for #5yrCodeJam."""

__author__  = "Rodgers Andati"
__email__ = "andatirodgers@gmail.com"
__version__ = "1.0"

import time, math

def sum_digits(num):
    sum_dig = 0
    while num > 0:
        (num, last) = (num / 10, num % 10)
        sum_dig += last
    return sum_dig


if __name__ == '__main__':
	special_nums = []
	for i in range(2, 400):
		temp = i
		for j in range(2, 100):
			temp *= i
			if sum_digits(temp) == i:
				special_nums.append(temp)
			if len(special_nums) > 100:
				break
		if len(special_nums) > 100:
			special_nums.sort()
			#print special_nums
			print special_nums[78]
			break




