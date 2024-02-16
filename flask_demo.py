import cv2
import numpy as np
from flask import Flask
from flask import Response
from main import get_next_state

HEIGHT,WIDTH = 100,100
ORGANISM_COUNT = 1
MASK_RATIO = 0.2
R_A = 16 # 21 11
FACTOR = 3
ALPHA_N = 0.028
ALPHA_M = 0.028 # 0.147
B1 = 0.278 # 0.278 0.257
B2 = 0.365 # 0.365 0.336
D1 = 0.267 # 0.267 0.365
D2 = 0.445 # 0.445 0.549
DT = 0.05 # 0.5 0.005
app = Flask(__name__)

def create_frame(generator):
    frame = next(generator)
    frame = np.stack((frame,)*3, axis=-1)*255
    frame = frame.astype(np.int32).astype(np.float32)
    return frame

def generate():
    gen = get_next_state(HEIGHT, WIDTH, R_A, FACTOR, MASK_RATIO, ALPHA_N, ALPHA_M, B1, B2, D1, D2, DT, ORGANISM_COUNT)
    while True:
        outputFrame = create_frame(gen)
        scaleFactor = 10
        resized_frame = cv2.resize(outputFrame, (HEIGHT*scaleFactor, WIDTH*scaleFactor), interpolation=cv2.INTER_NEAREST)
        (flag, encodedImage) = cv2.imencode(".jpg", resized_frame)
        if not flag:
            continue
        yield(b'--frame\r\n'b'Content-Type:image/jpeg\r\n\r\n'+bytearray(encodedImage)+b'\r\n')

@app.route("/")
def video_feed():
	return Response(generate(),
		mimetype = "multipart/x-mixed-replace;boundary=frame")

app.run(host='0.0.0.0', port=82)