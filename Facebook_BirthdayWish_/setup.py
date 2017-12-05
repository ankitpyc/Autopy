from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install
import base64
class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
		username = base64.b64encode(raw_input("Enter your facebook username : "))
		password = base64.b64encode(raw_input("Enter your facebook password : "))
		f = open('Fb_Birthday/Authentication.py', 'w' )
		f.write("Facebook_User_Id = "+'"'+str(username)+'"' +"\n")
		f.write("Facebook_Password = "+'"'+str(password)+'"' +"\n")
		f.close()
		print "Updated Credentials ..."
		

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
    	import Fb_Birthday.Facebook_Creds as creds 

        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        install.run(creds.Add_Credentials())



setup(name='Facebook Birthday Wish',
      version='0.1',
      description='Schedule your Birthday wishes for your facebook friends and never Miss any birthdays',
      url='http://github.com/storborg/funniest',
      author='Ankit Mishra',
      packages=['Fb_Birthday'],
      cmdclass = {
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    	'cron_job_setup' : setCronJob
    	},
      author_email='ankitmishra@gmail.com',
      license='MIT',
      install_requires=['python-crontab'],
      zip_safe=False)


