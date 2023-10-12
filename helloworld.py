from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World, flask'

@app.route('/hello/<name>')
def hello(name):
    return f'welcome you, {name}'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
    
