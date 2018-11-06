import requests

def my_oxford_dictionary(word, app_id, app_key):
    language = 'en'
    word_id = word
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})

    if r.status_code == 200:
        data = r.json()
        my_data = ((data["results"][0]["lexicalEntries"][0])["entries"][0]["senses"][0])["definitions"][0]
        return  (my_data)
    elif r.status_code == 404:

        return ("Sorry!  Could not fetch meaning of %s. Cannot recognize the word " %(word))

    elif r.status_code == 500:
        return ("Sorry!  Could not fetch meaning of %s. Error encountered while processing the word request " %(word))
    else:
        return ("Sorry!  Could not fetch meaning of %s. program crashed " %(word))



with open("api_details.txt", 'r') as mykeys:
    content = mykeys.read()
    content = content.split("\\n")

app_id = content[0]
app_key = content[1]
word = input("Enter word you want to know the meaning of: ")

meaning = my_oxford_dictionary(word,app_id,app_key)
print(meaning)