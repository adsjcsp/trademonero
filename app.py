from flask import Flask, render_template, redirect as direcionar_site
from ext.config.html import title


'''conecta ao bancod de dados para colocar os dados nas paginas web'''


'''Aplicação do nome do titulo nas poaginas de internet'''


'''cria o app do flask para funcionar na web'''


"""Creates a new Flask app"""
def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'v1rj@0d0@gr3st3'

	'''extenção adicionada no flask'''

	@app.route("/")
	def index():
		return render_template('index.html', title=title())

	@app.route("/login")
	def login():
		return render_template('login.html', title=title())

	@app.route("/contato")
	def lotofacil():
		return render_template('contato.html', title=title())

	@app.route("/sobre")
	def sobre():
		return render_template('sobre.html', title=title())

	@app.route("/github")
	def states():
		return direcionar_site('https://www.github.com/adsjcsp/trademonero')

	return app

if __name__ == '__main__':
	create_app()