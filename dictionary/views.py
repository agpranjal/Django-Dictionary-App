from django.shortcuts import render
from django.http import HttpResponse
import  requests
import json
import pprint

def get_meaning(word_id):
    app_id = 'a5c1918d'
    app_key = 'c1b612847fb02b290ed98615384aca82'
    language = 'en'

    url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/'  + language + '/'  + word_id.lower()
    # urlFR = 'https://od-api.oxforddictionaries.com:443/api/v2/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + word_id.lower()

    r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})

    return r.json()

def index(request):
    if request.method == "POST":
        word = request.POST["word"]
        response = get_meaning(word)        

        try:
            response = response["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]
            response["word"] = word
            return render(request, "index.html", {"response":response})
        except:
            return render(request, "index.html", {"error":True})           

    else:
        return render(request, "index.html")