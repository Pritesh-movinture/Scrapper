import requests
from bs4 import BeautifulSoup
import json

def json_from_html_using_bs4(base_url):

    page = requests.get(base_url)

    soup = BeautifulSoup(page.text, "html.parser")

    faqs = soup.find_all(
        'h2', attrs={'class':
            'lb-txt-bold lb-txt-none lb-txt-24 lb-h2 lb-title'})
    print(faqs)

    for faq in faqs:
        title = faq.find('h2')['id']

        link = faq.find('a')['href']

if __name__=="__main__":

    base_url = "https://aws.amazon.com/ec2/faqs/"

    res = json_from_html_using_bs4(base_url)

    with open('faqs.json', encoding='latin-1') as f:
        json.dump(res,f,indent=8)
    print("Created JSON file")

# base_url = "https://aws.amazon.com/ec2/faqs/"

# r = requests.get(base_url)
# htmlContent = r.content

# soup = BeautifulSoup(htmlContent,'html.parser')

# title = soup.title

# paras = soup.find('h2')
# print (paras.prettify())


