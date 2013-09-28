from flask import Blueprint, render_template, request

from ..extensions import db, document_uploads
from ..models import Document
from ..forms import DocumentForm
from ..tika import tika, FileInputStream, Metadata


root = Blueprint(__name__, 'root')


@root.route('/')
@root.route('/documents')
def index():
  return render_template('index.html')


@root.route('/documents/new', methods=['GET', 'POST'])
def new_document():
  form = DocumentForm(csrf_enabled=False)
  if form.validate_on_submit():
    filename = document_uploads.save(form.doc.data)
    stream = FileInputStream(document_uploads.path(filename))
    meta = Metadata()
    # TODO: Use metadata
    content = tika.parseToString(stream, meta).decode('utf-8')
    doc = Document(
      title=form.title.data,
      doc=filename,
      content=content,
      indexed=True,
    )
    db.session.add(doc)
  else:
    print form.errors
  return render_template('new.html', form=form)


@root.route('/documents/search')
def search_document():
  from flask import jsonify
  results = Document.query.whoosh_search(request.args['query'])
  return jsonify(docs=[doc.title for doc in results])
  # return render_template('search.html')


@root.route('/documents/<int:id>')
def document(id):
  return render_template('show.html')


@root.route('/documents/<int:id>/edit')
def edit_document(id):
  return render_template('edit.html')
