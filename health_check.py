'''check the self nertwork connectivty
check  if website is reachable
'''
import requests

def website_recheable_check(url):
    #print (url)
    payload  = {}
    try:
            response = requests.request("GET", url, data = payload,timeout=1,allow_redirects=True)

            if response.status_code==200:
               return True
            else:
                return False
    except:
            print("error")



def main():
    self_internet_check=website_recheable_check('https://www.google.com')
    if self_internet_check==True:
        print("Self intenet is working")
        website_check= website_recheable_check('https://api.instrumental.ai/healthcheck')
        if website_check == True:
            print("Website is recheable")
        else:
            print("website not recheable")
    else:
        print("No Internet connection to your pc")
if __name__== '__main__':
    main()






