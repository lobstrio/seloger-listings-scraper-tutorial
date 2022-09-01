import requests
from lxml import html
import argparse
import csv

# add manually from browser req.
HEADERS = {
    'authority': 'www.seloger.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': 'visitId=1657611082733-168489653; _gcl_au=1.1.1398385248.1657611083; _hjid=fd384eba-6c16-4f90-9c7e-c7d4ace2ce9f; _hjSessionUser_1719103=eyJpZCI6IjYwMDdhZGUzLWU1OWMtNTcwYi04ZjI1LWY3Y2FhM2I3YjI2MiIsImNyZWF0ZWQiOjE2NTc2MTEwODMzNjcsImV4aXN0aW5nIjp0cnVlfQ==; mics_uaid=web:1056:12cd1f14-72d4-4c0a-ae93-1e85e3591fc4; uid=12cd1f14-72d4-4c0a-ae93-1e85e3591fc4; mics_vid=28049671765; ABTasty=uid=wa8jg07q9m8gza0z&fst=1657611082763&pst=-1&cst=1657611082763&ns=1&pvt=4&pvis=4&th=; _ga_P0TGS7TPQ7=GS1.1.1657611082.1.1.1657612394.0; sl-pdd_LD_UserId=a4ffa357-d994-44ef-b211-9be3bae4e28c; sl-pdd.abtest.ali-ab-test=Prod; sl-pdd.abtest.c2C-block-redesign=control; sl-pdd.abtest.contact-form-ab-test=Prod; sl-pdd.abtest.enhance-map-ab-test=Excluded; sl-pdd.abtest.lead-phone-ab-test=PageVariante; sl-pdd.abtest.multivariate-test=b; sl-pdd.abtest.slider-ab-test=Excluded; sl-pdd.abtest.street-view-ab-test=Excluded; sl-pdd.abtest.tenant-file-redesign-v2=V2-reference; atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%22701f22cd-2a06-47c6-b632-aa089014ecfb%22%2C%22options%22%3A%7B%22end%22%3A%222023-09-04T08%3A52%3A21.103Z%22%2C%22path%22%3A%22%2F%22%7D%7D; _hjSessionUser_736989=eyJpZCI6IjhjOTQ1ZTdjLWQ1MTctNTY3MC05YzI2LTNjMTkxZGJkMGYxNiIsImNyZWF0ZWQiOjE2NTk1MTY3NDI1NDksImV4aXN0aW5nIjp0cnVlfQ==; mics_vid=28049671765; mics_lts=1659516743127; ry_ry-s3oa268o_realytics=eyJpZCI6InJ5X0IxOENEMkI0LTQ4ODYtNDg1Mi05MDdBLTEwNzg1MTQxNkRCMCIsImNpZCI6bnVsbCwiZXhwIjoxNjkxMDUyNzQxODMyLCJjcyI6MX0%3D; didomi_token=eyJ1c2VyX2lkIjoiMTdhNTMyZGEtMjUzMS02MDM2LWJlMTQtYmFmYTQyOTg1YWNjIiwiY3JlYXRlZCI6IjIwMjItMDgtMTFUMTA6MDU6MjAuOTc2WiIsInVwZGF0ZWQiOiIyMDIyLTA4LTExVDEwOjA1OjIwLjk3NloiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzphZHNjYWxlIiwiYzpmaXJlYmFzZS03OGROS0NGOSIsImM6YmluZy1hZHMiLCJjOmRpZG9taSIsImM6YWNjZW5nYWdlLUU3TGhSTEhRIiwiYzphZHZlcnRpc2luZ2NvbSIsImM6eWFob28tYWQtZXhjaGFuZ2UiLCJjOnlhaG9vLWFuYWx5dGljcyIsImM6eW91dHViZSIsImM6aG90amFyIiwiYzpvbW5pdHVyZS1hZG9iZS1hbmFseXRpY3MiLCJjOmNsb3VkLW1lZGlhIiwiYzphZHN0aXIiLCJjOmFkaW5nbyIsImM6YWNjZW5nYWdlIiwiYzppdmlkZW5jZSIsImM6aGFydmVzdC1QVlRUdFVQOCIsImM6Z29vZ2xlYW5hLTRUWG5KaWdSIiwiYzpzbm93cGxvdy1MclJxaDlxSiIsImM6YmF0Y2gtSEZQRkZGTmMiLCJjOmFwcHNmbHllci1CeWh3ZVZjYiIsImM6YWlyc2hpcC1qUTJ0YmlKZSIsImM6bGF1bmNoZGFyLThxYThRanQ3Il19LCJwdXJwb3NlcyI6eyJlbmFibGVkIjpbImFuYWx5c2VkZS1WRFRVVWhuNiIsImF1ZGllbmNlIiwicHVycG9zZV9hbmFseXRpY3MiLCJkZXZpY2VfY2hhcmFjdGVyaXN0aWNzIiwiZ2VvbG9jYXRpb25fZGF0YSJdfSwidmVuZG9yc19saSI6eyJlbmFibGVkIjpbImdvb2dsZSIsImM6bGF1bmNoZGFyLThxYThRanQ3Il19LCJwdXJwb3Nlc19saSI6eyJlbmFibGVkIjpbImFuYWx5c2VkZS1WRFRVVWhuNiJdfSwidmVyc2lvbiI6MiwiYWMiOiJDZ2VBV0FGa0Fvd0J1QUVUQUpBQVNXQkVrQ1g0RmlBUU1Bb0guQ2dlQVVBVVlBM0FDSmdFZ0FKTEFpU0JMOEN4QUlHQVVEZ0FBIn0=; euconsent-v2=CPdisEAPdisEAAHABBENCbCsAP_AAH_AAAAAIAwMgAFAANAAqABcADgAIAAVAAtABkADSAIoAjABMgCeAKAAUoAsgC2AF4AMIAZgA5gCAgEGAQgAjABHACUgEuATEApAClAFaALgAZYA8gB-gEDAIKAQeAjgCOgE8ALMAYEA0AB1AD9AH_ARqAj0BL4CjwF5gNaAeYBAEEAYDoAFQALgAcABAADIAGgARQAmQBPAFAAKQAZgA5gCEAEdAJcAmABSgDLAH6AQMAgoBBwCLQEcAR0AwIB1AD_gI9AXmBAEAAAA.f_gAD_gAAAAA; _gid=GA1.2.1948134911.1660212321; realytics=1; _hjDonePolls=816466; mics_lts=1659523834796; ry_ry-s3oa268o_so_realytics=eyJpZCI6InJ5X0IxOENEMkI0LTQ4ODYtNDg1Mi05MDdBLTEwNzg1MTQxNkRCMCIsImNpZCI6bnVsbCwib3JpZ2luIjpmYWxzZSwicmVmIjpudWxsLCJjb250IjpudWxsLCJucyI6ZmFsc2V9; _hjIncludedInSessionSample=0; _hjSession_736989=eyJpZCI6ImZkYTYxNDA4LTY4NmQtNGI4Mi05MTM5LWRkMGMxMGRjY2Q1OCIsImNyZWF0ZWQiOjE2NjAzMTEwMTY1ODksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7ImRpc3RyaWJ1dGlvbl90eXBlIjoidmVudGUifSwidXNlcklkIjpudWxsfQ==; _gat_tracker_ecommerce=1; datadome=OcMEwsIXNP_wOsDCZXp~JUnM7Ju8uneweTZB-8YmOZmTMOdA_1xCFMtt_Ef6LD7rfQNCVoRYZyDDEHrT6JYs8vNDywZ6c_kJ9nvFJRPG7qa5Ahv.VSEBbdvzBLtE8J; _ga=GA1.2.418942909.1657611083; _gat_tracker_pageview=1; cto_bundle=CUepsF82RUxOMnYxWXVjeVBNJTJCNWJyeGdyJTJCOUE3NDRTU05sYmhIdnhtZU1RUENJZDdpWjJ4bkczNCUyRkZSQ0tDV2VkR215WGRDZ081TDZkZlFBTm9UdGVucllaRkZZVjRPU005bjVUdWFTVzFLQVU4bHdtUFU3TWh6JTJGNWdabUJkNUV5TEZTMWt0UUtZN1RrbzR3bVVGaUgzYlNHZiUyQmlzOU9mT2V5QmM4QzBueEo0Y2ZsaFh1MlJXZmo0UExiYW1UUlVVZlV5; _dd_s=logs=1&id=91ab00e8-1544-4707-80d6-ca06f351ae24&created=1660311238488&expire=1660312284274; _ga_MC53H9VE57=GS1.1.1660311016.14.1.1660311384.0',
    'referer': 'https://www.seloger.com/',
    'sec-ch-device-memory': '8',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-arch': '"arm"',
    'sec-ch-ua-full-version-list': '"Chromium";v="104.0.5112.79", " Not A;Brand";v="99.0.0.0", "Google Chrome";v="104.0.5112.79"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}


class SeLogerScraper:

    def __init__(self):
        # initiating requests session
        self._s = requests.Session()

    def iter_listings(self, u):
        results = []
        
        # browsing
        response = self._s.get(u, headers=HEADERS)
        assert response.status_code == 200
        print('status code %s' % response.status_code)

        # parsing
        doc = html.fromstring(response.content)
        listings = doc.xpath("//div[@data-test='sl.card-container']")
        for i, listing in enumerate(listings):
            url = "".join(listing.xpath(".//div[contains(@class, 'Card__ContentZone')]/a[contains(@name, 'classified-link') and contains(@class, 'CoveringLink')]/@href"))
            url = 'https://www.seloger.com' + url
            price = "".join(listing.xpath(".//div[@data-test='sl.price-label']/text()"))
            title = "".join(listing.xpath(".//div[@data-test='sl.title']/text()"))
            print('%s %s %s' % (i, price, title))
            results.append(dict(zip(['url','price','title'],[url,price,title])))

        assert results
        return results

    def generate_csv(self, results): 
        # build csv file
        assert isinstance(results, list)
        with open('seloger-scraper-results.csv', "w") as f: 
            fieldnames = ['url','price','title']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for result in results: 
                writer.writerow(result)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--url', '-u', type=str, required=False, help='search url to scrape')
    args = argparser.parse_args()
    url = args.url or 'https://www.seloger.com/list.htm?projects=2&types=2&places=\\[\\{%22divisions%22:\\[2248\\]\\}\\]&mandatorycommodities=0&enterprise=0&qsVersion=1.0&m=search_refine-redirection-search_results.'
    s = SeLogerScraper()
    results = s.iter_listings(url)
    s.generate_csv(results)
    # :crab: :crab:
    print('~~ success')
    print(""" _       _         _            
| |     | |       | |           
| | ___ | |__  ___| |_ __ __  
| |/ _ \| '_ \/ __| __/| '__|
| | (_) | |_) \__ \ |_ | |   
|_|\___/|_.__/|___/\__||_|   
                                
""") 
    

