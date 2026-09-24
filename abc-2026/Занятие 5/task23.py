# todo: добавьте во Flask маршруты для страниц (endpoint)
"""
- О компании
- Контакты
- Список постов
"""
from flask import Flask

app = Flask(__name__)
@app.route('/about_us')
def route_about_us():
    return 'about_us page'

@app.route('/contacts')
def contacts():
    return 'contacts page'

@app.route('/posts')
def posts():
    return 'posts page'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)