''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer


#Initiate the flask app 
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    # Get text from request
    text_to_analyze = request.args.get('textToAnalyze')

    # Run sentiment analysis
    result = sentiment_analyzer(text_to_analyze)

    # Handle invalid or gibberish input
    if result.get('status') != 200:
        error_message = result.get('error', 'Unknown error occurred.')
        return f"{error_message}"

    # Extract sentiment result
    label = result['label']
    score = result['score']

    return f"The given text has been identified as {label}, with a confidence score of {score:.4f}"



@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    # Render the index.html template
    return render_template("index.html")

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    # Run the Flask app on port 5000    
    app.run(host = "0.0.0.0", port=5000, debug=True)
