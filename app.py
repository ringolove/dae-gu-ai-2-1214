from flask import Flask
import sqlite3
app = Flask(__name__)

@app.route("/")
def index():
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM topics')
    rows = cursor.fetchall()
    liTag = ''
    for row in rows:
        liTag = liTag + f'<li><a href="/read/{row[0]}">{row[1]}</a></li>'
    return f"""
    <!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ul>
                {liTag}
            </ul>
            <h2>Welcome</h2>
            Hello, web
            <ul>
                <li><a href="/create">create</a></li>
            </ul>
            </p>
        </body>
    </html>
    """

@app.route("/read/<id>/")
def read(id):
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM topics')
    rows = cursor.fetchall()
    liTag = ''
    for row in rows:
        liTag = liTag + f'<li><a href="/read/{row[0]}">{row[1]}</a></li>'
    
    cursor.execute('SELECT * FROM topics WHERE id = ?', (id,))
    topic = cursor.fetchone()
    return f"""
    <!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ul>
                {liTag}
            </ul>
            <h2>{topic[1]}</h2>
            {topic[2]}
            <ul>
                <li><a href="/create">create</a></li>
            </ul>
            </p>
        </body>
    </html>
    """

@app.route("/create/")
def create():
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM topics')
    rows = cursor.fetchall()
    liTag = ''
    for row in rows:
        liTag = liTag + f'<li><a href="/read/{row[0]}">{row[1]}</a></li>'
    return f"""
    <!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ul>
                {liTag}
            </ul>
            <form action="/create_process" method="post">
                <p><input type="text" placeholder="title" name="title"></p>
                <p><input type="text" placeholder="title" name="body"></p>
                <p><input type="submit" value="생성"</p>
            </form>
            <ul>
                <li><a href="/create">create</a></li>
            </ul>
        </body>
    </html>
    """

app.run(debug=True, host="0.0.0.0", port="8000")