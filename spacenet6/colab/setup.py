from IPython import get_ipython

_aptget = "sudo apt-get install libgdal-dev libspatialindex-dev python-rtree gdal-bin build-essential"

def prereqs():
	ipython = get_ipython()
	#dir(ipython)
	outp = ipython.system("echo 'Running Command "%s"'.  Please wait..." % _aptget )
	print(outp, type(outp))
	outp = ipython.system( _apt_get )
	print(outp, type(outp))

