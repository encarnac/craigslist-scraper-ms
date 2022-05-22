# craigslist-scraper
## Description
Scrapes Craigslist search results for the post id, date, title, price, location, post url, and photo url of all listings and stores the data in a text file.
  
<br /> 

## Getting Started
  
  
### Dependencies

  *   [ Requests](https://github.com/psf/requests)
  *   [ Beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
  *   [ Pandas](https://github.com/pandas-dev/pandas)  

### How to Install

1. Clone repository
      ```sh

          $ git clone https://github.com/cencarnado/craigslist-scraper-ms.git
          $ cd craigslist-scraper-ms

      ```

2. Create a virtual environment
      ```ps

          $ craigslist-scraper-ms> python -m venv venv

      ```

3. Activate your virtual environment
      ```ps

          $ craigslist-scraper-ms> venv\Scripts\Activate.ps1

      ```

4. Install all dependencies 
      ```ps

          $ (venv) craigslist-scraper-ms> python -m pip install -r  ./requirements.txt

      ```

### How to Use

1. Run the script `cl_scraper.py`
    ```ps

        $ (venv) craigslist-scraper-ms> python cl_scraper.py

    ```

2. Paste the Craigslist URL for the search results you want to scrape in `cl_search.txt`
    ```ps
    \cl_search.txt

        1  https://losangeles.craigslist.org/search/sss?query=holland+lop&hasPic=1&postedToday=1&max_price=200

    ```
    
3. View all the data in `cl_results.txt` as a dataframe in the form of
   
    ```ps
    \cl_results.txt

        1  post_id,     date,               title,        price,   location,      post-url,         photo
        2  1234567890,  2022-05-21 16:13,   holland lop,  $65,     Los Angeles,   http://...html,   http://...jpg
        3 ...
        .. 
        9  0987654321,  2022-05-21 16:39,   bunnies,      $75,      ,             http://...html,   http://...jpg

    ```

<br /> 

## Version History

* 0.1
    * Initial Release


<br /> 


## License

[MIT]()
        

