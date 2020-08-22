<p align="center">
    <a href="#"><img src="img/logo.png"></a>
</p>
<p align="center">
    <em>Python interface to the FDIC's API for publically available bank data</em>
</p>
<p align="center">
    <a href="https://travis-ci.com/dpguthrie/bankfind" target="_blank">
        <img src="https://travis-ci.com/dpguthrie/bankfind.svg?branch=master" alt="Build Status">
    </a>
    <a href="https://codecov.io/gh/dpguthrie/bankfind" target="_blank">
        <img src="https://img.shields.io/codecov/c/github/dpguthrie/bankfind" alt="Coverage">
    </a>
    <a href="https://pypi.org/project/bankfind" target="_blank">
        <img src="https://badge.fury.io/py/bankfind.svg" alt="Package version">
    </a>
</p>

---

**Documentation**: <a target="_blank" href="https://bankfind.dpguthrie.com">https://bankfind.dpguthrie.com</a>

<!-- **Interactive Demo**: <a target="_blank" href="https://bankfind-streamlit.dpguthrie.com">https://bankfind-streamlit.herokuapp.com</a> -->

**Source Code**: <a target="_blank" href="https://github.com/dpguthrie/bankfind">https://github.com/dpguthrie/bankfind</a>

**FDIC Documentation**: <a target="_blank" href="https://banks.data.fdic.gov/docs/">https://banks.data.fdic.gov/docs/</a>

---

## Overview

**bankfind** is a python interface to publically available bank data from the FDIC.

There are currently, as of 8/11/20, five endpoints that the FDIC has exposed to the public:

- **failures** - returns detail on failed financial institutions
- **institutions** - returns a list of financial institutions
- **history** - returns detail on structure change events
- **locations** - returns locations / branches of financial institutions
- **summary** - returns aggregate financial and structure data, subtotaled by year, regarding financial institutions

## Requirements

Python 2.7, 3.5+

- [Requests](https://requests.readthedocs.io/en/master/) - The elegant and simple HTTP library for Python, built for human beings.

## Installation

<div class="termynal" data-termynal data-ty-typeDelay="40" data-ty-lineDelay="700">
    <span data-ty="input">pip install bankfind</span>
    <span data-ty="progress"></span>
    <span data-ty>Successfully installed bankfind</span>
    <a href="#" data-terminal-control="">restart ↻</a>
</div>

## Example

```python
import bankfind as bf

# Get Institutions
data = bf.get_institutions()

# Get Institutions from Colorado with high ROE
data = bf.get_institutions(filters="STNAME:Colorado AND ROE:[25 TO *]")

# Get Commercial Banks from Colorado that aren't S-Corps
data = bf.get_institutions(filters="STNAME:Colorado AND SUBCHAPS:0 AND CB:1")
```

## License

This project is licensed under the terms of the MIT license.
