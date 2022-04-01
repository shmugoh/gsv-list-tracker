from urllib import request

def download():
    url = 'https://www.google.com/streetview/static/feed/driving/data.json'
    file_name = 'data.json'
    request.urlretrieve(url, file_name)

if __name__ == '__main__':
    download()