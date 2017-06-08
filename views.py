from flask import abort, jsonify, render_template, request
from app import app

from models import Note


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        if request.form.get('content'):
            note = Note.create(content=request.form['content'])

            rendered = render_template('note.html', note=note)

            return jsonify({'note': rendered, 'success': True})

        return jsonify({'success': False})

    notes = Note.public().limit(50)
    return render_template('homepage.html', notes=notes)


@app.route('/archive/<int:pk>/', methods=['POST'])
def archive_post(pk):
    try:
        note = Note.get(Note.id == pk)
    except Note.DoesNotExist:
        abort(404)

    note.archived = True
    note.save()

    return jsonify({'success': True})
