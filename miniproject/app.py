from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route("/test", methods=["POST"])
def test_post():
	sample_receive = request.form['test_give']
	print(sample_receive)
	return jsonify({'msg':'POST 연결 완료!'})

@app.route("/test", methods=["GET"])
def test_get():
	return jsonify({'msg':'GET 연결 완료!'})

@app.route('/sh')
def test():
	return render_template('sh.html')

@app.route('/my')
def test1():
	return render_template('my.html')

if __name__ == '__main__':
	app.run('0.0.0.0', port=5000, debug=True)