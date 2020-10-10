try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
def google_search(message):
    query = message.content.split(" ",1)[1]
    print(query)
    return search(query, tld="co.in", num=5, stop=5, pause=2) 