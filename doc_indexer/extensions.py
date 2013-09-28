from flask_sqlalchemy import SQLAlchemy
from flaskext.uploads import UploadSet, configure_uploads
import flask_whooshalchemy


__all__ = [
  'db',
  'db_start_session',
  'db_commit_session',
  'configure_uploads',
  'document_uploads',
]


db = SQLAlchemy()


def db_start_session():
  db.session()


def db_commit_session(exc):
  if exc:
    db.session.rollback()
  else:
    db.session.commit()
  db.session.remove()


ALLOWED_FILES = [
  'html',
  'xml',
  'doc',
  'docx',
  'odt',
  'pdf',
  'rtf',
  'epub',
]
document_uploads = UploadSet('documents', ALLOWED_FILES)
