from ocr import ocr_detect
from flask import Flask ,render_template , request
from flask_uploads import UploadSet, configure_uploads, IMAGES, DATA, ALL
app = Flask(__name__)

photos = UploadSet('photos',IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = './static/img'
configure_uploads(app,photos)
@app.route('/',methods=['GET','POST'])
def ac():
    re = "Hey please redirect to /upload"
    return re
@app.route('/home',methods=['GET','POST'])
def home():
    welcome = "Hey People!"
    return welcome


@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'POST' and  'photo' in request.files:
        filename = photos.save(request.files['photo'])
        print(list(request.files.lists()))
        
        res = ocr_detect('./static/img/'+filename)    
        

        return res

    return render_template('upload.html')


if __name__ == "__main__":
    app.run(port=5000,debug=True)
