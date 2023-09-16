from flask import Flask, jsonify
from serpapi import GoogleSearch
import cohere

SERP_API_KEY = "a240d146c529bc7e3c401e6ca82121c8b10f23be53d4b62537338bfbe7a11085"
COHERE_API_KEY = "OkdezIHQB1oWjY7pziAjufhf3oHXsdiPgTnb8puW"


# Presentation page
def present():
    # SerpAPI endpoint 
    # Searches with query and returns first google image result
    image_query = "big joshua tree"
    
    params = {
    "q": image_query,
    "engine": "google_images",
    "ijn": "0",
    "api_key": SERP_API_KEY
    }    
    
    search = GoogleSearch(params)
    results = search.get_dict()
    images_results = results["images_results"]
    
    
    # Cohere 
    co = cohere.Client(COHERE_API_KEY)

    # Get the text
    text = "The blue whale (Balaenoptera musculus) is a marine mammal and a baleen whale. Reaching a maximum confirmed length of 29.9 meters (98 ft) and weighing up to 199 tonnes (196 long tons; 219 short tons), it is the largest animal known ever to have existed.[a]"
    
    # Use Cohere to summarize the text
    response = co.summarize(
        text = text,
        length = 'medium',
        format = 'bullets',
        model = 'summarize-xlarge',
        additional_command = '',
        temperature = 0.4,
        )

    # Get the summary from the response
    print(response)

    return jsonify({
        "image": images_results[0]['original'],
        "summary": response[1]
    })

    