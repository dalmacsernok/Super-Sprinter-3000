from flask import Flask, render_template, request, redirect, url_for
import data_handler

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def list_stories():
    user_stories = data_handler.get_all_user_story()
    return render_template('list.html', user_stories=user_stories, header=data_handler.DATA_HEADER)


@app.route('/story', methods=['GET', 'POST'])
def add_story():
    if request.method == 'POST':
        result = request.form.to_dict()
        data_handler.add_user_story(result)
        return redirect('/')
    return render_template('add_story.html')


@app.route('/story/<int:id>', methods=['GET', 'POST'])
def update_story(id):
    result = data_handler.get_all_user_story()
    story = result[id-1]
    if request.method == 'POST':
        result = request.form.to_dict()
        result['id'] = id
        data_handler.update_user_story(result, id)
        return redirect('/')
    return render_template('update_story.html', story=story, status=data_handler.STATUSES)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
