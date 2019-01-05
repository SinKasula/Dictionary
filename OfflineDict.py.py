import json
from difflib import get_close_matches

def get_words_capital_first_letter():
    caps = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    capitals_letters = []
    data = json.load(open("data.json"))
    for every_key in data.keys():
        if every_key[0] in caps:
            capitals_letters.append(every_key)

    return capitals_letters



def translate(w):
    cap_first_letter_words = get_words_capital_first_letter()
    data = json.load(open("data.json"))
    if w in cap_first_letter_words:
        return data[w]


    elif w in list(data.keys()):
        w = w.lower()
        return data[w]

    elif len(get_close_matches(w, list(data.keys()), cutoff= 0.5)) > 0:
        n_w = (get_close_matches(w, list(data.keys()), cutoff= 0.5))[0]
        recommend_w = input("Did you mean %s instead? (Y/N)" %(n_w))
        if recommend_w.lower() == 'y':
            return translate(n_w)

        elif recommend_w.lower() == 'n':
            return "Cannot recognize %s. Sorry!" %(w)
        else:
            return "we did not understand your response"

    else:
        return "Cannot recognize %s" % (w)



user_input = input("Enter a word : ")

meaning = translate(user_input)
if type(meaning) == list:
    print("It's means the following : ")
    for i in range(len(meaning)):
        print((str(i+1)+". "+meaning[i]))
else:
    print(meaning)
