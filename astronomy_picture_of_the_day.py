#!pip install requests
import requests
import os
from urllib.request import urlretrieve
from datetime import date
def fetch_apod_data(api_key):
    url=f'https://api.nasa.gov/planetary/apod?api_key={api_key}'
    response=requests.get(url)
    if response.status_code==200:
        return response.json()
    else:
        print(f"Error {response.status_code}: Unable to fetch APOD data.")
        return None
def download_image(image_url,save_path):
    urlretrieve(image_url,save_path)
def main():
    api_key='z7VEA8OnPlX5bsRVt6qnwDdvoDsAcR2jgpzKkBj9'
    apod_data=fetch_apod_data(api_key)
    if apod_data:
        image_url=apod_data['url']
        image_title=apod_data['title']
        date_str=apod_data['date']
        save_dir='NASA_APOD_Images'
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        filename=f'{date_str}_{image_title.replace(" ", "_")}.jpg'
        save_path=os.path.join(save_dir, filename)
        download_image(image_url, save_path)
        abs_path=os.path.abspath(save_path)
        print(f"Image downloaded successfully: {abs_path}")
    else:
        print("Image download failed.")
if __name__=="__main__":
    main()

