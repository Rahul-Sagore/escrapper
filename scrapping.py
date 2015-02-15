# Importing python library for fetching Internet resource and pattern searching
import urllib2
import re
from BeautifulSoup import BeautifulSoup

def scrap_input(usr_input):
    
    inp = usr_input.split()
    format_input = "+".join(inp)
    

    junglee_url = "http://www.junglee.com/mn/search/junglee/ref=nb_sb_iss_cat_00000_9?url=node%3Daps&field-keywords="+format_input+"&rush=n"
    smartprix_url = "http://www.smartprix.com/products/?q="+format_input+"&cat=all"

    jung_soup = get_soup(junglee_url, format_input)
    smart_soup = get_soup(smartprix_url, format_input)
    
    #Calling fuction for finding text in html
    jung_products = get_result('a', "class", "title", jung_soup)
    jung_prices = get_result('span', "class", "price", jung_soup)

    smart_prod = get_result('div', "class", "info", smart_soup)
    smart_products = re.findall(r'<h2>(.*?)</h2>', str(smart_prod))
    smart_prices = get_result('span', "class", "price", smart_soup)

    return jung_products, jung_prices, smart_products, smart_prices

def get_soup(url, input):
    #Grabbing Html from the url
    response = urllib2.urlopen(url)
    html = response.read()
    
    #Creating beautifulsoup object
    soup = BeautifulSoup(html)
    return soup

#Custom function for finding particular tag with specific attribute
def get_result(tag, attr, val, soup):
    ''' Accepts 4 parameters : tag - html tag name, attr - html tag attr
        , val - value of attribute, soup - containing html response. Returns the list of matching
        patterns'''
    #fetching tag using beautifulSoup Method
    results = soup.findAll(tag, attrs={attr : val})

    return list(results)