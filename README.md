<p align = "center"><img width="248" height="248" src="https://i.imgur.com/IyUybvv.png"></p>
<p align = "center"><a href = "https://discord.gg/x3qAZV3" target = "_blank"><img src = "https://discord.com/api/guilds/759396489373155338/embed.png"></a></p>

# Animec

A module to get data about anime characters, news, info, lyrics and more.
The module scrapes [myanimelist](https://myanimelist.net/) to parse requested data.

If you wish to see a feature, please raise an [issue](https://github.com/DriftAsimov/animec). We will surely work on it.
You can also join our [Discord](https://discord.gg/x3qAZV3) to get regular updates about the module.

## Installation and Usage

To install the module:
```python
pip install animec
```

To import the module:
```python
import animec
# OR
from animec import *
```

## Examples

### Extracting an anime character's data

```python
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
news = aninews(3)   #default value is 2

print(news.titles)  #returns news titles
print(news.links)   #returns news links
print(news.descripion)   #returns news description
print(news.images)  #returns news images

```

### Getting anime info and recommendations

```python
anime = anime("dr stone")
recommendations = anime.recommend()

print(anime.url)
print(anime.name)
print(anime.description)    #check the documentation for a list of all supported attributes
print(recommendations)  #returns a list of anime recommendations
```

### Anime Lyrics

```python
lyrics = anilyrics("Ashiato")
print(lyrics.romaji)
```

## API Documentation

The Official Documentation for animec can be found [here](https://animec.readthedocs.io/en/latest/).

## Credits

```
Author: DriftAsimov
GitHub: https://github.com/DriftAsimov
Language Used: Python
Sites: 
https://myanimelist.net/
https://www.animesonglyrics.com/
```

## Contact Us
```
Mail: driftasimov@gmail.com
Discord: Drift Asimov#3338 | https://discord.gg/x3qAZV3
```
