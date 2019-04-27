from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
#from flaskext.mysql import MySQL

app = Flask(__name__)

#Mysql Conexion
app.config['MYSQL_HOST'] = 'python.cy1dshhchfxf.us-east-2.rds.amazonaws.com'
app.config['MYSQL_DB'] = 'flaskcontacts'
app.config['MYSQL_USER'] = 'python123'
app.config['MYSQL_PASSWORD'] = 'python123'
#app.config['MYSQL_DATABASE_HOST'] = '172.30.218.1'
mysql = MySQL(app)

#docker network create -d bridge // 

# Sesion
app.secret_key = 'mysecretkey'


@app.route('/')
def index():
		cur = mysql.connection.cursor()
		cur.execute('SELECT * FROM contacts')
		resultado = cur.fetchall()
		return render_template('index.html', contacts = resultado )
    	
    

@app.route('/add_contact', methods=['POST'])
def add_contact():
	if request.method == 'POST':
		fullname = request.form['fullname']
		phone = request.form['phone']
		email = request.form['email']
		cur = mysql.connection.cursor()
		cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)',
		(fullname, phone, email))
		mysql.connection.commit()
		flash('Contacto agregado correctamente')
		return redirect(url_for('index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
  cur = mysql.connection.cursor()
  cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
  mysql.connection.commit()
  flash('Contacto removido satisfactoriamente')
  return redirect(url_for('index'))
    	
    	

@app.route('/edit/<id>')
def get_contact(id):
  cur = mysql.connection.cursor()
  cur.execute('SELECT * FROM contacts WHERE id = %s', (id))
  resultado = cur.fetchall()
  return render_template('edit-contact.html', contact = resultado[0])

@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts
            SET fullname = %s,
            	phone = %s,
             	email = %s
            WHERE id = %s
        """, (fullname, phone, email, id))
        mysql.connection.commit()
        flash('Contacto actualizado')
        return redirect(url_for('index'))

app.run(port=5000, debug=True)

