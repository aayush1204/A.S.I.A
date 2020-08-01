import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint
pages = [str(i) for i in range(1,3)]

files = open('internships.csv','a')
writer = csv.writer(files)
# Add your filter for category eg. Computer Science
category = "computer%20science"
#Add location
location = "mumbai"
# header row of csv
writer.writerow(['Title','Company Name','Location','Website'])
for x in pages:
    URL = 'https://internshala.com/internships/'+ category +'-internship-in-'+ location +'/page-'+x
    page = requests.get(URL)

    sleep(3)
    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(id='internship_list_container')

    job_elems = results.find_all('div', class_='individual_internship')

    for job_elem in job_elems:
        # Each job_elem is a new BeautifulSoup object.
    
        title_elem = job_elem.find('div', class_='profile')
        company_elem = job_elem.find('div', class_='company_name')
        location_elem = job_elem.find('div', id='location_names')
        link_tag = job_elem.find('a', class_='view_detail_button')
        # link = job_elem.find('a', class_='view_detail_button')
        if None in (title_elem, company_elem, location_elem, link_tag):
            continue
        link = link_tag["href"]
        print(title_elem.text.strip() )
        print(company_elem.text.strip() )
        print(location_elem.text.strip() )
        print(f"Apply here: {link}")

        # Accessing individual page for website
        company_url = 'https://internshala.com'+ link
        company_page = requests.get(company_url)
    
        sleep(3)
        soup1 = BeautifulSoup(company_page.content, 'html.parser')

        results_individual_page = soup1.find(id='details_container')
        x = results_individual_page.find('div', class_='internship_details')
        # print(results)
        
        website_tag = x.find('a')
        
        if website_tag is None:
            print("yes")
            continue
        website = website_tag["href"]    
        print(f"Website: {website}")
        writer.writerow([title_elem.text.strip(),
                        company_elem.text.strip(),
                        location_elem.text.strip(),          
                        website,
                        ])

files.close()