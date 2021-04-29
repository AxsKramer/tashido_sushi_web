from flask import Flask, flash, redirect, url_for, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = 'clave_secreta_flask'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'tashidoDB'
app.config['MYSQL_PORT'] = 3306


mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html', title='Home')

@app.route('/sushis', methods=['GET'])
def sushis():
  if request.method == 'GET':
    cursor= mysql.connection.cursor()
    cursor.execute('Select * FROM sushis')
    sushis = cursor.fetchall()
    cursor.close()
    return render_template('sushis.html', sushis=sushis, title='Sushis')

@app.route('/promociones', methods=['GET'])
def promociones():
  return render_template('promociones.html', title='Promociones')

@app.route('/platillos', methods=['GET'])
def platillos():
  if request.method == 'GET':
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT * FROM platillos')
    platillos = cursor.fetchall()
    cursor.close()
    return render_template('platillos.html', platillos=platillos, title='Platillos')

@app.route('/contacto',methods=['GET', 'POST'])
def contacto():
  return render_template('contacto.html', title='Contacto')

if __name__ =='__main__':
  app.run(host='0.0.0.0', debug=False)
  # app.run(debug=True)