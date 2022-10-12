'''check the self nertwork connectivty
check  if website is reachable
'''
import requests
import logging
def website_reachable_check(url): #function to get response from any website we provide
    
    try:
            response = requests.request("GET", url,timeout=10,allow_redirects=True)

            if response.status_code==200:
               return True
            else:
                return False
    except:
            print("error")



def main():
    logging.basicConfig(filename="urlresults.txt",
                    filemode='w',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
    self_internet_check=website_reachable_check('https://www.google.com')
    if self_internet_check==True:
        logging.info('your server local connections is good and resolver is functioning correctly')
        website_check= website_reachable_check('https://api.instrumental.ai/healthcheck')
        if website_check == True:
            logging.info('The Health check Website  is Rechable')
        else:
            logging.warning('Health check website not recheable,Please check the URL')
    else:
        logging.warning("There is no internet connection available on your local machine")
if __name__== '__main__':
    main()






