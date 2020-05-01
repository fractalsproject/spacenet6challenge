from IPython import get_ipython

_apt_get = "sudo apt-get install libgdal-dev libspatialindex-dev python-rtree gdal-bin build-essential"

def prereqs():
	# verify its a notebook ( and version )
	ipython = get_ipython()
	# TODO

	# verify its colab ( and version )
	# TODO

	# do apt-get installs
	outp = ipython.system("echo 'Running system command: \"%s\"'.  Please wait..." % _apt_get )
	print(outp, type(outp))
	outp = ipython.system( _apt_get )
	print(outp, type(outp))

	# do (external) pip installs
