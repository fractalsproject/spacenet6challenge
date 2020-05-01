from google.colab import auth
import os

def checkjupyter(version=False):
        print("Checking for jupyter/ipython environment...")
        try:
                from IPython import get_ipython
                ipython = get_ipython()
                print("Passed.")
                return ipython
        except:
                return False

def checkcolab():
	print("Checking for colab environment...")
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

	ipython = checkjupyter()
	if not ipython: raise Exception("This is not a jupyter environment.")

	if not checkcolab(): raise Exception("This is not a colab environment.")

	if force_new_mount and os.path.exists("/content/mountOnColab"):
		runcmds( ipython, "fusermount -u mountOnColab" )
		runcmds( ipython, "rmdir mountOnColab" )

	if not os.path.exists("/content/mountOnColab"):
		print("Trying to authenticate GCP user...")
		auth.authenticate_user()
		runcmds( ipython, 'echo "deb http://packages.cloud.google.com/apt gcsfuse-bionic main" > /etc/apt/sources.list.d/gcsfuse.list')
		runcmds( ipython, 'curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - ' )
		runcmds( ipython, 'apt -qq update')
		runcmds( ipython, 'apt -qq install gcsfuse')
		runcmds( ipython, 'mkdir mountOnColab')
		runcmds( ipython, "gcsfuse --implicit-dirs %s mountOnColab" % bucket_name )
		print("Done. Getting folder contents...")
		runcmds( ipython, "ls -als /content/mountOnColab")
	else:
		print("The locat folder mount exists.  Remounting remote system just in case...")
		runcmds( ipython, "fusermount -u mountOnColab")
		runcmds( ipython, "rmdir mountOnColab")
		runcmds( ipython, "mkdir mountOnColab")
		runcmds( ipython, "gcsfuse --implicit-dirs %s mountOnColab" % bucket_name)
		print("Done. Getting folder contents...")
		runcmds(ipython,  "ls -als /content/mountOnColab")

	return True
