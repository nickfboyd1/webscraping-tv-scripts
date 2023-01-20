
### Setup
# Load libraries
import requests as r
from bs4 import BeautifulSoup
import pandas as pd

# Define URL for The Leftovers script db
url_base = "https://transcripts.foreverdreaming.org"
url_show = "/viewforum.php?f=48"
url_show_full = url_base + url_show

# Check status code
response = r.get(url_show_full)

# Get HTML document from link
html = response.text

# Convert HTML document into bs4 object
soup = BeautifulSoup(html, 'lxml')

# Find all episodes titles/links in bs4 object
all_epis = soup.find_all(class_="topictitle")

# Remove first and last elements (not episodes)
all_epis_clean = all_epis[1:-1]

# Create lists for storing episode info
seasons = []
episodes = []
titles = []
links = []

### Loop through each episode in soup object and extract relevant information
for i in all_epis_clean:
    
    # Extract text
    text = i.getText()
    
    # Append text to appropriate list
    seasons.append(text[0:2])
    episodes.append(text[4:6])
    titles.append(text[8:])
    
    # Extract url
    link = i.get("href")

    # Append url to url list
    link_full = url_base + link[1:]
    links.append(link_full)
    
### Loop through links, grab script text, add to dataframe
# Create script list
scripts = []

# Loop through links
for url in links:
    
    # Make request to url
    response = r.get(url)

    # Get HTML document from link
    html = response.text

    # Convert HTML document into bs4 object
    soup = BeautifulSoup(html, 'lxml')
    
    # Extract all text
    dialogue = soup.find("div", class_="content").getText().strip()
    
    # Append to list
    scripts.append(dialogue)

# Merge lists into single dataframe
the_leftovers_epis = pd.DataFrame({
    "season": seasons,
    "episode": episodes,
    "title": titles,
    "link": links,
    "script": scripts
})

### Enhance database
# Grab episode ratings from rotten tomatoes and add to db


# Grab episode viewing statistics and add to db
# Check this out --- https://en.wikipedia.org/wiki/List_of_The_Leftovers_episodes#Season_3_(2017)


# Write to CSV
the_leftovers_epis.to_csv("/Users/nickboyd/Desktop/GitHub/leftovers-tweet-bot/the_leftovers_scripts.csv", index=False)
