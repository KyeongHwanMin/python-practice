import os


repo_urls = [
    'https://github.com/ohgyulim/backend-mission',
    'https://github.com/SangRakee/backend-mission',
    'https://github.com/zoonong/backend-mission',
    'https://github.com/dhleeone/backend-mission',
    'https://github.com/jennharw/backend-mission',
    'https://github.com/SMin1620/backend-mission',
    'https://github.com/komo3344/backend-mission',
    'https://github.com/KimKyeongJun/backend-mission',
    'https://github.com/Hyes-y/backend-mission',
    'https://github.com/ulr0/backend-mission',
    'https://github.com/601chl/backend-mission',
    'https://github.com/sjy5386/backend-mission',
    'https://github.com/KyeongHwanMin/backend-mission',
    'https://github.com/wlsgh7608/backend-mission',
    'https://github.com/sohyeong-dev/backend-mission',
    'https://github.com/oswaldeff/backend-mission',
    'https://github.com/seah526/backend-mission',
    'https://github.com/tc-ha/backend-mission',
    'https://github.com/NQ-OO/backend-mission'
]

repo_urls = set(repo_urls)  # 중복제거를 위함


for url in repo_urls:
    folder_name = url.split('https://github.com/')[1].split('/')[0]
    path = f'/home/min/ably-extenship-repo/{folder_name}'
    
    if not os.path.exists(path):
        os.makedirs(path)
        os.chdir(path)
        os.system(f'git clone {url}')
    else:
        print(f'{folder_name}')
        os.chdir(f'{path}/backend-mission')
        os.system(f'git pull')
        print('-'*100)
