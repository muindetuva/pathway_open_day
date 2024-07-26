import webbrowser
import urllib.parse

def search_youtube(query):
    # Ensure the query is properly encoded to handle special characters and spaces
    query_encoded = urllib.parse.quote(query)
    url = f"https://www.youtube.com/results?search_query={query_encoded}"
    webbrowser.open(url)

search_youtube("Kante by Davido")

