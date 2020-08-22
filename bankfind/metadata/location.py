location_dict = {
    'ADDRESS': {
        'type': 'string',
        'title': 'Branch Address',
        'description': 'Street address at which the branch is physically located.',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_PHY_LNE1_TXT'
        }, {
            'file': 'VINST_BR_CUR_SDC',
            'field': 'LOCN_ADDR_LNE1_TXT'
        }]
    },
    'BKCLASS': {
        'type': 'string',
        'title': 'Institution Class',
        'description': "A classification code assigned by the FDIC based on the institution''s charter type (commercial bank or savings institution), charter agent (state or federal), Federal Reserve membership status (Fed member, Fed nonmember) and its primary federal regulator (state chartered institutions are subject to both federal and state supervision). N - Commercial bank, national (federal) charter and Fed member, supervised by the Office of the Comptroller of the Currency (OCC); NM - Commercial bank, state charter and Fed nonmember, supervised by the FDIC; OI - Insured U.S. branch of a foreign chartered institution (IBA); SA - Savings associations, state or federal charter, supervised by the Office of Thrift Supervision (OTS); SB - Savings banks, state charter, supervised by the FDIC; SM - Commercial bank, state charter and Fed member, supervised by the Federal Reserve (FRB)",
        'options': ['N', 'NM', 'OI', 'SA', 'SB', 'SM'],
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': 'if(ctx.INST_CLASS_CDE?.toLowerCase() == "sb" || ctx.INST_CLASS_CDE?.toLowerCase() == "sl") { \n  ctx.BKCLASS = \'SA\'; \n} else if (ctx.INST_CLASS_CDE?.toLowerCase() == "mi" || ctx.INST_CLASS_CDE?.toLowerCase() == "si") { \n  ctx.BKCLASS = \'SB\';\n} else {\n  ctx.BKCLASS = ctx.INST_CLASS_CDE;\n}\n'
                }
            }
        }]
    },
    'CBSA': {
        'type': 'string',
        'title': 'Core Based Statistical Area Name (Branch)',
        'description': 'Name of the Core Based Statistical Area (CBSA) as defined by the US Census Bureau Office of Management and Budget.',
        'x-source-mapping': [{
            'file': 'RELATION',
            'field': 'CBSANAME'
        }]
    },
    'CBSA_DIV': {
        'type': 'string',
        'title': 'Metropolitan Divisions Name (Branch)',
        'description': 'Name of the Core Based Statistical Division as defined by the US Census Bureau Office of Management and Budget.',
        'x-source-mapping': [{
            'file': 'RELATION',
            'field': 'CBSA_DIV_NAME'
        }]
    },
    'CBSA_DIV_FLG': {
        'type': 'string',
        'title': 'Metropolitan Divisions Flag (Branch)',
        'description': 'A flag (1=Yes) indicating member of a Core Based Statistical Division as defined by the US Census Bureau Office of Management and Budget.',
        'options': [0, 1],
        'x-source-mapping': [{
            'file': 'RELATION',
            'field': 'DIVISION_FLAG'
        }]
    },
    'CBSA_DIV_NO': {
        'type': 'string',
        'title': 'Metropolitan Divisions Number (Branch)',
        'description': 'Numeric code of the Core Based Statistical Division as defined by the US Census Bureau Office of Management and Budget.',
        'x-source-mapping': [{
            'file': 'RELATION',
            'field': 'CBSA_DIVISION'
        }]
    },
    'CBSA_METRO': {
        'type': 'string',
        'title': 'Metropolitan Division Number (Branch)',
        'description': 'Numeric code of the Metropolitan Statistical Area as defined by the US Census Bureau Office of Management and Budget',
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': 'if(ctx.CBSA_METRO_FLG == "1") {\n  ctx.CBSA_METRO = ctx.CBSA_NO;\n} else {\n  ctx.CBSA_METRO = 0;\n}      \n'
                }
            }
        }]
    },
    'CBSA_METRO_FLG': {
        'type': 'string',
        'title': 'Metropolitan Division Flag (Branch)',
        'description': 'A flag (1=Yes) used to indicate whether an branch is in a Metropolitan Statistical Area as defined by the US Census Bureau Office of Management and Budget',
        'x-source-mapping': [{
            'file': 'RELATION',
            'field': 'METRO_FLAG'
        }]
    },
    'CBSA_METRO_NAME': {
        'type': 'string',
        'title': 'Metropolitan Division Name (Branch)',
        'description': 'Name of the Metropolitan Statistical Area as defined by the US Census Bureau Office of Management and Budget',
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
        'type': 'string',
        'title': 'Micropolitan Division Flag (Branch)',
        'description': 'A flag (1=Yes) used to indicate whether an branch is in a Micropolitan Statistical Area as defined by the US Census Bureau Office of Management and Budget',
        'options': [0, 1],
        'x-source-mapping': [{
            'file': 'RELATION',
            'field': 'MICRO_FLAG'
        }]
    },
    'CBSA_NO': {
        'type': 'string',
        'title': 'Core Based Statistical Areas (Branch)',
        'description': 'Numeric code of the Core Based Statistical Area (CBSA) as defined by the US Census Bureau Office of Management and Budget.',
        'x-source-mapping': [{
            'file': 'RELATION',
            'field': 'CBSA'
        }]
    },
    'CERT': {
        'type': 'string',
        'title': 'Institution FDIC Certificate #',
        'description': 'A unique number assigned by the FDIC used to identify institutions and for the issuance of insurance certificates.',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'ORG_CERT_NUM'
        }, {
            'file': 'VINST_BR_CUR_SDC',
            'field': 'ORG_CERT_NUM'
        }]
    },
    'CITY': {
        'type': 'string',
        'title': 'Branch City',
        'description': 'City in which branch is physically located.',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_PHY_CTY_NME'
        }, {
            'file': 'VINST_BR_CUR_SDC',
            'field': 'LOCN_CTY_NME'
        }]
    },
    'COUNTY': {
        'type': 'string',
        'title': 'Branch County',
        'description': 'County where the branch is physically located.',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_PHY_CNTY_NME'
        }, {
            'file': 'VINST_BR_CUR_SDC',
            'field': 'LOCN_CNTY_NME'
        }]
    },
    'CSA': {
        'type': 'string',
        'title': 'Combined Statistical Area Name (Branch)',
        'description': 'Name of the Combined Statistical Area (CSA) as defined by the US Census Bureau Office of Management and Budget',
        'x-source-mapping': [{
            'file': 'RELATION',
            'field': 'CSANAME'
        }]
    },
    'CSA_FLG': {
        'type': 'string',
        'title': 'Combined Statistical Area Flag  (Branch)',
        'description': 'Flag (1=Yes) indicating member of a Combined Statistical Area (CSA) as defined by the US Census Bureau Office of Management and Budget',
        'options': [0, 1],
        'x-source-mapping': [{
            'file': 'RELATION',
            'field': 'CSA_FLAG'
        }]
    },
    'CSA_NO': {
        'type': 'string',
        'title': 'Combined Statistical Area Number  (Branch)',
        'description': 'Numeric code of the Combined Statistical Area (CSA) as defined by the US Census Bureau Office of Management and Budget',
        'x-source-mapping': [{
            'file': 'RELATION',
            'field': 'CSA'
        }]
    },
    'ESTYMD': {
        'type': 'string',
        'format': 'date-time',
        'title': 'Branch Established Date',
        'description': 'The date on which the branch began operations.',
        'x-source-mapping': [{
            'formula': {
                'type': 'date',
                'parameters': {
                    'inputFormat': "yyyy-MM-dd'T'HH:mm:ss",
                    'outputFormat': 'MM/dd/yyyy',
                    'inputField': 'ESTYMD_RAW',
                    'outputField': 'ESTYMD'
                }
            }
        }]
    },
    'FI_UNINUM': {
        'type': 'string',
        'title': 'FDIC UNINUM of the Owner Institution',
        'description': 'This is the FDIC UNINUM of the institution that owns the branch.  A UNINUM is a unique sequentially number added to the FDIC database for both banks and  branches.  There is no pattern imbedded within the number.  The FI_UNINUM is updated with every merger or purchase of branches to reflect the most current owner.',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'ORG_UNIQ_NUM'
        }, {
            'file': 'VINST_BR_CUR_SDC',
            'field': 'FI_ORG_UNIQ_NUM'
        }]
    },
    'MAINOFF': {
        'type': 'number',
        'title': 'Main Office',
        'description': 'Flag (1=Yes) indicating this location is the main office for the institution.',
        'options': [0, 1],
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'MAINOFF'
        }, {
            'file': 'VINST_BR_CUR_SDC',
            'field': 'MAINOFF'
        }]
    },
    'NAME': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'title': 'Institution Name',
        'description': 'Legal name of the FDIC Insured Institution',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'INST_FIN_LGL_NME'
        }, {
            'file': 'VINST_BR_CUR_SDC',
            'field': 'INST_FIN_LGL_NME'
        }]
    },
    'OFFNAME': {
        'type': 'string',
        'title': 'Office Name',
        'description': 'Name of the branch.',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'INST_FIN_LGL_NME'
        }, {
            'file': 'VINST_BR_CUR_SDC',
            'field': 'INST_BR_NME'
        }]
    },
    'OFFNUM': {
        'type': 'string',
        'title': 'Branch Number',
        'description': "The branch's corresponding office number.",
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'OFFNUM'
        }, {
            'file': 'VINST_BR_CUR_SDC',
            'field': 'INST_BR_OFC_NUM'
        }]
    },
    'RUNDATE': {
        'type': 'string',
        'format': 'date-time',
        'title': 'Run Date',
        'description': 'The day the institution information was updated.',
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
    'SERVTYPE': {
        'type': 'number',
        'title': 'Service Type Code',
        'description': 'Define the various types of offices of FDIC-insured institutions. 11 - Full Service Brick and Mortar Office; 12 - Full Service Retail Office; 13 - Full Service Cyber Office; 14 - Full Service Mobile Office; 15 - Full Service Home/Phone Banking; 16 - Full Service Seasonal Office; 21 - Limited Service Administrative Office; 22 - Limited Service Military Facility; 23 - Limited Service Facility Office; 24 - Limited Service Loan Production Office; 25 - Limited Service Consumer Credit Office; 26 - Limited Service Contractual Office; 27 - Limited Service Messenger Office; 28 - Limited Service Retail Office; 29 - Limited Service Mobile Office; 30 - Limited Service Trust Office;',
        'options': [11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'SERVTYPE'
        }, {
            'file': 'VINST_BR_CUR_SDC',
            'field': 'INST_BR_SVC_NUM'
        }]
    },
    'STALP': {
        'type': 'string',
        'title': 'Branch State Abbreviation',
        'description': 'State abbreviation in which the branch is physically located. The FDIC Act defines state as any State of the United States, the District of Columbia, and any territory of the United States, Puerto Rico, Guam, American Samoa, the Trust Territory of the Pacific Islands, the Virgin Island, and the Northern Mariana Islands.',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_PHY_ST_ABNME'
        }, {
            'file': 'VINST_BR_CUR_SDC',
            'field': 'LOCN_ST_ABBV_NME'
        }]
    },
    'STCNTY': {
        'type': 'string',
        'title': 'State and County Number',
        'description': 'A five digit number representing the state and county in which the institution is physically located.  The first two digits represent the FIPS state numeric code and the last three digits represent the FIPS county numeric code.',
        'x-source-mapping': [{
            'file': 'CALCULATED_IN_PIPELINE',
            'field': 'N/A'
        }]
    },
    'STNAME': {
        'type': 'string',
        'title': 'Branch State',
        'description': 'State in which the  branch is physically located. The FDIC Act defines state as any State of the United States, the District of Columbia, and any territory of the United States, Puerto Rico, Guam, American Samoa, the Trust Territory of the Pacific Islands, the Virgin Island, and the Northern Mariana Islands.',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'LOCN_PHY_ST_NME'
        }, {
            'file': 'VINST_BR_CUR_SDC',
            'field': 'LOCN_ST_NME'
        }]
    },
    'UNINUM': {
        'type': 'string',
        'title': 'Unique Identification Number for a Branch Office',
        'description': 'Unique Identification Number for a Branch Office as assigned by the FDIC',
        'x-source-mapping': [{
            'file': 'VINST_FIN_CUR_SDC',
            'field': 'ORG_UNIQ_NUM'
        }, {
            'file': 'VINST_BR_CUR_SDC',
            'field': 'ORG_UNIQ_NUM'
        }]
    },
    'ZIP': {
        'type': 'string',
        'title': 'Branch Zip Code',
        'description': 'The first five digits of the full postal zip code representing physical location of the branch.',
        'x-source-mapping': [{
            'formula': {
                'type': 'raw',
                'parameters': {
                    'script': "if (ctx.ZIP_RAW != null && ctx.ZIP_RAW?.length() < 5){\n  StringBuilder sb = new StringBuilder();\n  for (int i = 0; i < 5; i++) {\n    sb.append('0');\n  }\n  ctx.ZIP = sb.substring(ctx.ZIP_RAW.length()) + ctx.ZIP_RAW;\n} else {\n  ctx.ZIP = ctx.ZIP_RAW;\n}"
                }
            }
        }]
    }
}
