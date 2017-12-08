''' sets the Cronjobs for Automation of Birthday Wish on Every Night 12:10 '''
from crontab import CronTab
from Authentication import wish_time
import os
my_cron = CronTab('root')
def set_schedule():
	is_scheduled = False
	for job in my_cron:
		if (job.comment == 'FBCRON'):
			print "scheduling facebook automation"
			is_scheduled = True
	if(not(is_scheduled)):
		job_string = []
		job = my_cron.new(command='env DISPLAY=:0  python '+os.getcwd()+'/Fb_Birthday/Happy_Birthday.py',comment='FBCRON')
		print " writing new job"
		hour = wish_time.split(":")[0]
		minute = wish_time.split(":")[1]
		job_string.append(str(minute))
		job_string.append(' '+str(hour))
		job_string.append(" * * *")

		command = ''.join(job_string)
		print command
		job.setall(command)
		my_cron.write()    
		print " job written"
	else:
		print "job already exsist"
