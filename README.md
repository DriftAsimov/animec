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

result = charsearch("okabe rintarou")

print(result.title, result.url, result.image_url, sep="\n")

'''
Output: (As retrived from myanimelist)
Rintarou Okabe (岡部 倫太郎)
https://myanimelist.net/character/35252/Rintarou_Okabe
https://cdn.myanimelist.net/images/characters/6/122643.jpg
'''
```

## API Documentation

List of properties and methods currently supported by animec.

```
charsearch()
    .title
    .url
    .image_url
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
Discord: Drift Asimov#3338
```

> Note: I do not own myanimelist or any imported module or api. I have just used them to extract the data.
