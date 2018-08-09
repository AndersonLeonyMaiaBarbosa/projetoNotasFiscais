import os
from flask import Flask, request, url_for
from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join('uploaded_file', secure_filename(file.filename)))
        return 'Done !'
    
    return '''
    <!doctype html>
    <form action="" method=post enctype=multipart/form-data>
         <input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
	app.run()