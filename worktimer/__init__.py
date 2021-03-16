from flask import Flask
from worktimer.config import Config
from flask_sqlalchemy import SQLAlchemy

db =SQLAlchemy()

def create_app(config_class = Config):
  app = Flask(__name__)
  app.config.from_object(Config)

  db.init_app(app)

  from worktimer.stopwatch.routes import sw
  from worktimer.summary.routes import details
  app.register_blueprint(sw)
  app.register_blueprint(details)

  return app
