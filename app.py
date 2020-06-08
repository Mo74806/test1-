from model import *
import os
from PIL import Image
from flask import Flask, render_template, request, jsonify, send_file, make_response, send_from_directory, render_template
app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def mask_image():
   if request.method == 'GET':
      return render_template('index.html')
   if request.method == 'POST':
      if 'file' not in request.files:
         print('file not uploaded')
         return
   file1=request.files['file']
   img = Image.open(file1)
   image=to_tensor(img)
   array = image.detach().numpy()
   return send_file(io.BytesIO(array),mimetype="image/png", as_attachment=True,attachment_filename="aa.png")

if __name__ == "__main__":
    app.run(debug=True)

                   