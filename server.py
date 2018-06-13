from flask import Flask, render_template, redirect, session, flash, request
import re

app = Flask(__name__)
app.secret_key = "jej38fbaoejthhf2pork"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process', methods=['POST'])
def validate():

	#Set the variable to session because it will take many user submittions. Each will be tested. 
	session['email'] = request.form['email']
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['password'] = request.form['password']
	session['cfrm_password'] = request.form['cfrm_password']

	#tests email
	if len(session['email']) > 0 and EMAIL_REGEX.match(request.form['email']):
		flash("Welcome!", 'success')
	else:
		flash("Email is invalid", 'error')

	#tests first name
	if len(session['first_name']) > 0 and session['first_name'].isalpha():
		flash("welcome", 'success')
	elif len(session['first_name']) < 1:
		flash("Name is too short", 'error')

	#tests last name
	if len(session['last_name']) > 0 and session['last_name'].isalpha():
		flash("welcome", 'success')
	elif len(session['last_name']) < 1:
		flash("Name is too short", 'error')

	#test password
	if session['password'] == session['cfrm_password']:
		flash("Welcome", 'success')
	elif session['password'] != session['cfrm_password']:
		flash("Passwords do not match.",'error')
	
	return redirect('/')

@app.route('/logout', methods=['POST'])
def logout():
	session['email'].pop()
	session['first_name'].pop()
	session['last_name'].pop()
	session['password'].pop()
	session['cfrm_password'].pop()

	return redirect('/')

app.run(debug=True)