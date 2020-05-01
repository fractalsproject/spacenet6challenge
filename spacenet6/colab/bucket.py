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
		print("Passed.")
		return True

def runcmds(ipython, lines, errcheck=True, showoutput=False):
	cmds = [ cmd for cmd in lines.split("\n") if not cmd=="" ]
	for cmd in cmds:

		print( "Running command: \"%s\".  Please wait..." % cmd )
		outputs = ipython.getoutput( cmd + ' && echo "OK."' if errcheck else "" )
		ok = any( [ outp.startswith("OK") for outp in outputs ] )

		if errcheck and ok:
			if showoutput: print( "\n".join(outputs) )
			else: print("OK.")
			return True
		elif errcheck and not ok:
			if showoutput: print( "\n".join(outputs) )
			raise Exception("Command failed.")
		else: # not errcheck
			if showoutput: print( "\n".join(outputs) )
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
		runcmds( ipython, "ls -als /content/mountOnColab", errcheck=False, showoutput=True)
	else:
		print("The local folder mount exists.  Remounting remote system just in case...")
		runcmds( ipython, "fusermount -u mountOnColab")
		runcmds( ipython, "rmdir mountOnColab")
		runcmds( ipython, "mkdir mountOnColab")
		runcmds( ipython, "gcsfuse --implicit-dirs %s mountOnColab" % bucket_name)
		print("Done. Getting folder contents...")
		runcmds(ipython,  "ls -als /content/mountOnColab", errcheck=False, showoutput=True)

	print("Mount was successful.")
	return True
