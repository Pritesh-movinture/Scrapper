import requests
from bs4 import BeautifulSoup
import json

def json_from_html_using_bs4(base_url):
    res = ''
    awsPage = requests.get(base_url)

    soup = BeautifulSoup(awsPage.text, "html.parser")

    faqs = soup.find_all(
        'a', attrs={'class':
            'lb-txt-bold lb-txt-none lb-txt-16 lb-txt'})
    

# Here we get anchor tag data of side section
    for faq in faqs:
        print(faq.getText())
        
    data = {"section" : faq.getText()} # converting side section into json

    faqs.append(data)
    return res

if __name__=="__main__":

    base_url = "https://aws.amazon.com/ec2/faqs/"

    res = json_from_html_using_bs4(base_url)

    with open(res,'sidebar_menu_data_scrapped.json','w') as sidebarMenuJSON:
        json.dump(sidebarMenuJSON, ensure_ascii=False)
    print("Created JSON file")

