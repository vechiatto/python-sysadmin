from flask import Flask, render_template, redirect, request, flash
from modulos.DockerModulo import DockerModulo
from werkzeug.utils import secure_filename
import os

app = Flask (__name__)
app.secret_key = 'secret'

docker = DockerModulo()

@app.route('/')

def index():
	global docker
	containers = []
	
	

	for container in docker.getContainers():
		containers.append(
			{'id': container.get ('Id')[:7], 
			'nome': container.get('Names')[0].replace('/','').title(), 
			'status': container.get('Status')}
		)

	return render_template('index.html', containers=containers)

@app.route('/container/', methods=['POST', 'GET'])
def container_new():
	if request.method == 'POST':
		form = request.form
		global docker
		docker.createContainer(
			form.get('nome'),
			form.get('hostname'),
			form.get('image')
		)
		return redirect('/')

	return render_template('cadastro.html');



@app.route('/container/start/<id>')
def container_start(id):
	global docker
	docker.startContainer(id)

	return redirect('/')

@app.route('/container/stop/<id>')
def container_stop(id):
	global docker
	docker.stopContainer(id)

	return redirect('/')

@app.route('/container/delete/<id>')
def container_remove(id):
	global docker
	docker.removeContainer(id)
	return redirect('/')

@app.route('/container/upload', methods=['GET', 'POST'])
def container_upload():
	if request.method == 'POST':
		arq = request.files['arquivo']
		filename = secure_filename(arq.filename)
		arq.save(os.path.join('', filename))
		flash('Upload Concluido')
		return redirect('/')

	return render_template('upload.html')



if __name__ == '__main__':
	app.run(debug=True)

