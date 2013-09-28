from flask_wtf import Form
from wtforms_alchemy import ModelForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

from .models import Document
from .extensions import document_uploads


class DocumentForm(ModelForm, Form):

  class Meta:
    model = Document
    exclude = ['content']

  doc = FileField("Please select a file to upload", [
    FileRequired(),
    FileAllowed(document_uploads, "Unsupported file type")
  ])
