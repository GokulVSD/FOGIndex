<h3 align="center">FOG Index</h3>
<h5 align="center">Provides functions required for calculation of Gunning / regular FOG index</h5>

##

###### Part of an assignment in Software Engineering (SE) during 4th semester BE. These functions were developed as a preliminary solution to meet the deadline. A more accurate and complete version of the Gunning FOG Index calculator may be found here:  [AnushaB05/Fog-Index](https://www.github.com/anushab05/Fog-Index) 


##

<h5 align="center">The compound word splitter utilises PyEnchant's dictionary, it tries to split the word into non-compound words containing two or more letters. The simple syllable splitter may not be very accurate, but for the purpose of FOG index calculation, it gets the job done, while being relatively efficient.</h5>

##

## Install PyEnchant:

```Python
# PyEnchant doesn't work with 64 bit Python on Windows

pip install pyenchant
```

## Uses:

#### Syllable Counter
```Python
from SimpleSyllableCounter import syllables

  syllables('continuity')
  syllables('pierce')
  syllables('pain')
  syllables('unanimous')
  syllables('ancient')
  syllables('euphemism')
  syllables('oesophagus')
```
#### Returns:

```Python
5
1
1
4
2
3
4
```

#### Compound Word Splitter
```Python
from CompoundWordSplitter import split

  split('Undertake','en-UK')
  split('daydream','en-US')
  split('Nail-Polish')
  split('manual')
```
#### Returns:

```Python
['Under', 'take']
['day', 'dream']
['Nail', 'Polish']
['manual']
```
