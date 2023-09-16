from flask import Flask, jsonify, request
from serpapi import GoogleSearch
import cohere


SERP_API_KEY = "a240d146c529bc7e3c401e6ca82121c8b10f23be53d4b62537338bfbe7a11085"
COHERE_API_KEY = "OkdezIHQB1oWjY7pziAjufhf3oHXsdiPgTnb8puW"


def summarize():
    # Cohere
    co = cohere.Client(COHERE_API_KEY)

    # Get the text
    cohere_query = request.args.get("cohere_query")

    # Use Cohere to summarize the text
    response = co.summarize(
        text=cohere_query,
        length='medium',
        format='bullets',
        model='summarize-xlarge',
        additional_command='',
        temperature=0.4,
    )

    return jsonify({
        "summary": response[1]
    })


# Presentation page
def image_search():

    # Cohere
    co = cohere.Client(COHERE_API_KEY)
    
    # SerpAPI endpoint
    # Searches with query and returns first google image result
    image_query = request.args.get("image_query")
    
    # Filter image query to 3 words max using cohere
    query = co.summarize(
        text = image_query,
        length = 'short',
        format = 'auto',
        model = 'command-nightly',
        additional_command = 'only give me three words divided by a comma',
        temperature = 0.3,                                                                                                          
    )
    
    print("query")
    print(query)

    params = {
        "q": query[1],
        "engine": "google_images",
        "ijn": "0",
        "api_key": SERP_API_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    images_results = results["images_results"]

    return jsonify({
        "image": images_results[0]['original'],
    })
