function analyzeSentiment() {
    const inputText = document.getElementById('inputText').value;

    fetch('http://localhost:5000/analyze', {  // sends the user i/p to the backend @ given host
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' //request specify the content type is application/json
        },
        body: JSON.stringify({ text: inputText }) //it converts input text into JSON format,it provides a straightforward way to serialize and deserialize data. 
    })
    .then(response => response.json()) //response contains the json format of user i/p
    .then(data => {          //raw response is converted to javascript object
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `Sentiment: ${data.sentiment}`; //it'll return result of the text analysis
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


