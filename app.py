from flask import Flask, render_template, request, jsonify
from scriptWebFile import classify_text

app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def example():
    if request.method == 'POST':
        data = request.data.decode('utf-8')
        #return data
        #text = data['text']
        genres, sentiments = classify_text(data)
        return jsonify({'genres': genres, 'sentiments': sentiments})

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8999)

