import time
import pandas as pd
from bs4 import BeautifulSoup as bs
from fake_headers import Headers
import requests
import re


cookies = {'__ddg1': 'v2fr58pvdOtxGZlBEHal'}
header = Headers(headers=True).generate()

def hh(main_link, search_str, n_str):
    html = requests.get(main_link+'/search/vacancy?clusters=true&area=2&enable_snippets=true&salary=&st=searchVacancy&text='+search_str,headers=header).text
    parsed_html = bs(html,'lxml')

    jobs = []
    for i in range(n_str):
        jobs_block = parsed_html.find('div',{'class':'vacancy-serp'})
        jobs_list = jobs_block.findChildren(recursive=False)
        for job in jobs_list:
            job_data={}
            req=job.find('span',{'class':'g-user-content'})
            if req!=None:
                main_info = req.findChild()
                job_name = main_info.getText()
                job_link = main_info['href']
                salary = job.find('span',{'data-qa':'vacancy-serp__vacancy-compensation'})
                if not salary:
                    salary_min=None
                    salary_max=None
                    salary_currency = None
                else:
                    salary = salary.getText().replace(u'\xa0', u'')
                    salary = salary.replace(u'\u202f', u'')
                    salary_currency = re.findall(r'\b\w{3}\b', salary)
                    salaries = re.findall(r'\d+', salary)
                    salaries[0] = re.sub(r'[^0-9]', '', salaries[0])
                    salary_min=salaries[0]
                    if len(salaries)>1:
                        salaries[1] = re.sub(r'[^0-9]', '', salaries[1])
                        salary_max=int(salaries[1])
                    else:
                        salary_max=None
                job_data['name'] = job_name
                job_data['salary_min'] = salary_min
                job_data['salary_max'] = salary_max
                job_data['salary_currency'] = salary_currency
                job_data['link'] = job_link
                job_data['site'] = main_link
                jobs.append(job_data)
        time.sleep(5)
        next_btn_block=parsed_html.find('a',{'data-qa':'pager-next'})
        if next_btn_block != None:
            next_btn_link=next_btn_block['href']
            html = requests.get(main_link+next_btn_link,headers=header).text
            parsed_html = bs(html,'lxml')


    return jobs

def superjob(main_link, search_str, n_str):
    html = requests.get(main_link+'/vacancy/search/?keywords='+search_str,headers=header).text
    parsed_html = bs(html,'lxml')
    jobs = []
    for i in range(n_str):
        jobs_list = parsed_html.find_all('div', {'class': 'f-test-search-result-item'})
        for job in jobs_list:
            job_data = {}
            req = job.find('div', {'class': '_1h3Zg _2rfUm _2hCDz _21a7u'})
            if req != None:
                job_name = req.getText()
                job_link = req.findChild()['href']
                salary = job.find('span', {'class': '_1OuF_ _1qw9T f-test-text-company-item-salary'})
                if not salary:
                    salary_min = None
                    salary_max = None
                    salary_currency = None
                else:
                    salary_currency = salary.getText().replace(u'\xa0', u' ')
                    salary_currency = salary_currency.split(' ')
                    salary_currency = salary_currency[-1]
                    salary = salary.getText().replace(u'\xa0', u'')
                    salary = salary.replace(u'\u202f', u'')
                    salaries=salary.split('—')
                    salaries[0] = re.sub(r'[^0-9]', '', salaries[0])
                    salary_min=salaries[0]
                    if len(salaries) > 1:
                        salaries[1] = re.sub(r'[^0-9]', '', salaries[1])
                        salary_max = salaries[1]
                    else:
                        salary_max = None
                job_data['name'] = job_name
                job_data['salary_min'] = salary_min
                job_data['salary_max'] = salary_max
                job_data['salary_currency'] = salary_currency
                job_data['link'] = job_link
                job_data['site'] = main_link
                jobs.append(job_data)
        time.sleep(9)
        next_btn_block = parsed_html.find('a', {'rel': 'next'})
        if next_btn_block != None:
            next_btn_link = next_btn_block['href']
            html = requests.get(main_link + next_btn_link, headers=header).text
            parsed_html = bs(html, 'lxml')

    return jobs



def parser_vacancy(search_str,n_str):
    vacancy_data = []
    vacancy_data.extend(hh('https://spb.hh.ru',search_str,n_str))
    vacancy_data.extend(superjob('https://spb.superjob.ru/',search_str,n_str))

    df = pd.DataFrame(vacancy_data)

    return df

search_str = 'python'
n_str = 2
df = parser_vacancy('python',2)

print(df)