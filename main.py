from flask import flask, render_template, flash, request
from wtforms import Form, TextField, TextFieldArea, validators, StringField, SubmitField
from werkzeug import secure_filename
from normalizer import parse_distro_sheet

#app_config
DEBUG=True
app = Flask(__name__)
app.config.from_object(__name__)
app.config[‘UPLOAD_FOLDER’] = '/home/VirtualEnvs/SERIALNR_SERIALIZER/'

@app.route('/upload_shjabu')
def upload_file():
   return render_template('upload_shjabu.html')
	
@app.route('/uploader_shjabu', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      parse_distro_sheet(app.config[‘UPLOAD_FOLDER’] + f.filename)
      return 'File parsed successfully'



if (__name__ == '__main__'):
    app.run(host='0.0.0.0')
