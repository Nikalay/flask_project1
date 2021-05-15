import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/about')
def about_view():
    return flask.render_template('about.html')


@app.route('/welcome')
def welcome_view():
    weeks = 5
    course = 'Flask'
    group = 'A2'
    return flask.render_template('welcome.html', weeks=weeks, course=course, group=group)


@app.route('/students/<int:student_id>')
def third_view(student_id):
    students = {
        1: 'Александр',
        2: 'Владимир',
        3: 'Михаил',
        4: 'Григорий',
        5: 'Сергей'
    }
    try:
        student_name = students[student_id]
    except KeyError:
        return flask.abort(404)
    return flask.render_template('student.html', student_name=student_name)


@app.errorhandler(404)
def render_not_found(error):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!", 404


@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим", 500


if __name__ == '__main__':
    app.run(debug=True)
