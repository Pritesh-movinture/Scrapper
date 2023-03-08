import requests
from bs4 import BeautifulSoup
import json

def json_from_html_using_bs4(base_url):
    res = []
    dataNew = []
    dataNewQuestion = []
    awsPage = requests.get(base_url)

    
    soup = BeautifulSoup(awsPage.text, "html.parser")

    faqs = soup.find_all(
        'a', attrs={'class':
            'lb-txt-bold lb-txt-none lb-txt-16 lb-txt'})
    

# Here we get anchor tag data of side section
    # for faq in faqs:
    #     print(faq.getText())
        
    # data = {'section' : faq.getText()} # converting side section into json

    questions = soup.find_all(
        'div',attrs={'class':'lb-txt-16 lb-rtxt'}
    )

    for question in questions:
        # print(question.getText())
        dataNew.append(question.getText())
        # i = question.getText()
        # print(type(i))
        data = {'subsection': question.getText()}
        # print (data) 
        
        # for data in questions:
        #     print(data[0])     
    # print(dataNew)   
    
    for newData in dataNew:
        type = newData.split("\n")
        x = type[0]
        y= type[1]
        print(y)
        dataObj={"question":type[1]}
        dataNewQuestion.append(dataObj)
    faqs.append(data)
    res.append(dataNewQuestion)

    
    return res

if __name__=="__main__":

    base_url = "https://aws.amazon.com/ec2/faqs/"

    res = json_from_html_using_bs4(base_url)
    # print(res)
    with open('question-answer.json', 'w', encoding='utf8') as f:
        json.dump(res, f, indent=8, ensure_ascii=False)
    print("Created Json File")