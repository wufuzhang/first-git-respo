import os,sys
import pdb

if len( sys.argv) <2:
	print "usage : python main.py <your-name>" 
	exit()

print "This is %s's first python program" % sys.argv[1]

