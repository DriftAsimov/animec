# Anime Character API

An unofficial API to get data about anime characters, anime news and more.
The API scrapes [myanimelist](https://myanimelist.net/) to get data about anime characters and anime news.

Currently, the API is very basic, but I will be adding a lot of stuff to easily extract data.

If you wish to see a feature, please raise an [issue](https://github.com/DriftAsimov/animec). We will surely work on it.
You can also join our [Discord](https://discord.gg/x3qAZV3) to get regular updates about the API.

## Installation and Usage

To install the library:
```python
pip install animec
```

To import the library:
```python
import animec
# OR
from animec import *
```

## Examples

### Extracting an anime character's data

```python
from animec import *

result = charsearch("okabe rintarou")

print(result.title, result.url, result.image_url, sep="\n")

'''
Output: (As retrieved from myanimelist)
Rintarou Okabe (岡部 倫太郎)
https://myanimelist.net/character/35252/Rintarou_Okabe
https://cdn.myanimelist.net/images/characters/6/122643.jpg
'''
```

### Requesting anime news

```python
from animec import *

news = aninews(3)   #default value is 2

print(news.news)    #returns a dictionary with news titles as keys and values as links
print(news.titles)  #returns news titles
print(news.links)   #returns news links

```

## API Documentation

List of properties and methods currently supported by animec.
Official documentation coming soon!

```
charsearch()
----- .title
----- .url
----- .image_url

aninews()
----- .news
----- .titles
----- .links
```

## Credits

```
Author: DriftAsimov
GitHub: https://github.com/DriftAsimov
Language Used: Python
```

## Contact Us
```
Mail: driftasimov@gmail.com
Discord: Drift Asimov#3338 | https://discord.gg/x3qAZV3
```

> Note: I do not own myanimelist or any imported module or api. I have just used them to extract the data.
