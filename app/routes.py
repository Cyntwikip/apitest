from app import app
from flask import Flask, request
import pickle

@app.route('/')
@app.route('/index')
def index():
    return """
    <b>Hello, World!</b>
    <p>This is Jude Michael's website</p>
    """

@app.route('/apis/<string:text>', methods=['GET'])
def method1(text):
    s = 'The text you have submitted is:\n{0}\n'.format(text)
    return s

@app.route('/apis/list', methods=['GET'])
def method2():
    s = '<b>Here are the inputs:</b>'
    for key,val in request.args.items():
        s += '<p>{0} : {1}</p>'.format(key, val)
    return s

@app.route('/apis/json/', methods=['GET'])
def method3():
    req_data = request.get_json()
    s = '<b>Here are the inputs:</b>'
    for key,val in req_data.items():
        s += '<p>{0} : {1}</p>'.format(key, val)
    return s

@app.route('/apis/predict_iris_dataset', methods=['GET'])
def predict_iris_dataset():
    s = ''
    req_data = request.args
    
    if 'input' in req_data:
        s += '<b>Here are the inputs:</b>'
        input = req_data['input']
        try:
            input = list(map(float,input.split(',')))
            s += '<p>{0}</p>'.format(input)
        except:
            s = 'Input must only be 4 numbers separated by commas.'
            return s

        if len(input) !=4:
            s += '<b>The kNN model needs only 4 numbers to do the prediction.</b>'
        else:
            classifications = ['setosa', 'versicolor', 'virginica']
            pickle_in = open("model.pickle","rb")
            model = pickle.load(pickle_in)     
            result = classifications[model.predict([input])[0]]
            s += '<b>The flower is: {0}</b>'.format(result)
    else:
        s = '<b>There is no input :(</b>'
    return s

