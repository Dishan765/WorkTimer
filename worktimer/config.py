
username = "root"
#username = "dishan765"
password = "12345"
#password = "python12345"
server = "localhost"
#server = "dishan765.mysql.pythonanywhere-services.com"
database = "WorkTimer"
#database ="dishan765$WorkTimer"

class Config:
  #SEND_FILE_MAX_AGE_DEFAULT = 0#to remove
  #SECRET_KEY = 'l\x16\xc6\xd7\xc1\xd3\x17\xc9\xc0\xd1W\xa9kH\x01\xf0'
  #SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' 
  SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{username}:{password}@{server}/{database}"
  SQLALCHEMY_TRACK_MODIFICATION = False