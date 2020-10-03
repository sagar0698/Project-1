import flask
from flask import request, jsonify, g, current_app
import sqlite3 
from werkzeug.security import generate_password_hash, check_password_hash
import logging



app = flask.Flask(__name__)
app.config["DEBUG"] = True


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
        db.row_factory = dict_factory
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.cli.command('init')
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
   

@app.route('/', methods=['GET'])
def home():
    return '''<h1>MicroBlogging</h1>
<p>A microblogging service similar to twitter.</p>'''


@app.route('/users/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('data.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM users;').fetchall()

    return jsonify(all_books)


#User registration

@app.route('/register', methods=['POST'])
def createUser():
    query_parameters = request.form

    username = query_parameters.get('username')
    email = query_parameters.get('email')
    password = query_parameters.get('password')
    hashed_password = generate_password_hash(password, "sha256") #Generating hash for the user entered password
    
    app.logger.info(username)
    
    db = get_db()

    db.execute('INSERT INTO users (username, email, password) VALUES(?,?,?)',(username, email, hashed_password))
    res = db.commit()
    
    getusers = query_db('SELECT * FROM users')
    return jsonify(getusers)


@app.route('/login', methods=['POST'])
def authenticateUser():
    query_parameters = request.form
    
    username = query_parameters.get('username')
    password = query_parameters.get('password')
    
    db = get_db()
    result = query_db('SELECT password FROM users WHERE username = ?', [username])
    
    hashed_password = result[0].get('password')
    return jsonify(check_password_hash(hashed_password, password)) #checking if user entered password is equal to the hashed password in db
  


@app.errorhandler(404)
def page_not_found(e):
    return '''<h1>404</h1>
<p>The resource could not be found.</p>''', 404

app.run()



