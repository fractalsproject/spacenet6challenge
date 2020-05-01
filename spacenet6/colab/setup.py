from IPython import get_ipython

_init_apt_get = "sudo apt-get install libgdal-dev libspatialindex-dev python-rtree gdal-bin build-essential"

_pip_ext = '''
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
'''

_gdal = '''
sudo apt-get install -y software-properties-common
sudo add-apt-repository ppa:ubuntugis/ppa && apt-get update && apt-get update
sudo apt-get install -y build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev
sudo apt-get install -y gdal-bin
sudo apt-get install -y libgdal-dev
sudo gdal-config --version
'''

def prereqs():
	# verify its a notebook ( and version )
	ipython = get_ipython()
	# TODO

	# verify its colab ( and version )
	# TODO

	# do apt-get installs
	outp= ipython.system("echo 'Running system command: \"%s\"'.  Please wait..." % _init_apt_get )
	#print(outp, type(outp))
	outp = ipython.system( _init_apt_get )
	#print(outp, type(outp))

	# do (external) pip installs
	cmds = [ cmd for cmd in _pip_ext.split("\n") if not cmd=="" ]
	print(cmds)
	for cmd in cmds:
		outp = ipython.system("echo 'Running pip command: \"%s\"'.  Please wait..." % cmd )

		outp = ipython.system( cmd )
