from ext.config import title
import os
from ext.db import conexao as banco
from flask import Flask, render_template, request
from flask import redirect as direcionar_site

nome = banco
nome.banco.execute('select * from login')




#app = Flask(__name__)
title = title()

def create_app():

	"""Creates a new Flask app"""

	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'v1rj@0d0@gr3st3'

	#extenção adicionada no flask

	@app.route("/")
	def index():
		return render_template('index.html', title=title)

	@app.route("/login")
	def login():
		return render_template('sobre.html', title=title)

	@app.route("/lotofacil")
	def lotofacil():
		return render_template('lotofacil.html', title=title)

	@app.route("/sobre")
	def sobre():
		return render_template('sobre.html', title=title)

	@app.route("/github")
	def states():
		return direcionar_site('https://www.github.com/adsjcsp')

	return app

if __name__ == '__main__':
	create_app()
