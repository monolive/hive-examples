#!/usr/bin/python

import logging
import argparse
import random
import sys

def main():
	output = open('dataset_1.txt', 'w')
	for i in xrange(1, 3000000000):		
		toto = '{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18},{19},{20},{21},{22},{23},{24},{25},{26},{27},{28},{29},{30},{31},{32},{33},{34},{35}\n'\
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
		output.write(str(toto))
	output.close()


	output = open('dataset_2.txt', 'w')
	gen_file_2(1,500000000,166666666,output)
	gen_file_2(500000001,1000000000,166666666,output)
	gen_file_2(1000000001,1500000000,166666666,output)
	gen_file_2(1500000001,2000000000,166666666,output)
	gen_file_2(2000000001,2500000000,166666666,output)
	gen_file_2(2500000001,3000000000,166666670,output)
	output.close()

def gen_file_2(min,max,amount,output_file):
	for i in random.sample(xrange(min,max),amount):		
		toto = ('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18},{19},{20},{21},{22},{23},{24},{25},{26},{27},{28},{29},{30},{31},{32},{33},{34},{35}' +
		'{36},{37},{38},{38},{39},{40},{41},{42},{43},{44},{45},{46},{47},{48},{49},{50},{51},{52},{53},{54},{55},{56},{57},{58},{59},{60},{61},{62},{63},{64},{65},{66},{67},{68},{69},' +
		'{70},{71},{72},{73},{74},{75},{76},{77},{78},{79},{80},{81},{82},{83},{84},{85},{86},{87}\n')\
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
		output_file.write(str(toto))
	

if __name__ == "__main__":
	main()
	#logger.info('Finished data generation successfully')
	sys.exit(0)