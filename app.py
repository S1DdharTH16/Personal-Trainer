from flask import Flask, render_template, Response, request
import helper

app = Flask(__name__)
exercise = 'pushups' 


@app.route('/', methods=['GET', 'POST'])
def index():
    global exercise
    if request.method == 'POST':
        exercise = request.form.get('exercise')
    return render_template('index.html')


@app.route('/video_feed', methods=['POST'])
def video_feed():
    return Response(helper.generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
