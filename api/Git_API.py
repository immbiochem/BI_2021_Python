#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import re


# Первая функция

def get_user_info(username):
    url = 'https://github.com/' + username
    user_dict = {'Name': 'Nothing',
                 'Organization': 'Nothing',
                 'Number of repositories': 'Nothing',
                 'Number of followers': 'Nothing',
                 'Location': 'Nothing'}
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content)
    action_dict = {'Name': (lambda x: x.find('span', itemprop='name').text.strip()),
                   'Organization': (lambda x: x.find('span', class_="p-org").text),
                   'Number of repositories': (lambda x: x.find_all('span', class_='Counter')[0].text),
                   'Number of followers': (lambda x: x.find('span', class_="text-bold color-fg-default").text),
                   'Location': (lambda x: x.find('span', class_="p-label").text)}
    for name in user_dict:
        try:
            user_dict[name] = action_dict[name](soup)
        except AttributeError:
            pass
    return user_dict


# Вторая функция

def get_user_repositories(username):
    url = 'https://github.com/' + username + '?tab=repositories'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content)
    rep = soup.find_all('li', class_=re.compile('col-+'))
    reps_list = []
    for i in range(len(rep)):
        if rep[i].find('span', class_=re.compile('Label')).text == 'Public':
            block = {'User': soup.find('span', itemprop='name').text.strip()}
            try:
                block['Name'] = rep[i].find('a', itemprop="name codeRepository").text.strip()
            except AttributeError:
                block['Name'] = 'None'
            try:
                block['Language'] = rep[i].find(['ul', 'span'], itemprop=re.compile('pro+')).text
            except AttributeError:
                block['Language'] = 'None'
            reps_list.append(block)
    return reps_list


# Третья функция

def list_repository_contents(username, repository_path):
    url = 'https://github.com/' + username + repository_path
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content)
    black_box = soup.find('div', role='grid').find_all('div', role='row')
    repository_content = list()
    for tag in black_box:
        try:
            repository_content.append(tag.find('a', class_=re.compile('js+')).text)
        except AttributeError:
            pass
    return repository_content


# Четвертая функция

def download_file(username, repository, remote_file_path, local_file_path):
    url = 'https://raw.githubusercontent.com/' + username + '/' + repository + remote_file_path
    resp = requests.get(url)
    filename = url.split('/')[-1]
    if resp.ok:
        with open(local_file_path + filename, 'wb') as file:
            file.write(resp.content)
    else:
        raise ValueError('Check your input information')


# Пример

if __name__ == "__main__":
    slovar = get_user_info('immbiochem')
    print(slovar)
