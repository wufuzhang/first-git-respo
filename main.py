import os,sys
import pdb

if len( sys.argv) <2:
	print "usage : python main.py <your-name>" 
	exit()

print "This is %s's first python program" % sys.argv[1]
print "Add a new line to see if the server will be sync"

