def add_time(start, duration, day =''):
  new_time = ''
  new_days = 0
  # start time and duration
  initial_time = start.split()
  start_time = initial_time[0].split(':')
  duration_time = duration.split(':')
  # adding hour and minutes of start and duration to be added
  new_hour = int(start_time[0])+ int(duration_time[0])
  new_min = int(start_time[1])+ int(duration_time[1])
  # checking if new minute > 60 and add it to hour
  if (new_min /60) >= 1:
    new_hour = new_hour + int(new_min/60)
    new_min = new_min % 60
  elif (new_min /60) < 1:
    new_hour = new_hour 
    new_min = new_min % 60
    # checking for increase in days
  if initial_time[1] == 'AM':
    new_day = int(new_hour/24) 
  elif initial_time[1] == 'PM':
    new_day = int(new_hour/12)
    if new_day >= 1:
      new_day = int(new_hour/24) + 1
# changing am to pm vice versa when crossing 12 and mainting 12 division clock
  if initial_time[1] == 'AM':
    if (new_hour%24) > 12:
      new_suff = 'PM'
      new_hour = (new_hour%24)-12
    elif (new_hour%24) == 12:
      new_suff = 'PM'
      new_hour = (new_hour%24)
    elif (new_hour%24) < 12:
      new_suff = 'AM'
      new_hour = (new_hour%24)
  elif initial_time[1] == 'PM':
    if (new_hour%24) > 12:
      new_suff = 'AM'
      new_hour = (new_hour%24)-12
    elif (new_hour%24) == 12:
      new_suff = 'AM'
      new_hour = (new_hour%24)
    elif (new_hour%24) < 12:
      new_suff = 'PM'
      new_hour = (new_hour%24)
# for name of the day in case day is given  
  day_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
  # increament in day name due to increase in day due to addition
  for days in day_week:
    if day_week[day_week.index(days)].upper() == day.upper():
      new_days = day_week.index(days)  + new_day
  # maintaining the code so that with increase in day, day name also changes accordingly
  if new_days > 6:
    new_days = int((new_days+1)%7) -1
  # incase day is given and increament in days is >1 return
  if day != '' and new_day > 1:
    new_time = str(new_hour) + ':' + str(new_min).rjust(2,'0') + " " + new_suff + ',' +' ' +  day_week[new_days] + ' ' + '(' + str(new_day) + ' days later)'
    return new_time
  # incase  day is not given and increament in days is <1 return
  elif day == '' and new_day < 1:
    new_time = str(new_hour) + ':' + str(new_min).rjust(2,'0') + " " + new_suff
    return new_time
  # incase day is  given and increament in days is <1 return
  elif day != '' and new_day < 1:
    new_time = str(new_hour) + ':' + str(new_min).rjust(2,'0') + " " + new_suff + ',' +' ' +  day_week[new_days]
    return new_time
 # incase day is  given and increament in days is ==1 return
  elif  day != '' and new_day == 1:
    new_time = str(new_hour) + ':' + str(new_min).rjust(2,'0') + " " + new_suff + ',' +' ' +  day_week[new_days] + ' ' + '(' + 'next day)'
    return new_time
# incase day is not given and increament in days is ==1 return
  elif day == '' and new_day == 1:
    new_time = str(new_hour) + ':' + str(new_min).rjust(2,'0') + " " + new_suff + ' (next day)'
    return new_time
  # incase day is not given and increament in days is >1 return
  elif day == '' and new_day > 1:
    new_time = str(new_hour) + ':' + str(new_min).rjust(2,'0') + " " + new_suff + ' (' + str(new_day) + ' days later)'
    return new_time
  # completed the time calculator
  
    
    
  
  
      
  
  
      
    
    
    





  