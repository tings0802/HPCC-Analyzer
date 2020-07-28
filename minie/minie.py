#!/usr/bin/python3

import os, argparse
from datetime import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt

def parse(targets, path='./example/log.lammps'):
	time = []
	data = {}
	for i in targets:
		data[i] = []

	with open(path, 'r') as file:
		for line in file:
			pieces = line.split()
			for i in range(len(pieces)):
				if pieces[i] in targets:
					data[pieces[i]].append(float(pieces[i + 2]))
				elif pieces[i] == 'Step':
					time.append(int(pieces[i + 1]))

	return pd.DataFrame(data, index=time)

def save(data, path=dt.now().strftime(f'EM%y%m%d%H%M%S.csv')):
	data.to_csv(path)

def plot(data, path=dt.now().strftime(f'EM%y%m%d%H%M%S.png'), xlabel='', ylabel='', title=''):
	plt.cla()
	ax = data.plot()
	ax.set_title(title)
	ax.set_xlabel(xlabel)
	ax.set_ylabel(ylabel)
	plt.savefig(path)

def prep():
	parser = argparse.ArgumentParser(prog='minie.py')
	parser.add_argument(
		'input',
		help='specify the input file'
	)
	parser.add_argument(
		'-v', '--verbose',
		help='print data as tablular format verbosely',
		action='store_true'
	)
	parser.add_argument(
		'--cfg',
		metavar='<file>',
		help='specify the configuration file, default: config.txt',
		default='config.txt'
	)
	parser.add_argument(
		'--csv',
		metavar='<file>',
		help='specify the csv file path, default: EM[timestamp].csv',
		default=dt.now().strftime(f'EM%y%m%d%H%M%S.csv')
	)
	parser.add_argument(
		'--png',
		metavar='<file>',
		help='specify the png file path, default: EM[timestamp]-[type].png',
		default=dt.now().strftime(f'EM%y%m%d%H%M%S.png')
	)

	args = parser.parse_args()

	if not os.path.isfile(args.input):
		raise argparse.ArgumentTypeError(f'input file {args.input} is invalid')

	if not os.path.isfile(args.cfg):
		raise argparse.ArgumentTypeError(f'input file {args.cfg} is invalid')

	return args
	
def setpath(filename, extension='', postfix=''):
	path = f'{os.path.splitext(filename)[0]}-{postfix}.{extension}'
	if os.path.exists(path):
		raise argparse.ArgumentTypeError(f'{path} has already existed')
	return path

def main():
	args = prep()

	with open(args.cfg, 'r') as file:
		targets = (''.join(file.readlines())).split()
	data = parse(targets, args.input)

	save(data, setpath(args.csv, extension='csv'))

	for i in targets:
		plot(data[i], setpath(args.png, postfix=i, extension='png'),
			xlabel='time', ylabel=i, title='Energy minimization')

	if args.verbose:
		print(data)

if __name__ == '__main__':
	main()
