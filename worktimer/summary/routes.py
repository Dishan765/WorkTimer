from flask import Blueprint, render_template,request
from datetime import date,datetime
from worktimer.summary.utils import getWeekDates,getTimesFromDb,avgWorkTime

details = Blueprint('details', __name__)


@details.route('/summary',methods=["POST","GET"])
def summary():
  if request.method == 'POST':
    inputDate = request.form['chooseDate']
    if inputDate == "":
      inputDate = date.today()
      weekDates = getWeekDates(inputDate)
      data = getTimesFromDb(weekDates) 
    else:
      inputDate = datetime.strptime(inputDate,"%Y-%m-%d").date()
      weekDates = getWeekDates(inputDate)
      data = getTimesFromDb(weekDates)  
  else:
    #get current date
    inputDate = date.today()
    weekDates = getWeekDates(inputDate)
    data = getTimesFromDb(weekDates) 

  avgTime = avgWorkTime()
  

  return render_template('summary.html',data=data,startDate=weekDates[0],endDate=weekDates[len(weekDates)-1],avgTime=avgTime)



