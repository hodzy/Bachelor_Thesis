import requests 
def task(ent_id):
    labels = []
    API_ENDPOINT = "https://www.wikidata.org/w/api.php"
    params = {
        'action': 'wbgetentities',
        'format': 'json',
        'languages': 'en',
        'props': 'labels|aliases',    
        'ids': ''
    }

        
    params['ids'] = str(ent_id)
    try:
        response = requests.get(API_ENDPOINT, params = params).json()['entities']
        labels.append(response[str(ent_id)]['labels']['en']['value'])
        
        for alias in response[str(ent_id)]['aliases']['en']:
            labels.append(alias['value'])
    except:
        return (ent_id, labels)
    return (ent_id, labels)
