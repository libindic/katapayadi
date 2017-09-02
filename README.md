# LibIndic Katapayadi


[![Build Status](https://travis-ci.org/libindic/katapayadi.svg?branch=master)](https://travis-ci.org/libindic/katapayadi)
[![Coverage Status](https://coveralls.io/repos/github/libindic/katapayadi/badge.svg?branch=master)](https://coveralls.io/github/libindic/katapayadi?branch=master)

[Katapayadi sankhya](http://en.wikipedia.org/wiki/Katapayadi_sankhya) is a
simplification of [Aryabhata](http://en.wikipedia.org/wiki/Aryabhata)'s
[Sanskrit numerals](http://en.wikipedia.org/wiki/Sanskrit_numerals), due
probably to
[Haridatta](http://www.google.com/search?hl=en&q=Haridatta&btnG=Google+Search)
from Kerala. In Malayalam it is also known as 'Paralperu'. For eg:
ചണ്ഡാംശുചന്ദ്രാധമകുംഭിപാല represents 31415926536 which is π*1000000000000000. More examples
in Malayalam are given in [this page](http://ml.wikipedia.org/wiki/Paralperu)

LibIndic's katapayadi module may be used to find out katapayadi number of a
given string, as well as to get Swarasthanas of a Melakartha number.

## Installation
1. Clone the repository `git clone https://github.com/libindic/katapayadi.git`
2. Change to the cloned directory `cd katapayadi`
3. Run setup.py to create installable source `python setup.py sdist`
3. Install using pip `pip install dist/katapayadi*.tar.gz`

## Usage
```
>>> from libindic.katapayadi import Katapayadi
>>> instance = Katapayadi()
>>> instance.get_number(u"സത്യം")
17
>>> instance.get_swarasthanas(1)
['Sa', 'Ri1', 'Ga1', 'Ma1', 'Pa', 'Da1', 'Ni1', 'Sa']
```

For more details read the [docs](http://katapayadi.rtfd.org/)
