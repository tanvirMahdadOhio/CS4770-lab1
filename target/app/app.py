from flask import Flask, request, render_template, send_from_directory
import sqlite3, os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "/app/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def query_db(q, params=()):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    try:
        c.execute(q, params)
        rows = c.fetchall()
    finally:
        conn.close()
    return rows

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    rows = query_db("SELECT id, username FROM users")
    return render_template('users.html', users=rows)

@app.route('/search')
def search():
    # intentionally vulnerable to SQL injection
    name = request.args.get('name', '')
    q = "SELECT id, username FROM users WHERE username = '%s'" % (name,)
    rows = query_db(q)
    return render_template('search.html', results=rows, query=name)

@app.route('/secrets')
def secrets():
    # NOT exposed to users normally; included for instructor debug only
    rows = query_db("SELECT id, secret FROM secrets")
    return "<pre>%s</pre>" % (rows,)

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        if not f:
            return "No file", 400
        filename = secure_filename(f.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(path)
        return f"File uploaded to {path}"
    return render_template('upload.html')

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
