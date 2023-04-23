import torch
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from transformers import pipeline as transformers_pipeline

import lxml
def search_bing(query):
#     url = f"https://www.google.com/search?q={query}"
    print(query)
    url = f"https://www.bing.com/search?form=QBRE&q={query}" 
    user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36']

    HEADERS = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Cache-Control": "max-age=0",
        }
    
    response = requests.get( url, headers=HEADERS).text
    soup = BeautifulSoup(response, 'lxml')
    
    links = []
    for container in soup.select('.b_algo h2 a'):
        link = container['href']
        links.append(link)
    return links

def take_text(head):
#     print("Heading to be searched : ", head)
    query = head.split("\n")[0]
#     print("Query retrieved from head : ", query)
    links = []
    for link in search(query):
        links.append(link)
    # Format of links
    # links = ['https://www.newsweek.com/pope-francis-trump-immigration-jerusalem-christmas-758710','https://www.reuters.com/article/christmas-season-pope-urbi-et-orbi-idAFL8N1OP0DJ',]

    return links


def query_search_text(links, questions, answers, k):
    topK_links = links[0: k]
    for link in topK_links:
        
        URL = link
        headers = {'User-Agent': 
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
        
        
        
        r = requests.get(URL, headers=headers)
        soup = BeautifulSoup(r.content, 'html5lib')
        tags = soup.find_all('h1')
        heading = ""
        i = 0
        for t in tags:
            try:
                if i == 0:
                    heading = t.text
                    i += 1
                # print(t.text)
            except:
                continue

        tags1 = soup.find_all('p')
        para = ""
        i = 0
        for t in tags1:
            try:
                # print(t.text)
                para += t.text
            except:
                continue
        answer_from_link(para, questions, answers)

def answer_from_link(para, questions, answers):
#     print("Context: ", para)
    with torch.no_grad():
        question_answerer = transformers_pipeline("question-answering", model='distilbert-base-cased-distilled-squad')
        context = para
        ans = []
        for question in questions:
            result = question_answerer(question=question, context=context)
            ans.append(result['answer'])
        answers.append(ans)


def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num

def getMajority(ans):
    n = len(ans)
    m = len(ans[0])
    final = []
    for i in range(0, m):
        temp = []
        for j in range(0, n):
            temp.append(ans[j][i])
        element = most_frequent(temp)
        final.append(element)
    return final


def get_answers(dict, ans):
    for ques in dict:
        ans.append(dict[ques])


def importf(dict, list):
    ques_ans = dict
    majority_l = list
