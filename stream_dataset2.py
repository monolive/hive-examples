#!/usr/bin/python
#
# Write to HDFS directly by 
# python stream_dataset2.py | hdfs dfs -put - newData.txt

import logging
from optparse import OptionParser
import random
import sys

def cmd_line_arg():
	parser = OptionParser()
	parser.add_option("-o", "--output", type="string", dest="output", help="output file")
	parser.add_option("--min", type="int", dest="min", default="1", help="min value")
	parser.add_option("--max", type="int", dest="max", default="1000", help="max value")
	parser.add_option("--sample", type="int", dest="sample", default="10", help="how many sample in range")
	(options, args) = parser.parse_args()
	return options


def main():
	options = cmd_line_arg()
	if options.output:
		output = open(options.output, 'w')


	for i in random.sample(xrange(options.min,options.max),options.sample):		
		toto = ('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18},{19},{20},{21},{22},{23},{24},{25},{26},{27},{28},{29},{30},{31},{32},{33},{34},{35}' +
		'{36},{37},{38},{38},{39},{40},{41},{42},{43},{44},{45},{46},{47},{48},{49},{50},{51},{52},{53},{54},{55},{56},{57},{58},{59},{60},{61},{62},{63},{64},{65},{66},{67},{68},{69},' +
		'{70},{71},{72},{73},{74},{75},{76},{77},{78},{79},{80},{81},{82},{83},{84},{85},{86},{87}')\
		.format(str(i).zfill(10),\
		'%08x' % random.randrange(16**8),'%08x' % random.randrange(16**8),\
		'%08x' % random.randrange(16**8),'%08x' % random.randrange(16**8),\
		str(random.randint(0,99999999)).zfill(8),str(random.randint(0,99999999)).zfill(8),\
		str(random.randint(0,99999999)).zfill(8),str(random.randint(0,99999999)).zfill(8),\
		str(random.randint(0,99999999)).zfill(8),str(random.randint(0,99999999)).zfill(8),\
		str(random.randint(0,99999999)).zfill(8),str(random.randint(0,99999999)).zfill(8),\
		str(random.randint(0,99999999)).zfill(8),str(random.randint(0,99999999)).zfill(8),\
		str(random.randint(0,99999999)).zfill(8),str(random.randint(0,99999999)).zfill(8),\
		str(random.randint(0,99999999)).zfill(8),str(random.randint(0,99999999)).zfill(8),\
		str(random.randint(0,99999999)).zfill(8),str(random.randint(0,99999999)).zfill(8),\
		str(random.randint(0,99999999)).zfill(8),str(random.randint(0,99999999)).zfill(8),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip(),\
		str('%08x' % random.randrange(16**20)).strip(),str('%08x' % random.randrange(16**20)).strip())
		
		if options.output:
			output.write(str(toto + '\n'))
		else:
			print toto
	

if __name__ == "__main__":
	main()
	#logger.info('Finished data generation successfully')
	sys.exit(0)