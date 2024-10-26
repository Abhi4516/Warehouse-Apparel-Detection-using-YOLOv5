from flask import Flask, request, jsonify, render_template,Response
import os
from flask_cors import CORS, cross_origin
from apparel.com_utils.utils import decodeImage
from apparel.predictor_yolo_detector.detector_test import Detector

# import sys
# sys.path.insert(0, './apparel')

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


# @cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        
        self.objectDetection = Detector(self.filename)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=['POST','GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)
        result = clApp.objectDetection.detect_action()
    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)



if __name__ == "__main__":
    clApp = ClientApp()
    port = 9500
    app.run(host='0.0.0.0', port=port)