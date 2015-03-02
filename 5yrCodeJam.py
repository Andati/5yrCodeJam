
"""5yrCodeJam.py: Solves the Kitakale Kingdom Break-in problem for #5yrCodeJam. Answer is: 0.9462000000"""

__author__  = "Rodgers Andati"
__email__ = "andatirodgers@gmail.com"
__version__ = "1.0"


def okoa_kitakale_kingdom(key):
	letters_map = {} # store count of whether the letters are even or odd
	for c in key:
		letters_map[c]=letters_map.setdefault(c,0) ^ 1 # toggle the count between even and odd i.e 0 is even, 1 is odd

	total = sum(letters_map.values()) # total of even or odd flag

	if len(key) % 2 == 0: # if length of string is even
		return True if total == 0 else False
	else: # if length of string is odd
		return True if total == 1 else False


if __name__ == '__main__':	
	# open key_bag.txt file for reading the keys
	with open('key_bag.txt', 'r') as key_bag_file:
		# split the keys which are comma separated
		keys = key_bag_file.read().split(',')
		valid_keys = 0 # to store num of valid keys
		# iterate to count the number of valid keys
		for key in keys:
			if okoa_kitakale_kingdom(key.strip('"')) == True:
				valid_keys += 1 # increase count of valid keys

		print "%.10f" % ((10000 - valid_keys) / 10000.0)