import os

#conecta ao bancod de dados para colocar os dados nas paginas web

#Aplicação do nome do titulo nas poaginas de internet
from ext.config import title
title = title()


#cria o app do flask para funcionar na web
def create_app():
	from flask import Flask, render_template, request
	from flask import redirect as direcionar_site

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