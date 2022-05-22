import requests
from bs4 import BeautifulSoup
import pandas as pd

while True:
  # Read file to get Craigslist URL and query filter
  infile = open('cl_search.txt', 'r+') 
  text = infile.readline()
  infile.truncate(0)
  infile.close()
  if "craigslist.org/search/" in text:
    BASE_URL = text

    response = requests.get(BASE_URL) # Get HTML of the BASE_URL?query=
    soup = BeautifulSoup(response.content, "html.parser") #b4s object to parse HTML

    # Determine number of pages to scrape
    total_count = int(soup.find('span','totalcount').text)
    range_count = int(soup.find('span','rangeTo').text)
    if range_count == total_count:
      page_count = 1
    else:
      page_count = (total_count // range_count)+1 

    results_data = [] # Stores data to be returned
    IMG_URL = 'https://images.craigslist.org/{}_300x300.jpg' # Image source template to be filled by scrape

    for i in range (0, page_count): 
      # Updates URL with new starting index to get parasable HTML data
      params = {
        's': i*120, # Starting range 
      }
      response = requests.get(BASE_URL, params=params)
      soup = BeautifulSoup(response.content, "html.parser")
      print('Scraping Page {0} out of {1} '.format(i+1,page_count))

      # Finds all result elements and saves releveant data from each result
      result_rows = soup.find_all("li", class_="result-row") 
      for result in result_rows: 
        post_id = result.h3.a['data-id'] 
        date = result.time['datetime']
        title = result.h3.a.text
        price = result.find('span','result-price').text if result.find('span','result-price') else ''
        location = result.find('span','result-hood').text.replace("(","").replace(")","").strip() if result.find('span','result-hood') else ''
        post_url = result.h3.a['href']
        photo_ids = result.find('a', class_='result-image gallery') 
        photo = IMG_URL.format(photo_ids['data-ids'].split(',')[0][2:]) if photo_ids else '' 
        
        results_data.append([post_id, date, title, price, location, post_url, photo])

    print("Finished processing all pages.")

    # Create data frame from collected data and save it to a .txt file
    columns = ('post_id', 'date', 'title', 'price', 'location', 'post-url', 'photo')
    df = pd.DataFrame(results_data, columns=columns)
    print(df)
    outfile = open("cl_results.txt", "r+")
    outfile.truncate(0)
    outfile.close()
    df.to_csv('cl_results.txt', index=False)


