''' sets the Cronjobs for Automation of Birthday Wish on Every Night 12:10 '''


from crontab import CronTab
my_cron = CronTab('root')
is_scheduled = False
for job in my_cron:
	if (job.comment == 'FBCRON'):
		print "scheduling facebook automation"
		is_scheduled = True
if(not(is_scheduled)):
	job = my_cron.new(command='env DISPLAY=:0  xclock',comment='FBCRON')
	print " writing new job"
	my_cron.write()    
	print " job written"
else:
	print "job already exsist"
