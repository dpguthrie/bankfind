The API uses the Elastic Search [query string syntax](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html#query-string-syntax) for filtering.

## Overview

First, get an idea of what fields you can use to filter from the `meta_dict`.  

```python
>>> import bankfind as bf
>>> fields = bf.meta_dict.keys()
dict_keys(['failures', 'history', 'institutions', 'locations', 'summary'])
```

Each of the keys above represent an endpoint.  The values corresponding to each of the keys above are dictionaries.  The dictionaries contain the fields available as well as the data type, description, and, sometimes, options to filter with.

```python
>>> bf.meta_dict['failures'].keys()
dict_keys(['NAME', 'CERT', 'FIN', 'CITYST', 'FAILDATE', 'FAILYR', 'SAVR', 'RESTYPE1', 'CHCLASS1', 'RESTYPE', 'QBFDEP', 'QBFASSET', 'COST', 'PSTALP'])

>>> bf.meta_dict['failures']['NAME']
{'type': 'string', 'x-elastic-type': 'keyword', 'title': 'Institution Name', 'description': "This is the legal name of the institution. When available, the Institution's name links to useful information for the customers and vendors of these institutions. This information includes press releases, information about the acquiring institution, (if applicable), how your accounts and loans are affected, and how vendors can file claims against the receivership."}
```

## Filters

The syntax for filtering will change based on the data-type.

### strings

**Syntax**: `<FIELD>:<VALUE>`

First, let's filter based on cert, which as you can see from the `meta_dict` is a string field.

```python
>>> bf.meta_dict['failures']['CERT']['type']
'string'

>>> data = bf.get_institutions(filters="CERT:57295")
>>> len(data['data'])
1
```

Chain filters together with "AND":

```python
>>> data = bf.get_institutions(filters="STNAME:Colorado AND CITY:Denver")
>>> len(data['data'])
108
```

Filtering with "OR" is easy also:

```python
>>> data = bf.get_institutions(filters='STNAME:("Colorado","Wyoming")')
>>> len(data['data'])
844
```

### dates

Dates must be entered in the following format:

**Syntax**: `<FIELD>:yyyy-mm-dd`

```python
>>> data = bf.get_institutions(filters='DATEUPDT:2019-12-31')
>>> len(data['data'])
3919
```

They can also be used as ranges:

#### exclusive

Use curly braces `{}` and the range will exclude the beginning and end dates used in the range:

**Syntax**: `<FIELD>:{yyyy-mm-dd TO yyyy-mm-dd}`

```python
>>> data = bf.get_institutions(filters='DATEUPDT:{2015-01-01 TO 2018-12-31}')
>>> len(data['data'])
1921
```

#### inclusive

Use brackets `[]` and the range will the include the beginning and end dates used in the range

**Syntax**: `<FIELD>:[yyyy-mm-dd TO yyyy-mm-dd]`

```python
>>> data = bf.get_institutions(filters='DATEUPDT:[2010-01-01 TO 2018-12-31]')
>>> len(data['data'])
4556
```

### numbers

Numbers can also be used in ranges with the same syntax as dates

#### exclusive

Use curly braces `{}` and the range will exclude the beginning and end values in the range.  Most of the values are represented in thousands.

**Syntax**: `<FIELD>:{Number TO Number}`

```python
>>> data = bf.get_institutions(filters='ASSET:{25000 TO 75000}')
>>> len(data['data'])
5530
```

#### inclusive

Use brackets `[]` and the range will the include the beginning and end dates used in the range

**Syntax**: `<FIELD>:[Number TO Number]`

*The filter below will retrieve institutions with assets greater than or equal to 2 billion or less than or equal to 5 billion.*

```python
>>> data = bf.get_institutions(filters='ASSET:[2000000 TO 5000000]')
>>> len(data['data'])
685
```

#### wildcard

**Syntax**: `<FIELD>:[Number to *]`

*The filter below will retrieve institutions with assets greater than or equal to 5 billion.*

```python
>>> data = bf.get_institutions(filters='ASSET:[5000000 TO *]')
>>> len(data['data'])
602
```

## Search

Flexible text search is also available. Search supports text search and fuzzy matching, as opposed to filters that are exact matches.  Currently, only two endpoints support the search functionality:  `get_institutions` and `get_history`.

The only field that currently supports the search functionality is `NAME`.  It's a similar syntax to the [string filter](#strings).

```python
>>> data = bf.get_institutions(search='NAME:AMG')
>>> len(data['data'])
5
```

Take it a little further:

```python
>>> data = bf.get_institutions(search='NAME:AMG National')
>>> len(data['data'])
1
```
