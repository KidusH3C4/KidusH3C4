import requests

target_url = input ("Entert the target url :-")
file_name = input ("Entert the file name :-")

def request(url) :
    try :
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        print ("I AM Not discover :" + full_url )

file = open (file_name , 'r')
for line in file :
    directory = line.strip()
    full_url = target_url + "/" + directory
    response = request (full_url)
    if response :
        print ("Discovered Directory Attispath :" + full_url )
