# Anime Character Module

This is an unofficial module to extract an anime character data from [myanimelist](https://myanimelist.net/).

Currently, the module is very basic, but I will be adding a lot of stuff to easily extract data.

If you wish to see a feature, please raise an issue. We will surely work on it.

## Installation and Usage

To install the library:
```python
pip install animec
```

To import the library:
```python
from animec import *
```

## Example 

### Getting info about an anime character

```python
from animec import *

url = charinfo("senku ishigami")
print(url)

```

### Obtaining the character's image url

```python
from animec import *

image_url = animechar("okabe rintarou")
print(image_url)

```


```
Author: Drift Asimov
GitHub: https://github.com/DriftAsimov
Language Used: Python
```


> Note: I do not own myanimelist or any imported module or api. I have just used them to extract the data.