from flask import Flask, jsonify
from serpapi import GoogleSearch

# SerpAPI endpoint 
# Searches with query and returns first google image result
def present():
    image_query = "big joshua tree"
    
    params = {
    "q": image_query,
    "engine": "google_images",
    "ijn": "0",
    "api_key": "a240d146c529bc7e3c401e6ca82121c8b10f23be53d4b62537338bfbe7a11085"
    }    
    
    search = GoogleSearch(params)
    results = search.get_dict()
    images_results = results["images_results"]
    
    return images_results[0]['link']
    