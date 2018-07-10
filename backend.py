#!/usr/bin/python
import mysql.connector as db, flask

conn = db.connect(user='POPSTACK_USER', password='fuckthefreeworld03#', database='POPSTACK')
cursor = conn.cursor()

app = flask.Flask("POPSTACK")
app.config["DEBUG"] = True

# login users
@app.route('/login', methods=['GET'])
def login():
  if 'uname' && 'pword' in request.args:
    return cursor.execute("SELECT * FROM users WHERE username=%s && password=%s", (request.args['uname'], request.args['pword']))
  else:
    return "Missing Params"

# Register new user
@app.route('/register', methods=['POST'])
def register():
  if 'uname' && 'pword' in request.args:
    return cursor.execute("INSERT INTO users VALUES (%s, %s)", request.args['uname'], request.args['pword'])
  else:
    return "missing params"

# Post new Thread or retrive existing one
@app.route('/post', methods=['POST','GET'])
def post():
  if request.method == 'POST':
    uname = request.args['uname']
    subject = request.args['subject']
    message = request.args['message']
    img = requests.args['message']
    if 'uname' && 'subject' && 'message' in request.args:
      cursor.execute("INSERT INTO threads VALUES (%s, %s, %s)", uname, subject, message)
    else:
      return "missing params"
      
# Post new reply to thread
@app.route('/reply', methods=['POST'])
def reply():
  uname = request.args['uname']
  message = request.args['message']
  img = requests.args['message']
  threadId = requests.args['threadId']
  if 'uname' && 'message' in request.args:
    cursor.execute("INSERT INTO replies VALUES (%s, %s, %s, %s)", uname, subject, message, threadId)
  else:
    return "missing params"

@app.route('/reply')

# run application
app.run()
