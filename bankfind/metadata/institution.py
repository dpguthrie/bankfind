institution_dict = {
    'ACTIVE': {
        'type': 'string',
        'title': 'inactive',
        'description': 'Institutions that are currently open and insured by the FDIC',
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': 'if(ctx.INST_FIN_ACTV_FLG?.toLowerCase() == "y") { \n  ctx.ACTIVE = 1; \n} else { \n  ctx.ACTIVE = 0;\n}\n'
                }
            }
        }],
    },
    'ADDRESS': {
        'type': 'string',
        'title': 'Physical Street Address',
        'description': 'Street address at which the institution or one of its branches is physically located.',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_PHY_LNE1_TXT'
        }]
    },
    'ASSET': {
        'type': 'number',
        'title': 'Total assets',
        'description': 'The sum of all assets owned by the institution including cash, loans, securities, bank premises and other assets. This total does not include off-balance-sheet accounts.',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'ASSET'
        }]
    },
    'BKCLASS': {
        'title': 'Bank Charter Class',
        'options': ['N', 'SM', 'NM', 'SB', 'SA', 'OI'],
        'description': "A classification code assigned by the FDIC based on the institution's charter type (commercial bank or savings institution), charter agent (state or federal), Federal Reserve membership status (Fed member, Fed nonmember)and its primary federal regulator (state chartered institutions are subject to both federal and state supervision).   N = commercial bank, national (federal) charter and Fed member, supervised by the Office of the Comptroller of the Currency (OCC)  SM = commercial bank, state charter and Fed member, supervised by the Federal Reserve (FRB)  NM = commercial bank, state charter and Fed nonmember, supervised by the FDIC  SB = savings banks, state charter, supervised by the FDIC  SA = savings associations, state or federal charter, supervised by the Office of Thrift Supervision (OTS)  OI = insured U.S. branch of a foreign chartered institution (IBA)",
        'type': 'string',
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': 'if(ctx.INST_CLASS_CDE?.toLowerCase() == "sb" || ctx.INST_CLASS_CDE?.toLowerCase() == "sl") { \n  ctx.BKCLASS = \'SA\'; \n} else if (ctx.INST_CLASS_CDE?.toLowerCase() == "mi" || ctx.INST_CLASS_CDE?.toLowerCase() == "si") { \n  ctx.BKCLASS = \'SB\';\n} else {\n  ctx.BKCLASS = ctx.INST_CLASS_CDE;\n}\n'
                }
            }
        }]
    },
    'CB': {
        'title': 'Community Bank',
        'description': 'FDIC community banks are identified based on criteria defined in the FDIC Community Banking Study. Using detailed balance sheet and geographic data, the study defines communtiy banks in terms of their traditional relationship banking and limited geographic scope of operations',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'CB'
        }]
    },
    'CBSA': {
        'title': 'Name of the Core Based Statistical Area',
        'description': 'The name associated with the numeric code that the U.S. Census Bureau Office of Management and Budget assigns for the CBSA. The 2000 standards provide that each CBSA must contain at least one urban area of 10,000 or more population.  Metropolitan and micropolitan statistical areas are two categories of core based statistical areas. If an institution is not defined as a CBSA, the value of the field will be zero. For more information see: http://www.census.gov/population/www/estimates/metroarea.html .  ',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RELATION',
            'field': 'CBSANAME'
        }]
    },
    'CBSA_DIV': {
        'title': 'Name of the Core Based Statistical Division',
        'description': 'The name associated with the numeric code given by the US Census Bureau office of Management and Budget (2000 standards) that represents the core based statistical division (CBSADIV). A metropolitan division is a county or group of counties within a core based statistical area that contains a core with a population of at least 2.5 million. A CBSA metropolitan division consists of one or more main/secondary counties that represent an employment center or centers, plus adjacent counties associated with the main county or counties through commuting ties. If an institution is not defined as a CBSA division the value of the field will be zero.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RELATION',
            'field': 'CBSA_DIV_NAME'
        }]
    },
    'CBSA_DIV_FLG': {
        'title': 'CBSA Statistical Area Flag',
        'description': 'A flag used to indicate whether an institution is in a CBSA division 1=yes, 0=no',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RELATION',
            'field': 'DIVISION_FLAG'
        }]
    },
    'CBSA_DIV_NO': {
        'title': 'Core Based Statistical Division Number',
        'description': 'The numeric code given by the US Census Bureau office of Management and Budget that represents the core based statistical division (CBSADIV)under the year 2000 standards. A metropolitan division is a county or group of counties within a core based statistical area that contains a core with a population of at least 2.5 million. A CBSA metropolitan division consists of one or more main/secondary counties that represent an employment center or centers, plus adjacent counties associated with the main county or counties through commuting ties. If an institution is not defined as a CBSA division the value of the field will be zero. ',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RELATION',
            'field': 'CBSA_DIVISION'
        }]
    },
    'CBSA_METRO': {
        'title': 'CBSA Metro Code',
        'description': "Numeric code assigned by the U.S. Census Bureau's Office of Management and Budget for a metropolitan area within a CBSA",
        'type': 'string',
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': 'if(ctx.CBSA_METRO_FLG == "1") {\n  ctx.CBSA_METRO = ctx.CBSA_NO;\n} else {\n  ctx.CBSA_METRO = 0;\n}\n'
                }
            }
        }]
    },
    'CBSA_METRO_FLG': {
        'title': 'Metro Statistical Area Flag',
        'description': 'A flag used to indicate whether an institution is in a metropolitan statistical area.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RELATION',
            'field': 'METRO_FLAG'
        }],
        'options': [0, 1]
    },
    'CBSA_METRO_NAME': {
        'title': 'CBSA Metro Name',
        'description': "Name associated with the numeric code that the U.S. Census Bureau's Office of Management and Budget assigns for the metropolitan areas within a CBSA; are now also the basis for Metropolitan Statistical Areas (MSAs)",
        'type': 'string',
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': 'if(ctx.CBSA_METRO_FLG == "1") {\n  ctx.CBSA_METRO_NAME = ctx.CBSA;\n} else {\n  ctx.CBSA_METRO_NAME = 0;\n}\n'
                }
            }
        }]
    },
    'CBSA_MICRO_FLG': {
        'title': 'Micro Statistical Area Flag',
        'description': 'A flag used to indicate whether an institution is in a micropolitan statistical area',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RELATION',
            'field': 'MICRO_FLAG'
        }],
        'options': [0, 1]
    },
    'CBSA_NO': {
        'title': 'Numeric Code for the Core Based Statistical Area',
        'description': 'The numeric code that the U.S. Census Bureaus Office of Management and Budget assigns for the CBSA. The 2000 standards provide that each CBSA must contain at least one urban area of 10,000 or more population.  Metropolitan and micropolitan statistical areas are two categories of core based statistical areas. If an institution is not defined as a CBSA, the value of the field will be zero. For more information see: http://www.census.gov/population/www/estimates/metroarea.html .  ',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RELATION',
            'field': 'CBSA'
        }]
    },
    'CERT': {
        'title': 'FDIC Certificate #',
        'description': 'A unique NUMBER assigned by the FDIC used to identify institutions and for the issuance of insurance certificates.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'ORG_CERT_NUM'
        }]
    },
    'CERTCONS': {
        'title': 'Directly owned by another bank (CERT)',
        'description': 'FDIC certificate number of the parent bank or savings institution with which the reported institution’s financial data has been consolidated. Beginning in March 1997, both the Thrift Financial Reports and Call Reports are completed on a fully consolidated basis.  Previously, the consolidation of subsidiary depository institutions was prohibited.  Now, parent institutions are required to file consolidated reports, while their subsidiary financial institutions are still required to file separate reports.  Click on the certificate number to identify the parent bank or thrift.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'CERTCONS'
        }]
    },
    'CFPBEFFDTE': {
        'title': 'CFPB Effective Date',
        'description': 'Date the institution began secondary supervision by CFPB',
        'type': 'string',
        'format': 'date-time',
        'x-source-mapping': [{
            'formula': {
                'type': 'date',
                'parameters': {
                    'inputFormat': "yyyy-MM-dd'T'HH:mm:ss",
                    'outputFormat': 'dd-MMM-yyyy',
                    'inputField': 'AGY_CFPB_REGL_EFF_DTE',
                    'outputField': 'CFPBEFFDTE'
                }
            }
        }]
    },
    'CFPBENDDTE': {
        'title': 'CFPB End Date',
        'description': 'Date the institution ended supervision by CFPB',
        'type': 'string',
        'format': 'date-time',
        'x-source-mapping': [{
            'formula': {
                'type': 'date',
                'parameters': {
                    'inputFormat': "yyyy-MM-dd'T'HH:mm:ss",
                    'outputFormat': 'dd-MMM-yyyy',
                    'inputField': 'AGY_CFPB_REGL_END_DTE',
                    'outputField': 'CFPBENDDTE'
                }
            }
        }]
    },
    'CFPBFLAG': {
        'title': 'CFPB Flag',
        'description': "Indicates secondary supervision by CFPB ('0' - not supervised by CFPB, '1'- secondarily supervised by CFPB)",
        'type': 'string',
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': 'if(ctx.REGAGENT2?.toLowerCase() == "cfpb" && ctx.CFPBENDDTE?.toString() == "31-Dec-99") { \n  ctx.CFPBFLAG = 1; \n} else { \n  ctx.CFPBFLAG = 0 \n}\n'
                }
            }
        }],
        'options': [0, 1]
    },
    'CHANGEC1': {
        'title': 'Change Code',
        'description': 'FDIC code used to signify a structural event relating to an institution.  Structure codes are as follows:',
        'type': 'string',
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': 'if(ctx.EVENTS !== null ) { \n\n  List changeCodeList = new ArrayList();\n  String[] codeList = new String[] {"1", "110", "150", "211", "212", "213", "215", "216", "217", "221", "222", "223", "225", "230", "231", "235", "240", "350", "360", "410", "411", "430", "440", "470", "510", "520", "610", "810", "811", "812", "820", "830"};\n  List includeCodeList = Arrays.asList(codeList);\n\n  \n  for (int i = 0; i < ctx.EVENTS.length; ++i) {\n    if (ctx.EVENTS[i].EFFDATE == ctx.ORG_EFF_NUM_DTE && \n        ctx.EVENTS[i].ENDEFYMD == ctx.ORG_END_NUM_DTE &&\n        includeCodeList.contains(Integer.toString(ctx.EVENTS[i].ACT_EVT_NUM))) {\n\n      ctx.EVENTS[i].CHANGE_ORDER = 3;\n      if (ctx.EVENTS[i].ACT_EVT_NUM !== null) {\n        if(ctx.EVENTS[i]?.ACT_EVT_NUM > 200 && ctx.EVENTS[i]?.ACT_EVT_NUM <= 299) {\n          ctx.EVENTS[i].CHANGE_ORDER = 1;\n        } else if(ctx.EVENTS[i]?.ACT_EVT_NUM > 800 && ctx.EVENTS[i]?.ACT_EVT_NUM <= 899) {\n          ctx.EVENTS[i].CHANGE_ORDER = 2;\n        }\n      }\n\n      changeCodeList.add(ctx.EVENTS[i])\n    }\n  }\n\n  changeCodeList.sort((x,y) -> {\n    int change = x.CHANGE_ORDER.compareTo(y.CHANGE_ORDER);\n    if (change === 0) { change = y.PROCDATE.compareTo(x.PROCDATE); }\n    if (change === 0) { change = y.ACT_EVT_NUM.compareTo(x.ACT_EVT_NUM); }\n    return change;\n  });\n  \n  ctx.PARSED_EVENTS = changeCodeList;\n\n  for (int a = 0; a < ctx.PARSED_EVENTS.length; ++a) {\n    String changeCodeProperty = "CHANGEC" + (a+1);\n    ctx[changeCodeProperty] = ctx.PARSED_EVENTS[a].ACT_EVT_NUM\n  }\n}\n'
                }
            }
        }]
    },
    'CHANGEC2': {
        'title': 'Change Code',
        'description': 'FDIC code used to signify a structural event relating to an institution (see CHANGECODE for the key to the codes).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_BR_SDC',
            'field': 'ACT_EVT2_NUM'
        }]
    },
    'CHANGEC3': {
        'title': 'Change Code',
        'description': 'FDIC code used to signify a structural event relating to an institution (see CHANGECODE for the key to the codes).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_BR_SDC',
            'field': 'ACT_EVT3_NUM'
        }]
    },
    'CHANGEC4': {
        'title': 'Change Code',
        'description': 'FDIC code used to signify a structural event relating to an institution (see CHANGECODE for the key to the codes).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_BR_SDC',
            'field': 'ACT_EVT4_NUM'
        }]
    },
    'CHANGEC5': {
        'title': 'Change Code',
        'description': 'FDIC code used to signify a structural event relating to an institution (see CHANGECODE for the key to the codes).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_BR_SDC',
            'field': 'ACT_EVT5_NUM'
        }]
    },
    'CHANGEC6': {
        'title': 'Change Code',
        'description': 'FDIC code used to signify a structural event relating to an institution (see CHANGECODE for the key to the codes).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_BR_SDC',
            'field': 'ACT_EVT5_NUM'
        }]
    },
    'CHANGEC7': {
        'title': 'Change Code',
        'description': 'FDIC code used to signify a structural event relating to an institution (see CHANGECODE for the key to the codes).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_BR_SDC',
            'field': 'ACT_EVT5_NUM'
        }]
    },
    'CHANGEC8': {
        'title': 'Change Code',
        'description': 'FDIC code used to signify a structural event relating to an institution (see CHANGECODE for the key to the codes).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_BR_SDC',
            'field': 'ACT_EVT5_NUM'
        }]
    },
    'CHANGEC9': {
        'title': 'Change Code',
        'description': 'FDIC code used to signify a structural event relating to an institution (see CHANGECODE for the key to the codes).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_BR_SDC',
            'field': 'ACT_EVT5_NUM'
        }]
    },
    'CHANGEC10': {
        'title': 'Change Code',
        'description': 'FDIC code used to signify a structural event relating to an institution (see CHANGECODE for the key to the codes).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_BR_SDC',
            'field': 'ACT_EVT5_NUM'
        }]
    },
    'CHANGEC11': {
        'title': 'Change Code',
        'description': 'FDIC code used to signify a structural event relating to an institution (see CHANGECODE for the key to the codes).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_BR_SDC',
            'field': 'ACT_EVT5_NUM'
        }]
    },
    'CHANGEC12': {
        'title': 'Change Code',
        'description': 'FDIC code used to signify a structural event relating to an institution (see CHANGECODE for the key to the codes).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_BR_SDC',
            'field': 'ACT_EVT5_NUM'
        }]
    },
    'CHANGEC13': {
        'title': 'Change Code',
        'description': 'FDIC code used to signify a structural event relating to an institution (see CHANGECODE for the key to the codes).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_BR_SDC',
            'field': 'ACT_EVT5_NUM'
        }]
    },
    'CHANGEC14': {
        'title': 'Change Code',
        'description': 'FDIC code used to signify a structural event relating to an institution (see CHANGECODE for the key to the codes).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_BR_SDC',
            'field': 'ACT_EVT5_NUM'
        }]
    },
    'CHANGEC15': {
        'title': 'Change Code',
        'description': 'FDIC code used to signify a structural event relating to an institution (see CHANGECODE for the key to the codes).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_BR_SDC',
            'field': 'ACT_EVT5_NUM'
        }]
    },
    'CHARTER': {
        'title': 'OCC Charter Number',
        'description': 'A unique number assigned by the Office of the Comptroller of the Currency (OCC) used to identify institutions that it has chartered and regulates (i.e. national  banks).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'INST_OCC_CHTR_NUM'
        }]
    },
    'CHRTAGNT': {
        'title': 'Chartering Agency',
        'description': 'All Chartering Agencies - State and Federal  Comptroller of the Currency - Chartering authority for nationally chartered commercial banks and for federally chartered savings associations (The Office of Thrift Supervision (OTS) before 7/21/11)  State (includes U.S. Territories) - Chartering authority for institutions that are not chartered by the OCC or OTS',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'AGY_CHTR_CDE'
        }]
    },
    'CITY': {
        'title': 'City',
        'description': "City in which an institution's headquarters or one of its branches is physically located. Either the entire name or part of the name of a specific city may be entered to produce an Institution List.",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_PHY_CTY_NME'
        }]
    },
    'CITYHCR': {
        'title': 'City of High Holder',
        'description': "City in which the headquarters of the institution's regulatory high holder are physically located.",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'CITYHCR'
        }]
    },
    'CLCODE': {
        'title': 'Numeric code',
        'description': 'Numeric code which identifies the major and minor categories of an institution.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'INST_CAT_NUM'
        }]
    },
    'CMSA_NO': {
        'title': 'Consolidated Metropolitan Statistical Division Number',
        'description': 'The numeric code given by the US Census Bureau office of Management and Budget that represents the CMSA prior to the year 2000 standards. 1=yes',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_CMSA_NUM'
        }]
    },
    'CMSA': {
        'title': 'Consolidated Metropolitan Statistical Area',
        'description': 'The Federal Information Processing Standards (FIPS) Consolidated Metropolitan Statistical Area (CMSA) code is a number representing the institution location. CMSA consists of two or more contiguous Metropolitan Statistical Areas (MSA) with a combined population of over 1 Million.  Note: If an institution is not located in a CMSA, the value of the field will be zeroes.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_CMSA_NME'
        }]
    },
    'CONSERVE': {
        'title': 'Conservatorship',
        'description': 'A flag (1=yes;0=no) that indicates if an institution is being operated in government conservatorship.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'INST_FIN_CNS_FLG'
        }]
    },
    'COUNTY': {
        'title': 'County',
        'description': 'County where the institution is physically located (abbreviated if the county name exceeds 16 characters).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_PHY_CNTY_NME'
        }]
    },
    'CSA': {
        'title': 'Name of the Combined Statistical Area',
        'description': 'The name associated with the numeric code that the U.S. Census Bureau Office of Management and Budget assigns for the combined statistical area (CSA) per the 2000 standards. If an institution is not defined as a CSA, the value of the field will be blank. For more information see: http://www.census.gov/population/www/estimates/metroarea.html . ',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RELATION',
            'field': 'CSANAME'
        }]
    },
    'CSA_NO': {
        'title': 'Numeric Code for the Combined Statistical Area',
        'description': 'The numeric code that the U.S. Census Bureau Office of Management and Budget assigns for the combined statistical area (CSA) per the 2000 standards. If an institution is not defined as a CSA, the value of the field will be zero.  For more information see: http://www.census.gov/population/www/estimates/metroarea.html .',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RELATION',
            'field': 'CSA'
        }]
    },
    'CSA_FLG': {
        'title': 'CSA Area Flag',
        'description': 'A flag used to indicate whether an institution is in a Combined Statistical Area. 1=yes and 0=no.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RELATION',
            'field': 'CSA_FLAG'
        }],
        'options': [0, 1]
    },
    'DATEUPDT': {
        'title': 'Last update',
        'description': 'The date of the last data update.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'see PROCDATE script',
            'field': 'see PROCDATE script'
        }]
    },
    'DENOVO': {
        'title': 'Denovo Institution',
        'description': 'A flag used to indicate whether an institution is a new institution (not a recharter). This flag is set quarterly. For instance, if REPDTE is 3/31/98 and DENOVO equals 1, the institution was a denovo during the first quarter of 1998.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'DENOVO'
        }]
    },
    'DEP': {
        'title': 'Total deposits',
        'description': 'The sum of all deposits including demand deposits, money market deposits, other savings deposits, time deposits and deposits in foreign offices.',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'DEP'
        }]
    },
    'DEPDOM': {
        'title': 'Deposits held in domestic offices',
        'description': 'The sum of all domestic office deposits, including demand deposits, money market deposits, other savings deposits and time deposits.',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'DEPDOM'
        }]
    },
    'DOCKET': {
        'title': 'OTS Docket Number',
        'description': "An identification number assigned to institutions chartered by the office of thrift supervision or members of the federal housing finance board (FHFB) and formerly by the federal home loan bank board.  The value is '00000' for institutions not members of the FHFB.",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'ORG_DKT_NUM'
        }]
    },
    'EFFDATE': {
        'title': 'Last Structure Change Effective Date',
        'description': 'Effective Start Date of the data contained in this row.',
        'type': 'string',
        'format': 'date-time',
        'x-source-mapping': [{
            'formula': {
                'type': 'date',
                'parameters': {
                    'inputFormat': 'yyyyMMdd',
                    'outputFormat': 'MM/dd/yyyy',
                    'inputField': 'ORG_EFF_NUM_DTE',
                    'outputField': 'EFFDATE'
                }
            }
        }]
    },
    'ENDEFYMD': {
        'title': 'End date',
        'description': 'The date that ends or closes out the last structural event relating to an institution. For closed institutions, this date represents the day that the institution became inactive.',
        'type': 'string',
        'format': 'date-time',
        'x-source-mapping': [{
            'formula': {
                'type': 'date',
                'parameters': {
                    'inputFormat': 'yyyyMMdd',
                    'outputFormat': 'MM/dd/yyyy',
                    'inputField': 'ORG_END_NUM_DTE',
                    'outputField': 'ENDEFYMD'
                }
            }
        }]
    },
    'EQ': {
        'title': 'Equity capital',
        'description': 'Total equity capital (includes preferred and common stock, surplus and undivided profits).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'EQ'
        }]
    },
    'ESTYMD': {
        'title': 'Established Date',
        'description': 'The date on which the institution began operations.',
        'type': 'string',
        'format': 'date-time',
        'x-source-mapping': [{
            'formula': {
                'type': 'date',
                'parameters': {
                    'inputFormat': "yyyy-MM-dd'T'HH:mm:ss",
                    'outputFormat': 'MM/dd/yyyy',
                    'inputField': 'INST_FIN_ESTB_DTE',
                    'outputField': 'ESTYMD'
                }
            }
        }]
    },
    'FDICDBS': {
        'title': 'FDIC Geographic Region',
        'description': 'The FDIC Office assigned to the geographic area.  The eight FDIC Regions and their respective states are:    Boston - Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont  New York - Delaware, District of Columbia, Maryland, New Jersey, New York, Pennsylvania, Puerto Rico, U.S. Virgin Islands  Atlanta - Alabama, Florida, Georgia, North Carolina, South Carolina, Virginia, West Virginia  Memphis - Arkansas, Kentucky, Louisiana, Mississippi, Tennessee  Chicago - Illinois, Indiana, Michigan, Ohio, Wisconsin   Kansas City - Iowa, Kansas, Minnesota, Missouri, Nebraska, North Dakota, South Dakota  Dallas - Colorado, New Mexico, Oklahoma, Texas  San Francisco - Alaska, American Samoa, Arizona, California, Guam, Hawaii, Idaho, Montana, Nevada, Oregon, States of Micronesia, Utah, Washington, Wyoming',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_REGN_OFC_CDE'
        }]
    },
    'FDICREGN': {
        'title': 'FDIC Supervisory Region',
        'description': 'The supervisory FDIC office assigned to the institution.  The eight FDIC Supervisory Regions and their respective states are:    Boston - Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont  New York - Delaware, District of Columbia, Maryland, New Jersey, New York, Pennsylvania, Puerto Rico, U.S. Virgin Islands  Atlanta - Alabama, Florida, Georgia, North Carolina, South Carolina, Virginia, West Virginia  Memphis - Arkansas, Kentucky, Louisiana, Mississippi, Tennessee  Chicago - Illinois, Indiana, Michigan, Ohio, Wisconsin   Kansas City - Iowa, Kansas, Minnesota, Missouri, Nebraska, North Dakota, South Dakota  Dallas - Colorado, New Mexico, Oklahoma, Texas  San Francisco - Alaska, American Samoa, Arizona, California, Guam, Hawaii, Idaho, Montana, Nevada, Oregon, States of Micronesia, Utah, Washington, Wyoming',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_REGN_OFC_DESC'
        }]
    },
    'FDICSUPV': {
        'title': 'Federal Reserve District',
        'description': 'The supervisory FDIC office assigned to the institution. There are twelve Federal Reserve Districts, with two Districts serving one state in some instances. The list of Federal Reserve Districts and their respective states are as follows: Boston - Connecticut, Maine, Massachuestts, New Hampshire, Rhode Island, Vermont New York - Connecticut, New Jersey, New York, Puerto Rico U.S. Virgin Islands  Phildelphia - Delaware, New Jersey, Pennsylvania Cleveland - Kentucky, Ohio, Pennsylvania, West Virginia Richmond - Maryland, North Carolina, South Carolina, Virginia, West Virginia Atlanta - Alabama, Florida, Georgia, Louisiana, Mississippi, Tennessee Chicago - Illinois, Indiana, Iowa, Michigan, Wisconsin St. Louis - Arkansas, Illinois, Indiana, Kentucky, Mississippi, Missouri, Tennessee Minneapolis - Michigan, Minnesota, Montana, North Dakota, South Dakota, Wisconsin Kansas City - Colorado, Kansas, Missouri, Nebraska, New Mexico, Oklahoma, Wyoming Dallas - Louisiana, New Mexico, Texas San Francisco> - Alaska, American Samoa, Arizona, California, Guam, Hawaii, Idaho, Nevada, Oregon, States of Micronesia, Utah, Washington',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'ORG_SPVR_REGN_DESC'
        }, {
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': "if (ctx.SUPRV_FD == '16') {\n  ctx.FDICSUPV = 'WASHINGTON';\n}\n"
                }
            }
        }]
    },
    'FED': {
        'title': 'Federal Reserve ID Number',
        'description': 'A number used to identify the Federal Reserve district in which the institution is located. 01 – Boston, 02 - New York,03 – Philadelphia, 04 – Cleveland,05 – Richmond,06 – Atlanta,07 – Chicago,08 - St. Louis,09 – Minneapolis,10 - Kansas city,11 – Dallas,12 - San Francisco',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_FRB_DIST_CDE'
        }]
    },
    'FED_RSSD': {
        'title': 'Federal Reserve ID Number',
        'description': "A unique number assigned by the Federal Reserve board as the entity's unique identifier",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'ID_RSSD'
        }]
    },
    'FEDCHRTR': {
        'title': 'Federal charter flag',
        'description': 'A flag used to indicate whether the institution is chartered by an agent of the federal government.',
        'type': 'string',
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': "if (ctx.CHRTAGNT?.toLowerCase() == 'occ' || ctx.CHRTAGNT?.toLowerCase() == 'ots') {\n  ctx.FEDCHRTR = 1;\n} else {\n  ctx.FEDCHRTR = 0;\n}      \n"
                }
            }
        }],
        'options': [0, 1]
    },
    'FLDOFF': {
        'title': 'FDIC Field Office',
        'description': 'The FDIC Field Office where an institution is physically located.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_DOS_FLD_NME'
        }]
    },
    'FORM31': {
        'title': 'FFIEC Call Report 31 Filer',
        'description': 'A flag (1=yes,0=no) that indicates whether and institution filed an FFIEC 031 Call Report. Commercial banks with domestic and foreign offices are required to file such a report.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'FORM31'
        }],
        'options': [0, 1]
    },
    'HCTMULT': {
        'title': 'Bank Holding Company Type',
        'description': 'A flag used to indicate whether an institution is a member of a multibank holding company 1=yes, 0=no',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'HCTMULT'
        }]
    },
    'IBA': {
        'title': 'Insured offices of foreign banks',
        'description': 'Includes Bank Insurance Fund insured branches in the U.S. established by banks chartered and headquartered in foreign countries.  These institutions are regulated by one of the three Federal commercial bank regulators and submit financial data to the Federal Reserve.',
        'type': 'string',
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': 'if (ctx.INST_IBA_FLG?.toLowerCase() == "y" || ctx.INST_IBA_FLG?.toLowerCase() == "l") { \n  ctx.IBA = 1;\n} else { \n  ctx.IBA = 0;\n}\n'
                }
            }
        }]
    },
    'INACTIVE': {
        'title': 'Inactive',
        'description': 'Institutions that are currently closed but were once insured by the FDIC.',
        'type': 'string',
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': 'if (ctx.INST_FIN_ACTV_FLG?.toLowerCase() == "y") { \n  ctx.INACTIVE = 0;\n} else { \n  ctx.INACTIVE = 1;\n}\n'
                }
            }
        }],
        'options': [0, 1]
    },
    'INSAGNT1': {
        'title': 'Insurance Fund Membership',
        'description': 'Deposit Insurance Fund (DIF), Bank Insurance Fund (BIF), Savings Association Insurance Fund (SAIF) ',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'AGY_1_INS_ABBV_NME'
        }]
    },
    'INSAGNT2': {
        'title': 'Secondary Insurance Fund',
        'description': 'As a result of the establishment of a single Deposit Insurance Fund (DIF) effective April 1, 2006, the Secondary Insurance fund is no longer applicable. previously both bif and saif bank insurance fund - institutions that are members of the bank insurance fund savings association insurance fund - Institutions that are members of the Savings Association Insurance Fund',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'AGY_2_INS_ABBV_NME'
        }]
    },
    'INSBIF': {
        'title': 'Bank Insurance Fund',
        'description': 'Institutions who are members of the Bank Insurance Fund. As of April 1, 2006 BIF was merged together with the Savings Institution Insurance Fund (SAIF) to create a single Deposit Insurance Fund (DIF).  All FDIC insured BIF member institutions, that are still active or open, are now insured members of DIF.',
        'type': 'string',
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': 'if (ctx.INSAGNT1?.toLowerCase() == "bif") { \n  ctx.INSBIF = 1;\n} else { \n  ctx.INSBIF = 0;\n}\n'
                }
            }
        }],
        'options': [0, 1]
    },
    'INSCOML': {
        'title': 'Insured commercial banks',
        'description': 'Includes commercial banks insured by the FDIC.  These institutions are regulated by one of the three Federal commercial bank regulators (FDIC, Federal Reserve Board, or Office of the Comptroller of the Currency).  They submit financial reports to the Federal Reserve (state member banks) or the FDIC (state non-member banks and national banks).',
        'type': 'string',
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': "if (\n  (ctx.INSAGNT1?.toLowerCase() == 'bif' || ctx.INSAGNT1?.toLowerCase() == 'saif' || ctx.INSAGNT1?.toLowerCase() == 'dif' ) && \n  (ctx.BKCLASS?.toLowerCase() == 'n' || ctx.BKCLASS?.toLowerCase() == 'nc' || ctx.BKCLASS?.toLowerCase() == 'nm')\n  )\n{\n  ctx.INSCOML = 1;\n} else if (\n  (ctx.INSAGNT1?.toLowerCase() == 'bif' || ctx.INSAGNT1?.toLowerCase() == 'saif' || ctx.INSAGNT1?.toLowerCase() == 'dif' ) && \n  (ctx.BKCLASS?.toLowerCase() == 'sm') && (ctx.ORG_TYP_NUM != 110) && (ctx.ORG_TYP_NUM != 115) && (ctx.ORG_TYP_NUM != 130) && (ctx.ORG_TYP_NUM != 135)\n) {\n  ctx.INSCOML = 1;\n}\nelse {\n  ctx.INSCOML = 0;\n}\n"
                }
            }
        }],
        'options': [0, 1]
    },
    'INSDATE': {
        'title': 'Date of Deposit Insurance',
        'description': 'The date that an institution obtained federal deposit insurance.',
        'type': 'string',
        'format': 'date-time',
        'x-source-mapping': [{
            'formula': {
                'type': 'date',
                'parameters': {
                    'inputFormat': "yyyy-MM-dd'T'HH:mm:ss",
                    'outputFormat': 'MM/dd/yyyy',
                    'inputField': 'POL_1_INS_BEG_DTE',
                    'outputField': 'INSDATE'
                }
            }
        }]
    },
    'INSDIF': {
        'title': 'Deposit Insurance Fund member',
        'description': 'A flag used to indicate whether an institution is insured under the Deposit Insurance Fund (DIF).  As of April 1, 2006 the Bank Insurance Fund (BIF) was merged together with the Savings Institution Insurance Fund (SAIF) to create a single Deposit Insurance Fund (DIF).  All FDIC insured BIF and SAIF member institutions that are still active or open are now insured members of DIF.    0 = No, not DIF insured and 1 = Yes, DIF insured.  Note that institutions that became inactive prior to April 1006 will also have zero value.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'INSDIF'
        }],
        'options': [0, 1]
    },
    'INSFDIC': {
        'title': 'FDIC Insured',
        'description': 'Includes institutions insured by the FDIC.',
        'type': 'number',
        'x-source-mapping': [{
            'formula': {
                'type': 'simpleSet',
                'parameters': {
                    'setField': 'INSFDIC',
                    'setValue': 1
                }
            }
        }],
        'options': [0, 1]
    },
    'INSSAIF': {
        'title': 'SAIF Insured',
        'description': 'Institutions who are members of the Savings Association Insurance Fund. As of April 1, 2006 SAIF was merged together with the Bank Insurance Fund (BIF) to create a single Deposit Insurance Fund (DIF).  All FDIC insured SAIF member institutions, that are still active or open, are now insured members of DIF.',
        'type': 'string',
        'x-source-mapping': [{
            'formula': {
                'type': 'simpleSet',
                'parameters': {
                    'setField': 'INSSAIF',
                    'setValue': 0
                }
            }
        }],
        'options': [0, 1]
    },
    'INSSAVE': {
        'title': 'Insured Savings Institution',
        'description': 'Includes savings institutions insured by the FDIC that operate under state or federal banking codes applicable to thrift institutions.  These institutions are regulated by and submit financial reports to one of two Federal regulators (FDIC or Office of Thrift Supervision).',
        'type': 'string',
        'x-source-mapping': [{
            'formula': {
                'type': 'simpleSet',
                'parameters': {
                    'setField': 'INSSAVE',
                    'setValue': 0
                }
            }
        }],
        'options': [0, 1]
    },
    'INSTAG': {
        'title': 'Agricultural lending institution indicator',
        'description': 'An indicator specifying whether an institution is primarily an agricultural lending institution.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'INSTAG'
        }],
        'options': [0, 1]
    },
    'INSTCRCD': {
        'title': 'Credit Card Institutions',
        'description': 'Institutions with total loans greater than 50% of total assets and credit card loans greater than 50% of total loans, including loans that have been securitized and sold.',
        'type': 'string',
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': 'ctx.INSTCRCD = 0;'
                }
            }
        }]
    },
    'LAW_SASSER_FLG': {
        'title': 'Law Sasser Flag',
        'description': 'A flag, yes=1 and no=0 associated with OTS supervised savings associations that converted their charter to that of a commercial or savings bank.  Converted associations remain members of the SAIF, but they become subject to supervision by one of the three federal banking agencies. Not Applicable as of March 31, 2006.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LAW_SASSER_FLG'
        }],
        'options': [0, 1]
    },
    'MSA': {
        'title': 'Metropolitan Statistical Area (MSA)',
        'description': 'The Metropolitan Statistical Areas based on Census Bureau data, as defined by the US Office of Management (OMB) prior to the year 2000.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_MSA_NME'
        }]
    },
    'MSA_NO': {
        'title': 'Metropolitan Statistical Area Number',
        'description': 'The Metropolitan Statistical Area Number (MSA_NO) in which the institution is physically located.  The Office of Managment and Budget defines MSAs in terms of entire counties surrounding central cities, except in the six New England states where they are defined in terms of cities and towns within counties. Before 200 standards',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_MSA_NUM'
        }]
    },
    'MUTUAL': {
        'title': 'Ownership Type',
        'description': 'Banking institutions fall into one of two ownership types, stock or non-stock. An institution which sells stock to raise capital is called a stock institution. It is owned by the shareholders who benefit from profits earned by the institution. A non-stock institution, or mutual institution, is owned and controlled solely by its depositors. A mutual does not issue capital stock.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'MUTUAL'
        }]
    },
    'NAME': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'title': 'Institution name',
        'description': 'The legal name of the institution.',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'INST_FIN_LGL_NME'
        }]
    },
    'NAMEHCR': {
        'title': 'Bank Holding Company (Regulatory Top Holder)',
        'description': "Regulatory top holder is assigned by the Federal Reserve Board based on ownership and control percentages. Note: Information on bank holding companies is only as of quarter-end. Regulatory top holder is any company that directly or indirectly owns, controls or has power to vote 25 percent or more of a bank's or direct holding company's shares or  controls in any manner the election of a majority of the directors or trustees of a bank or direct holding company or  exercises a controlling influence over the management or policies of a bank or direct holding company.   Information on Thrift Holding Companies that own Savings Associations but do not own banks is not currently available in the ID System.  Source:  Federal Reserve Board National Information Center data base.",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'NAMEHCR'
        }]
    },
    'NETINC': {
        'title': 'Net income',
        'description': 'Net interest income plus total noninterest income plus realized gains (losses) on securities and extraordinary items, less total noninterest expense, loan loss provisions and income taxes.',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'NETINC'
        }]
    },
    'NETINCQ': {
        'title': 'Net income - quarterly',
        'description': 'Quarterly net interest income plus total noninterest income plus realized gains (losses) on securities and extraordinary items, less total noninterest expense, loan loss provisions and income taxes.',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'NETINCQ'
        }]
    },
    'NEWCERT': {
        'title': 'New certificate number',
        'description': 'A new certificate number of an already existing FDIC-insured institution resulting from either a merger or an acquisition.',
        'type': 'string',
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': 'ctx.NEWCERT = 0;\nif(ctx.PARSED_EVENTS !== null && ctx.PARSED_EVENTS.length > 0) {\n  for (int i = 0; i < ctx.PARSED_EVENTS.length; ++i) {\n    ctx.NEWCERT = ctx.PARSED_EVENTS[i].ORG_ACQ_CERT_NUM;\n    if (ctx.PARSED_EVENTS[i].ORG_ACQ_CERT_NUM < 0 ) {\n      ctx.NEWCERT = 0;\n    } \n  }\n\n  if (ctx.CHANGEC1 == 150)  {\n    ctx.NEWCERT = 0;\n  } \n  if ((ctx.CHANGEC1 < 200) && (ctx.CHANGEC1 > 300)) {\n    if (((ctx.CHANGEC1 < 831) && (ctx.CHANGEC1 > 700)) ||\n    ((ctx.CHANGEC2 < 831) && (ctx.CHANGEC1 > 700)) ||\n    ((ctx.CHANGEC3 < 831) && (ctx.CHANGEC1 > 700)) ||\n    ((ctx.CHANGEC4 < 831) && (ctx.CHANGEC1 > 700)) ||\n    ((ctx.CHANGEC5 < 831) && (ctx.CHANGEC1 > 700))) {\n      ctx.NEWCERT = 0;\n    }\n  }\n}\n'
                }
            }
        }]
    },
    'OAKAR': {
        'title': 'Oakar Institutions',
        'description': "A member of one insurance fund that acquired deposits insured by the other fund, where that portion of the buyer's deposits remained insured by, and assessable by, the other fund.",
        'type': 'string',
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': 'if (ctx.INSAGNT1?.toLowerCase() == "bif" && ctx.INSAGNT2?.toLowerCase() == "saif") {\n  ctx.OAKAR = 1; \n} else { \n  ctx.OAKAR = 0; \n}\n'
                }
            }
        }],
        'options': [0, 1]
    },
    'OCCDIST': {
        'title': 'Office of the Comptroller',
        'description': 'The Office of the Comptroller of the Currency (OCC) District in which the institution is physically located. The six OCC Districts and their respective states are: Northeast - Connecticut, Delaware, District of Columbia, Maine, Maryland, Massachusetts, New Hampshire, New Jersey, New York, Pennsylvania, Puerto Rico, Rhode Island, Vermont, U.S. Virgin Islands  Southeast - Alabama, Florida, Georgia, Mississippi, North Carolina, South Carolina, Tennessee, Virginia, West Virginia  Central - Illinois, Indiana, Kentucky, Michigan, Ohio, Wisconsin  Midwest - Iowa, Kansas, Minnesota, Missouri, Nebraska, North Dakota, South Dakota  Southwest - Arkansas, Louisiana, New Mexico, Oklahoma, Texas  West - Alaska, American Samoa, Arizona, California, Colorado, Guam, Hawaii, Idaho, Montana, Nevada, Oregon, States of Micronesia, Utah, Washington, Wyoming ',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_OCC_DIST_CDE'
        }]
    },
    'OFFDOM': {
        'title': 'Number of Domestic Offices',
        'description': 'The number of domestic offices (including headquarters) operated by active institutions in the 50 states of the U.S.A.',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'OFFDOM'
        }]
    },
    'OFFFOR': {
        'title': 'Number of Foreign Offices',
        'description': 'The number of foreign offices (outside the U.S.) operated by the institution.',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'OFFFOR'
        }]
    },
    'OFFICES': {
        'title': 'Office',
        'description': 'A branch/office is any location, or facility, of a financial institution, including its main office, where deposit accounts are opened, deposits are accepted, checks paid, and loans granted. Some branches include, but are not limited to, brick and mortar locations, detached or attached drive-in facilities, seasonal offices, offices on military bases or government installations, paying/receiving stations or units, nondeposit offices, Internet and PhoneBanking locations where a customer can open accounts, make deposits and borrow money. A branch does not include Automated Teller Machines (ATM), Consumer Credit Offices, Contractual Offices, Customer Bank Communication Terminals (CBCT), Electronic Fund Transfer Units (EFTU), and Loan Production Offices Summary of Deposits information is required for each insured office located in any State, the District of Columbia, the Commonwealth of Puerto Rico or any U.S. territory or possession such as Guam or the U.S. Virgin Islands, without regard to the location of the main office.',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'test'
        }]
    },
    'OFFOA': {
        'title': 'Number of US Offices',
        'description': 'The number of offices operated by an FDIC-insured institution in all commonwealths and terrirtories of the US, along with those in freely associated states under the Compact of Free Association',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'OFFOA'
        }]
    },
    'OTSDIST': {
        'title': 'OTS District',
        'description': 'Office of Thrift Supervision (OTS) District - Sunset (ended)  7/21/11',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_OTS_DIST_CDE'
        }]
    },
    'OTSREGNM': {
        'title': 'Office of Thrift Supervision Region',
        'description': 'Prior to 7/21/11, the Office of Thrift Supervision (OTS) Region in which the institution is physically located. The five OTS Regions and their respective states are: Northeast - Connecticut, Delaware, Maine, Massachusetts, New Hampshire, New Jersey, New York, Pennsylvania, Rhode Island, Vermont, West Virginia Southeast - Alabama, District of Columbia, Florida, Georgia, Maryland, North Carolina, Puerto Rico, South Carolina, U.S. Virgin Islands, Virginia Central - Illinois, Indiana, Kentucky, Michigan, Ohio, Tennessee, Wisconsin Midwest - Arkansas, Colorado, Iowa, Kansas, Louisiana, Minnesota, Mississippi, Missouri, Nebraska, New Mexico, North Dakota, Oklahoma, South Dakota, Texas West - Alaska, American Samoa, Arizona, California, Guam, Hawaii, Idaho, Montana, Nevada, States of Micronesia, Oregon, Utah, Washington, Wyoming',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_OTS_DIST_DESC'
        }]
    },
    'PARCERT': {
        'title': 'Directly owned by another bank (CERT)',
        'description': 'The PARCERT number identifies the subsidiary institutions parent certificate number. Beginning in March 1997, both the Thrift Financial Reports and Call Reports are completed on a fully consolidated basis.  Previously, the consolidation of subsidiary depository institutions was prohibited.  Now, parent institutions are required to file consolidated reports, while their subsidiary financial institutions are still required to file separate reports.  ',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'PARCERT'
        }]
    },
    'PROCDATE': {
        'title': 'Last Structure Change Process Date',
        'description': "A date field indicating the date that a change to this record was processed. Standard format = 'CCYYMMDD' (Length = 8) which has been converted to Month, Day, Year format for display purposes.",
        'type': 'string',
        'format': 'date-time',
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': 'if(ctx.EVENTS !== null ) { \n  Date procDate = null;\n  for (int i = 0; i < ctx.EVENTS.length; ++i) {\n    if (ctx.EVENTS[i]?.EFFDATE == ctx.ORG_EFF_NUM_DTE && ctx.EVENTS[i]?.ENDEFYMD == ctx.ORG_END_NUM_DTE) {\n        SimpleDateFormat dateFormatIn = new SimpleDateFormat("yyyy-MM-dd\'T\'HH:mm:ss");\n        SimpleDateFormat dateFormatOut = new SimpleDateFormat("MM/dd/yyyy");\n        if(ctx.EVENTS[i].PROCDATE !== null) {\n          Date formattedProcDate = dateFormatIn.parse(ctx.EVENTS[i].PROCDATE);\n\n          if (procDate == null || formattedProcDate.after(procDate)) {\n            String currentProcDate = dateFormatOut.format(formattedProcDate);\n            ctx.PROCDATE = currentProcDate;\n            ctx.DATEUPDT = currentProcDate;\n          } \n        }\n\n    }\n  }\n}\n'
                }
            }
        }]
    },
    'QBPRCOML': {
        'title': 'Quarterly Banking Profile Commercial Bank Region',
        'description': 'The Quarterly Banking Profile (QBP) Commercial Bank Region in which the institution is physically located. Select from a drop down box. regional breakdown. group data by qbp region is only available for insured commercial banks and insured savings institutions and NOT All Insured Institutions, Insured Commercial Banks by asset size and Insured Savings Institutions by asset size. ',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'QBPRCOML',
            'field': 'QBPRCOML'
        }]
    },
    'REGAGNT': {
        'title': 'Regulator',
        'description': 'There are four Federal regulators of banks and savings and loan institutions (There are now three federal regulators of banks and savings and loan institutions. Berfore July 21, 2011, there were four federal regulators): federal deposit insurance corporation (fdic) - primary federal regulator responsible for state-chartered banks not members of the Federal Reserve System and state chartered savings banks. Federal Reserve Board (FRB) - Primary Federal regulator responsible for state-chartered commercial bank members of the Federal Reserve System. Office of the Comptroller of the Currency (OCC) - Primary Federal regulator responsible for nationally chartered commercial banks and federally chartered savings and loan associations. Before 7/21/11, Office of Thrift Supervision (OTS) - Primary Federal regulator responsible for federally chartered savings and loan associations, federal savings banks and state-chartered savings and loan associations. FDIC insured depository institutions are members of the Deposit Insurance Fund (DIF). ',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'AGY1_GOV_SPVRABNME'
        }]
    },
    'REGAGENT2': {
        'title': 'Regulator 2',
        'description': 'There are four Federal regulators of banks and savings and loan institutions (There are now three federal regulators of banks and savings and loan institutions. Berfore July 21, 2011, there were four federal regulators): federal deposit insurance corporation (fdic) - primary federal regulator responsible for state-chartered banks not members of the Federal Reserve System and state chartered savings banks. Federal Reserve Board (FRB) - Primary Federal regulator responsible for state-chartered commercial bank members of the Federal Reserve System. Office of the Comptroller of the Currency (OCC) - Primary Federal regulator responsible for nationally chartered commercial banks and federally chartered savings and loan associations. Before 7/21/11, Office of Thrift Supervision (OTS) - Primary Federal regulator responsible for federally chartered savings and loan associations, federal savings banks and state-chartered savings and loan associations. FDIC insured depository institutions are members of the Deposit Insurance Fund (DIF). ',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'AGY2_GOV_SPVRABNME'
        }]
    },
    'REPDTE': {
        'title': 'Report Date',
        'description': 'The last day of the financial reporting period selected.',
        'type': 'string',
        'x-source-mapping': [{
            'formula': {
                'type': 'date',
                'parameters': {
                    'inputFormat': "yyyy-MM-dd'T'HH:mm:ss",
                    'outputFormat': 'MM/dd/yyyy',
                    'inputField': 'REPDTE_RAW',
                    'outputField': 'REPDTE'
                }
            }
        }]
    },
    'RISDATE': {
        'title': 'Report Date',
        'description': 'The financial reporting period selected in CCYYMM format.',
        'type': 'string',
        'format': 'date-time',
        'x-source-mapping': [{
            'formula': {
                'type': 'date',
                'parameters': {
                    'inputFormat': "yyyy-MM-dd'T'HH:mm:ss",
                    'outputFormat': 'MM/dd/yyyy',
                    'inputField': 'REPDTE_RAW',
                    'outputField': 'RISDATE'
                }
            }
        }]
    },
    'ROA': {
        'title': 'Return on assets (ROA)',
        'description': 'Net income after taxes and extraordinary items (annualized) as a percent of average total assets.',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'ROA'
        }]
    },
    'ROAPTX': {
        'title': 'Pretax return on assets',
        'description': 'Annualized pre-tax net income as a percent of average assets. Note: Includes extraordinary items and other adjustments, net of taxes.',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'ROAPTX'
        }]
    },
    'ROAPTXQ': {
        'title': 'Quarterly Pretax return on assets',
        'description': 'Quarterly pre-tax net income as a percent of average assets. Note: Includes extraordinary items and other adjustments, net of taxes.',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'ROAPTXQ'
        }]
    },
    'ROAQ': {
        'title': 'Quarterly return on assets',
        'description': 'Quarterly net income after taxes and extraordinary items as a percent of average total assets.',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'ROAQ'
        }]
    },
    'ROE': {
        'title': 'Return on Equity (ROE)',
        'description': 'Annualized net income as a percent of average equity on a consolidated basis.     Note: If retained earnings are  negative, the ratio is shown as NA. ',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'ROE'
        }]
    },
    'ROEQ': {
        'title': 'Quarterly return on equity',
        'description': 'Quarterly net income (including gains or losses on securities and extraordinary items) as a percentage of average total equity capital.',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'ROEQ'
        }]
    },
    'RSSDHCR': {
        'title': 'RSSDID - High Regulatory Holder',
        'description': 'The unique number assigned by the Federal Reserve Board to the regulatory high holding company of the institution.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'RSSDHCR'
        }]
    },
    'RUNDATE': {
        'title': 'Run Date',
        'description': 'The day the institution information was updated.',
        'type': 'string',
        'format': 'date-time',
        'x-source-mapping': [{
            'formula': {
                'type': 'simpleSetScript',
                'parameters': {
                    'setField': 'RUNDATE',
                    'script': 'new SimpleDateFormat("MM/dd/yyyy").format(new Date())'
                }
            }
        }]
    },
    'SASSER': {
        'title': 'Sasser Institutions',
        'description': 'OTS supervised savings associations that converted their charter to that of a commercial or savings bank.  Converted associations remain members of the SAIF, but they become subject to supervision by one of the three federal banking agencies. Not Applicable as of March 31, 2006.',
        'type': 'string',
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': "if (ctx.LAW_SASSER_FLG?.toLowerCase() == 'y' ) {\n  ctx.SASSER = 1;\n} else {\n  ctx.SASSER  = 0;\n}\n"
                }
            }
        }],
        'options': [0, 1]
    },
    'SPECGRP': {
        'title': 'Asset Concentration Hierarchy',
        'description': "An indicator of an institution's primary specialization in terms of asset concentration",
        'type': 'number',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'SPECGRP'
        }]
    },
    'SPECGRPN': {
        'title': 'Specialization Group',
        'description': "Name associated with the numeric indicator (SPECGRP) of an institution's primary specialization in terms of asset concentration",
        'type': 'string',
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': "if (ctx.SPECGRP == 0) {\n  ctx.SPECGRPN = 'No Specialization Group';\n} \nelse if (ctx.SPECGRP == 1) {\n  ctx.SPECGRPN = 'International Specialization';\n} \nelse if (ctx.SPECGRP == 2) {\n  ctx.SPECGRPN = 'Agricultural Specialization';\n} \nelse if (ctx.SPECGRP == 3) {\n  ctx.SPECGRPN = 'Credit-card Specialization';\n} \nelse if (ctx.SPECGRP == 4) {\n  ctx.SPECGRPN = 'Commercial Lending Specialization';\n} \nelse if (ctx.SPECGRP == 5) {\n  ctx.SPECGRPN = 'Mortgage Lending Specialization';\n} \nelse if (ctx.SPECGRP == 6) {\n  ctx.SPECGRPN = 'Consumer Lending Specialization';\n} \nelse if (ctx.SPECGRP == 7) {\n  ctx.SPECGRPN = 'Other Specialized Under 1 Billion';\n} \nelse if (ctx.SPECGRP == 8) {\n  ctx.SPECGRPN = 'All Other Under 1 Billion';\n} \nelse if (ctx.SPECGRP == 9) {\n  ctx.SPECGRPN = 'All Other Over 1 Billion';\n} \nelse  {\n  ctx.SPECGRPN = 'Error in Specialization Group';\n} \n"
                }
            }
        }]
    },
    'STALP': {
        'title': 'State Alpha code',
        'description': 'State in which the the headquarters are physically located. The FDIC Act defines state as any State of the United States, the District of Columbia, and any territory of the United States, Puerto Rico, Guam, American Samoa, the Trust Territory of the Pacific Islands, the Virgin Island, and the Northern Mariana Islands.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_PHY_ST_ABNME'
        }],
    },
    'STALPHCR': {
        'title': 'Regulatory holding company state location',
        'description': 'State location of the regulatory high holding company (either direct or indirect owner).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'STALPHCR'
        }]
    },
    'STCHRTR': {
        'title': 'State Charter',
        'description': 'A flag (1=yes;0=no) that indicates if an institution is state chartered.',
        'type': 'string',
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': "if (ctx.CHRTAGNT?.toLowerCase() == 'state') {\n  ctx.STCHRTR = 1;\n} else  {\n  ctx.STCHRTR = 0;\n}\n"
                }
            }
        }],
        'options': [0, 1]
    },
    'STCNTY': {
        'title': 'State and county number',
        'description': 'A five digit number representing the state and county in which the institution is physically located.  The first two digits represent the FIPS state numeric code and the last three digits represent the FIPS county numeric code.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'SEE METADATA',
            'field': 'SEE METADATA'
        }]
    },
    'STNAME': {
        'title': 'State Name',
        'description': 'State in which the the institution is physically located. The FDIC Act defines state as any State of the United States, the District of Columbia, and any territory of the United States, Puerto Rico, Guam, American Samoa, the Trust Territory of the Pacific Islands, the Virgin Island, and the Northern Mariana Islands.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_PHY_ST_NME'
        }],
    },
    'STNUM': {
        'title': 'State Number',
        'description': 'The Federal Information Processing Standard code used to identify states',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_PHY_ST_NUM'
        }]
    },
    'SUBCHAPS': {
        'title': 'Subchapter S Corporations',
        'description': "The Small Business Job Protection Act of 1996 changed the Internal Revenue Code to allow financial institutions to elect Subchapter S corporation status, beginning in 1997. Banks are required to indicate on the Call Report whether there is currently in effect an election to file under Subchapter S. Thrifts have a similar requirement as of March 1998.  The most important IRS requirements to elect and maintain Subchapter S status are: There can be no more than 75 eligible shareholders and no more than one class of stock. (In general, shareholders can only be individuals, estates, and certain types of trusts. Certain retirement plans and charitable organizations will be eligible in 1998.) All shareholders must consent.  Banks and thrifts converting to Subchapter S status must use the specific charge-off method for tax purposes rather than the reserve method of accounting for bad debts and recapture tax bad debt reserves over a period of six years, if the reserve method had been used prior to conversion. (Note: even though the specific charge-off method is required for tax purposes, an adequate allowance for loan and lease losses must still be maintained on the financial statements and Call Reports.) Banks and thrifts are subject to a built-in gains (BIG) tax, if the aggregate fair market value of assets is greater than their aggregate adjusted bases on the date of conversion to Subchapter S status.     [Banks are required to indicate separately on the Call Report in December of each year, the deferred portion of income taxes reported in net income. For Subchapter S banks, some or all of their deferred tax assets and liabilities may be eliminated upon conversion to Subchapter S status; however, deferred taxes related to the BIG tax and the recapture of bad debt reserves must be recognized.].   A Subchapter S corporation is treated as a pass-through entity, similar to a partnership, for federal income tax purposes. It is generally not subject to any federal income taxes at the corporate level. Its taxable income flows through to its shareholders in proportion to their stock ownership, and the shareholders generally pay federal income taxes on their share of this taxable income. This can have the effect of reducing institutions' reported income tax expense and increasing their after-tax earnings..   The election of Subchapter S status may result in an increase in shareholders' personal tax liabilities. Therefore, S corporations typically increase the amount of earnings distributed as dividends to compensate for higher personal taxes.",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'SUBCHAPS'
        }]
    },
    'SUPRV_FD': {
        'title': 'Supervisory Region Number',
        'description': 'A numeric value associated with the name of an FDIC supervisory region',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'ORG_SPVR_REGN_CDE'
        }]
    },
    'TE01N528': {
        'title': 'Web Site URL 01',
        'description': 'URL of other public-facing internet web site the reporting institution uses to accept or solicit deposits from the public',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'TCALL_PUB_NRTV_TXT',
            'field': 'TE01N528'
        }]
    },
    'TE02N528': {
        'title': 'Web Site URL 02',
        'description': 'URL of other public-facing internet web site the reporting institution uses to accept or solicit deposits from the public',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'TCALL_PUB_NRTV_TXT',
            'field': 'TE02N528'
        }]
    },
    'TE03N528': {
        'title': 'Web Site URL 03',
        'description': 'URL of other public-facing internet web site the reporting institution uses to accept or solicit deposits from the public',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'TCALL_PUB_NRTV_TXT',
            'field': 'TE03N528'
        }]
    },
    'TE04N528': {
        'title': 'Web Site URL 04',
        'description': 'URL of other public-facing internet web site the reporting institution uses to accept or solicit deposits from the public',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'TCALL_PUB_NRTV_TXT',
            'field': 'TE04N528'
        }]
    },
    'TE05N528': {
        'title': 'Web Site URL 05',
        'description': 'URL of other public-facing internet web site the reporting institution uses to accept or solicit deposits from the public',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'TCALL_PUB_NRTV_TXT',
            'field': 'TE05N528'
        }]
    },
    'TE06N528': {
        'title': 'Web Site URL 06',
        'description': 'URL of other public-facing internet web site the reporting institution uses to accept or solicit deposits from the public',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'TCALL_PUB_NRTV_TXT',
            'field': 'TE06N528'
        }]
    },
    'TE07N528': {
        'title': 'Web Site URL 07',
        'description': 'URL of other public-facing internet web site the reporting institution uses to accept or solicit deposits from the public',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'TCALL_PUB_NRTV_TXT',
            'field': 'TE07N528'
        }]
    },
    'TE08N528': {
        'title': 'Web Site URL 08',
        'description': 'URL of other public-facing internet web site the reporting institution uses to accept or solicit deposits from the public',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'TCALL_PUB_NRTV_TXT',
            'field': 'TE08N528'
        }]
    },
    'TE09N528': {
        'title': 'Web Site URL 09',
        'description': 'URL of other public-facing internet web site the reporting institution uses to accept or solicit deposits from the public',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'TCALL_PUB_NRTV_TXT',
            'field': 'TE09N528'
        }]
    },
    'TE10N528': {
        'title': 'Web Site URL 10',
        'description': 'URL of other public-facing internet web site the reporting institution uses to accept or solicit deposits from the public',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'TCALL_PUB_NRTV_TXT',
            'field': 'TE10N528'
        }]
    },
    'TE01N529': {
        'title': 'Trade Name 01',
        'description': "Trade name other than the institution's legal name used to identify one of the institution's physical offices at which deposits are accepted or solicited from the public",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'TCALL_PUB_NRTV_TXT',
            'field': 'TE01N529'
        }]
    },
    'TE02N529': {
        'title': 'Trade Name 02',
        'description': "Trade name other than the institution's legal name used to identify one of the institution's physical offices at which deposits are accepted or solicited from the public",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'TCALL_PUB_NRTV_TXT',
            'field': 'TE02N529'
        }]
    },
    'TE03N529': {
        'title': 'Trade Name 03',
        'description': "Trade name other than the institution's legal name used to identify one of the institution's physical offices at which deposits are accepted or solicited from the public",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'TCALL_PUB_NRTV_TXT',
            'field': 'TE03N529'
        }]
    },
    'TE04N529': {
        'title': 'Trade Name 04',
        'description': "Trade name other than the institution's legal name used to identify one of the institution's physical offices at which deposits are accepted or solicited from the public",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'TCALL_PUB_NRTV_TXT',
            'field': 'TE04N529'
        }]
    },
    'TE05N529': {
        'title': 'Trade Name 05',
        'description': "Trade name other than the institution's legal name used to identify one of the institution's physical offices at which deposits are accepted or solicited from the public",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'TCALL_PUB_NRTV_TXT',
            'field': 'TE05N529'
        }]
    },
    'TE06N529': {
        'title': 'Trade Name 06',
        'description': "Trade name other than the institution's legal name used to identify one of the institution's physical offices at which deposits are accepted or solicited from the public",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'TCALL_PUB_NRTV_TXT',
            'field': 'TE06N529'
        }]
    },
    'TRACT': {
        'title': '',
        'description': 'Beyond having trust powers granted and exercised, institutions with fiduciary assets accounts, income, or other reportable fiduciary related service',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'TRACT'
        }]
    },
    'TRUST': {
        'title': 'Trust Powers',
        'description': "A flag used to indicate an institution's Trust Powers Granted status. 0 = No Trust Power Granted 1 = Trust Power Granted Where Trust Power has been granted specific codes are: 00 - Trust powers not know 10 - Full trust powers granted 11 - Full trust powers granted, exercised 12 - Full trust powers granted, not exercised 20 - Limited trust powers granted 21 - Limited trust powers granted, exercised 22 - Limited trust powers granted, not exercised 30 - Trust powers not granted 31 - Trust powers not granted, but exercised ",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'RISVIEW',
            'field': 'TRUST'
        }],
        'options': [0, 1]
    },
    'ULTCERT': {
        'title': 'Ultimate Cert',
        'description': 'The cert number of the last successor or acquirer of the institution ',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FNL_SDC',
            'field': 'ORG_FNL_CERT_NUM'
        }]
    },
    'UNINUM': {
        'title': "FDIC's unique number",
        'description': "FDIC's unique identifier number for holding companies, banks, branches and nondeposit subsidiaries.",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'ORG_UNIQ_NUM'
        }]
    },
    'WEBADDR': {
        'title': 'Primary Internet Web Address',
        'description': "The primary internet web address is the public internet site obtained from the most recent FFIEC Call Report (CALL) for commercial banks or from the supplemental information for Thrift Financial Reporters (TFR). The primary internet web address is included only for those institutions reporting an address on the most recent FFIEC Call Report or Thrift Financial Report.  This information resides in the most recent demographic information file. For some institutions users will find that for the item Primary Internet Web Address: the caption will read 'Web site not available'.  Possible reasons that a Web site may not be available are: The institution failed to file on the most recent call report or TFR. The institution filed a primary Internet Web address on its most recent FFIEC Call Report; however, the address filed by the institution was not in accordance with the instructions provided by the FFIEC on how to file a primary Internet Web address or FDIC attempts to validate and access the site were unsuccessful. Users may also experience instances where the URL provided for primary Internet Web address in ID returns an error stating that the site is not found. Possible reasons for such occurrences are: The institution?s reported primary Web address was valid as of the date that the demographic information was updated in ID, but is no longer valid. The institution?s reported Internet Web address is valid, but the institution?s Web site was inoperable at the time that the user attempted to access it due to technical problems being experienced by the institution?s Web site, the institution?s web provider, the user?s Web provider, or other issues not related to the validity of the Web address.  Users are advised to contact the institution on any questions regarding the services provided by the institution. For questions involving the reporting of primary Internet Web address by those institutions that file a FFIEC Call report, users are advised to contact supervision@fdic.gov.  For questions involving the primary Internet Web address of institutions that file a Thrift Financial Report, users are advised to contact pamela.schaar@ots.treas.gov or call Ms. Schaar at (202) 906-7205. Disclaimer: The Primary Internet Web Addresses listed have been reported to the FDIC by each institution. The hyperlinks to institution Internet sites are provided solely as a convenience to users of the FDIC Internet site. The FDIC has made a limited effort to determine that these links function properly. However, linked sites are not under the control of FDIC, and FDIC is not responsible for the contents of any linked site, or any link contained in a linked site.  Even if you access an institution?s site by means of the link provided by FDIC, you are responsible for confirming the identity and authenticity of any institution you visit and transact business with online. The inclusion of a link does not imply or constitute an endorsement by FDIC of the institution, its ownership or management, the products or services it offers, or any advertisers or sponsors appearing on the institution?s web site.",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'TCALL_CNF_CNTC_INF',
            'field': 'BKWEBADDR'
        }]
    },
    'ZIP': {
        'type': 'string',
        'title': 'Zip Code',
        'description': 'The first three, four, or five digits of the full postal zip code representing physical location of the institution or its branch office.',
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': "if (ctx.ZIP_RAW != null && ctx.ZIP_RAW?.length() < 5){\n  StringBuilder sb = new StringBuilder();\n  for (int i = 0; i < 5; i++) {\n    sb.append('0');\n  }\n  ctx.ZIP = sb.substring(ctx.ZIP_RAW.length()) + ctx.ZIP_RAW;\n} else {\n  ctx.ZIP = ctx.ZIP_RAW;\n}\n"
                }
            }
        }]
    }
}