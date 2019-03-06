import requests
import asyncio
import os

ships = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04196502'
cats = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02121808'
dogs = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02084071'
persons = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n00007846'

download_url = persons
path_to_save = 'C:/Users/'


def get_file_format(url):
    try:
        idx = url.rindex('.', -5)
        file_format = url[idx:]
    except Exception as e:
        return None
    return file_format


async def download_images(url):
    urls = requests.get(url).text
    urls = urls.split('\r\n')
    print('Number of URLs: ' + str(len(urls)))

    for url in urls:
        try:
            file_format = get_file_format(url)
            filename = path_to_save + str(i) + file_format
            if os.path.exists(filename):
                continue

            response = requests.get(url)
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(response.content)

            if i % 10 == 0:
                print(i)
        except Exception as e:
            print('Exception occurred at: ' + str(i))
            print(e)


async def main():
    loop.create_task(download_images(download_url))

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except Exception as e:
        pass
    finally:
        loop.close()









