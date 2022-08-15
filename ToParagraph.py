import re
import os
import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-r", "--read", help="input txt file", type=str, default='trash.txt')
	parser.add_argument("-w", "--write", help="output txt file",type=str, default="rubbish.txt")
	args = parser.parse_args()
	except_list = [('onshelf', 'on-shelf'), ('shortterm', 'short-term'), ('longterm', 'long-term')]

	with open(args.read, 'r') as f:
		with open(args.write, 'w') as ff:
			tmp_p = ""
			for line in f:
				l = line
				if l=="\n":
					tmp_p = tmp_p.replace("\n", ' ')
					tmp_p = tmp_p.replace("- ", '')
					for r, s in except_list:
						tmp_p = tmp_p.replace(r, s)
					ff.write(tmp_p)
					ff.write('\n\n')
					tmp_p = ""
				else:
					tmp_p += l

			tmp_p = tmp_p.replace("\n", ' ')
			tmp_p = tmp_p.replace("- ", '')
			for r, s in except_list:
				tmp_p = tmp_p.replace(r, s)
			ff.write(tmp_p)

if __name__ == '__main__':
	main()