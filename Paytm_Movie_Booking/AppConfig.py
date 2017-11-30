
'''' Constants '''
from gi.repository import Notify,GdkPixbuf
App_Name = "Paytm_Movie_Checker"
Paytm_Base_Url = "https://paytm.com" 
Paytm_Url = "https://paytm.com/movies/bhopal"
def Init_Notificaton():
	notification = Notify.Notification.new("Movies Nearby","Watch Some of Your favorite shows")
	image = GdkPixbuf.Pixbuf.new_from_file("paytm.jpg")
	notification.set_icon_from_pixbuf(image)
	notification.set_image_from_pixbuf(image)
	return notification

