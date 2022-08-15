import re
import os
import argparse

texs = list()

def get_bib(path):
	bib = set()
	dup = set()
	with open(path, 'r') as f:
		for line in f:
			if line[0]=='@':
				b = line.split('{')[1].split(',')[0].strip()
				if b in bib:
					dup.add(b)
				bib.add(b)
	return bib, dup

def get_tex(path):
	fs = os.listdir(path)
	for f in fs:
		if os.path.isdir(os.path.join(path, f)):
			get_tex(os.path.join(path, f))
		elif f[-4:]=='.tex':
			texs.append(os.path.join(path, f))

def get_txt(path):
	used = set()
	get_tex(path)
	for f in texs:
		with open(f, 'r') as ff:
			for line in ff:
				ans = re.findall("cite\{([A-Za-z0-9,]*)\}", line)
				for a in ans:
					a = a.split(',')
					for b in a:
						if b!='':
							used.add(b.strip())
	return used


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", "--dir", help="dir contains .tex files", type=str, default='./tex')
	parser.add_argument("-b", "--bib", help="bib text files",type=str, default="bib.txt")
	args = parser.parse_args()

	bib, bad = get_bib(args.bib)
	used = get_txt(args.dir)
	print("total reference in bib file:")
	print(len(bib))
	print("")
	print("total reference in tex file:")
	print(len(used))
	print("")
	print("redundent reference in bib file:")
	print(bib-used)


if __name__ == '__main__':
	main()