from flask import Flask, render_template, redirect, request, url_for, send_file
from flask import jsonify, json
from werkzeug.utils import secure_filename
import prediction
import os


app = Flask("__main__", template_folder="templates")
Uploaded_images = "Uploaded_images"
app.config['Uploaded_images'] = Uploaded_images

@app.route('/', methods=['POST', 'GET'])
def homepage():
  if request.method == 'GET':
    return render_template('index.html')

@app.route('/getFile', methods=['POST'])
def getOutput():
  output=""
  if request.method == 'POST':
        myimage = request.files.get('myfile')
        imgname = secure_filename(myimage.filename)
        imgpath = "Uploaded_images/"+imgname
        myimage.save(os.path.join(app.config["Uploaded_images"], imgname))
        output = prediction.prediction(imgpath)
        print(output)
        return output
      

  

app.run(port=3000);
