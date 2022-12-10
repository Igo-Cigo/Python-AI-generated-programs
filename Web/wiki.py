# prompt used: make a python script that lets the user input a topic then print out the wiki page for that topic

import requests

# Prompt the user to enter a topic
topic = input("Enter a topic: ")

# Format the topic as a Wikipedia search query
query = topic.replace(" ", "+")

# Construct the Wikipedia API URL for search
api_url = f"https://en.wikipedia.org/w/api.php?format=json&action=query&list=search&srsearch={query}&utf8=1&formatversion=2"

# Send a GET request to the Wikipedia API and retrieve the response
response = requests.get(api_url)

# Convert the response to a Python dictionary
data = response.json()

# Extract the first search result from the dictionary
result = data["query"]["search"][0]

# Print the page title and snippet of the search result
print(f"Page title: {result['title']}")

# Construct the Wikipedia API URL for page content
api_url = f"https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles={result['title']}"

# Send a GET request to the Wikipedia API and retrieve the response
response = requests.get(api_url)

# Convert the response to a Python dictionary
data = response.json()

# Extract the page content from the dictionary
page = data["query"]["pages"][next(iter(data["query"]["pages"]))]

# Print the page content
print(page["extract"])
