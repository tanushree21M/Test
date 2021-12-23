# Retrives Data from web 

- Problem Stament : Retrieves "Top Stories" from this parliament data RSS feed endpoint. Url : 'https://www.europarl.europa.eu/rss/doc/top-stories/en.xml'
- Programming Laungague - Python

### Solution :

- Install & Import Python Libraries Like BeautifulSoup & urlopen.
- Using Soup from BeautifulSoup we can find the Top Stories which is inside the item.
- Store all Top Stories Data in list and Make DataFrame using command - pd.DataFrame(data)
- Make csv file from DataFrame using syntax - data.to_csv('path')
- Make single function where we can pass the url only & its give final output.

# Csv file
- CSV is generated at the required location.








