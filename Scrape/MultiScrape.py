from bs4 import BeautifulSoup  # to parse the website
import requests  # to access the webpage
import csv

csv_file = open('Earthquake14-17.csv', 'w', newline='')  # opening the CSV file, if file not found, it will create a new file
csv_write = csv.writer(csv_file)
csv_write.writerow(['Date', 'Time(UTC)', 'Time(IST)', 'Lat', 'Lang', 'Depth(KM)', 'Magnitude', 'Region'])  # writing the headers in the CSV file

years = ['2014', '2015', '2016', '2017']  # year list for URLs
for year in years:
    URL = "http://www.imd.gov.in/pages/lyear1.php?year=" + year  # getting URL for each year
    # print(URL)
    result = requests.get(URL)
    src = result.content  # storing the contents of the website into variable src
    soup = BeautifulSoup(src, 'lxml')  # creating object to parse the website
    # print(soup.prettify())

    list = []  # creating empty list ot append data to

    for see in soup.findAll('font'):  # replacing all font tags with its immediate children tag, that is, b tag here
        see.replaceWithChildren()

    for row in soup.find_all('tr'):  # getting all b tags within all tr tags to get relevant information
        for data in row.find_all('b'):
            data = data.text  # getting text within the tag
            list.append(data.strip())  # using strip() to remove any extra unwanted data
        csv_write.writerow(list)  # writing into the csv file by giving the list
        list = []  # setting list to empty for next batch of data

csv_file.close()
