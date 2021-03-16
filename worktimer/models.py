from worktimer import db
from datetime import date

class WorkTime(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  work_time = db.Column(db.DateTime(),nullable=False)
  created_date = db.Column(db.Date(), default=date.today())