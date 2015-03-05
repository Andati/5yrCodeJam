
"""5yrCodeJam.py: Solves the supplementary problem for #5yrCodeJam. Answer is: 58837602739217760256"""

__author__  = "Rodgers Andati"
__email__ = "andatirodgers@gmail.com"
__version__ = "1.0"

import time, math

def sum_nums(n):
    sum_nums = 0
    while n > 0:
        (n, last_num) = (n / 10, n % 10)
        sum_nums += last_num
    return sum_nums


if __name__ == '__main__':
	special_nums = []
	for i in range(2, 245):
		temp_num = i
		for j in range(2, 25):
			temp_num *= i
			if sum_nums(temp_num) == i:
				special_nums.append(temp_num)
			if len(special_nums) > 95:
				break
		if len(special_nums) > 95:
			special_nums.sort()
			print str(special_nums[78])[20:]
			break




