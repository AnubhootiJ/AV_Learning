from bs4 import BeautifulSoup  # import required libraries

with open("Example.html") as f:
    soup = BeautifulSoup(f, 'lxml')  # creating beautiful soup object

# print(soup.prettify())  # printing the stored content in formatted

print(soup.a)  # will return the first occurrence of a tag in the whole file
print(soup.find('a'))  # same work as above.


all_td = soup.find_all('td')  # will return all the occurrences of td in a result set
print(all_td, "\n")

for all in all_td:  # printing all occurrences of td outside the set
    print(all)


tag = soup.h1
print(tag.name)  # will return name of the tag, if name is missing, it will return the tag itself
tag.name = "Heading"  # we can give a name or update the value of name
print(tag.name)  # will return the updated name


# ###### -- USING STRING -- ###### #
ptag = soup.p
print(ptag.string)  # Getting only the text between the first paragraph tag
ptag.string.replace_with("We changed the text")  # replacing the text of paragraph
print(ptag.string, "\n")

# ###### -- USING TEXT -- ###### #
all_p = soup.find_all('p')
for all in all_p:
    if "documentation" in all.text:  # search all paragraphs for one particular word
        print(all.text)  # printing the text of the resulted paragraph

tag=soup.li
print(tag['id'], "\n")  # getting the id of first li tag

all_a = soup.find_all('a')  
for all in all_a:  # printing all attributes of each a tag
    print(all.attrs)