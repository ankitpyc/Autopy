App_Name = "Facebook_Birthday_Wish"
Base_Url = "https://facebook.com" 
Event_Url = "https://www.facebook.com/events/birthdays/"

def Add_Credentials():
	username = base64.b64encode(raw_input("Enter your facebook username"))
	password = base64.b64encode(raw_input("Enter your facebook username"))
	f = open( 'Authentication.py', 'w' )
	f.write("Facebook_User_Id = "+str(username)+"\n")
	f.write("Facebook_Password = "+str(password)+"\n")
	f.close()
	print "Updated Credentials"