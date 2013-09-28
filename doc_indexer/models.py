from datetime import datetime

from .extensions import db


class Document(db.Model):
  __tablename__ = 'documents'
  __searchable__ = ['title', 'content']

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), info=dict(label='Title'))
  doc = db.Column(db.String(255))
  content = db.Column(db.Text)
  indexed = db.Column(db.Boolean, default=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow,
                         onupdate=datetime.utcnow)
