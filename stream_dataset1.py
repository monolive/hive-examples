#!/usr/bin/python
#
# Write to HDFS directly by 
# python stream_dataset1.py | hdfs dfs -put - refData.txt

import logging
import argparse
import random
import sys

def main():
	#output = open('dataset_1.txt', 'w')
	for i in xrange(1, 30):		
		toto = '{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18},{19},{20},{21},{22},{23},{24},{25},{26},{27},{28},{29},{30},{31},{32},{33},{34},{35}'\
		.format(str(i).zfill(10),\
		str('%08x' % random.randrange(16**8)),str('%08x' % random.randrange(16**8)),\
		str('%08x' % random.randrange(16**8)),str('%08x' % random.randrange(16**8)),\
		str(random.randint(0,99)).zfill(2),str(random.randint(0,99)).zfill(2),\
		str(random.randint(0,99)).zfill(2),str(random.randint(0,99)).zfill(2),\
		str(random.randint(0,99)).zfill(2),str(random.randint(0,99)).zfill(2),\
		str(random.randint(0,99)).zfill(2),str(random.randint(0,99)).zfill(2),\
		str(random.randint(0,99)).zfill(2),str(random.randint(0,99)).zfill(2),\
		str(random.randint(0,99)).zfill(2),str(random.randint(0,99)).zfill(2),\
		str(random.randint(0,99)).zfill(2),str(random.randint(0,99)).zfill(2),\
		str(random.randint(0,99)).zfill(2),str(random.randint(0,99)).zfill(2),\
		str(random.randint(0,99999999)).zfill(8),str(random.randint(0,99999999)).zfill(8),\
		str(random.randint(0,99999999)).zfill(8),str(random.randint(0,99999999)).zfill(8),\
		str(random.randint(0,99999999)).zfill(8),str(random.randint(0,99999999)).zfill(8),\
		str(random.randint(0,99999999)).zfill(8),str(random.randint(0,99999999)).zfill(8),\
		str(random.randint(0,99999999)).zfill(8),str(random.randint(0,99999999)).zfill(8),\
		str(random.randint(0,99999999)).zfill(8),str(random.randint(0,99999999)).zfill(8),\
		str(random.randint(0,99999999)).zfill(8),str(random.randint(0,99999999)).zfill(8),\
		str(random.randint(0,99999999)).zfill(8),str(random.randint(0,99999999)).zfill(8),\
		str(random.randint(0,99999999)).zfill(8),str(random.randint(0,99999999)).zfill(8))
		print toto
	

if __name__ == "__main__":
	main()
	#logger.info('Finished data generation successfully')
	sys.exit(0)