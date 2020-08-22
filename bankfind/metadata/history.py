history_dict = {
    'TRANSNUM': {
        'type': 'number',
        'title': 'System Transaction Number',
        'description': 'System Transaction Number',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'TRANSNUM'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'TRANSNUM'
        }, {
            'file': 'UPDATE',
            'field': 'TRANSNUM'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'TRANSNUM'
        }, {
            'file': 'PANDAS',
            'field': 'TRANSNUM'
        }]
    },
    'CHANGECODE': {
        'type': 'number',
        'title': 'Activity Event Code',
        'description': 'Activity Event Code',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'CHANGECODE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'CHANGECODE'
        }, {
            'file': 'UPDATE',
            'field': 'CHANGECODE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'CHANGECODE'
        }, {
            'file': 'PANDAS',
            'field': 'CHANGECODE'
        }]
    },
    'CHANGECODE_DESC': {
        'type': 'string',
        'title': 'Activity Event Code Description',
        'description': 'Activity Event Code Description',
        'x-elastic-type': 'keyword',
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'CHANGECODE_DESC'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'CHANGECODE_DESC'
        }, {
            'file': 'UPDATE',
            'field': 'CHANGECODE_DESC'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'CHANGECODE_DESC'
        }, {
            'file': 'PANDAS',
            'field': 'CHANGECODE_DESC'
        }]
    },
    'PROCDATE': {
        'type': 'string',
        'format': 'date-time',
        'title': 'Process Date',
        'description': 'Activity Event Code',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'PROCDATE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'PROCDATE'
        }, {
            'file': 'UPDATE',
            'field': 'PROCDATE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'PROCDATE'
        }, {
            'file': 'PANDAS',
            'field': 'PROCDATE'
        }]
    },
    'EFFDATE': {
        'type': 'string',
        'format': 'date-time',
        'title': 'Effective Date',
        'description': 'Effective Date',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'EFFDATE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'EFFDATE'
        }, {
            'file': 'UPDATE',
            'field': 'EFFDATE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'EFFDATE'
        }, {
            'file': 'PANDAS',
            'field': 'EFFDATE'
        }]
    },
    'ENDDATE': {
        'type': 'string',
        'format': 'date-time',
        'title': 'Effective Date',
        'description': 'Effective Date',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ENDDATE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'ENDDATE'
        }, {
            'file': 'UPDATE',
            'field': 'ENDDATE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'ENDDATE'
        }, {
            'file': 'PANDAS',
            'field': 'ENDDATE'
        }]
    },
    'UNINUM': {
        'type': 'number',
        'title': "FDIC's unique number",
        'description': "FDIC's unique identifier number for holding companies, banks, branches and nondeposit subsidiaries.",
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'UNINUM'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'UNINUM'
        }, {
            'file': 'UPDATE',
            'field': 'UNINUM'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'UNINUM'
        }, {
            'file': 'PANDAS',
            'field': 'UNINUM'
        }]
    },
    'ACQ_UNINUM': {
        'type': 'number',
        'title': "FDIC's unique number of who is Acquiring",
        'description': "FDIC's unique identifier number for holding companies, banks, branches and nondeposit subsidiaries. This value maps to the main office for  the acquiring Institution in a merger, acquisition, etc.",
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_UNINUM'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'ACQ_UNINUM'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_UNINUM'
        }]
    },
    'OUT_UNINUM': {
        'type': 'number',
        'title': "FDIC's unique number of who is Divesting",
        'description': "FDIC's unique identifier number for holding companies, banks, branches and nondeposit subsidiaries. This value maps to the main office for  the divesting Institution in a merger, acquisition, etc.",
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_UNINUM'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'OUT_UNINUM'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_UNINUM'
        }]
    },
    'ORG_ROLE_CDE': {
        'type': 'string',
        'title': 'Organization Role Code',
        'description': 'Codes include FI (Financial Institution), BR (Branch), and PA',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ORG_ROLE_CDE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'ORG_ROLE_CDE'
        }, {
            'file': 'UPDATE',
            'field': 'ORG_ROLE_CDE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'ORG_ROLE_CDE'
        }, {
            'file': 'PANDAS',
            'field': 'ORG_ROLE_CDE'
        }]
    },
    'REPORT_TYPE': {
        'type': 'number',
        'title': 'Report Type',
        'description': 'Type of Report',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'REPORT_TYPE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'REPORT_TYPE'
        }, {
            'file': 'UPDATE',
            'field': 'REPORT_TYPE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'REPORT_TYPE'
        }, {
            'file': 'PANDAS',
            'field': 'REPORT_TYPE'
        }]
    },
    'CLASS': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'title': 'TBD',
        'description': 'TBD',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_CLASS'
        }, {
            'file': 'UPDATE',
            'field': 'CLASS'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'CLASS'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_CLASS'
        }]
    },
    'BANK_INSURED': {
        'type': 'string',
        'title': 'Bank Insurance Status',
        'description': 'Bank Insurance Status',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'BANK_INSURED'
        }, {
            'file': 'UPDATE',
            'field': 'BANK_INSURED'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'BANK_INSURED'
        }, {
            'file': 'PANDAS',
            'field': 'BANK_INSURED'
        }]
    },
    'ACQ_CHANGECODE': {
        'type': 'number',
        'title': 'Activity Event Code',
        'description': 'Activity Event Code',
        'x-source-mapping': [{
            'file': 'PANDAS',
            'field': 'ACQ_CHANGECODE'
        }]
    },
    'ACQ_ORG_EFF_DTE': {
        'type': 'string',
        'format': 'date-time',
        'title': 'Effective Date',
        'description': 'Effective Date',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_ORG_EFF_DTE'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_ORG_EFF_DTE'
        }]
    },
    'ACQ_INSTNAME': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'x-elastic-normalizer': 'case_insensitive',
        'title': 'Institution name',
        'description': 'The legal name of the institution.',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_INSTNAME'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_INSTNAME'
        }]
    },
    'ACQ_CERT': {
        'title': 'FDIC Certificate #',
        'description': 'A unique NUMBER assigned by the FDIC used to identify institutions and for the issuance of insurance certificates.',
        'type': 'number',
        'x-source-overwrite': False,
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_CERT'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_CERT'
        }]
    },
    'ACQ_CLCODE': {
        'title': 'Numeric code',
        'description': 'Numeric code which identifies the major and minor categories of an institution.',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_CLCODE'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_CLCODE'
        }]
    },
    'ACQ_CHARTER': {
        'title': 'OCC Charter Number',
        'description': 'A unique number assigned by the Office of the Comptroller of the Currency (OCC) used to identify institutions that it has chartered and regulates (i.e. national  banks).',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_CHARTER'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_CHARTER'
        }]
    },
    'ACQ_CHARTAGENT': {
        'title': 'Acquiring Chartering Agency',
        'description': 'All Chartering Agencies - State and Federal  Comptroller of the Currency - Chartering authority for nationally chartered commercial banks and for federally chartered savings associations (The Office of Thrift Supervision (OTS) before 7/21/11)  State (includes U.S. Territories) - Chartering authority for institutions that are not chartered by the OCC or OTS',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_CHARTAGENT'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_CHARTAGENT'
        }]
    },
    'ACQ_FDICREGION': {
        'title': 'Supervisory Region Number',
        'description': 'A numeric value associated with the name of an FDIC supervisory region',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_FDICREGION'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_FDICREGION'
        }]
    },
    'ACQ_FDICREGION_DESC': {
        'title': 'Supervisory Region Description',
        'description': 'A description associated with the name of an FDIC supervisory region',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_FDICREGION_DESC'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_FDICREGION_DESC'
        }]
    },
    'ACQ_PADDR': {
        'type': 'string',
        'title': 'Physical Street Address',
        'description': 'Street address at which the institution or one of its branches is physically located.',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_PADDR'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_PADDR'
        }]
    },
    'ACQ_PCITY': {
        'title': 'City',
        'description': "City in which an institution's headquarters or one of its branches is physically located. Either the entire name or part of the name of a specific city may be entered to produce an Institution List.",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_PCITY'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_PCITY'
        }]
    },
    'ACQ_PSTALP': {
        'title': 'State Alpha code',
        'description': 'State in which the the headquarters are physically located. The FDIC Act defines state as any State of the United States, the District of Columbia, and any territory of the United States, Puerto Rico, Guam, American Samoa, the Trust Territory of the Pacific Islands, the Virgin Island, and the Northern Mariana Islands.',
        'type': 'string',
        'x-elastic-type': 'keyword',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_PSTALP'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_PSTALP'
        }]
    },
    'ACQ_PZIP5': {
        'type': 'string',
        'title': 'Zip Code',
        'description': 'The first three, four, or five digits of the full postal zip code representing physical location of the institution or its branch office.',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_PZIP5_RAW'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_PZIP5_RAW'
        }]
    },
    'ACQ_PZIPREST': {
        'type': 'string',
        'title': 'Zip Code Extension',
        'description': 'Zip Code Extension',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_PZIPREST'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_PZIPREST'
        }]
    },
    'ACQ_MADDR': {
        'type': 'string',
        'title': 'Mailing Street Address',
        'description': 'Street address at which the institution or one of its branches receives mail.',
        'x-source-mapping': [{
            'file': 'PANDAS',
            'field': 'ACQ_MADDR'
        }]
    },
    'ACQ_MCITY': {
        'title': 'City',
        'description': "City in which an institution's headquarters or one of its branches is physically located. Either the entire name or part of the name of a specific city may be entered to produce an Institution List.",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'PANDAS',
            'field': 'ACQ_MCITY'
        }]
    },
    'ACQ_MSTATE': {
        'title': 'Mailing State',
        'description': 'Mailing State',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'PANDAS',
            'field': 'ACQ_MSTATE'
        }]
    },
    'ACQ_MSTALP': {
        'title': 'Mailing State Abbbreviation',
        'description': 'Mailing State Abbbreviation',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'PANDAS',
            'field': 'ACQ_MSTALP'
        }]
    },
    'ACQ_MZIP5': {
        'title': 'Zip Code',
        'description': 'The first three, four, or five digits of the full postal zip code representing physical location of the institution or its branch office.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'PANDAS',
            'field': 'ACQ_MZIP5_RAW'
        }]
    },
    'ACQ_MZIPREST': {
        'type': 'string',
        'title': 'Zip Code Extension',
        'description': 'Zip Code Extension',
        'x-source-mapping': [{
            'file': 'PANDAS',
            'field': 'ACQ_MZIPREST'
        }]
    },
    'ACQ_CLASS': {
        'type': 'string',
        'title': 'TBD',
        'description': 'TBD',
        'x-elastic-type': 'keyword',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_CLASS'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_CLASS'
        }]
    },
    'ACQ_CNTYNAME': {
        'title': 'County',
        'description': 'County where the institution is physically located (abbreviated if the county name exceeds 16 characters).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_CNTYNAME'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_CNTYNAME'
        }]
    },
    'ACQ_CNTYNUM': {
        'type': 'number',
        'title': 'TBD',
        'description': 'TBD',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_CNTYNUM'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_CNTYNUM'
        }]
    },
    'ACQ_INSAGENT1': {
        'title': 'Insurance Fund Membership',
        'description': 'Deposit Insurance Fund (DIF), Bank Insurance Fund (BIF), Savings Association Insurance Fund (SAIF)',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_INSAGENT1'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_INSAGENT1'
        }]
    },
    'ACQ_INSAGENT2': {
        'title': 'Secondary Insurance Fund',
        'description': 'As a result of the establishment of a single Deposit Insurance Fund (DIF) effective April 1, 2006, the Secondary Insurance fund is no longer applicable. previously both bif and saif bank insurance fund - institutions that are members of the bank insurance fund savings association insurance fund - Institutions that are members of the Savings Association Insurance Fund',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_INSAGENT2'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_INSAGENT2'
        }]
    },
    'ACQ_REGAGENT': {
        'title': 'Acquiring Regulator',
        'description': 'There are four Federal regulators of banks and savings and loan institutions (There are now three federal regulators of banks and savings and loan institutions. Berfore July 21, 2011, there were four federal regulators): federal deposit insurance corporation (fdic) - primary federal regulator responsible for state-chartered banks not members of the Federal Reserve System and state chartered savings banks. Federal Reserve Board (FRB) - Primary Federal regulator responsible for state-chartered commercial bank members of the Federal Reserve System. Office of the Comptroller of the Currency (OCC) - Primary Federal regulator responsible for nationally chartered commercial banks and federally chartered savings and loan associations. Before 7/21/11, Office of Thrift Supervision (OTS) - Primary Federal regulator responsible for federally chartered savings and loan associations, federal savings banks and state-chartered savings and loan associations. FDIC insured depository institutions are members of the Deposit Insurance Fund (DIF).',
        'type': 'string',
        'x-elastic-type': 'keyword',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_REGAGENT'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_REGAGENT'
        }]
    },
    'ACQ_TRUST': {
        'title': 'Trust Power',
        'description': 'Trust Power',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_TRUST'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_TRUST'
        }]
    },
    'ACQ_LATITUDE': {
        'type': 'number',
        'title': 'Location Address Latitude',
        'description': 'Surviving Location Address Latitude',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_LATITUDE'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_LATITUDE'
        }]
    },
    'ACQ_LONGITUDE': {
        'type': 'number',
        'title': 'Location Address Latitude',
        'description': 'Surviving Location Address Latitude',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'ACQ_LONGITUDE'
        }, {
            'file': 'PANDAS',
            'field': 'ACQ_LONGITUDE'
        }]
    },
    'OUT_INSTNAME': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'x-elastic-normalizer': 'case_insensitive',
        'title': 'Institution name',
        'description': 'The legal name of the institution.',
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_INSTNAME'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_INSTNAME'
        }]
    },
    'OUT_CERT': {
        'title': 'FDIC Certificate #',
        'description': 'A unique NUMBER assigned by the FDIC used to identify institutions and for the issuance of insurance certificates.',
        'type': 'number',
        'x-source-overwrite': False,
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_CERT'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_CERT'
        }]
    },
    'OUT_CLCODE': {
        'title': 'Numeric code',
        'description': 'Numeric code which identifies the major and minor categories of an institution.',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_CLCODE'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_CLCODE'
        }]
    },
    'OUT_CHARTER': {
        'title': 'OCC Charter Number',
        'description': 'A unique number assigned by the Office of the Comptroller of the Currency (OCC) used to identify institutions that it has chartered and regulates (i.e. national  banks).',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_CHARTER'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_CHARTER'
        }]
    },
    'OUT_CHARTAGENT': {
        'title': 'Outgoing Chartering Agency',
        'description': 'All Chartering Agencies - State and Federal  Comptroller of the Currency - Chartering authority for nationally chartered commercial banks and for federally chartered savings associations (The Office of Thrift Supervision (OTS) before 7/21/11)  State (includes U.S. Territories) - Chartering authority for institutions that are not chartered by the OCC or OTS',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_CHARTAGENT'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_CHARTAGENT'
        }]
    },
    'OUT_FDICREGION': {
        'title': 'Supervisory Region Number',
        'description': 'A numeric value associated with the name of an FDIC supervisory region',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_FDICREGION'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_FDICREGION'
        }]
    },
    'OUT_FDICREGION_DESC': {
        'title': 'Supervisory Region Description',
        'description': 'A description associated with the name of an FDIC supervisory region',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_FDICREGION_DESC'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_FDICREGION_DESC'
        }]
    },
    'OUT_PADDR': {
        'type': 'string',
        'title': 'Physical Street Address',
        'description': 'Street address at which the institution or one of its branches is physically located.',
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_PADDR'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_PADDR'
        }]
    },
    'OUT_PCITY': {
        'title': 'City',
        'description': "City in which an institution's headquarters or one of its branches is physically located. Either the entire name or part of the name of a specific city may be entered to produce an Institution List.",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_PCITY'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_PCITY'
        }]
    },
    'OUT_PSTALP': {
        'title': 'State Alpha code',
        'description': 'State in which the the headquarters are physically located. The FDIC Act defines state as any State of the United States, the District of Columbia, and any territory of the United States, Puerto Rico, Guam, American Samoa, the Trust Territory of the Pacific Islands, the Virgin Island, and the Northern Mariana Islands.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_PSTALP'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_PSTALP'
        }]
    },
    'OUT_PZIP5': {
        'type': 'string',
        'title': 'Zip Code',
        'description': 'The first three, four, or five digits of the full postal zip code representing physical location of the institution or its branch office.',
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_PZIP5_RAW'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_PZIP5'
        }]
    },
    'OUT_PZIPREST': {
        'type': 'string',
        'title': 'Zip Code Extension',
        'description': 'Zip Code Extension',
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_PZIPREST'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_PZIPREST'
        }]
    },
    'OUT_MADDR': {
        'type': 'string',
        'title': 'Mailing Street Address',
        'description': 'Street address at which the institution or one of its branches receives mail.',
        'x-source-mapping': [{
            'file': 'PANDAS',
            'field': 'OUT_MADDR'
        }]
    },
    'OUT_MCITY': {
        'title': 'City',
        'description': "City in which an institution's headquarters or one of its branches is physically located. Either the entire name or part of the name of a specific city may be entered to produce an Institution List.",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'PANDAS',
            'field': 'OUT_MCITY'
        }]
    },
    'OUT_MSTATE': {
        'title': 'Mailing State',
        'description': 'Mailing State',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'PANDAS',
            'field': 'OUT_MSTATE'
        }]
    },
    'OUT_MSTALP': {
        'title': 'Mailing State Abbbreviation',
        'description': 'Mailing State Abbbreviation',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'PANDAS',
            'field': 'OUT_MSTALP'
        }]
    },
    'OUT_MZIP5': {
        'type': 'string',
        'title': 'Zip Code',
        'description': 'The first three, four, or five digits of the full postal zip code representing physical location of the institution or its branch office.',
        'x-source-mapping': [{
            'file': 'PANDAS',
            'field': 'OUT_MZIP5_RAW'
        }]
    },
    'OUT_MZIPREST': {
        'type': 'string',
        'title': 'Zip Code Extension',
        'description': 'Zip Code Extension',
        'x-source-mapping': [{
            'file': 'PANDAS',
            'field': 'OUT_MZIPREST'
        }]
    },
    'OUT_CLASS': {
        'type': 'string',
        'title': 'TBD',
        'description': 'TBD',
        'x-elastic-type': 'keyword',
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_CLASS'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_CLASS'
        }]
    },
    'OUT_CNTYNAME': {
        'title': 'County',
        'description': 'County where the institution is physically located (abbreviated if the county name exceeds 16 characters).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_CNTYNAME'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_CNTYNAME'
        }]
    },
    'OUT_CNTYNUM': {
        'type': 'number',
        'title': 'TBD',
        'description': 'TBD',
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_CNTYNUM'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_CNTYNUM'
        }]
    },
    'OUT_INSAGENT1': {
        'title': 'Insurance Fund Membership',
        'description': 'Deposit Insurance Fund (DIF), Bank Insurance Fund (BIF), Savings Association Insurance Fund (SAIF)',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_INSAGENT1'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_INSAGENT1'
        }]
    },
    'OUT_INSAGENT2': {
        'title': 'Secondary Insurance Fund',
        'description': 'As a result of the establishment of a single Deposit Insurance Fund (DIF) effective April 1, 2006, the Secondary Insurance fund is no longer applicable. previously both bif and saif bank insurance fund - institutions that are members of the bank insurance fund savings association insurance fund - Institutions that are members of the Savings Association Insurance Fund',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_INSAGENT2'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_INSAGENT2'
        }]
    },
    'OUT_REGAGENT': {
        'title': 'Outgoing Regulator',
        'description': 'There are four Federal regulators of banks and savings and loan institutions (There are now three federal regulators of banks and savings and loan institutions. Berfore July 21, 2011, there were four federal regulators): federal deposit insurance corporation (fdic) - primary federal regulator responsible for state-chartered banks not members of the Federal Reserve System and state chartered savings banks. Federal Reserve Board (FRB) - Primary Federal regulator responsible for state-chartered commercial bank members of the Federal Reserve System. Office of the Comptroller of the Currency (OCC) - Primary Federal regulator responsible for nationally chartered commercial banks and federally chartered savings and loan associations. Before 7/21/11, Office of Thrift Supervision (OTS) - Primary Federal regulator responsible for federally chartered savings and loan associations, federal savings banks and state-chartered savings and loan associations. FDIC insured depository institutions are members of the Deposit Insurance Fund (DIF).',
        'type': 'string',
        'x-elastic-type': 'keyword',
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_REGAGENT'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_REGAGENT'
        }]
    },
    'OUT_TRUST': {
        'title': 'Trust Power',
        'description': 'Trust Power',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_TRUST'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_TRUST'
        }]
    },
    'OUT_LATITUDE': {
        'type': 'number',
        'title': 'Location Address Latitude',
        'description': 'Location Address Latitude',
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_LATITUDE'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_LATITUDE'
        }]
    },
    'OUT_LONGITUDE': {
        'type': 'number',
        'title': 'Location Address Latitude',
        'description': 'Location Address Latitude',
        'x-source-mapping': [{
            'file': 'MERGER_OUT',
            'field': 'OUT_LONGITUDE'
        }, {
            'file': 'PANDAS',
            'field': 'OUT_LONGITUDE'
        }]
    },
    'SUR_CHANGECODE': {
        'type': 'number',
        'title': 'Activity Event Code',
        'description': 'Activity Event Code',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_CHANGECODE'
        }]
    },
    'SUR_INSTNAME': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'x-elastic-normalizer': 'case_insensitive',
        'title': 'Institution name',
        'description': 'The legal name of the institution.',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_INSTNAME'
        }]
    },
    'SUR_CERT': {
        'title': 'FDIC Certificate #',
        'description': 'A unique NUMBER assigned by the FDIC used to identify institutions and for the issuance of insurance certificates.',
        'type': 'number',
        'x-source-overwrite': False,
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_CERT'
        }]
    },
    'SUR_CLCODE': {
        'title': 'Numeric code',
        'description': 'Numeric code which identifies the major and minor categories of an institution.',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_CLCODE'
        }]
    },
    'SUR_CHARTER': {
        'title': 'OCC Charter Number',
        'description': 'A unique number assigned by the Office of the Comptroller of the Currency (OCC) used to identify institutions that it has chartered and regulates (i.e. national  banks).',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_CHARTER'
        }]
    },
    'SUR_CHARTAGENT': {
        'title': 'Surviving Chartering Agency',
        'description': 'All Chartering Agencies - State and Federal  Comptroller of the Currency - Chartering authority for nationally chartered commercial banks and for federally chartered savings associations (The Office of Thrift Supervision (OTS) before 7/21/11)  State (includes U.S. Territories) - Chartering authority for institutions that are not chartered by the OCC or OTS',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_CHARTAGENT'
        }]
    },
    'SUR_FDICREGION': {
        'title': 'Supervisory Region Number',
        'description': 'A numeric value associated with the name of an FDIC supervisory region',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_FDICREGION'
        }]
    },
    'SUR_FDICREGION_DESC': {
        'title': 'Supervisory Region Description',
        'description': 'A description associated with the name of an FDIC supervisory region',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_FDICREGION_DESC'
        }]
    },
    'SUR_MADDR': {
        'type': 'string',
        'title': 'Mailing Street Address',
        'description': 'Street address at which the institution or one of its branches receives mail.',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_MADDR'
        }]
    },
    'SUR_MCITY': {
        'title': 'City',
        'description': "City in which an institution's headquarters or one of its branches is physically located. Either the entire name or part of the name of a specific city may be entered to produce an Institution List.",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_MCITY'
        }]
    },
    'SUR_MSTATE': {
        'title': 'Mailing State',
        'description': 'Mailing State',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_MSTATE'
        }]
    },
    'SUR_MSTALP': {
        'title': 'Mailing State Abbreviation',
        'description': 'Mailing State Abbreviation',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_MSTALP'
        }]
    },
    'SUR_MZIP5': {
        'title': 'Zip Code',
        'description': 'The first three, four, or five digits of the full postal zip code representing physical location of the institution or its branch office.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_MZIP5_RAW'
        }]
    },
    'SUR_PZIP5': {
        'type': 'string',
        'title': 'Zip Code',
        'description': 'The first three, four, or five digits of the full postal zip code representing physical location of the institution or its branch office.',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_PZIP5_RAW'
        }]
    },
    'SUR_CLASS': {
        'type': 'string',
        'title': 'TBD',
        'description': 'TBD',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_CLASS'
        }]
    },
    'SUR_CNTYNAME': {
        'title': 'County',
        'description': 'County where the institution is physically located (abbreviated if the county name exceeds 16 characters).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_CNTYNAME'
        }]
    },
    'SUR_CNTYNUM': {
        'type': 'number',
        'title': 'TBD',
        'description': 'TBD',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_CNTYNUM'
        }]
    },
    'SUR_INSAGENT1': {
        'title': 'Insurance Fund Membership',
        'description': 'Deposit Insurance Fund (DIF), Bank Insurance Fund (BIF), Savings Association Insurance Fund (SAIF)',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_INSAGENT1'
        }]
    },
    'SUR_INSAGENT2': {
        'title': 'Secondary Insurance Fund',
        'description': 'As a result of the establishment of a single Deposit Insurance Fund (DIF) effective April 1, 2006, the Secondary Insurance fund is no longer applicable. previously both bif and saif bank insurance fund - institutions that are members of the bank insurance fund savings association insurance fund - Institutions that are members of the Savings Association Insurance Fund',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_INSAGENT2'
        }]
    },
    'SUR_PADDR': {
        'type': 'string',
        'title': 'Physical Street Address',
        'description': 'Street address at which the institution or one of its branches is physically located.',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_PADDR'
        }]
    },
    'SUR_PCITY': {
        'title': 'City',
        'description': "City in which an institution's headquarters or one of its branches is physically located. Either the entire name or part of the name of a specific city may be entered to produce an Institution List.",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_PCITY'
        }]
    },
    'SUR_PSTALP': {
        'title': 'State Alpha code',
        'description': 'State in which the the headquarters are physically located. The FDIC Act defines state as any State of the United States, the District of Columbia, and any territory of the United States, Puerto Rico, Guam, American Samoa, the Trust Territory of the Pacific Islands, the Virgin Island, and the Northern Mariana Islands.',
        'type': 'string',
        'x-elastic-type': 'keyword',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_PSTALP'
        }]
    },
    'SUR_PZIPREST': {
        'type': 'string',
        'title': 'Zip Code Extension',
        'description': 'Zip Code Extension',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_PZIPREST'
        }]
    },
    'SUR_REGAGENT': {
        'title': 'Surviving Regulator',
        'description': 'There are four Federal regulators of banks and savings and loan institutions (There are now three federal regulators of banks and savings and loan institutions. Berfore July 21, 2011, there were four federal regulators): federal deposit insurance corporation (fdic) - primary federal regulator responsible for state-chartered banks not members of the Federal Reserve System and state chartered savings banks. Federal Reserve Board (FRB) - Primary Federal regulator responsible for state-chartered commercial bank members of the Federal Reserve System. Office of the Comptroller of the Currency (OCC) - Primary Federal regulator responsible for nationally chartered commercial banks and federally chartered savings and loan associations. Before 7/21/11, Office of Thrift Supervision (OTS) - Primary Federal regulator responsible for federally chartered savings and loan associations, federal savings banks and state-chartered savings and loan associations. FDIC insured depository institutions are members of the Deposit Insurance Fund (DIF).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_REGAGENT'
        }]
    },
    'SUR_TRUST': {
        'title': 'Trust Power',
        'description': 'Trust Power',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_TRUST'
        }]
    },
    'SUR_LATITUDE': {
        'type': 'number',
        'title': 'Location Address Latitude',
        'description': 'Surviving Location Address Latitude',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_LATITUDE'
        }]
    },
    'SUR_LONGITUDE': {
        'type': 'number',
        'title': 'Location Address Latitude',
        'description': 'Surviving Location Address Latitude',
        'x-source-mapping': [{
            'file': 'MERGER_ACQ',
            'field': 'SUR_LONGITUDE'
        }]
    },
    'FRM_CNTYNUM': {
        'type': 'number',
        'title': 'TBD',
        'description': 'TBD',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'FRM_CNTYNUM'
        }]
    },
    'FRM_PCITY': {
        'title': 'City',
        'description': "City in which an institution's headquarters or one of its branches is physically located. Either the entire name or part of the name of a specific city may be entered to produce an Institution List.",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'FRM_PCITY'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_PCITY'
        }]
    },
    'FRM_REGAGENT': {
        'title': 'From Regulator',
        'description': 'There are four Federal regulators of banks and savings and loan institutions (There are now three federal regulators of banks and savings and loan institutions. Berfore July 21, 2011, there were four federal regulators): federal deposit insurance corporation (fdic) - primary federal regulator responsible for state-chartered banks not members of the Federal Reserve System and state chartered savings banks. Federal Reserve Board (FRB) - Primary Federal regulator responsible for state-chartered commercial bank members of the Federal Reserve System. Office of the Comptroller of the Currency (OCC) - Primary Federal regulator responsible for nationally chartered commercial banks and federally chartered savings and loan associations. Before 7/21/11, Office of Thrift Supervision (OTS) - Primary Federal regulator responsible for federally chartered savings and loan associations, federal savings banks and state-chartered savings and loan associations. FDIC insured depository institutions are members of the Deposit Insurance Fund (DIF).',
        'type': 'string',
        'x-elastic-type': 'keyword',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'FRM_REGAGENT'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_REGAGENT'
        }]
    },
    'FRM_PSTALP': {
        'title': 'State Alpha code',
        'description': 'State in which the the headquarters are physically located. The FDIC Act defines state as any State of the United States, the District of Columbia, and any territory of the United States, Puerto Rico, Guam, American Samoa, the Trust Territory of the Pacific Islands, the Virgin Island, and the Northern Mariana Islands.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'FRM_PSTALP'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_PSTALP'
        }]
    },
    'FRM_TRUST': {
        'title': 'Trust Power',
        'description': 'Trust Power',
        'type': 'string',
        'x-elastic-type': 'keyword',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'FRM_TRUST'
        }]
    },
    'FRM_CLCODE': {
        'title': 'Numeric code',
        'description': 'Numeric code which identifies the major and minor categories of an institution.',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'FRM_CLCODE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_CLCODE'
        }]
    },
    'FRM_PADDR': {
        'type': 'string',
        'title': 'Physical Street Address',
        'description': 'Street address at which the institution or one of its branches is physically located.',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'FRM_PADDR'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_PADDR'
        }]
    },
    'FRM_CHARTAGENT': {
        'title': 'From/Before Chartering Agency',
        'description': 'All Chartering Agencies - State and Federal  Comptroller of the Currency - Chartering authority for nationally chartered commercial banks and for federally chartered savings associations (The Office of Thrift Supervision (OTS) before 7/21/11)  State (includes U.S. Territories) - Chartering authority for institutions that are not chartered by the OCC or OTS',
        'type': 'string',
        'x-elastic-type': 'keyword',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'FRM_CHARTAGENT'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_CHARTAGENT'
        }]
    },
    'FRM_CLASS': {
        'type': 'string',
        'title': 'TBD',
        'description': 'TBD',
        'x-elastic-type': 'keyword',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'FRM_CLASS'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_CLASS'
        }]
    },
    'FRM_PZIP5': {
        'title': 'Zip Code',
        'description': 'The first three, four, or five digits of the full postal zip code representing physical location of the institution or its branch office.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'FRM_PZIP5_RAW'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_PZIP5_RAW'
        }]
    },
    'FRM_PZIPREST': {
        'type': 'string',
        'title': 'Zip Code Extension',
        'description': 'Zip Code Extension',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'FRM_PZIPREST'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_PZIPREST'
        }]
    },
    'FRM_INSTNAME': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'x-elastic-normalizer': 'case_insensitive',
        'title': 'Institution name',
        'description': 'The legal name of the institution.',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'FRM_INSTNAME'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_INSTNAME'
        }]
    },
    'FRM_CNTYNAME': {
        'title': 'County',
        'description': 'County where the institution is physically located (abbreviated if the county name exceeds 16 characters).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'FRM_CNTYNAME'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_CNTYNAME'
        }]
    },
    'FRM_CERT': {
        'title': 'Previous FDIC Certificate #',
        'description': 'A unique NUMBER assigned by the FDIC used to identify institutions and for the issuance of insurance certificates.',
        'type': 'number',
        'x-source-overwrite': False,
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'FRM_CERT'
        }]
    },
    'FRM_OFF_CNTYNAME': {
        'title': 'County',
        'description': 'County where the institution is physically located (abbreviated if the county name exceeds 16 characters).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_OFF_CNTYNAME'
        }]
    },
    'FRM_OFF_CNTYNUM': {
        'type': 'number',
        'title': 'TBD',
        'description': 'TBD',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_OFF_CNTYNUM'
        }]
    },
    'FRM_OFF_PADDR': {
        'type': 'string',
        'title': 'Physical Street Address',
        'description': 'Street address at which the institution or one of its branches is physically located.',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_OFF_PADDR'
        }]
    },
    'FRM_OFF_PCITY': {
        'title': 'City',
        'description': "City in which an institution's headquarters or one of its branches is physically located. Either the entire name or part of the name of a specific city may be entered to produce an Institution List.",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_OFF_PCITY'
        }]
    },
    'FRM_OFF_PSTALP': {
        'title': 'State Alpha code',
        'description': 'State in which the the headquarters are physically located. The FDIC Act defines state as any State of the United States, the District of Columbia, and any territory of the United States, Puerto Rico, Guam, American Samoa, the Trust Territory of the Pacific Islands, the Virgin Island, and the Northern Mariana Islands.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_OFF_PSTALP'
        }]
    },
    'FRM_OFF_PZIP5': {
        'type': 'string',
        'title': 'Zip Code',
        'description': 'The first three, four, or five digits of the full postal zip code representing physical location of the institution or its branch office.',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_OFF_PZIP5_RAW'
        }]
    },
    'FRM_OFF_PZIPREST': {
        'type': 'string',
        'title': 'Zip Code Extension',
        'description': 'Zip Code Extension',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_OFF_PZIPREST'
        }]
    },
    'FRM_OFF_SERVTYPE': {
        'type': 'number',
        'title': 'Service Type',
        'description': 'Service Type',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_OFF_SERVTYPE'
        }]
    },
    'FRM_OFF_SERVTYPE_DESC': {
        'type': 'string',
        'title': 'Service Type Description',
        'description': 'Service Type Description',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_OFF_SERVTYPE_DESC'
        }]
    },
    'FRM_OFF_STATE': {
        'type': 'string',
        'title': 'Office State',
        'description': 'Office State',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_OFF_STATE'
        }]
    },
    'FRM_OFF_NAME': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'title': 'Office Name',
        'description': 'Name of the branch.',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_OFF_NAME'
        }]
    },
    'FRM_OFF_NUM': {
        'type': 'string',
        'title': 'Branch Number',
        'description': "The branch's corresponding office number.",
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_OFF_NUM'
        }]
    },
    'FRM_OFF_TRUST': {
        'title': 'Trust Power',
        'description': 'Trust Power',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_TRUST'
        }]
    },
    'FRM_OFF_CLCODE': {
        'title': 'Numeric code',
        'description': 'Numeric code which identifies the major and minor categories of an institution.',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_OFF_CLCODE'
        }]
    },
    'FRM_OFF_LATITUDE': {
        'type': 'number',
        'title': 'Location Address Latitude',
        'description': 'Location Address Latitude',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_OFF_LATITUDE'
        }]
    },
    'FRM_OFF_LONGITUDE': {
        'type': 'number',
        'title': 'Location Address Latitude',
        'description': 'Location Address Latitude',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_OFF_LONGITUDE'
        }]
    },
    'FRM_LATITUDE': {
        'type': 'number',
        'title': 'Location Address Latitude',
        'description': 'Location Address Latitude',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_LATITUDE'
        }, {
            'file': 'MERGER_ACQ',
            'field': 'FRM_LATITUDE'
        }, {
            'file': 'MERGER_OUT',
            'field': 'FRM_LATITUDE'
        }, {
            'file': 'PANDAS',
            'field': 'FRM_LATITUDE'
        }]
    },
    'FRM_LONGITUDE': {
        'type': 'number',
        'title': 'Location Address Latitude',
        'description': 'Location Address Latitude',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'FRM_LONGITUDE'
        }, {
            'file': 'MERGER_ACQ',
            'field': 'FRM_LONGITUDE'
        }, {
            'file': 'MERGER_OUT',
            'field': 'FRM_LONGITUDE'
        }, {
            'file': 'PANDAS',
            'field': 'FRM_LONGITUDE'
        }]
    },
    'CERT': {
        'title': 'FDIC Certificate #',
        'description': 'A unique NUMBER assigned by the FDIC used to identify institutions and for the issuance of insurance certificates.',
        'type': 'number',
        'x-source-overwrite': False,
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'CERT'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'CERT'
        }]
    },
    'INSTNAME': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'x-elastic-normalizer': 'case_insensitive',
        'title': 'Institution name',
        'description': 'The legal name of the institution.',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'INSTNAME'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'INSTNAME'
        }]
    },
    'CHARTAGENT': {
        'title': 'Chartering Agency',
        'description': 'All Chartering Agencies - State and Federal  Comptroller of the Currency - Chartering authority for nationally chartered commercial banks and for federally chartered savings associations (The Office of Thrift Supervision (OTS) before 7/21/11)  State (includes U.S. Territories) - Chartering authority for institutions that are not chartered by the OCC or OTS',
        'type': 'string',
        'x-elastic-type': 'keyword',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'CHARTAGENT'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'CHARTAGENT'
        }]
    },
    'CLCODE': {
        'title': 'Numeric code',
        'description': 'Numeric code which identifies the major and minor categories of an institution.',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'CLCODE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'CLCODE'
        }]
    },
    'FDICREGION': {
        'title': 'Supervisory Region Number',
        'description': 'A numeric value associated with the name of an FDIC supervisory region',
        'type': 'number',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'FDICREGION'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'FDICREGION'
        }]
    },
    'FDICREGION_DESC': {
        'title': 'Supervisory Region Description',
        'description': 'A description associated with the name of an FDIC supervisory region',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'FDICREGION_DESC'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'FDICREGION_DESC'
        }]
    },
    'CNTYNAME': {
        'title': 'County',
        'description': 'County where the institution is physically located (abbreviated if the county name exceeds 16 characters).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'CNTYNAME'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'CNTYNAME'
        }]
    },
    'CNTYNUM': {
        'type': 'number',
        'title': 'TBD',
        'description': 'TBD',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'CNTYNUM'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'CNTYNUM'
        }]
    },
    'INSAGENT1': {
        'title': 'Insurance Fund Membership',
        'description': 'Deposit Insurance Fund (DIF), Bank Insurance Fund (BIF), Savings Association Insurance Fund (SAIF)',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'INSAGENT1'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'INSAGENT1'
        }]
    },
    'INSAGENT2': {
        'title': 'Secondary Insurance Fund',
        'description': 'As a result of the establishment of a single Deposit Insurance Fund (DIF) effective April 1, 2006, the Secondary Insurance fund is no longer applicable. previously both bif and saif bank insurance fund - institutions that are members of the bank insurance fund savings association insurance fund - Institutions that are members of the Savings Association Insurance Fund',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'INSAGENT2'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'INSAGENT2'
        }]
    },
    'MADDR': {
        'type': 'string',
        'title': 'Mailing Street Address',
        'description': 'Street address at which the institution or one of its branches receives mail.',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'MADDR'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'MADDR'
        }]
    },
    'MCITY': {
        'title': 'City',
        'description': "City in which an institution's headquarters or one of its branches is physically located. Either the entire name or part of the name of a specific city may be entered to produce an Institution List.",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'MCITY'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'MCITY'
        }]
    },
    'MSTATE': {
        'title': 'Mailing State',
        'description': 'Mailing State',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'MSTATE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'MSTATE'
        }]
    },
    'MSTALP': {
        'title': 'Mailing State',
        'description': 'Mailing State',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'MSTALP'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'MSTALP'
        }]
    },
    'MZIP5': {
        'type': 'string',
        'title': 'Zip Code',
        'description': 'The first three, four, or five digits of the full postal zip code representing physical location of the institution or its branch office.',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'MZIP5_RAW'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'MZIP5_RAW'
        }]
    },
    'MZIPREST': {
        'type': 'string',
        'title': 'Zip Code Extension',
        'description': 'Zip Code Extension',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'MZIPREST'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'MZIPREST'
        }]
    },
    'PADDR': {
        'type': 'string',
        'title': 'Physical Street Address',
        'description': 'Street address at which the institution or one of its branches is physically located.',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'PADDR'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'PADDR'
        }]
    },
    'PZIP5': {
        'type': 'string',
        'title': 'Zip Code',
        'description': 'The first three, four, or five digits of the full postal zip code representing physical location of the institution or its branch office.',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'PZIP5_RAW'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'PZIP5_RAW'
        }]
    },
    'PSTALP': {
        'title': 'State Alpha code',
        'description': 'State in which the the headquarters are physically located. The FDIC Act defines state as any State of the United States, the District of Columbia, and any territory of the United States, Puerto Rico, Guam, American Samoa, the Trust Territory of the Pacific Islands, the Virgin Island, and the Northern Mariana Islands.',
        'type': 'string',
        'x-elastic-type': 'keyword',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'PSTALP'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'PSTALP'
        }]
    },
    'PZIPREST': {
        'type': 'string',
        'title': 'Zip Code Extension',
        'description': 'Zip Code Extension',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'PZIPREST'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'PZIPREST'
        }]
    },
    'PCITY': {
        'title': 'City',
        'description': "City in which an institution's headquarters or one of its branches is physically located. Either the entire name or part of the name of a specific city may be entered to produce an Institution List.",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'PCITY'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'PCITY'
        }]
    },
    'STATE': {
        'type': 'string',
        'title': 'Physical State',
        'description': 'State in which the institution or one of its branches is physically located.',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'STATE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'STATE'
        }]
    },
    'TRUST': {
        'title': 'Trust Power',
        'description': 'Trust Power',
        'type': 'string',
        'x-elastic-type': 'keyword',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'TRUST'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'TRUST'
        }]
    },
    'REGAGENT': {
        'title': 'Regulator',
        'description': 'There are four Federal regulators of banks and savings and loan institutions (There are now three federal regulators of banks and savings and loan institutions. Berfore July 21, 2011, there were four federal regulators): federal deposit insurance corporation (fdic) - primary federal regulator responsible for state-chartered banks not members of the Federal Reserve System and state chartered savings banks. Federal Reserve Board (FRB) - Primary Federal regulator responsible for state-chartered commercial bank members of the Federal Reserve System. Office of the Comptroller of the Currency (OCC) - Primary Federal regulator responsible for nationally chartered commercial banks and federally chartered savings and loan associations. Before 7/21/11, Office of Thrift Supervision (OTS) - Primary Federal regulator responsible for federally chartered savings and loan associations, federal savings banks and state-chartered savings and loan associations. FDIC insured depository institutions are members of the Deposit Insurance Fund (DIF).',
        'type': 'string',
        'x-elastic-type': 'keyword',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'REGAGENT'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'REGAGENT'
        }]
    },
    'SERVTYPE': {
        'type': 'number',
        'title': 'Service Type',
        'description': 'Service Type',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'SERVTYPE'
        }]
    },
    'SERVTYPE_DESC': {
        'type': 'string',
        'title': 'Service Type Description',
        'description': 'Service Type Description',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'SERVTYPE_DESC'
        }]
    },
    'OFF_CNTYNAME': {
        'title': 'County',
        'description': 'County where the institution is physically located (abbreviated if the county name exceeds 16 characters).',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'OFF_CNTYNAME'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'OFF_CNTYNAME'
        }, {
            'file': 'PANDAS',
            'field': 'OFF_CNTYNAME'
        }]
    },
    'OFF_NUM': {
        'type': 'number',
        'title': 'Branch Number',
        'description': "The branch's corresponding office number.",
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'OFF_NUM'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'OFF_NUM'
        }, {
            'file': 'PANDAS',
            'field': 'OFF_NUM'
        }]
    },
    'OFF_CNTYNUM': {
        'type': 'number',
        'title': 'TBD',
        'description': 'TBD',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'OFF_CNTYNUM'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'OFF_CNTYNUM'
        }, {
            'file': 'PANDAS',
            'field': 'OFF_CNTYNUM'
        }]
    },
    'OFF_PADDR': {
        'type': 'string',
        'title': 'Physical Street Address',
        'description': 'Street address at which the institution or one of its branches is physically located.',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'OFF_PADDR'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'OFF_PADDR'
        }, {
            'file': 'PANDAS',
            'field': 'OFF_PADDR'
        }]
    },
    'OFF_PSTATE': {
        'type': 'string',
        'title': 'Office State',
        'description': 'Office State',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'OFF_PSTATE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'OFF_PSTATE'
        }, {
            'file': 'PANDAS',
            'field': 'OFF_PSTATE'
        }]
    },
    'OFF_PZIP5': {
        'title': 'Zip Code',
        'description': 'The first three, four, or five digits of the full postal zip code representing physical location of the institution or its branch office.',
        'type': 'string',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'OFF_PZIP5'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'OFF_PZIP5'
        }, {
            'file': 'PANDAS',
            'field': 'OFF_PZIP5'
        }]
    },
    'OFF_PZIPREST': {
        'type': 'string',
        'title': 'Zip Code Extension',
        'description': 'Zip Code Extension',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'OFF_PZIPREST'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'OFF_PZIPREST'
        }, {
            'file': 'PANDAS',
            'field': 'OFF_PZIPREST'
        }]
    },
    'OFF_NAME': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'title': 'Office name',
        'description': 'The legal name of the office.',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'OFF_NAME'
        }, {
            'file': 'PANDAS',
            'field': 'OFF_NAME'
        }]
    },
    'OFF_PSTALP': {
        'type': 'string',
        'title': 'State',
        'description': 'State in which the institution or one of its branches is physically located.',
        'x-elastic-type': 'keyword',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'OFF_PSTALP'
        }, {
            'file': 'PANDAS',
            'field': 'OFF_PSTALP'
        }]
    },
    'OFF_PCITY': {
        'title': 'City',
        'description': "City in which an institution's headquarters or one of its branches is physically located. Either the entire name or part of the name of a specific city may be entered to produce an Institution List.",
        'type': 'string',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'OFF_PCITY'
        }, {
            'file': 'PANDAS',
            'field': 'OFF_PCITY'
        }]
    },
    'OFF_SERVTYPE': {
        'type': 'number',
        'title': 'Service Type',
        'description': 'Service Type',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'OFF_SERVTYPE'
        }, {
            'file': 'PANDAS',
            'field': 'OFF_SERVTYPE'
        }]
    },
    'OFF_LATITUDE': {
        'type': 'number',
        'title': 'Location Address Latitude',
        'description': 'Location Address Latitude',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'OFF_LATITUDE'
        }, {
            'file': 'PANDAS',
            'field': 'OFF_LATITUDE'
        }]
    },
    'OFF_LONGITUDE': {
        'type': 'number',
        'title': 'Location Address Latitude',
        'description': 'Location Address Latitude',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'OFF_LONGITUDE'
        }, {
            'file': 'PANDAS',
            'field': 'OFF_LONGITUDE'
        }]
    },
    'OFF_SERVTYPE_DESC': {
        'type': 'string',
        'title': 'Service Type Description',
        'description': 'Service Type Description',
        'x-elastic-type': 'keyword',
        'x-source-mapping': [{
            'file': 'UPDATE_BRANCHES',
            'field': 'OFF_SERVTYPE_DESC'
        }, {
            'file': 'PANDAS',
            'field': 'OFF_SERVTYPE_DESC'
        }]
    },
    'ESTDATE': {
        'type': 'string',
        'format': 'date-time',
        'title': 'Office Established Date',
        'description': 'Office Established Date',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'ESTDATE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'ESTDATE'
        }, {
            'file': 'PANDAS',
            'field': 'ESTDATE'
        }]
    },
    'ACQDATE': {
        'type': 'string',
        'format': 'date-time',
        'title': 'Office Acquired Date',
        'description': 'Office Acquired Date',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'ACQDATE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'ACQDATE'
        }, {
            'file': 'PANDAS',
            'field': 'ACQDATE'
        }]
    },
    'FI_EFFDATE': {
        'type': 'string',
        'format': 'date-time',
        'title': 'Financial Institution Effective Date',
        'description': 'Financial Institution Effective Date',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'FI_EFFDATE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'FI_EFFDATE'
        }]
    },
    'FI_UNINUM': {
        'type': 'number',
        'title': "FDIC's unique number",
        'description': "FDIC's unique identifier number for holding companies, banks, branches and nondeposit subsidiaries.",
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'FI_UNINUM'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'FI_UNINUM'
        }]
    },
    'ORG_STAT_FLG': {
        'type': 'string',
        'title': 'Organization Status Flag',
        'description': 'Organization Status Flag',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'ORG_STAT_FLG'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'ORG_STAT_FLG'
        }, {
            'file': 'PANDAS',
            'field': 'ORG_STAT_FLG'
        }, {
            'file': 'MERGER_ACQ',
            'field': 'ORG_STAT_FLG'
        }, {
            'file': 'MERGER_OUT',
            'field': 'ORG_STAT_FLG'
        }]
    },
    'LATITUDE': {
        'type': 'number',
        'title': 'Location Address Latitude',
        'description': 'Location Address Latitude',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'LATITUDE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'LATITUDE'
        }]
    },
    'LONGITUDE': {
        'type': 'number',
        'title': 'Location Address Latitude',
        'description': 'Location Address Latitude',
        'x-source-mapping': [{
            'file': 'UPDATE',
            'field': 'LONGITUDE'
        }, {
            'file': 'UPDATE_BRANCHES',
            'field': 'LONGITUDE'
        }]
    }
}
