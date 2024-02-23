import cv2
import numpy as np
from flask import Flask
from flask import Response, request
from main import get_next_state

HEIGHT,WIDTH = 90,90
ORGANISM_COUNT = 2
MASK_RATIO = 0.2
R_A = 7 # 21 11
FACTOR = 3
ALPHA_N = 0.028
ALPHA_M = 0.5 # 0.147
B1 = 0.05 # 0.278 0.257
B2 = 0.2 # 0.365 0.336
D1 = 0.5 # 0.267 0.365
D2 = 0.05 # 0.445 0.549
DT = 0.05 # 0.5 0.005

app = Flask(__name__)

def create_frame(generator):
    frame = next(generator)
    frame = np.stack((frame,)*3, axis=-1)*255
    frame = frame.astype(np.int32).astype(np.float32)#frame.astype(np.uint16)
    return frame

def generate(R_A=21, FACTOR=3, ORGANISM_COUNT=2, ALPHA_N=0.028, ALPHA_M=0.5, B1=0.05, B2=0.2, D1=0.5, D2=0.05):
    gen = get_next_state(HEIGHT, WIDTH, R_A, FACTOR, MASK_RATIO, ALPHA_N, ALPHA_M, B1, B2, D1, D2, DT, ORGANISM_COUNT)
    while True:
        outputFrame = create_frame(gen)
        scaleFactor = 12
        resized_frame = cv2.resize(outputFrame, (HEIGHT*scaleFactor, WIDTH*scaleFactor), interpolation=cv2.INTER_NEAREST)
        (flag, encodedImage) = cv2.imencode(".jpg", resized_frame)
        if not flag:
            continue
        yield(b'--frame\r\n'b'Content-Type:image/jpeg\r\n\r\n'+bytearray(encodedImage)+b'\r\n')

@app.route("/", methods = ['GET'])
def video_feed():
    R_A = int(request.args.get('R_A') or 21)
    FACTOR = int(request.args.get('FACTOR') or 3)
    ORGANISM_COUNT = int(request.args.get('ORGANISM_COUNT') or 2)
    ALPHA_N = float(request.args.get('ALPHA_N') or 0.028)
    ALPHA_M = float(request.args.get('ALPHA_M') or 0.5)
    B1 = float(request.args.get('B1') or 0.05)
    B2 = float(request.args.get('B2') or 0.2)
    D1 = float(request.args.get('D1') or 0.05)
    D2 = float(request.args.get('D2') or 0.05)
    return Response(generate(R_A=R_A, FACTOR=FACTOR, ORGANISM_COUNT=ORGANISM_COUNT, ALPHA_N=ALPHA_N, ALPHA_M=ALPHA_M, B1=B1, B2=B2, D1=D1, D2=D2),
        mimetype = "multipart/x-mixed-replace;boundary=frame")