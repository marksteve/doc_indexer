from flask import Flask

from .models import *
from .extensions import *
from .views import *


def register_blueprints(app):
  app.register_blueprint(root)


def create_app():
  app = Flask(__name__)
  app.config.from_object('doc_indexer.config')

  # Flask-SQLAlchemy
  db.init_app(app)
  app.before_request(db_start_session)
  app.teardown_request(db_commit_session)

  # Flask-Uploads
  configure_uploads(app, (document_uploads,))

  register_blueprints(app)
  return app
