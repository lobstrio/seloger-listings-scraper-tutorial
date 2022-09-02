# seloger-listings-scraper-tutorial

`seloger-listings-scraper-tutorial` will let you download all **25 first listings from a Seloger search URL** 🏡

With **3 main features** per listing

* url
* price
* type

Below, the power of the `.py` script: 

```bash
$ python3 seloger-listings-scraper-tutorial.py --url "https://www.seloger.com/list.htm?projects=2&types=2&places=\\[\\{%22divisions%22:\\[2248\\]\\}\\]&mandatorycommodities=0&enterprise=0&qsVersion=1.0&m=search_refine-redirection-search_results."
status code 200
0 420 000 € Appartement
1 545 000 € Appartement
2 324 000 € Appartement
3 599 000 € Appartement
4 399 000 € Appartement
~~ success
 _       _         _            
| |     | |       | |           
| | ___ | |__  ___| |_ __ __  
| |/ _ \| '_ \/ __| __/| '__|
| | (_) | |_) \__ \ |_ | |   
|_|\___/|_.__/|___/\__||_|   
```

You can scrape the data from the very search URL you need, using the dynamic `--url` argument. And data is immediately exported to a clean and structured `.csv` file named as `seloger-scraper-results.csv`, in the same folder of your `.py` script.

## Feature Support

`seloger-listings-scraper-tutorial` is a Python scraper, developed for demo purpose, which let you download listings from a SeLoger search URL.

* 25 listings from the first page
* 3 attributes per listing
* elegant `@class` structure
* dynamic `--url` argument
* data exported in structure `.csv` file

`seloger-listings-scraper-tutorial` supports Python 3.9.12.

## Installation

To run `seloger-listings-scraper-tutorial`: 

1. Download the `.py` file
2. Install dependencies
3. Go to [seloger.com](https://www.seloger.com/) and copy headers from a **valid** request 
3. Run the `.py` script

```
$ pip3 install requests lxml
$ python3 seloger-listings-scraper-tutorial.py
```

NB: by default, listings are scraped from this specific search URL https://www.seloger.com/list.htm?projects=2&types=2&places=\\[\\{%22divisions%22:\\[2248\\]\\}\\]&mandatorycommodities=0&enterprise=0&qsVersion=1.0&m=search_refine-redirection-search_results.

:sparkles:

## Notes

This Python script has been written for demo purposes only. You can **only collect up to 25 listings** i.e. you’ll collect only data from the first page, and there is no pagination handling here.

Furthermore, in order to bypass datadome limitations, you’ll need to go on the home page https://www.seloger.com, open the Network tab of your Chrome dev console, and collect headers which led to the 200 request.

If you need extended ressources on this topic, feel free to check our step-by-step tutorial: https://lobstr.io/blog/comment-scraper-seloger-avec-python-et-requests.

Besides, after a certain amount of requests, **you will face consistent bot-mitigation**. The website will possibly enter into an endless loop of captcha challenges. No scalability promise of any kind here.

Though, if you need to **collect data at scale**, please check our ready-made crawler, available here: 
https://lobstr.io/store/a7e1864ab37570369c69a68d1b943d8b/seloger-iter-listings

It will let you: 

* paginate
* collect +20 attributes per listing
* schedule your launch
* auto-export data (.csv, s3, googlesheet)
* multi-thread
* no-code launch

With the possibility to setup and control your scraper from our **human-friendly interface**, or directly from our **[developer-ready API](https://lobstrio.docs.apiary.io/)**.

🦀


