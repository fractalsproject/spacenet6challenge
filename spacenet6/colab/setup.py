
# These are the prereq commands that get individual invoked in the ipython session and checked.
_prereq_cmds = '''\
pip install affine>=2.3.0 
pip install albumentations==0.4.3
pip install fiona>=1.7.13 
pip install geopandas>=0.7.0
pip install matplotlib>=3.1.2
pip install networkx>=2.4 
pip install opencv-python>=4.1
pip install pandas>=0.25.3 
pip install pyproj>=2.1 
pip install pyyaml==5.2
pip install rasterio>=1.0.23
pip install requests==2.22.0
pip install rtree>=0.9.3 
pip install scikit-image>=0.16.2
pip install scipy>=1.3.2 
pip install torchvision>=0.5.0
pip install tqdm>=4.40.0 
pip install urllib3>=1.25.7
sudo apt-get install -y software-properties-common 
sudo add-apt-repository -y ppa:ubuntugis/ppa && apt-get -y update
sudo apt-get install -y libspatialindex-dev python-rtree gdal-bin
sudo apt-get install -y build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev
sudo apt-get install -y libgdal-dev 
sudo gdal-config --version 
pip install gdal>=3.0.2 
cp /content/spacenet6challenge/solaris_setup_adj.py /content/spacenet6challenge/solaris/setup.py && cd /content/spacenet6challenge/solaris && python setup.py install
'''

def checksolaris(version=False):

	# We assume if we can import solaris then all the dependencies 
	# were already dealt with
	try:
		import solaris
		return True
	except:
		return False

def checkjupyter(version=False):
	print("Checking for jupyter/ipython environment...")
	try:
		from IPython import get_ipython
		ipython = get_ipython()
		print("Passed.")
		return ipython
	except:
		return False

def checkcolab(version=False):
	print("Checking for Colab environment...")
	import os
	if not os.path.exists("/content"):
		return False
	else:
		print("Passed.")
		return True

def runcmds(ipython, lines):
	cmds = [ cmd for cmd in lines.split("\n") if not cmd=="" ]
	for cmd in cmds:
		print( "Running command: \"%s\".  Please wait..." % cmd )
		outputs = ipython.getoutput( cmd + ' && echo "OK."' )
		#print(outputs)
		if any( [ outp.startswith("OK") for outp in outputs ] ):
			print("OK.")
		else:
			print("Command Failed.")
			return False
	return True

def prereqs(force=False):

	# check if we already ran this successfully
	if not force and checksolaris():
		print("It looks like prerequisites may have already been installed. Pass force=True to force it.")
		return True	

	# verify its jupyter
	ipython = checkjupyter()
	if ipython == False: raise Exception("This is not a jupyter notebook.")

	# verify its colab 
	if not checkcolab(): raise Exception("This is not a Colab notebook.")

	# run prereq shell commands
	status = runcmds( ipython, _prereq_cmds )
	if not status: raise Exception("Could not install all prerequisite packages.")

	print("All prereqs hav been installed.")	
	return True
