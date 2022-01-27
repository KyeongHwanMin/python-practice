import requests
import shutil
import os

# 개발자도구 network 탭에서 재생 한번하면 나옴.
url_template = 'https://d35ai18pny966l.cloudfront.net/transcode/ably_externship_backend/hls/Backend_c03r01/media-1/segment-{sagment_number}.ts'
file_name = '미션 해설 영상(3-1)'


def download(url, file_path):
    with open(file_path, "wb") as file:
        response = requests.get(url)
        if response.status_code == 404:
            return False
        file.write(response.content)
        return True


ts_file_list = []

# download
sagment_number = 1
while True:
    url = url_template.format(sagment_number=sagment_number)
    temp_file_name = file_name + f'_{sagment_number}.ts'
    result = download(url, temp_file_name)

    if result:
        ts_file_list.append(temp_file_name)
        sagment_number += 1
    else:
        os.remove(temp_file_name)
        break


# ts merge
with open(f'{file_name}.ts', 'wb') as f1:
    for ts_file in ts_file_list:
        with open(ts_file, 'rb') as f2:
            shutil.copyfileobj(f2, f1)

# remove files
for ts_file in ts_file_list:
    os.remove(ts_file)
