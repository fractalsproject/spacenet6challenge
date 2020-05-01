from IPython import get_ipython

_aptget = "sudo apt-get install libgdal-dev libspatialindex-dev python-rtree gdal-bin build-essential"

def prereqs():
	python = get_ipython()
	#dir(ipython)
	outp = ipython.system("echo 'Running Command %s'" % _aptget )
	print(outp)	

