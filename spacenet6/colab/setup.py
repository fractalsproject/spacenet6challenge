from IPython import get_ipython

_cmds = '''
pip install affine>=2.3.0 && echo "ok affine"
pip install albumentations==0.4.3 && echo "ok albumentations"
pip install fiona>=1.7.13 && echo "ok fiona"
pip install geopandas>=0.7.0 && echo "ok geopandas"
pip install matplotlib>=3.1.2 && echo "ok matplotlib"
pip install networkx>=2.4 && echo "ok networkx"
pip install opencv-python>=4.1 && echo "ok opencv"
pip install pandas>=0.25.3 && echo "ok pandas"
pip install pyproj>=2.1 && echo "ok pyproj"
pip install pyyaml==5.2 && echo "ok pyyaml"
pip install rasterio>=1.0.23 && echo "ok rasterio"
pip install requests==2.22.0 && echo "ok requests"
pip install rtree>=0.9.3 && echo "ok rtree"
pip install scikit-image>=0.16.2 && echo "ok scikit-image"
pip install scipy>=1.3.2 && echo "ok scipy"
pip install torchvision>=0.5.0 && echo "ok torchvision"
pip install tqdm>=4.40.0 && echo "ok tqdm"
pip install urllib3>=1.25.7 && echo "ok urllib3"
sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:ubuntugis/ppa && apt-get -y update 
sudo apt-get install -y libspatialindex-dev python-rtree gdal-bin
sudo apt-get install -y build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev
sudo apt-get install -y libgdal-dev
sudo gdal-config --version 
pip install gdal>=3.0.2 && echo "ok gdal"
'''

def runcmds(ipython, lines):
	cmds = [ cmd for cmd in lines.split("\n") if not cmd=="" ]
	for cmd in cmds:
		print( "Running command: \"%s\".  Please wait..." % cmd )
		outp = ipython.getoutput( cmd )
		print(outp)

def prereqs():
	# verify its a notebook ( and version )
	ipython = get_ipython()
	# TODO

	# verify its colab ( and version )
	# TODO

	status = runcmds( ipython, _cmds )
