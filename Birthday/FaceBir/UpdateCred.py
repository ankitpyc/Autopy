import click
from colorama import Fore,Back,Style
import base64
@click.command()
@click.option('--userid', prompt='[Facebook]Your user id please or registered phone no')
@click.password_option()
@click.option("--wishtime",prompt="Enter your Wish Time")
def Update(userid,password,wishtime):
	f = open('Authentication.py', 'w' )
	f.write("Facebook_User_Id = "+'"'+str(base64.b64encode(userid))+'"' +"\n")
	f.write("Facebook_Password = "+'"'+str(base64.b64encode(password))+'"' +"\n")
	f.write("wish_time = "+'"'+str(wishtime)+'"' +"\n")
	f.close()
	print ""
	print Fore.GREEN+'Changes Saved Successfully'
	print(Style.RESET_ALL)
	print "\n"
