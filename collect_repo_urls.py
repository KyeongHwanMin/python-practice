import re
import requests
from bs4 import BeautifulSoup


pr_urls = [
    'https://github.com/ably-externship/backend-mission/pull/47',
    'https://github.com/ably-externship/backend-mission/pull/43',
    'https://github.com/ably-externship/backend-mission/pull/11',
    'https://github.com/ably-externship/backend-mission/pull/39',
    'https://github.com/ably-externship/backend-mission/pull/41',
    'https://github.com/ably-externship/backend-mission/pull/42',
    'https://github.com/ably-externship/backend-mission/pull/44',
    'https://github.com/ably-externship/backend-mission/pull/45',
    'https://github.com/ably-externship/backend-mission/pull/46',
    'https://github.com/ably-externship/backend-mission/pull/48',
    'https://github.com/ably-externship/backend-mission/pull/49',
    'https://github.com/ably-externship/backend-mission/pull/50',
    'https://github.com/ably-externship/backend-mission/pull/51',
    'https://github.com/ably-externship/backend-mission/pull/52',
    'https://github.com/ably-externship/backend-mission/pull/53',
    'https://github.com/ably-externship/backend-mission/pull/55',
    'https://github.com/ably-externship/backend-mission/pull/56',
    'https://github.com/ably-externship/backend-mission/pull/57',
    'https://github.com/ably-externship/backend-mission/pull/54',
    'https://github.com/ably-externship/backend-mission/pull/58',
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
