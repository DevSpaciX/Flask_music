from flask import Flask, render_template, request
from models import Music, Artist

app = Flask(__name__)


@app.route('/', methods=['get'])
def all_music():
    context = {'music': Music.select()}
    return render_template("music_list.html", **context)


@app.route('/add/music', methods=['get', 'post'])
def music_add():
    context = {'authors': Artist.select()}
    if request.method == 'POST':
        Music(
            name=request.form['name'],
            duration=request.form['duration'],
            author=request.form['authors']
        ).save()
    return render_template('add_music.html', **context)

@app.route('/delete/music/', methods=['get','post','delete'])
def music_delete():
    context = {'music': Music.select()}
    if request.method == 'POST':
        q = Music.delete().where(Music.id == request.form['music.id'])
        q.execute()
    return render_template('delete_music.html', **context)



if __name__ == '__main__':
    app.run(debug=True)