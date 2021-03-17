from worktimer import db
from datetime import datetime, date

class WorkTime(db.Model):
  id = db.Column(db.Integer, primary_key=True,autoincrement=True)
  work_time = db.Column(db.DateTime(),nullable=False)
  created_date = db.Column(db.Date(), default=datetime.utcnow,nullable=False)