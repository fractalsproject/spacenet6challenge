
a = '''
!sudo apt-get install -y software-properties-common
!sudo add-apt-repository ppa:ubuntugis/ppa && apt-get update && apt-get update
!sudo apt-get install -y build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev
!sudo apt-get install -y gdal-bin
!sudo apt-get install -y libgdal-dev
!sudo gdal-config --version
'''

print( a.split("\n") )
