from flask import Flask, request, jsonify #to handle http & json request/resp  
from flask_cors import CORS #handles cross orign resource sharing
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__) #initilize the flask app..
CORS(app)  # enable CORS for all routes to accept requests from different doimain

# load the saved model that is pretrained
model = pickle.load(open('trained_model.sav', 'rb'))

# load the TF-IDF vectorizer(numeric data) used in training
vectorizer = pickle.load(open('vectorizer.sav', 'rb'))

@app.route('/analyze', methods=['POST'])  #accepts the POST request
def analyze():  #handle POST request
    data = request.get_json(force=True) #extract json data sent in POST req.., force will force the data in json format
    text = data['text'] #retrive the text from json data
    
    # transform the text using the loaded vectorizer
    text_transformed = vectorizer.transform([text]) #convert to numerical format
    
    # predict sentiment
    prediction = model.predict(text_transformed) #uses pretrained data
    sentiment = 'Positive Tweet' if prediction[0] == 1 else 'Negative Tweet'
    
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
