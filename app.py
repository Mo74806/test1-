from torchvision.utils import save_image

import os
from PIL import Image
import io
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
   save_image(img, "ccc.png")

   return send_file('ccc.png', as_attachment=True,attachment_filename="aa.png")

if __name__ == "__main__":
    app.run(debug=True)

                   