import requests
from bs4 import BeautifulSoup

base_url = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc='
loc = 'Newport+Beach,+CA,+United+States'
current_page = 0

while current_page < 201:
    print(current_page)
    url = base_url + loc + "&start=" + str(current_page)
    yelp_r = requests.get(url)
    yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
    businesses = yelp_soup.findAll('div', {'class': 'biz-listing-large'})
    file_path = 'yelp-{loc}-2.txt'.format(loc=loc)
    with open(file_path, "a") as textfile:
        businesses = yelp_soup.findAll('div', {'class': 'biz-listing-large'})
        for biz in businesses:
            #print(biz)
            title = biz.findAll('a', {'class': 'biz-name'})[0].text
            print(title)
            second_line = ""
            first_line = ""
            try:
                address = biz.findAll('address')[0].contents
                for item in address:
                    if "br" in str(item):
                        #print(item.getText())
                        second_line += item.getText().strip(" \n\t\r")
                    else:
                        #print(item.strip(" \n\t\r"))
                        first_line = item.strip(" \n\t\r")
                print(first_line)
                print(second_line)
            except:
                pass
            print('\n')
            try:
                phone = biz.findAll('span', {'class': 'biz-phone'})[0].getText().strip(" \n\t\r")
            except:
                phone = None
            print(phone)
            page_line = "{title}\n{address_1}\n{address_2}\n{phone}\n\n".format(
                    title=title,
                    address_1=first_line,
                    address_2=second_line,
                    phone = phone
                )
            textfile.write(page_line)
    current_page += 10



'''
Working with Django
obj = SomeModel()
obj.title = title
obj.line_1 = first_line
obj.save()
'''




