import cv2
import numpy as np
from flask import Flask
from flask import Response, request
from main import get_next_state

HEIGHT = WIDTH = 100

app = Flask(__name__)

def create_frame(generator):
    frame = next(generator)
    frame = np.stack((frame,)*3, axis=-1)*255
    frame = frame.astype(np.int32).astype(np.float32)
    return frame

def generate(r_a, factor, mask_ratio, organism_count, alpha_n, alpha_m, b1, b2, d1, d2, dt):
    gen = get_next_state(HEIGHT, WIDTH, r_a, factor, mask_ratio, alpha_n, alpha_m, b1, b2, d1, d2, dt, organism_count)
    while True:
        outputFrame = create_frame(gen)
        scale = 10
        resized_frame = cv2.resize(outputFrame, (HEIGHT*scale, WIDTH*scale), interpolation=cv2.INTER_NEAREST)
        (flag, encodedImage) = cv2.imencode(".jpg", resized_frame)
        if not flag:
            continue
        yield(b'--frame\r\n'b'Content-Type:image/jpeg\r\n\r\n'+bytearray(encodedImage)+b'\r\n')

@app.route("/", methods = ['GET'])
def video_feed():
    r_a = int(request.args.get('r_a') or 21)
    factor = int(request.args.get('factor') or 3)
    mask_ratio = float(request.args.get('mask_ratio') or 0.2)
    organism_count = int(request.args.get('organism_count') or 2)
    alpha_n = float(request.args.get('alpha_n') or 0.028)
    alpha_m = float(request.args.get('alpha_m') or 0.5)
    b1 = float(request.args.get('b1') or 0.05)
    b2 = float(request.args.get('b2') or 0.2)
    d1 = float(request.args.get('d1') or 0.05)
    d2 = float(request.args.get('d2') or 0.05)
    dt = float(request.args.get('dt') or 0.05)
    return Response(generate(r_a=r_a, factor=factor, mask_ratio=mask_ratio, organism_count=organism_count, alpha_n=alpha_n, alpha_m=alpha_m, b1=b1, b2=b2, d1=d1, d2=d2, dt=dt),
        mimetype = "multipart/x-mixed-replace;boundary=frame")