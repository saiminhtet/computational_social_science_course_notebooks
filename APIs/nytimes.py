import requests
import json
#sign up and get a key -- I chose Top Stories
key = "a1b6d14c03494629990937518357c475"
# within Top Stories, there are list of parameters to work with. Choose one param or a list of params to iterate through. 
url = 'https://api.nytimes.com/svc/topstories/v2/politics.json?q=&api-key=%s' % key
def data_fetch(a):
    r = requests.get(url)
    try: 
        r.raise_for_status()
        r.status_code()
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e)
    
    obj = r.json()
    print(obj)
    return obj


def __main__():
    data_fetch()
    
if __name__ == "__main__":
    main()