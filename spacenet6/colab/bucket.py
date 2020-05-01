from google.colab import auth
import os

def checkcolab():
	if not os.path.exists("/content"):
		return False
	else:
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

def mount(bucket_name, force_new_mount=False):

	if force_new_mount and os.path.exists("/content/mountOnColab"):
		runcmds( "fusermount -u mountOnColab" )
		runcmds( "rmdir mountOnColab" )

	if not os.path.exists("/content/mountOnColab"):
		print("Trying to authenticate GCP user...")
		auth.authenticate_user()
		runcmds('echo "deb http://packages.cloud.google.com/apt gcsfuse-bionic main" > /etc/apt/sources.list.d/gcsfuse.list')
		runcmds('curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - ' )
	  	runcmds('apt -qq update')
	  	runcmds('apt -qq install gcsfuse')
	  	runcmds('mkdir mountOnColab')
	  	runcmds("gcsfuse --implicit-dirs %s mountOnColab" % bucket_name )
	  	print("Done. Getting folder contents...")
	  	runcmds("ls -als /content/mountOnColab
	else:
		print("The locat folder mount exists.  Remounting remote system just in case...")
		runcmds("fusermount -u mountOnColab")
		runcmds("rmdir mountOnColab")
		runcmds("mkdir mountOnColab")
		runcmds("gcsfuse --implicit-dirs %s mountOnColab" % bucket_name)
		print("Done. Getting folder contents...")
		runcmds("ls -als /content/mountOnColab

	return True
