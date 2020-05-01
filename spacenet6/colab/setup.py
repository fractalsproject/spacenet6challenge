
# These are the prereq commands that get individual invoked in the ipython session and checked.
_prereq_cmds = '''\
pip install affine>=2.3.0 && echo "OK affine"
pip install albumentations==0.4.3 && echo "OK albumentations"
pip install fiona>=1.7.13 && echo "OK fiona"
pip install geopandas>=0.7.0 && echo "OK geopandas"
pip install matplotlib>=3.1.2 && echo "OK matplotlib"
pip install networkx>=2.4 && echo "OK networkx"
pip install opencv-python>=4.1 && echo "OK opencv"
pip install pandas>=0.25.3 && echo "OK pandas"
pip install pyproj>=2.1 && echo "OK pyproj"
pip install pyyaml==5.2 && echo "OK pyyaml"
pip install rasterio>=1.0.23 && echo "OK rasterio"
pip install requests==2.22.0 && echo "OK requests"
pip install rtree>=0.9.3 && echo "OK rtree"
pip install scikit-image>=0.16.2 && echo "OK scikit-image"
pip install scipy>=1.3.2 && echo "OK scipy"
pip install torchvision>=0.5.0 && echo "OK torchvision"
pip install tqdm>=4.40.0 && echo "OK tqdm"
pip install urllib3>=1.25.7 && echo "OK urllib3"
sudo apt-get install -y software-properties-common && echo "OK"
sudo add-apt-repository -y ppa:ubuntugis/ppa && apt-get -y update && echo "OK"
sudo apt-get install -y libspatialindex-dev python-rtree gdal-bin && echo "OK"
sudo apt-get install -y build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev && echo "OK"
sudo apt-get install -y libgdal-dev && echo "OK"
sudo gdal-config --version && echo "OK"
pip install gdal>=3.0.2 && echo "OK gdal"
cp /content/spacenet6challenge/solaris_req_adj.txt /content/spacenet6challenge/solaris/requirements.txt && cd /content/spacenet6challenge/solaris && python setup.py install && echo "OK"
'''

def checkjupyter(version=False):
	print("Checking for jupyter/ipython environment...")
	try:
		from IPython import get_ipython
		ipython = get_ipython()
		return ipython
	except:
		return False

	print("Passed.")

def checkcolab(version=False):
	print("Checking for Colab environment...")
	import os
	if not os.path.exists("/content"):
		return False
	print("Passed.")

def runcmds(ipython, lines):
	cmds = [ cmd for cmd in lines.split("\n") if not cmd=="" ]
	for cmd in cmds:
		print( "Running command: \"%s\".  Please wait..." % cmd )
		outputs = ipython.getoutput( cmd )
		#print(outputs)
		if any( [ outp.startswith("OK") for outp in outputs ] ):
			print("OK.")
		else:
			print("Command Failed.")
			return False

def prereqs():

	# verify its jupyter
	ipython = checkjupyter()
	if ipython == False: raise Exception("This is not a jupyter notebook.")

	# verify its colab 
	if not checkcolab(): raise Exception("This is not a Colab notebook.")

	# run prereq shell commands
	status = runcmds( ipython, _prereq_cmds )
	if not status: raise Exception("Could not install all prerequisite packages.")
