## **get_failures**

=== "Details"

    - *Description*:  Detail on failed financial institutions
    - *Return*:  `dict`
    - *Arguments*

    | Argument   | Description                              | Type                         | Default   | Required   | Options                                                                               |
    |:-----------|:-----------------------------------------|:-----------------------------|:----------|:-----------|:--------------------------------------------------------------------------------------|
    | filters     | Filter(s) for the bank search                           | `str`                        | `None`     | optional   |  |
    | fields      | Comma delimited list of fields to retrieve | `str` | All fields included by default         | optional   | |                                                                                      |
    | sort_by      | Field name by which to sort returned data                     | `str`| `FAILDATE`          | optional   | See meta_dict
    | sort_order     | Indicator if ascending or descending                     | `str` | `DESC`       | optional   | `ASC`<br>`DESC`
    | limit      | Number of records to return   | `int` | `10000`       | optional   | 0 to 10,000
    | offset      | Offset of page to return   | `int` | `0`       | optional   | 
    | output      | Format of data to return   | `str` | `json`       | optional   | `json`<br>`pandas`
    | limit      | Number of records to return   | `int` | `10000`       | optional   | 0 to 10,000
    | friendly_fields      | Replace keys / column names with friendlier title   | `bool` | `False`       | optional   | `True`<br>`False`

=== "Example"

    ```python hl_lines="3"
    import bankfind as bf

    data = bf.get_failures()
    data['data'][0]
    ```

=== "Data"

    ```python
    {
        'data': {
            'QBFDEP': 139526,
            'PSTALP': 'WV',
            'FIN': '10536',
            'FAILDATE': '04/03/2020',
            'RESTYPE': 'FAILURE',
            'CITYST': 'BARBOURSVILLE, WV',
            'SAVR': 'DIF',
            'RESTYPE1': 'PA',
            'CHCLASS1': 'NM',
            'NAME': 'THE FIRST STATE BANK',
            'COST': None,
            'QBFASSET': 152400,
            'CERT': 14361,
            'FAILYR': '2020',
            'ID': '4102'
        },
        'score': 1
    }
    ```

## **get_history**


=== "Details"

    - *Description*:  Detail on structure change events
    - *Return*:  `dict`
    - *Arguments*

    | Argument   | Description                              | Type                         | Default   | Required   | Options                                                                               |
    |:-----------|:-----------------------------------------|:-----------------------------|:----------|:-----------|:--------------------------------------------------------------------------------------|
    | filters     | Filter(s) for the bank search                           | `str`                        | `None`     | optional   |  |
    | search   | Flexible text search against institution records (fuzzy name matching)                 | `str`                        | `None`     | optional   |  |
    | fields      | Comma delimited list of fields to retrieve | `str` | All fields included by default         | optional   | |                                                                                      |
    | sort_by      | Field name by which to sort returned data                     | `str`| `FAILDATE`          | optional   | See meta_dict
    | sort_order     | Indicator if ascending or descending                     | `str` | `DESC`       | optional   | `ASC`<br>`DESC`
    | limit      | Number of records to return   | `int` | `10000`       | optional   | 0 to 10,000
    | offset      | Offset of page to return   | `int` | `0`       | optional   | 
    | output      | Format of data to return   | `str` | `json`       | optional   | `json`<br>`pandas`
    | limit      | Number of records to return   | `int` | `10000`       | optional   | 0 to 10,000
    | friendly_fields      | Replace keys / column names with friendlier title   | `bool` | `False`       | optional   | `True`<br>`False`


=== "Example"

    ```python hl_lines="3"
    import bankfind as bf

    data = bf.get_history()
    data['data'][0]
    ```

=== "Data"

    ```python
    {
        'data': {
            'REPORT_TYPE': 711,
            'INSAGENT1': 'DIF',
            'INSAGENT2': '',
            'OFF_PCITY': 'Colorado Springs',
            'EFFDATE': '2020-07-27T00:00:00',
            'CHARTAGENT': 'STATE',
            'PSTALP': 'NE',
            'CLASS': 'NM',
            'FRM_OFF_SERVTYPE': 0,
            'OFF_LONGITUDE': -104.87635200138965,
            'OFF_PSTATE': 'COLORADO',
            'BANK_INSURED': 'Y',
            'CNTYNUM': 157,
            'INSTNAME': 'First State Bank',
            'OFF_PADDR': '3216 W Colorado AVE',
            'FRM_CLCODE': 0,
            'OFF_SERVTYPE_DESC': 'FULL SERVICE - BRICK AND MORTAR',
            'TRANSNUM': 202012234,
            'MZIPREST': '0000',
            'FDICREGION_DESC': 'KANSAS CITY',
            'FRM_OFF_CLCODE': 0,
            'PZIP5': '69361',
            'OFF_PZIPREST': '1906',
            'OFF_NAME': 'First State Bank Colorado Springs West Branch',
            'CERT': 15586,
            'OFF_PSTALP': 'CO',
            'PCITY': 'SCOTTSBLUFF',
            'LATITUDE': 0,
            'PROCDATE': '2020-08-05T00:00:00',
            'ACQDATE': '9999-12-31T00:00:00',
            'CHANGECODE': 711,
            'PADDR': '2002 BROADWAY',
            'MZIP5': '69361',
            'FI_UNINUM': 9873,
            'LONGITUDE': 0,
            'FRM_LATITUDE': 0,
            'STATE': 'NEBRASKA',
            'MSTALP': 'NE',
            'CNTYNAME': 'SCOTTS BLUFF',
            'ACQ_UNINUM': 0,
            'OFF_CNTYNUM': 41,
            'FI_EFFDATE': '2019-06-10T00:00:00',
            'FDICREGION': 11,
            'MSTATE': 'NEBRASKA',
            'FRM_LONGITUDE': 0,
            'OFF_CNTYNAME': 'EL PASO',
            'CHANGECODE_DESC': 'BRANCH OPENING',
            'MCITY': 'SCOTTSBLUFF',
            'MADDR': 'P.O. BOX  1267',
            'OFF_PZIP5': '80904',
            'OUT_UNINUM': 0,
            'PZIPREST': '0000',
            'ORG_STAT_FLG': 'Y',
            'FRM_OFF_LONGITUDE': 0,
            'ENDDATE': '9999-12-31T00:00:00',
            'UNINUM': 625952,
            'OFF_NUM': 6,
            'CLCODE': 21,
            'OFF_SERVTYPE': 11,
            'FRM_OFF_CNTYNUM': 0,
            'ORG_ROLE_CDE': 'BR',
            'REGAGENT': 'FDIC',
            'OFF_LATITUDE': 38.85583298227556,
            'ESTDATE': '2020-07-27T00:00:00',
            'FRM_OFF_LATITUDE': 0,
            'TRUST': 'Full',
            'ID': '20eb98a36c7c77cf6bc019ce391ba7c9'
        },
        'score': 1
    }
    ```


## **get_institutions**

=== "Details"

    - *Description*:  List of financial institutions
    - *Return*:  `dict`
    - *Arguments*

    | Argument   | Description                              | Type                         | Default   | Required   | Options                                                                               |
    |:-----------|:-----------------------------------------|:-----------------------------|:----------|:-----------|:--------------------------------------------------------------------------------------|
    | filters     | Filter(s) for the bank search                           | `str`                        | `None`     | optional   |  |
    | search   | Flexible text search against institution records (fuzzy name matching)                 | `str`                        | `None`     | optional   |  |
    | fields      | Comma delimited list of fields to retrieve | `str` | All fields included by default         | optional   | |                                                                                      |
    | sort_by      | Field name by which to sort returned data                     | `str`| `FAILDATE`          | optional   | See meta_dict
    | sort_order     | Indicator if ascending or descending                     | `str` | `DESC`       | optional   | `ASC`<br>`DESC`
    | limit      | Number of records to return   | `int` | `10000`       | optional   | 0 to 10,000
    | offset      | Offset of page to return   | `int` | `0`       | optional   | 
    | output      | Format of data to return   | `str` | `json`       | optional   | `json`<br>`pandas`
    | limit      | Number of records to return   | `int` | `10000`       | optional   | 0 to 10,000
    | friendly_fields      | Replace keys / column names with friendlier title   | `bool` | `False`       | optional   | `True`<br>`False`


=== "Example"

    ```python hl_lines="3"
    import bankfind as bf

    data = bf.get_institutions()
    data['data'][0]
    ```

=== "Data"

    ```python
    {
        'data': {
            'ZIP': '31087',
            'SASSER': 0,
            'CHRTAGNT': 'STATE',
            'CONSERVE': 'N',
            'REGAGENT2': '',
            'STNAME': 'Georgia',
            'ROAQ': 0.65,
            'INSDATE': '01/01/1934',
            'TE06N528': '',
            'TE06N529': '',
            'OFFOA': 0,
            'FDICDBS': '05',
            'NAMEHCR': '',
            'OCCDIST': '5',
            'CMSA': '',
            'DEPDOM': 59267,
            'CBSA_METRO_FLG': '0',
            'TE10N528': '',
            'NETINC': 124,
            'CBSA_DIV_NO': '',
            'MUTUAL': '0',
            'MSA_NO': '0',
            'OFFFOR': 0,
            'INSSAVE': 0,
            'CHARTER': '0',
            'RSSDHCR': '',
            'TE04N528': '',
            'TE04N529': '',
            'CERT': '10057',
            'STALP': 'GA',
            'SPECGRP': 7,
            'CFPBENDDTE': '31-Dec-9999',
            'TE09N528': '',
            'IBA': 0,
            'INSBIF': 0,
            'INSFDIC': 1,
            'ENDEFYMD': '12/31/9999',
            'MSA': '',
            'TE02N528': '',
            'CB': '1',
            'TE02N529': '',
            'TE07N528': '',
            'FDICSUPV': 'Atlanta',
            'FED': '6',
            'REGAGNT': 'FDIC',
            'NEWCERT': 0,
            'ASSET': 76416,
            'CBSA_MICRO_FLG': '1',
            'OFFICES': 1,
            'STCNTY': '13141',
            'CSA_FLG': '0',
            'CITY': 'Sparta',
            'CLCODE': '21',
            'INACTIVE': 0,
            'CMSA_NO': '0',
            'STALPHCR': '',
            'INSAGNT1': 'DIF',
            'BKCLASS': 'NM',
            'EFFDATE': '08/31/2009',
            'SUPRV_FD': '05',
            'DATEUPDT': '09/02/2009',
            'INSAGNT2': '',
            'TE05N528': '',
            'TE05N529': '',
            'ROEQ': 2.96,
            'FDICREGN': 'Atlanta',
            'FLDOFF': 'Savannah',
            'WEBADDR': 'http://www.bankofhancock.com',
            'QBPRCOML': '2',
            'COUNTY': 'Hancock',
            'DOCKET': '0',
            'ULTCERT': '10057',
            'OTSDIST': '2',
            'LAW_SASSER_FLG': 'N',
            'PARCERT': '0',
            'ROA': 0.65,
            'CFPBFLAG': 0,
            'RISDATE': '12/31/2019',
            'ROE': 2.96,
            'INSCOML': 1,
            'OTSREGNM': 'Southeast',
            'EQ': '17026',
            'RUNDATE': '08/08/2020',
            'TE03N528': '',
            'TE03N529': '',
            'NAME': 'Bank of Hancock County',
            'HCTMULT': '',
            'CBSA_DIV': '',
            'ADDRESS': '12855 Broad Street',
            'OFFDOM': 1,
            'SUBCHAPS': '0',
            'PROCDATE': '09/02/2009',
            'INSSAIF': 0,
            'DENOVO': '0',
            'CBSA_NO': '33300',
            'ACTIVE': 1,
            'CFPBEFFDTE': '31-Dec-9999',
            'STCHRTR': 1,
            'REPDTE': '03/31/2020',
            'FORM31': '0',
            'CSA': '',
            'INSDIF': 1,
            'TE01N529': '',
            'ROAPTX': 0.65,
            'STNUM': '13',
            'OAKAR': 0,
            'SPECGRPN': 'Other Specialized Under 1 Billion',
            'ROAPTXQ': 0.65,
            'FED_RSSD': '37',
            'CSA_NO': '',
            'CBSA_METRO': 0,
            'INSTCRCD': 0,
            'DEP': 59267,
            'UNINUM': '6429',
            'INSTAG': '0',
            'TE01N528': '',
            'CITYHCR': '',
            'TRACT': '0',
            'CBSA': 'Milledgeville, GA',
            'CBSA_DIV_FLG': '0',
            'TE08N528': '',
            'NETINCQ': 124,
            'CHANGEC1': 520,
            'CERTCONS': '0',
            'ESTYMD': '09/01/1904',
            'FEDCHRTR': 0,
            'TRUST': '0',
            'ID': '10057'
        },
        'score': 1
    }
    ```

## **get_locations**

=== "Details"

    - *Description*:  Detail on failed financial institutions
    - *Return*:  `dict`
    - *Arguments*

    | Argument   | Description                              | Type                         | Default   | Required   | Options                                                                               |
    |:-----------|:-----------------------------------------|:-----------------------------|:----------|:-----------|:--------------------------------------------------------------------------------------|
    | filters     | Filter(s) for the bank search                           | `str`                        | `None`     | optional   |  |
    | fields      | Comma delimited list of fields to retrieve | `str` | All fields included by default         | optional   | |                                                                                      |
    | sort_by      | Field name by which to sort returned data                     | `str`| `FAILDATE`          | optional   | See meta_dict
    | sort_order     | Indicator if ascending or descending                     | `str` | `DESC`       | optional   | `ASC`<br>`DESC`
    | limit      | Number of records to return   | `int` | `10000`       | optional   | 0 to 10,000
    | offset      | Offset of page to return   | `int` | `0`       | optional   | 
    | output      | Format of data to return   | `str` | `json`       | optional   | `json`<br>`pandas`
    | limit      | Number of records to return   | `int` | `10000`       | optional   | 0 to 10,000
    | friendly_fields      | Replace keys / column names with friendlier title   | `bool` | `False`       | optional   | `True`<br>`False`


=== "Example"

    ```python hl_lines="3"
    import bankfind as bf

    data = bf.get_locations()
    data['data'][0]
    ```

=== "Data"

    ```python
    {
        'data': {
            'ZIP': '21613',
            'CBSA_NO': '15700',
            'BKCLASS': 'SM',
            'FI_UNINUM': 3221,
            'STNAME': 'Maryland',
            'CSA': 'Salisbury-Cambridge, MD-DE',
            'COUNTY': 'Dorchester',
            'MAINOFF': 0,
            'OFFNAME': 'WOODS ROAD BRANCH',
            'CBSA_METRO_FLG': '0',
            'CBSA_MICRO_FLG': '1',
            'CSA_NO': '480',
            'CBSA_METRO': 0,
            'CBSA_DIV_NO': '',
            'RUNDATE': '08/07/2020',
            'NAME': '1880 Bank',
            'UNINUM': 204568,
            'SERVTYPE': 11,
            'CSA_FLG': '1',
            'STCNTY': '24019',
            'CBSA': 'Cambridge, MD',
            'CBSA_DIV': '',
            'CBSA_DIV_FLG': '0',
            'CITY': 'Cambridge',
            'ADDRESS': '803 Woods Road',
            'CERT': '4829',
            'STALP': 'MD',
            'OFFNUM': 1,
            'ESTYMD': '12/23/1968',
            'ID': '204568'
        },
        'score': 1
    }
    ```

## **get_summary**

=== "Details"

    - *Description*:  Detail on failed financial institutions
    - *Return*:  `dict`
    - *Arguments*

    | Argument   | Description                              | Type                         | Default   | Required   | Options                                                                               |
    |:-----------|:-----------------------------------------|:-----------------------------|:----------|:-----------|:--------------------------------------------------------------------------------------|
    | filters     | Filter(s) for the bank search                           | `str`                        | `None`     | optional   |  |
    | fields      | Comma delimited list of fields to retrieve | `str` | All fields included by default         | optional   | |                                                                                      |
    | sort_by      | Field name by which to sort returned data                     | `str`| `FAILDATE`          | optional   | See meta_dict
    | sort_order     | Indicator if ascending or descending                     | `str` | `DESC`       | optional   | `ASC`<br>`DESC`
    | limit      | Number of records to return   | `int` | `10000`       | optional   | 0 to 10,000
    | offset      | Offset of page to return   | `int` | `0`       | optional   | 
    | output      | Format of data to return   | `str` | `json`       | optional   | `json`<br>`pandas`
    | limit      | Number of records to return   | `int` | `10000`       | optional   | 0 to 10,000
    | friendly_fields      | Replace keys / column names with friendlier title   | `bool` | `False`       | optional   | `True`<br>`False`

=== "Example"

    ```python hl_lines="3"
    import bankfind as bf
    
    data = bf.get_failures()
    data['data'][0]
    ```

=== "Data"

    ```python
    {
        'data': {
            'INTINC2': 51722726,
            'EXTRA': 1316,
            'LNATRES': 9769341,
            'chrtrest': 0,
            'STNAME': 'United States and Other Areas',
            'ILNS': 39718788,
            'LNAG': 3306388,
            'EINTEXP2': 10348941,
            'EPREMAGG': 2063405,
            'YEAR': '2019',
            'BKPREM': 8315925,
            'INTAN': 12025281,
            'LNRE': 444072342,
            'chartoth': 1,
            'IGLSEC': 482482,
            'OT_BIF': 0,
            'EAMINTAN': 456598,
            'newcount': 0,
            'DEPI': 840535976,
            'EFHLBADV': None,
            'tofail': 1,
            'SCMTGBK': 292023664,
            'NTRTMLG': 118177154,
            'OEA': 1483578,
            'EFREPP': 90846,
            'LNLSGR': 655127513,
            'NETINC': 15194171,
            'TOT_OTS': 334,
            'CONS': 0,
            'OTHNBORR': 91479748,
            'LNREMULT': 68529412,
            'P9LNLS': 7463014,
            'COUNT': 659,
            'LNRERES': 253541537,
            'EQCS': 790384,
            'SCAGE': 304050945,
            'LNRECONS': 23453492,
            'TOT_FDIC': 325,
            'EINTEXP': 10348941,
            'TPD': 13656751,
            'LNCI': 43378018,
            'EQNM': 125002942,
            'INTBLIB': 1007906756,
            'liqasstd': 0,
            'SC': 385021771,
            'INTBAST': 1096557030,
            'EDEPDOM': 8287049,
            'ILNDOM': 39718603,
            'NCLNLS': 11414221,
            'UNINC': 133264,
            'ISC': 10339424,
            'LIABEQ': 1153906385,
            'tochrt': 7,
            'IFEE': 865589,
            'TOT_SAVE': 659,
            'LNRESRE': None,
            'alsonew': 0,
            'NUMEMP': 121746,
            'ASSET': 1153906405,
            'TINTINC': 11723463,
            'NALNLS': 3951207,
            'EOTHNINT': 14513593,
            'TRADES': 0,
            'ESAL': 12889946,
            'ILNLS': 39999263,
            'LIAB': 1028873691,
            'LNDEP': 417597,
            'OTHBFHLB': 75972627,
            'ITAX': 4361954,
            'EQCDIVP': 12402,
            'SCRES': None,
            'TRADE': 356945,
            'MISSADJ': -1,
            'FD_BIF': 0,
            'CRLNLS': 1422110,
            'LS': 5575099,
            'tomerg': 11,
            'ELNATR': 5247975,
            'LNCRCD': 99551689,
            'INTINC': 51722726,
            'EQUPTOT': 70024149,
            'CHBALI': 64693509,
            'EQPP': 282890,
            'PTXNOINC': 19078526,
            'OINTINC': 11723463,
            'tortc': 0,
            'ILS': 280475,
            'FD_SAIF': 0,
            'EQNWCERT': None,
            'OINTBOR': 85304294,
            'SCUST': 12170713,
            'combos': 12,
            'P3LNLS': 6193737,
            'OTLNCNTA': None,
            'OTHLIAB': 16342193,
            'IFREPO': 18439,
            'LNLSNET': 645358172,
            'LNCONOT1': None,
            'EQCDIVC': 13089203,
            'SCUSA': 316221658,
            'DRLNLS': 7211296,
            'OTHBORR': 1685904,
            'EQCDIV': 13101605,
            'EDEP': 8287065,
            'BRWDMONY': 1685904,
            'comboass': 0,
            'FREPO': 1126633,
            'CHBAL': 73009001,
            'ALLOTHER': 14950385,
            'FREPP': 6067807,
            'IRAKEOGH': 123424709,
            'OT_SAIF': 0,
            'ORE': 302690,
            'SCMUNI': 10308292,
            'ESUBND': 278,
            'SCUS': 316221658,
            'ITRADE': 0,
            'OINTEXP': 1777028,
            'liqunass': 1,
            'DDT': 58550380,
            'EDEPFOR': 16,
            'LNALLOTH': 42378773,
            'SCEQ': 258574,
            'ITAXR': 19078526,
            'ILNFOR': 185,
            'ICHBAL': 1365600,
            'LNRELOC': 21179492,
            'STNUM': '0',
            'SUBLLPF': 26052,
            'OONONII': 11554071,
            'CORPBNDS': 55721897,
            'NONIX': 29466944,
            'NCHGREC': 5789186,
            'OTHASST': 28389467,
            'DEP': 921025698,
            'NIM': 41373785,
            'LNCON': 141930462,
            'EQSUR': 53905519,
            'SAVINGS': 659,
            'ORET': 302690,
            'CB_SI': 'SI',
            'TOINTEXP': 2061876,
            'LNMUNI': 1630491,
            'LNRENRES': 98547901,
            'NONII': 12419660,
            'BRO': 104643398,
            'ID': 'SI_2019_0'
        },
        'score': 1
    }
    ```
