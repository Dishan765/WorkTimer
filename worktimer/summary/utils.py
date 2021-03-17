from datetime import date,datetime,timedelta
from worktimer.models import WorkTime

#Take argument day as a datetime
#Return all dates as datetime for which the day is in
def getWeekDates(dateSelected):
  dates = [dateSelected + timedelta(days=i) for i in range(0 - dateSelected.weekday(), 7 - dateSelected.weekday())]
  return dates


#Add Two datetimes
def sumTime(t1,t2):
  time_zero = datetime.strptime('00:00:00', '%H:%M:%S')
  return (t1 - time_zero + t2)

#Argument: A list of datetimes
#Return: The amt of time worked on each datetime
def getTimesFromDb(weekDates):
  timeData = []
  for wd in weekDates:
      #print(wd)
      total = datetime.strptime('00:00:00', '%H:%M:%S')
      records = WorkTime.query.filter_by(created_date=wd).all()
      for r in records:
        #print(type(r.work_time))
        #print(type(total))
        total = sumTime(total,r.work_time)  
      timeStr = datetime.strftime(total,"%H:%M:%S")
      timeHrs = TimeToHrs(timeStr)
      timeData.append(timeHrs)
   
  return timeData

#Argument:Time in string
#Return: time in hrs (as decimal)
def TimeToHrs(time):
  (h,m,s) = time.split(":")
  timeSec = (int(h)*60*60)+(int(m)*60) +int(s)
  timeHrs = timeSec/3600
  return round(timeHrs,3)



def avgWorkTime():
  records = WorkTime.query.all()
  total = datetime.strptime('00:00:00', '%H:%M:%S')
  for r in records:
    total = sumTime(total,r.work_time)  
  
  timeStr = datetime.strftime(total,"%H:%M:%S")
  timeHrs = TimeToHrs(timeStr)
  avg = timeHrs/(len(records))
  return round(avg,3)
  