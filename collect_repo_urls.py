import re
import requests
from bs4 import BeautifulSoup


pr_urls = [
    'https://github.com/ably-externship/backend-mission/pull/59',
    'https://github.com/ably-externship/backend-mission/pull/61',
    'https://github.com/ably-externship/backend-mission/pull/60',
    'https://github.com/ably-externship/backend-mission/pull/62',
    'https://github.com/ably-externship/backend-mission/pull/64',
    'https://github.com/ably-externship/backend-mission/pull/65',
    'https://github.com/ably-externship/backend-mission/pull/71',
    'https://github.com/ably-externship/backend-mission/pull/70',
    'https://github.com/ably-externship/backend-mission/pull/73',
    'https://github.com/ably-externship/backend-mission/pull/66',
    'https://github.com/ably-externship/backend-mission/pull/74',
    'https://github.com/ably-externship/backend-mission/pull/69',
    'https://github.com/ably-externship/backend-mission/pull/72',
    'https://github.com/ably-externship/backend-mission/pull/75',
    'https://github.com/ably-externship/backend-mission/pull/63',
    'https://github.com/ably-externship/backend-mission/pull/77',
    'https://github.com/ably-externship/backend-mission/pull/78',
    'https://github.com/ably-externship/backend-mission/pull/67',
    'https://github.com/ably-externship/backend-mission/pull/68',
    
]

repo_urls = []
for url in pr_urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for a_element in soup.find_all('a', {'href': re.compile(r'(.+)\/backend-mission')}):
        href = a_element['href']
        if href.startswith('/ably-externship'):
            continue
        else:
            repo_urls.append(f'https://github.com{href}')
            break

print(repo_urls)
