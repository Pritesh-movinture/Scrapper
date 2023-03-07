import requests
from bs4 import BeautifulSoup
import json

def json_from_html_using_bs4(base_url):

    page = requests.get(base_url)

    soup = BeautifulSoup(page.text, "html.parser")

    faqs = soup.find_all(
        'a', attrs={'class':
            'lb-txt-bold lb-txt-none lb-txt-16 lb-txt'})
    # print(faqs)

    for faq in faqs:
        print(faq.getText())
        
    #     res.append(title)
    #     div += 1
    # return res

    data = '''faq'''

    faqs.append(data)
    # title += 1
    return res

if __name__=="__main__":

    base_url = "https://aws.amazon.com/ec2/faqs/"

    res = json_from_html_using_bs4(base_url)

    with open(res,'sidebar_menu_data_scrapped.json','w') as sidebarMenuJSON:
        json.dump(sidebarMenuJSON, ensure_ascii=False)
    print("Created JSON file")

# base_url = "https://aws.amazon.com/ec2/faqs/"

# r = requests.get(base_url)
# htmlContent = r.content

# soup = BeautifulSoup(htmlContent,'html.parser')

# title = soup.title

# paras = soup.find('h2')
# print (paras.prettify())
