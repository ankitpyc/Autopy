import click
from colorama import Fore,Back
import base64
@click.command()
@click.option('--userid', prompt='[Facebook]Your user id please or registered phone no')
@click.password_option()
@click.option("--wishtime",prompt="Enter your Wish Time")
def Update(userid,password,wishtime):
	f = open('FaceBir/Authentication.py', 'w' )
	f.write("Facebook_User_Id = "+'"'+str(base64.b64encode(userid))+'"' +"\n")
	f.write("Facebook_Password = "+'"'+str(base64.b64encode(password))+'"' +"\n")
	f.write("wish_time = "+'"'+str(wishtime)+'"' +"\n")
	f.close()
	print Back.GREEN+'Changes Saved Successfully'