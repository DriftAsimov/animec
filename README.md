# Anime Character API

This is an unofficial API to extract an anime character data from [myanimelist](https://myanimelist.net/).

Currently, the API is very basic, but I will be adding a lot of stuff to easily extract data.

If you wish to see a feature, please raise an issue. We will surely work on it.

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

## Example 

### Obtaining the character's image url

```python
from animec import *

our_object = Character("okabe rintarou")
result = our_object.search()

title = result["title"]
image_url = result["image"]
link = result["url"]

print(f"Title: {title} \nImage Url: {image_url} \nLink: {link}")
```

## API Documentation

List of properties and methods currently supported by animec.

```
Character(search_query)
Character.search()

Character.search()["title"]
Character.search()["image"]
Character.search()["url]
```

## Credits

```
Author: DriftAsimov
GitHub: https://github.com/DriftAsimov
Language Used: Python
```



> Note: I do not own myanimelist or any imported module or api. I have just used them to extract the data.
