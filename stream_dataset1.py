#!/usr/bin/python
#
# Write to HDFS directly by 
# python stream_dataset1.py | hdfs dfs -put - refData.txt

from optparse import OptionParser
import random
import sys

def cmd_line_arg():
	parser = OptionParser()
	parser.add_option("-o", "--output", type="string", dest="output", help="output file")
	parser.add_option("--min", type="int", dest="min", default="1", help="min value")
	parser.add_option("--max", type="int", dest="max", default="1000", help="max value")
	(options, args) = parser.parse_args()
	return options

def main():
	options = cmd_line_arg()
	if options.output:
		output = open(options.output, 'w')

	for i in xrange(options.min, options.max):		
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
		if options.output:
			output.write(str(toto + '\n'))
		else:
			print toto
	

if __name__ == "__main__":
	main()
	sys.exit(0)