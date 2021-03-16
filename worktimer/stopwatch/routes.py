from datetime import datetime
from worktimer.models import WorkTime,db
from flask import Blueprint, render_template,redirect,request
from flask.helpers import url_for
import json

sw = Blueprint('sw', __name__)


@sw.route('/stopwatch')
@sw.route('/')
def stopwatch():
  return render_template('stopwatch.html')

@sw.route('/saveTime', methods=['POST','GET'])
def saveTime():
  if request.method == 'POST':
    timeWorked = request.get_json()
    time_obj = datetime.strptime(timeWorked['workTime'],'%H:%M:%S')
    print(time_obj)
    #save to database
    worktime = WorkTime(work_time=time_obj)
    db.session.add(worktime)
    db.session.commit()
    return "success"
  return "error"