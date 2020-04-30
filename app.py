from flask import Flask
app = Flask(__name__) # create instance of Flask class

@app.route('/') # the site to route to, index/main in this case
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
