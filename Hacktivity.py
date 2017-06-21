import requests
import json

with requests.Session() as c:
    url='https://hackerone.com/hacktivity?sort_type=latest_disclosable_activity_at&filter=type%3Apublic&page=1&range=forever'
    c.get(url)
    allcookies=c.cookies
    
    cfduid=allcookies['__cfduid']
    hostsession=allcookies['__Host-session']

    page= c.get(url,headers={'Cookie':cfduid+hostsession,
    'Host':'hackerone.com',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Content-Type':'application/json',
    'Referer':'https://hackerone.com/hacktivity?sort_type=popular&filter=type%3Aall&page=1&range=forever',
    'X-Requested-With':'XMLHttpRequest',
    'Connection':'keep-alive'})



    reports=json.loads(page.text)
    for i in reports['reports']:
        rep_title   =   i['title'].encode('utf-8')
        rep_rating  =   'no rating'
        rep_url     =   'https://hackerone.com'+ i['url']
        rep_reporter=   i['reporter']['username']
        rep_team    =   i['team']['profile']['name']
        rep_date    =   i['latest_disclosable_activity_at'][:10]
        if 'severity_rating' in i:
            rep_rating= i['severity_rating']

        print('{}\nTeam: {}\nRating: {}\nReporter: {}\nDate: {}\n{}\n'.format(rep_title,rep_team,rep_rating,rep_reporter,rep_date,rep_url))
    
