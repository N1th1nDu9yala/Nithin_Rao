import requests
import re
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup


url = "https://cs.illinois.edu/about/people/all-faculty"


# Send an HTTP request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, "html.parser")

# Find and extract faculty member URLs
faculty_links = []
for faculty_link in soup.find_all("a", href=True):
    faculty_url = faculty_link["href"]
    # Check if the URL is a faculty homepage URL (you may need to filter URLs)
    if "faculty" in faculty_url:
        faculty_links.append("https://cs.illinois.edu"+faculty_url)


print(faculty_links)






index =0 
index2=0
while index < len(faculty_links):

 try:
   response = requests.get(faculty_links[index])
   soup = BeautifulSoup(response.text, "html.parser")
   name_element = soup.find('title')
   name = name_element.get_text(strip=True)
   name = name.split('|')[0].strip()

# Check if the request was successful (status code 200)
   
   response.status_code == 200
        
   #soup = BeautifulSoup(response.text, "html.parser")
   biography_section = soup.find('h2', text='Biography')
       
   biography = biography_section.find_next('p').get_text()
       
       
       
   print("Biography of professor:",name,"  ","Url:",faculty_links[index])
   print(" ")
   print(" ")
   print(biography)
   print(" ")
   print(" ")
   index=index+1


 except:
       print("Biography of professor:",name,"  ","Url:",faculty_links[index])
       print(" ")
       print(" ")
       print("Biography of ",name," is not mentioned in this url")
       print(" ")
       print(" ")
       index=index+1


while index2 < len(faculty_links):

 try:
   response = requests.get(faculty_links[index2])
   soup = BeautifulSoup(response.text, "html.parser")
   name_element = soup.find('title')
   name = name_element.get_text(strip=True)
   name = name.split('|')[0].strip()

   
   response.status_code == 200
       
   recent_courses_section = soup.find('h2', text='Recent Courses Taught')

# Extract the list of courses
   courses_list = []
   for li in recent_courses_section.find_next('ul').find_all('li'):
    courses_list.append(li.get_text())
       
       
       
   print("Recent courses taught by professor:",name,"  ","Url:",faculty_links[index2])
   print(" ")
   print(" ")
   print(courses_list)
   print(" ")
   print(" ")
   index2=index2+1


 except:
       print("Recent courses taught by professor:",name,"  ","Url:",faculty_links[index2])
       print(" ")
       print(" ")
       print(" Recent courses taught by ",name," is not mentioned in this url")
       print(" ")
       print(" ")
       index2=index2+1

     