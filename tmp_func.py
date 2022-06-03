import requests 
def task(candidate_entities):
    API_ENDPOINT = "https://www.wikidata.org/w/api.php"
    params = {
        'action': 'wbsearchentities',
        'format': 'json',
        'language': 'en',
        'search': ''
    }
    
    candidates_sent = []
    for label in candidate_entities:
        candidates_for_one = []
        if len(label) ==0:
            continue
        
        params['search'] = str(label)  # set search from the params to our query word
        try:
            r = requests.get(API_ENDPOINT, params = params).json()
        except:
            return "API failed  " + label
#             return label


        try:
            search_arr = r["search"]
        except:
            print (label)
            return label

        for c in search_arr:
            c_in =[]
            try:
                c_in.append(c["id"])
                c_in.append(c["label"])
                c_in.append(c["description"])
            except:
                c_in.append("missing")
                print(c)

            candidates_for_one.append(c_in)
        candidates_sent.append(candidates_for_one)
            
    return candidates_sent
