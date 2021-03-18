from flask import Blueprint, render_template, request
from datetime import date
import json
from worktimer.summary.utils import (getWeekDates, getTimesFromDb,
                                     avgWorkTime, getTimeCurrentDate)
from worktimer.summary.forms import DateForm, converterForm


details = Blueprint('details', __name__)

@details.route('/summary', methods=["POST", "GET"])
def summary():
    formDate = DateForm()
    formConverter = converterForm()
    
    if formDate.validate_on_submit():
        inputDate = formDate.date.data
        if inputDate == "":
            #get current date
            weekDates = getWeekDates(date.today())
            data = getTimesFromDb(weekDates)
        else:
            weekDates = getWeekDates(inputDate)
            data = getTimesFromDb(weekDates)
    else:
        weekDates = getWeekDates(date.today())
        data = getTimesFromDb(weekDates)

    avgTime = avgWorkTime()

    
    
    return render_template('summary.html', data=data, startDate=weekDates[0], endDate=weekDates[len(weekDates)-1], avgTime=avgTime,formDate=formDate,formConverter=formConverter)




@details.route('/convertTime', methods=['POST','GET'])
def convertTime():
  if request.method == 'POST':
    inputTimeArr = request.get_json()
    if inputTimeArr['timeInput'] != "":
        inputTime = float(inputTimeArr['timeInput'])

        #https://www.calculatorsoup.com/calculators/time/decimal-to-time-calculator.php
        #Click on link for logic below
        hour = inputTime
        fullHour = int(hour)
        decimalHour = hour - fullHour
        min = decimalHour * 60
        fullMin = int(min)
        decimalMin = min - fullMin
        fullSec = round(decimalMin *60,0)
        fullSec = int(fullSec)

        #If seconds/minutes/hours are only one digit, add a leading 0 to the value
        if fullSec < 10:
            displaySeconds = "0" + str(fullSec)
        else:
            displaySeconds = str(fullSec)
        
        if fullMin < 10:
            displayMinutes = "0" + str(fullMin)
        else:
            displayMinutes = str(fullMin)

        if fullHour < 10:
            displayHours = "0" + str(fullHour)
        else:
            displayHours = str(fullHour)
    
        
        displayTime = displayHours +":" + displayMinutes +":" + displaySeconds 
        print(displayTime)
        return json.dumps(displayTime)
  return json.dumps("00:00:00")