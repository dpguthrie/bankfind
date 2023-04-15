financials_dict = {
    "ASSET": {
        "type": "number",
        "title": "Total assets",
        "description": "The sum of all assets owned by the institution including cash, loans, securities, bank premises and other assets. This total does not include off-balance-sheet accounts.",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ASSET"
            },
            {
                "file": "RISVIEW_MERGED",
                "field": "L_ASSET"
            }
        ]
    },
    "CALLFORM": {
        "title": "Call Form Number",
        "description": "TBD",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CALLFORM"
            },
            {
                "file": "RISVIEW_MERGED",
                "field": "CALLFORM"
            }
        ]
    },
    "CB": {
        "title": "Community Bank",
        "description": "FDIC community banks are identified based on criteria defined in the FDIC Community Banking Study. Using detailed balance sheet and geographic data, the study defines communtiy banks in terms of their traditional relationship banking and limited geographic scope of operations",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CB"
            }
        ]
    },
    "CBLRIND": {
        "title": "Community Bank Ratio",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CBLRIND"
            }
        ]
    },
    "CBLRINDQ": {
        "title": "Community Bank Ratio Quarterly",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CBLRINDQ"
            }
        ]
    },
    "CD1T3": {
        "title": "TIME DEP $250,000 OR MORE REMAINING MATURITY REPRICING OF 1-3 YEARS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CD1T3"
            }
        ]
    },
    "CD1T3R": {
        "title": "TIME DEP $250,000 OR MORE REMAINING MATURITY REPRICING OF 1-3 YEARS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "CD1T3R",
                        "numerator": "CD1T3",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "CD3LES": {
        "title": "TIME DEP $250,000 OR MORE REMAINING MATURITY REPRICING OF 3 MONTH OR LESS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CD3LES"
            }
        ]
    },
    "CD3LESR": {
        "title": "TIME DEP $250,000 OR MORE REMAINING MATURITY REPRICING OF 3 MONTH OR LESS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "CD3LESR",
                        "numerator": "CD3LES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "CD3LESS": {
        "title": "TIME DEP $250,000 OR LESS REMAINING MATURITY REPRICING OF 3 MONTH OR LESS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CD3LESS"
            }
        ]
    },
    "CD3LESSR": {
        "title": "TIME DEP $250,000 OR LESS REMAINING MATURITY REPRICING OF 3 MONTH OR LESS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "CD3LESSR",
                        "numerator": "CD3LESS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "CDOV3": {
        "title": "TIME DEP $250,000 OR MORE REMAINING MATURITY OR REPRICING OVER 3 YEARS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CDOV3"
            }
        ]
    },
    "CDOV3R": {
        "title": "TIME DEP $250,000 OR MORE REMAINING MATURITY OR REPRICING OVER 3 YEARS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "CDOV3R",
                        "numerator": "CDOV3",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "CDOV3S": {
        "title": "TIME DEP $250,000 OR LESS REMAINING MATURITY OR REPRICING OVER 3 YEARS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CDOV3S"
            }
        ]
    },
    "CDOV3SR": {
        "title": "TIME DEP $250,000 OR LESS REMAINING MATURITY OR REPRICING OVER 3 YEARS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "CDOV3SR",
                        "numerator": "CDOV3S",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "CD3T12": {
        "title": "TIME DEP $250,000 OR MORE REMAINING MATURITY OR REPRICING 3-12 MONTHS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CD3T12"
            }
        ]
    },
    "CD3T12R": {
        "title": "TIME DEP $250,000 OR MORE REMAINING MATURITY OR REPRICING 3-12 MONTHS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "CD3T12R",
                        "numerator": "CD3T12",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "CD3T12S": {
        "title": "TIME DEP $250,000 OR LESS REMAINING MATURITY OR REPRICING 3-12 MONTHS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CD3T12S"
            }
        ]
    },
    "CD3T12SR": {
        "title": "TIME DEP $250,000 OR LESS REMAINING MATURITY OR REPRICING 3-12 MONTHS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "CD3T12SR",
                        "numerator": "CD3T12S",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "CD1T3S": {
        "title": "TIME DEP $250,000 OR LESS REMAINING MATURITY OR REPRICING 1-3 YEARS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CD1T3S"
            }
        ]
    },
    "CD1T3SR": {
        "title": "TIME DEP $250,000 OR LESS REMAINING MATURITY OR REPRICING 1-3 YEARS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "CD1T3SR",
                        "numerator": "CD1T3S",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "CERT": {
        "title": "FDIC Certificate #",
        "description": "A unique NUMBER assigned by the FDIC used to identify institutions and for the issuance of insurance certificates.",
        "type": "number",
        "x-source-overwrite": False,
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CERT"
            },
            {
                "file": "RISVIEW_MERGED",
                "field": "C_CERT"
            },
            {
                "file": "VINST_FIN_CUR_SDC",
                "field": "ORG_CERT_NUM"
            }
        ]
    },
    "CERTCONS": {
        "title": "Directly owned by another bank (CERT)",
        "description": "FDIC certificate number of the parent bank or savings institution with which the reported institution\u2019s financial data has been consolidated. Beginning in March 1997, both the Thrift Financial Reports and Call Reports are completed on a fully consolidated basis.  Previously, the consolidation of subsidiary depository institutions was prohibited.  Now, parent institutions are required to file consolidated reports, while their subsidiary financial institutions are still required to file separate reports.  Click on the certificate number to identify the parent bank or thrift.",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CERTCONS"
            }
        ]
    },
    "CITYHCR": {
        "title": "City of High Holder",
        "description": "City in which the headquarters of the institution's regulatory high holder are physically located.",
        "type": "string",
        "x-elastic-type": "keyword",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CITYHCR"
            }
        ]
    },
    "DENOVO": {
        "title": "Denovo Institution",
        "description": "A flag used to indicate whether an institution is a new institution (not a recharter). This flag is set quarterly. For instance, if REPDTE is 3/31/98 and DENOVO equals 1, the institution was a denovo during the first quarter of 1998.",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DENOVO"
            }
        ]
    },
    "DEP": {
        "title": "Total deposits",
        "description": "The sum of all deposits including demand deposits, money market deposits, other savings deposits, time deposits and deposits in foreign offices.",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEP"
            },
            {
                "file": "RISVIEW_MERGED",
                "field": "L_DEP"
            }
        ]
    },
    "DEPR": {
        "title": "TOTAL DEPOSITS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "DEPR",
                        "numerator": "DEP",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DEPDOM": {
        "title": "Deposits held in domestic offices",
        "description": "The sum of all domestic office deposits, including demand deposits, money market deposits, other savings deposits and time deposits.",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPDOM"
            }
        ]
    },
    "DEPDOMR": {
        "title": "DEPOSITS HELD IN DOM OFF RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "DEPDOMR",
                        "numerator": "DEPDOM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "EQ": {
        "title": "Equity capital",
        "description": "Total equity capital (includes preferred and common stock, surplus and undivided profits).",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQ"
            }
        ]
    },
    "EQ2": {
        "title": "Equity capital",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQ2"
            }
        ]
    },
    "EQR": {
        "title": "EQUITY CAPITAL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "EQR",
                        "numerator": "EQ",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "FORM31": {
        "title": "FFIEC Call Report 31 Filer",
        "description": "A flag (1=yes,0=no) that indicates whether and institution filed an FFIEC 031 Call Report. Commercial banks with domestic and foreign offices are required to file such a report.",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "FORM31"
            }
        ]
    },
    "HCTMULT": {
        "title": "Bank Holding Company Type",
        "description": "A flag used to indicate whether an institution is a member of a multibank holding company 1=yes, 0=no",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "HCTMULT"
            }
        ]
    },
    "INSBIF": {
        "title": "TBD",
        "description": "TBD",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INSBIF"
            }
        ]
    },
    "INSDIF": {
        "title": "Deposit Insurance Fund member",
        "description": "A flag used to indicate whether an institution is insured under the Deposit Insurance Fund (DIF).  As of April 1, 2006 the Bank Insurance Fund (BIF) was merged together with the Savings Institution Insurance Fund (SAIF) to create a single Deposit Insurance Fund (DIF).  All FDIC insured BIF and SAIF member institutions that are still active or open are now insured members of DIF.    0 = No, not DIF insured and 1 = Yes, DIF insured.  Note that institutions that became inactive prior to April 1006 will also have zero value.",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INSDIF"
            }
        ]
    },
    "INSTAG": {
        "title": "Agricultural lending institution indicator",
        "description": "An indicator specifying whether an institution is primarily an agricultural lending institution.",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INSTAG"
            }
        ]
    },
    "INSTCRCD": {
        "title": "Credit Card Institutions",
        "description": "Institutions with total loans greater than 50% of total assets and credit card loans greater than 50% of total loans, including loans that have been securitized and sold.",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INSTCRCD"
            }
        ]
    },
    "INSSAIF": {
        "title": "SAIF Insured",
        "description": "Institutions who are members of the Savings Association Insurance Fund. As of April 1, 2006 SAIF was merged together with the Bank Insurance Fund (BIF) to create a single Deposit Insurance Fund (DIF).  All FDIC insured SAIF member institutions, that are still active or open, are now insured members of DIF.",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INSSAIF"
            },
            {
                "file": "RISVIEW_MERGED",
                "field": "C_INSSAI"
            }
        ]
    },
    "MINORITY": {
        "title": "MINORITY OWNED INSTITUTIONS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "MINORITY"
            }
        ]
    },
    "MUTUAL": {
        "title": "Ownership Type",
        "description": "Banking institutions fall into one of two ownership types, stock or non-stock. An institution which sells stock to raise capital is called a stock institution. It is owned by the shareholders who benefit from profits earned by the institution. A non-stock institution, or mutual institution, is owned and controlled solely by its depositors. A mutual does not issue capital stock.",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "MUTUAL"
            }
        ]
    },
    "NAMEHCR": {
        "title": "Bank Holding Company (Regulatory Top Holder)",
        "description": "Regulatory top holder is assigned by the Federal Reserve Board based on ownership and control percentages. Note: Information on bank holding companies is only as of quarter-end. Regulatory top holder is any company that directly or indirectly owns, controls or has power to vote 25 percent or more of a bank's or direct holding company's shares or  controls in any manner the election of a majority of the directors or trustees of a bank or direct holding company or  exercises a controlling influence over the management or policies of a bank or direct holding company.   Information on Thrift Holding Companies that own Savings Associations but do not own banks is not currently available in the ID System.  Source: Federal Reserve Board National Information Center data base.",
        "type": "string",
        "x-elastic-type": "keyword",
        "x-elastic-analyzer": [
            {
                "variable": "raw",
                "analyzer": "whitespace_analyzer"
            },
            {
                "variable": "autocomplete",
                "analyzer": "autocomplete_analyzer"
            }
        ],
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NAMEHCR"
            }
        ]
    },
    "NETINC": {
        "title": "Net income",
        "description": "Net interest income plus total noninterest income plus realized gains (losses) on securities and extraordinary items, less total noninterest expense, loan loss provisions and income taxes.",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NETINC"
            }
        ]
    },
    "NETINCR": {
        "title": "NET INCOME - RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NETINCR",
                        "numerator": "NETINC",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NETINCQ": {
        "title": "Net income - quarterly",
        "description": "Quarterly net interest income plus total noninterest income plus realized gains (losses) on securities and extraordinary items, less total noninterest expense, loan loss provisions and income taxes.",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NETINCQ"
            }
        ]
    },
    "NETINCQA": {
        "title": "Net income - quarterly",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NETINCQA"
            }
        ]
    },
    "NETINCQR": {
        "title": "NET INCOME - QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NETINCQR",
                        "numerator": "NETINCQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "OFFDOM": {
        "title": "Number of Domestic Offices",
        "description": "The number of domestic offices (including headquarters) operated by active institutions in the 50 states of the U.S.A.",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OFFDOM"
            }
        ]
    },
    "OFFFOR": {
        "title": "Number of Foreign Offices",
        "description": "The number of foreign offices (outside the U.S.) operated by the institution.",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OFFFOR"
            }
        ]
    },
    "OFFOA": {
        "title": "Number of US Offices",
        "description": "The number of offices operated by an FDIC-insured institution in all commonwealths and terrirtories of the US, along with those in freely associated states under the Compact of Free Association",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OFFOA"
            }
        ]
    },
    "PARCERT": {
        "title": "Directly owned by another bank (CERT)",
        "description": "The PARCERT number identifies the subsidiary institutions parent certificate number. Beginning in March 1997, both the Thrift Financial Reports and Call Reports are completed on a fully consolidated basis.  Previously, the consolidation of subsidiary depository institutions was prohibited.  Now, parent institutions are required to file consolidated reports, while their subsidiary financial institutions are still required to file separate reports.",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "PARCERT"
            }
        ]
    },
    "L_REPDTE": {
        "title": "Report Date",
        "description": "The last day of the financial reporting period selected.",
        "type": "string",
        "x-elastic-type": "keyword",
        "x-source-mapping": [
            {
                "file": "RISVIEW_MERGED",
                "field": "L_REPDTE"
            }
        ]
    },
    "REPDTE_RAW": {
        "title": "Report Date",
        "description": "The last day of the financial reporting period selected.",
        "type": "string",
        "x-elastic-type": "keyword",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "REPDTE"
            },
            {
                "file": "RISVIEW_MERGED",
                "field": "REPDTE"
            }
        ]
    },
    "REPDTE": {
        "title": "Report Date",
        "description": "The last day of the financial reporting period selected.",
        "type": "string",
        "x-elastic-type": "keyword",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "REPDTE"
            },
            {
                "file": "RISVIEW_MERGED",
                "field": "REPDTE"
            }
        ]
    },
    "REPYEAR": {
        "title": "REPORT YEAR",
        "description": "",
        "type": "string",
        "x-elastic-type": "keyword",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def reportDate = ctx.REPDTE ?: \"9999\";\nctx.REPYEAR = reportDate.substring(0, 4);\n"
                    }
                }
            }
        ]
    },
    "RISDATE": {
        "title": "Report Date",
        "description": "The financial reporting period selected in CCYYMM format.",
        "type": "string",
        "format": "date-time",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "REPDTE"
            },
            {
                "file": "RISVIEW_MERGED",
                "field": "REPDTE"
            }
        ]
    },
    "ROA": {
        "title": "Return on assets (ROA)",
        "description": "Net income after taxes and extraordinary items (annualized) as a percent of average total assets.",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ROA",
                        "numerator": "NETINCA",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "ROAPTX": {
        "title": "Pretax return on assets",
        "description": "Annualized pre-tax net income as a percent of average assets. Note: Includes extraordinary items and other adjustments, net of taxes.",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ROAPTX",
                        "numerator": "NETINBXA",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "ROAPTXQ": {
        "title": "Quarterly Pretax return on assets",
        "description": "Quarterly pre-tax net income as a percent of average assets. Note: Includes extraordinary items and other adjustments, net of taxes.",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ROAPTXQ"
            }
        ]
    },
    "ROAQ": {
        "title": "Quarterly return on assets",
        "description": "Quarterly net income after taxes and extraordinary items as a percent of average total assets.",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ROAQ"
            }
        ]
    },
    "ROE": {
        "title": "Return on Equity (ROE)",
        "description": "Annualized net income as a percent of average equity on a consolidated basis.     Note: If retained earnings are  negative, the ratio is shown as NA.",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ROE"
            }
        ]
    },
    "ROEQ": {
        "title": "Quarterly return on equity",
        "description": "Quarterly net income (including gains or losses on securities and extraordinary items) as a percentage of average total equity capital.",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ROEQ"
            }
        ]
    },
    "RSSDHCR": {
        "title": "RSSDID - High Regulatory Holder",
        "description": "The unique number assigned by the Federal Reserve Board to the regulatory high holding company of the institution.",
        "type": "string",
        "x-elastic-type": "keyword",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RSSDHCR"
            }
        ]
    },
    "SPECGRP": {
        "title": "Asset Concentration Hierarchy",
        "description": "An indicator of an institution's primary specialization in terms of asset concentration",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SPECGRP"
            }
        ]
    },
    "SPECGRPDESC": {
        "title": "Asset Concentration Hierarchy Description",
        "description": "An indicator of an institution's primary specialization in terms of asset concentration Description",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SPECGRPDESC"
            }
        ]
    },
    "STALPHCR": {
        "title": "Regulatory holding company state location",
        "description": "State location of the regulatory high holding company (either direct or indirect owner).",
        "type": "string",
        "x-elastic-type": "keyword",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "STALPHCR"
            }
        ]
    },
    "SUBCHAPS": {
        "title": "Subchapter S Corporations",
        "description": "The Small Business Job Protection Act of 1996 changed the Internal Revenue Code to allow financial institutions to elect Subchapter S corporation status, beginning in 1997. Banks are required to indicate on the Call Report whether there is currently in effect an election to file under Subchapter S. Thrifts have a similar requirement as of March 1998.  The most important IRS requirements to elect and maintain Subchapter S status are: There can be no more than 75 eligible shareholders and no more than one class of stock. (In general, shareholders can only be individuals, estates, and certain types of trusts. Certain retirement plans and charitable organizations will be eligible in 1998.) All shareholders must consent.  Banks and thrifts converting to Subchapter S status must use the specific charge-off method for tax purposes rather than the reserve method of accounting for bad debts and recapture tax bad debt reserves over a period of six years, if the reserve method had been used prior to conversion. (Note: even though the specific charge-off method is required for tax purposes, an adequate allowance for loan and lease losses must still be maintained on the financial statements and Call Reports.) Banks and thrifts are subject to a built-in gains (BIG) tax, if the aggregate fair market value of assets is greater than their aggregate adjusted bases on the date of conversion to Subchapter S status.     [Banks are required to indicate separately on the Call Report in December of each year, the deferred portion of income taxes reported in net income. For Subchapter S banks, some or all of their deferred tax assets and liabilities may be eliminated upon conversion to Subchapter S status; however, deferred taxes related to the BIG tax and the recapture of bad debt reserves must be recognized.].   A Subchapter S corporation is treated as a pass-through entity, similar to a partnership, for federal income tax purposes. It is generally not subject to any federal income taxes at the corporate level. Its taxable income flows through to its shareholders in proportion to their stock ownership, and the shareholders generally pay federal income taxes on their share of this taxable income. This can have the effect of reducing institutions' reported income tax expense and increasing their after-tax earnings..   The election of Subchapter S status may result in an increase in shareholders' personal tax liabilities. Therefore, S corporations typically increase the amount of earnings distributed as dividends to compensate for higher personal taxes.",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SUBCHAPS"
            }
        ]
    },
    "TRACT": {
        "title": "",
        "description": "Beyond having trust powers granted and exercised, institutions with fiduciary assets accounts, income, or other reportable fiduciary related service",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRACT"
            }
        ]
    },
    "TRUST": {
        "title": "Trust Powers",
        "description": "A flag used to indicate an institution's Trust Powers Granted status. 0 = No Trust Power Granted 1 = Trust Power Granted Where Trust Power has been granted specific codes are: 00 - Trust powers not know 10 - Full trust powers granted 11 - Full trust powers granted, exercised 12 - Full trust powers granted, not exercised 20 - Limited trust powers granted 21 - Limited trust powers granted, exercised 22 - Limited trust powers granted, not exercised 30 - Trust powers not granted 31 - Trust powers not granted, but exercised",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRUST"
            }
        ]
    },
    "ACEPT": {
        "title": "BANKS LIABILITY ON ACCEPTANCES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ACEPT"
            }
        ]
    },
    "ACTIVE": {
        "title": "ACTIVE INSTITUTION FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ACTIVE"
            }
        ]
    },
    "BKCLASS": {
        "title": "INSTITUTION CLASS",
        "description": "A classification code assigned by the FDIC based on the institution's charter type (commercial bank or savings institution), charter agent (state or federal), Federal Reserve membership status (Fed member, Fed non-member) and its primary federal regulator (state chartered institutions are subject to both federal and state supervision). N - Commercial bank, national (federal) charter, Fed member, and supervised by the Office of the Comptroller of the Currency (OCC); NM - Commercial bank, state charter, Fed non-member, and supervised by the Federal Deposit Insurance Corporation (FDIC); OI - Insured U.S. branch of a foreign chartered institution (IBA) and supervised by the OCC or FDIC; SB \u2013 Federal savings banks, federal charter, supervised by the OCC or before July 21,2011 the Office of Thrift Supervision (OTS); SI - State chartered stock savings banks, supervised by the FDIC; SL - State chartered stock savings and loan associations, supervised by the FDIC or before July 21,2011 the OTS; SM - Commercial bank, state charter, Fed member, and supervised by the Federal Reserve Bank (FRB); NC \u2013 Noninsured non-deposit commercial banks and/or trust companies regulated by the OCC, a state, or a territory; NS - Noninsured stock savings bank supervised by a state or territory; CU - state or federally chartered credit unions supervised by the National Credit Union Association (NCUA).",
        "type": "string",
        "x-elastic-type": "keyword",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "BKCLASS"
            }
        ]
    },
    "BKPREM": {
        "title": "PREMISES AND FIXED ASSETS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "BKPREM"
            }
        ]
    },
    "BKPREMR": {
        "title": "PREMISES AND FIXED ASSETS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "BKPREMR",
                        "numerator": "BKPREM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "BRO": {
        "title": "BROKERED DEP",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "BRO"
            }
        ]
    },
    "BROR": {
        "title": "BROKERED RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "BROR",
                        "numerator": "BRO",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "CALLYM": {
        "title": "REPORT DATE (CCYYMM)",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CALLYM"
            }
        ]
    },
    "CHBAL": {
        "title": "CASH & DUE FROM DEPOSITORY INST",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CHBAL"
            }
        ]
    },
    "CHBALR": {
        "title": "CASH & DUE FROM DEPOSITORY INST RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "CHBALR",
                        "numerator": "CHBAL",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "CHBALI": {
        "title": "INTEREST-BEARING CASH & DUE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CHBALI"
            }
        ]
    },
    "CHBALIR": {
        "title": "INTEREST-BEARING CASH & DUE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "CHBALIR",
                        "numerator": "CHBALI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "CHRTAGNT": {
        "title": "CHARTER AGENT",
        "description": "",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CHRTAGNT"
            }
        ]
    },
    "CONSERVE": {
        "title": "RTC CONSERVATORSHIP FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CONSERVE"
            }
        ]
    },
    "CRLNLS": {
        "title": "TOTAL LN&LS RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRLNLS"
            }
        ]
    },
    "CRLNLSR": {
        "title": "TOTAL LN&LS RECOVERIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRLNLSR",
                        "numerator": "CRLNLS",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRLNLSQ": {
        "title": "TOTAL LN&LS RECOVERIES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRLNLSQ"
            }
        ]
    },
    "CRLNLSQR": {
        "title": "TOTAL LN&LS RECOVERIES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRLNLSQR",
                        "numerator": "CRLNLSQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CUSLI": {
        "title": "CUSTOMERS ACCEPTANCES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CUSLI"
            }
        ]
    },
    "DDT": {
        "title": "DDA TRANS-TOTAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DDT"
            }
        ]
    },
    "DDTR": {
        "title": "DDA TRANS-TOTAL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "DDTR",
                        "numerator": "DDT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DEPFOR": {
        "title": "TOTAL DEPOSITS-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPFOR"
            }
        ]
    },
    "DEPFORR": {
        "title": "TOTAL DEPOSITS-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "DEPFORR",
                        "numerator": "DEPFOR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DEPI": {
        "title": "INTEREST-BEARING DEP",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPI"
            }
        ]
    },
    "DEPIFOR": {
        "title": "INTEREST-BEARING DEP-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPIFOR"
            }
        ]
    },
    "DEPIFORR": {
        "title": "INTEREST-BEARING DEP-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "DEPIFORR",
                        "numerator": "DEPIFOR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DEPIPCCF": {
        "title": "IPC & OFFICIAL CHECKS-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPIPCCF"
            }
        ]
    },
    "DEPIPCCFR": {
        "title": "IPC & OFFICIAL CHECKS-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "DEPIPCCFR",
                        "numerator": "DEPIPCCF",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DEPIPCF": {
        "title": "IPC-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPIPCF"
            }
        ]
    },
    "DEPNI": {
        "title": "NONINTEREST-BEARING DEP",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPNI"
            }
        ]
    },
    "DEPNIFOR": {
        "title": "NONINTEREST-BEARING DEP-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPNIFOR"
            }
        ]
    },
    "DEPNIFORR": {
        "title": "NONINTEREST-BEARING DEP-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "DEPNIFORR",
                        "numerator": "DEPNIFOR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DRLNLS": {
        "title": "TOTAL LN&LS CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRLNLS"
            }
        ]
    },
    "DRLNLSR": {
        "title": "TOTAL LN&LS CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRLNLSR",
                        "numerator": "DRLNLS",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRLNLSQ": {
        "title": "TOTAL LN&LS CHARGE-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRLNLSQ"
            }
        ]
    },
    "DRLNLSQR": {
        "title": "TOTAL LN&LS CHARGE-OFFS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRLNLSQR",
                        "numerator": "DRLNLSQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "EAMINTAN": {
        "title": "AMORT & IMPAIR LOSS AST",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EAMINTAN"
            }
        ]
    },
    "EAMINTANR": {
        "title": "AMORT & IMPAIR LOSS AST RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "EAMINTANR",
                        "numerator": "EAMINTAN",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "EAMINTQ": {
        "title": "AMORT & IMPAIR LOSS AST QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EAMINTQ"
            }
        ]
    },
    "EAMINTQR": {
        "title": "AMORT & IMPAIR LOSS AST QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "EAMINTQR",
                        "numerator": "EAMINTQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "EDEP": {
        "title": "DEPOSIT INTEREST EXPENSE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EDEP"
            }
        ]
    },
    "EDEPDOM": {
        "title": "DEPOSIT INTEREST EXPENSE-DOM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EDEPDOM"
            }
        ]
    },
    "EDEPDOMR": {
        "title": "DEPOSIT INTEREST EXPENSE-DOM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "EDEPDOMR",
                        "numerator": "EDEPDOM",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "EDEPDOMQ": {
        "title": "DEPOSIT INTEREST EXPENSE-DOM QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EDEPDOMQ"
            }
        ]
    },
    "EDEPDOMQR": {
        "title": "DEPOSIT INTEREST EXPENSE-DOM QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "EDEPDOMQR",
                        "numerator": "EDEPDOMQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "EDEPFOR": {
        "title": "DEPOSIT INTEREST EXPENSE-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EDEPFOR"
            }
        ]
    },
    "EDEPFORR": {
        "title": "DEPOSIT INTEREST EXPENSE-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "EDEPFORR",
                        "numerator": "EDEPFOR",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "EDEPFORQ": {
        "title": "DEPOSIT INTEREST EXPENSE-FOR QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EDEPFORQ"
            }
        ]
    },
    "EDEPFORQR": {
        "title": "DEPOSIT INTEREST EXPENSE-FOR QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "EDEPFORQR",
                        "numerator": "EDEPFORQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "EFHLBADV": {
        "title": "ADVANCES FROM FHLBANK INT EXP",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EFHLBADV"
            }
        ]
    },
    "EFREPP": {
        "title": "FED FUNDS & REPOS INT EXPENSE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EFREPP"
            }
        ]
    },
    "EFREPPR": {
        "title": "FED FUNDS & REPOS INT EXPENSE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "EFREPPR",
                        "numerator": "EFREPP",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "EFREPPQ": {
        "title": "FED FUNDS & REPOS INT EXPENSE QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EFREPPQ"
            }
        ]
    },
    "EFREPPQR": {
        "title": "FED FUNDS & REPOS INT EXPENSE QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "EFREPPQR",
                        "numerator": "EFREPPQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "EINTEXP": {
        "title": "TOTAL INTEREST EXPENSE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EINTEXP"
            }
        ]
    },
    "EINTEXPR": {
        "title": "TOTAL INTEREST EXPENSE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "EINTEXPR",
                        "numerator": "EINTEXP",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "EINTXQ": {
        "title": "TOTAL INTEREST EXPENSE QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EINTXQ"
            }
        ]
    },
    "EINTXQA": {
        "title": "TOTAL INTEREST EXPENSE QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EINTXQA"
            }
        ]
    },
    "EINTEXPA": {
        "title": "TOTAL INTEREST EXPENSE ANNUALLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EINTEXPA"
            }
        ]
    },
    "EINTXQR": {
        "title": "TOTAL INTEREST EXPENSE QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "EINTXQR",
                        "numerator": "EINTXQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "ELNATR": {
        "title": "PROVISIONS FOR CREDIT LOSSES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ELNATR"
            }
        ]
    },
    "ELNATRR": {
        "title": "PROVISIONS FOR CREDIT LOSSES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "ELNATRR",
                        "numerator": "ELNATR",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "ELNATQ": {
        "title": "PROVISIONS FOR CREDIT LOSSES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ELNATQ"
            }
        ]
    },
    "ELNATQA": {
        "title": "PROVISIONS FOR CREDIT LOSSES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ELNATQA"
            }
        ]
    },
    "ELNATQR": {
        "title": "PROVISIONS FOR CREDIT LOSSES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "ELNATQR",
                        "numerator": "ELNATQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "ELNLOS": {
        "title": "PROVISIONS FOR LN & LEASE LOSSES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ELNLOS"
            }
        ]
    },
    "EMTGLS": {
        "title": "MORTGAGE DEBT INTEREST EXPENSE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EMTGLS"
            }
        ]
    },
    "ADDNONINTEXP": {
        "title": "ADDITIONAL NONINTEREST EXPENSE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def EOTHNINT = ctx.EOTHNINT ?: 0;\ndef EAMINTAN = ctx.EAMINTAN ?: 0;\nif (Integer.parseInt(ctx.REPYEAR) > 2000) {\n  ctx.ADDNONINTEXP = EOTHNINT + EAMINTAN;\n} else {\n  ctx.ADDNONINTEXP = EOTHNINT;\n}\n"
                    }
                }
            }
        ]
    },
    "ADDNONINTEXPR": {
        "title": "ADDITIONAL NONINTEREST EXPENSE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "ADDNONINTEXPR",
                        "numerator": "ADDNONINTEXP",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "ADDNONINTEXPQ": {
        "title": "ADDITIONAL NONINTEREST EXPENSE QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def EOTHNINQ = ctx.EOTHNINQ ?: 0;\ndef EAMINTQ = ctx.EAMINTQ ?: 0;\nif (Integer.parseInt(ctx.REPYEAR) > 2000) {\n  ctx.ADDNONINTEXPQ = EOTHNINQ + EAMINTQ;\n} else {\n  ctx.ADDNONINTEXPQ = EOTHNINQ;\n}\n"
                    }
                }
            }
        ]
    },
    "ADDNONINTEXPQR": {
        "title": "ADDITIONAL NONINTEREST EXPENSE QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "ADDNONINTEXPQR",
                        "numerator": "ADDNONINTEXPQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "EOTHNINT": {
        "title": "ALL OTHER NONINTEREST EXPENSE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EOTHNINT"
            }
        ]
    },
    "EOTHNINTR": {
        "title": "ALL OTHER NONINTEREST EXPENSE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "EOTHNINTR",
                        "numerator": "EOTHNINT",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "EOTHNINQ": {
        "title": "ALL OTHER NONINTEREST EXPENSE QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EOTHNINQ"
            }
        ]
    },
    "EOTHNINQR": {
        "title": "ALL OTHER NONINTEREST EXPENSE QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "EOTHNINQR",
                        "numerator": "EOTHNINQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "EPREMAGG": {
        "title": "PREMISES & FIXED ASSETS EXPENSE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EPREMAGG"
            }
        ]
    },
    "EPREMAGGR": {
        "title": "PREMISES & EQUIPMENT EXPENSE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "EPREMAGGR",
                        "numerator": "EPREMAGG",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "EPREMAGQ": {
        "title": "PREMISES & FIXED ASSETS EXPENSE QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EPREMAGQ"
            }
        ]
    },
    "EPREMAGQR": {
        "title": "PREMISES & EQUIPMENT EXPENSE QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "EPREMAGQR",
                        "numerator": "EPREMAGQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "EQCDIV": {
        "title": "CASH DIVIDENDS ON COMM & PREF",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQCDIV"
            }
        ]
    },
    "EQCDIVR": {
        "title": "CASH DIVIDENDS ON COMM & PREF RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "EQCDIVR",
                        "numerator": "EQCDIV",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "EQCDIVC": {
        "title": "CASH DIVIDENDS ON COMM STOCK",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQCDIVC"
            }
        ]
    },
    "EQCDIVCR": {
        "title": "CASH DIVIDENDS ON COMM STOCK RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "EQCDIVCR",
                        "numerator": "EQCDIVC",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "EQCDIVP": {
        "title": "CASH DIVIDENDS ON PREF STOCK",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQCDIVP"
            }
        ]
    },
    "EQCDIVPR": {
        "title": "CASH DIVIDENDS ON PREF STOCK RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "EQCDIVPR",
                        "numerator": "EQCDIVP",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "EQCDIVQ": {
        "title": "CASH DIVIDENDS ON COMM & PREF QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQCDIVQ"
            }
        ]
    },
    "EQCDIVQR": {
        "title": "CASH DIVIDENDS ON COMM & PREF QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "EQCDIVQR",
                        "numerator": "EQCDIVQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "EQCFCTA": {
        "title": "EQCFCTA",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQCFCTA"
            }
        ]
    },
    "EQCONSUB": {
        "title": "MINOR INT IN CONSOL SUBS-EQ",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQCONSUB"
            }
        ]
    },
    "EQCS": {
        "title": "COMMON STOCK",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQCS"
            }
        ]
    },
    "EQCSR": {
        "title": "COMMON STOCK RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "EQCSR",
                        "numerator": "EQCS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "EQNWCERT": {
        "title": "NET WORTH CERTIFICATES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQNWCERT"
            }
        ]
    },
    "EQOTHCC": {
        "title": "OTHER EQUITY CAPITAL COMPONENTS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQOTHCC"
            }
        ]
    },
    "EQPP": {
        "title": "PERPETUAL PREFERRED STOCK",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQPP"
            }
        ]
    },
    "EQPPR": {
        "title": "PERPETUAL PREFERRED STOCK RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "EQPPR",
                        "numerator": "EQPP",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "EQSUR": {
        "title": "SURPLUS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQSUR"
            }
        ]
    },
    "EQSURR": {
        "title": "SURPLUS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "EQSURR",
                        "numerator": "EQSUR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "EQUP": {
        "title": "EQUP",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQUP"
            }
        ]
    },
    "EQUPTOT": {
        "title": "UP-NET & OTHER CAPITAL COMP",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQUPTOT"
            }
        ]
    },
    "EQUPTOTR": {
        "title": "UP-NET & OTHER CAPITAL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "EQUPTOTR",
                        "numerator": "EQUPTOT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "ESAL": {
        "title": "SALARIES AND EMPLOYEE BENEFITS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ESAL"
            }
        ]
    },
    "ESALR": {
        "title": "SALARIES AND EMPLOYEE BENEFITS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "ESALR",
                        "numerator": "ESAL",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "ESALQ": {
        "title": "SALARIES AND EMPLOYEE BENEFITS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ESALQ"
            }
        ]
    },
    "ESALQR": {
        "title": "SALARIES AND EMPLOYEE BENEFITS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "ESALQR",
                        "numerator": "ESALQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "ESUBND": {
        "title": "SUBORDINATED NOTES INT EXPENSE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ESUBND"
            }
        ]
    },
    "ETTLOTBO": {
        "title": "TT&L & OTHER BORROWINGS INT EXP",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ETTLOTBO"
            }
        ]
    },
    "EXTRA": {
        "title": "NET DISCONTINUED OPERATIONS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EXTRA"
            }
        ]
    },
    "EXTRAR": {
        "title": "NET DISCONTINUED RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "EXTRAR",
                        "numerator": "EXTRA",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "EXTRAQ": {
        "title": "NET DISCONTINUED OPERATIONS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EXTRAQ"
            }
        ]
    },
    "EXTRAQR": {
        "title": "NET DISCONTINUED OPERATIONS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "EXTRAQR",
                        "numerator": "EXTRAQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "FDICDBS": {
        "title": "FDIC REGION",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "FDICDBS"
            }
        ]
    },
    "FDICDBSDESC": {
        "title": "FDIC REGION DESC",
        "description": "",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "FDICDBSDESC"
            }
        ]
    },
    "FDICSUPV": {
        "title": "FDIC REGION - SUPERVISORY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "FDICSUPV"
            }
        ]
    },
    "FDICSUPVDESC": {
        "title": "FDIC REGION - SUPERVISORY DESC",
        "description": "",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "FDICSUPVDESC"
            }
        ]
    },
    "FED": {
        "title": "FED DISTRICT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "FED"
            }
        ]
    },
    "FEDDESC": {
        "title": "FED DISTRICT DESC",
        "description": "",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "FEDDESC"
            }
        ]
    },
    "FEDCHRTR": {
        "title": "FEDERAL CHARTER FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "FEDCHRTR"
            }
        ]
    },
    "FLDOFF": {
        "title": "FDIC RISK MANAGEMENT FIELD OFFICE",
        "description": "",
        "type": "string",
        "x-elastic-type": "keyword",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "FLDOFF"
            }
        ]
    },
    "FORCHRTR": {
        "title": "FOREIGN CHARTER FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "FORCHRTR"
            }
        ]
    },
    "FORMCFR": {
        "title": "COMMERCIAL FINANCIAL REPORT FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "FORMCFR"
            }
        ]
    },
    "FREPO": {
        "title": "FED FUNDS & REPOS SOLD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "FREPO"
            }
        ]
    },
    "FREPOR": {
        "title": "FED FUNDS & REPOS SOLD",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "FREPOR",
                        "numerator": "FREPO",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "FREPP": {
        "title": "FED FUNDS & REPOS PURCHASED",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "FREPP"
            }
        ]
    },
    "FREPPR": {
        "title": "FED FUNDS & REPOS PURCHASED RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "FREPPR",
                        "numerator": "FREPP",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "FRSMEM": {
        "title": "FRS MEMBER FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "FRSMEM"
            }
        ]
    },
    "HCTONE": {
        "title": "MEMBER OF A ONE BANK HOLDING CO",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "HCTONE"
            }
        ]
    },
    "IBA": {
        "title": "INTL BANKING ACT ENTITY FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IBA"
            }
        ]
    },
    "IBEFTAX": {
        "title": "INCOME BEFORE INC TAXES & DISC",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IBEFTAX"
            }
        ]
    },
    "ICHBAL": {
        "title": "DEPOSITORY INSTITUTIONS INT INC",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ICHBAL"
            }
        ]
    },
    "ICHBALR": {
        "title": "BALANCES FROM DEPOSITORY INSTITUTIONS YTD RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "ICHBALR",
                        "numerator": "ICHBAL",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "ICHBALQ": {
        "title": "DEPOSITORY INSTITUTIONS INT INC QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ICHBALQ"
            }
        ]
    },
    "ICHBALQR": {
        "title": "DEPOSITORY INSTITUTIONS INT INC QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "ICHBALQR",
                        "numerator": "ICHBALQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "IFREPO": {
        "title": "FED FUNDS & REPO INTEREST INCOME",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IFREPO"
            }
        ]
    },
    "IFREPOR": {
        "title": "FEDERAL FUNDS SOLD YTD RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "IFREPOR",
                        "numerator": "IFREPO",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "IFREPOQ": {
        "title": "FED FUNDS & REPO INTEREST INCOME QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IFREPOQ"
            }
        ]
    },
    "IFREPOQR": {
        "title": "FED FUNDS & REPO INTEREST INCOME QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "IFREPOQR",
                        "numerator": "IFREPOQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "IGLSEC": {
        "title": "SECURITIES GAINS AND LOSSES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IGLSEC"
            }
        ]
    },
    "IGLSECR": {
        "title": "SECURITIES GAINS AND LOSSES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "IGLSECR",
                        "numerator": "IGLSEC",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "IGLSECQR": {
        "title": "SECURITIES GAINS AND LOSSES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "IGLSECQR",
                        "numerator": "IGLSECQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "ILNDOM": {
        "title": "LOAN INCOME-DOM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ILNDOM"
            }
        ]
    },
    "ILNDOMR": {
        "title": "DOMESTIC OFFICE LOANS YTD RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "ILNDOMR",
                        "numerator": "ILNDOM",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "ILNDOMQ": {
        "title": "LOAN INCOME-DOM QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ILNDOMQ"
            }
        ]
    },
    "ILNDOMQR": {
        "title": "LOAN INCOME-DOM QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "ILNDOMQR",
                        "numerator": "ILNDOMQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "ILNFOR": {
        "title": "LOAN INCOME-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ILNFOR"
            }
        ]
    },
    "ILNFORR": {
        "title": "FOREIGN OFFICE LOANS YTD RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "ILNFORR",
                        "numerator": "ILNFOR",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "ILNFORQ": {
        "title": "LOAN INCOME-FOR QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ILNFORQ"
            }
        ]
    },
    "ILNFORQR": {
        "title": "LOAN INCOME-FOR QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "ILNFORQR",
                        "numerator": "ILNFORQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "ILS": {
        "title": "LEASE INCOME",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ILS"
            }
        ]
    },
    "ILSR": {
        "title": "LEASE FINANCING RECEIVABLES YTD RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "ILSR",
                        "numerator": "ILS",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "ILSQ": {
        "title": "LEASE INCOME QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ILSQ"
            }
        ]
    },
    "ILSQR": {
        "title": "LEASE INCOME QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "ILSQR",
                        "numerator": "ILSQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "INSALL": {
        "title": "INSURED INSTITUTION FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INSALL"
            }
        ]
    },
    "INSCOML": {
        "title": "INSURED COMMERCIAL FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INSCOML"
            }
        ]
    },
    "INSFDIC": {
        "title": "FDIC INSURED FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INSFDIC"
            }
        ]
    },
    "INSNONE": {
        "title": "NOT FEDERALLY INSURED FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INSNONE"
            }
        ]
    },
    "INSSAVE": {
        "title": "INSURED SAVINGS INSTITUTION FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INSSAVE"
            }
        ]
    },
    "INSTCOML": {
        "title": "COMMERCIAL INSTITUTION FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INSTCOML"
            }
        ]
    },
    "INSTSAVE": {
        "title": "SAVING & S&L INSTITUTION FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INSTSAVE"
            }
        ]
    },
    "INSTTYPE": {
        "title": "INSTITUTION TYPE",
        "description": "",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INSTTYPE"
            }
        ]
    },
    "INTAN": {
        "title": "INTANGIBLE ASSETS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INTAN"
            }
        ]
    },
    "INTANR": {
        "title": "INTANGIBLE ASSETS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "INTANR",
                        "numerator": "INTAN",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "INTEXPY": {
        "title": "INTEREST EXPENSE TO EARNING ASSETS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "INTEXPY",
                        "numerator": "EINTEXPA",
                        "denominator": "ERNAST5"
                    }
                }
            }
        ]
    },
    "INTEXPYQ": {
        "title": "COST OF FUNDING EARNING ASSETS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INTEXPYQ"
            }
        ]
    },
    "INTINC": {
        "title": "TOTAL INTEREST INCOME",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INTINC"
            }
        ]
    },
    "INTINCR": {
        "title": "TOTAL INTEREST INCOME YTD RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "INTINCR",
                        "numerator": "INTINC",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "INTINQ": {
        "title": "TOTAL INTEREST INCOME QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INTINQ"
            }
        ]
    },
    "INTINQR": {
        "title": "TOTAL INTEREST INCOME QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "INTINQR",
                        "numerator": "INTINQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "INTINQA": {
        "title": "",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INTINQA"
            }
        ]
    },
    "INVSUB": {
        "title": "INVEST IN UNCONSOLIDATED SUBS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INVSUB"
            }
        ]
    },
    "INVSUORE": {
        "title": "INVESTMENTS IN RE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INVSUORE"
            }
        ]
    },
    "IOTHFEE": {
        "title": "OTHER FEE INCOME",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IOTHFEE"
            }
        ]
    },
    "IOTHII": {
        "title": "OTHER INTEREST INCOME",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IOTHII"
            }
        ]
    },
    "IOTHIIR": {
        "title": "OTHER INTEREST INCOME YTD RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "IOTHIIR",
                        "numerator": "IOTHII",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "IOTHIIQ": {
        "title": "OTHER INTEREST INCOME QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IOTHIIQ"
            }
        ]
    },
    "IOTHIIQR": {
        "title": "OTHER INTEREST INCOME QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "IOTHIIQR",
                        "numerator": "IOTHIIQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "IRAKEOGH": {
        "title": "IRAS AND KEOGH PLANS-DEPOSITS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IRAKEOGH"
            }
        ]
    },
    "IRAKEOGHR": {
        "title": "IRAS AND KEOGH PLANS-DEPOSITS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "IRAKEOGHR",
                        "numerator": "IRAKEOGH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "ISC": {
        "title": "TOTAL SECURITY INCOME",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ISC"
            }
        ]
    },
    "ISCR": {
        "title": "SECURITIES YTD RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "ISCR",
                        "numerator": "ISC",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "ISCQ": {
        "title": "TOTAL SECURITY INCOME QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ISCQ"
            }
        ]
    },
    "ISCQR": {
        "ttitle": "TOTAL SECURITY INCOME QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "ISCQR",
                        "numerator": "ISCQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "ISERCHG": {
        "title": "SERVICE CHARGE ON DEPOSIT ACCTS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ISERCHG"
            }
        ]
    },
    "ISERCHGR": {
        "title": "SERVICE CHARGE ON DEPOSIT ACCTS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "ISERCHGR",
                        "numerator": "ISERCHG",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "ITAX": {
        "title": "APPLICABLE INCOME TAXES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ITAX"
            }
        ]
    },
    "ITAXR": {
        "title": "APPLICABLE INCOME TAXES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "ITAXR",
                        "numerator": "ITAX",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "ITAXQ": {
        "title": "APPLICABLE INCOME TAXES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ITAXQ"
            }
        ]
    },
    "ITAXQR": {
        "title": "APPLICABLE INCOME TAXES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "ITAXQR",
                        "numerator": "ITAXQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "ITRADE": {
        "title": "INTEREST INCOME ON TRADING ACCTS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ITRADE"
            }
        ]
    },
    "ITRADER": {
        "title": "TRADING ACCOUNTS YTD RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "ITRADER",
                        "numerator": "ITRADE",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "ITRADEQ": {
        "title": "INTEREST INCOME ON TRADING ACCTS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ITRADEQ"
            }
        ]
    },
    "ITRADEQR": {
        "title": "INTEREST INCOME ON TRADING ACCTS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "ITRADEQR",
                        "numerator": "ITRADEQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "LIAB": {
        "title": "TOTAL LIABILITIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LIAB"
            }
        ]
    },
    "LIABR": {
        "title": "TOTAL LIABILITIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LIABR",
                        "numerator": "LIAB",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LIABEQ": {
        "title": "TOTAL LIABILITIES & CAPITAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LIABEQ"
            }
        ]
    },
    "LIABEQR": {
        "title": "TOTAL LIABILITIES & CAPITAL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LIABEQR",
                        "numerator": "LIABEQ",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LIPMTG": {
        "title": "MORTGAGE LOANS IN PROCESS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LIPMTG"
            }
        ]
    },
    "LLPFDSTK": {
        "title": "LIMITED-LIFE PREFERRED STOCK",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LLPFDSTK"
            }
        ]
    },
    "LNACOTH": {
        "title": "ACCEPTANCES OF OTHER BANKS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNACOTH"
            }
        ]
    },
    "LNAG": {
        "title": "AGRICULTURAL LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNAG"
            }
        ]
    },
    "LNAGR": {
        "title": "AGRICULTURAL LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNAGR",
                        "numerator": "LNAG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNATRES": {
        "title": "ALLOW FOR LOANS LOSS ADJUSTED",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNATRES"
            }
        ]
    },
    "LNATRESJ": {
        "title": "ALLOW FOR LOANS + ALLOC TRN RISK",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNATRESJ"
            }
        ]
    },
    "LNATRESRR": {
        "title": "ALLOW FOR LOANS + ALLOC TRN RISK RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNATRESRR",
                        "numerator": "LNATRES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNAUTO": {
        "title": "CONSUMER LOANS - AUTO",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNAUTO"
            }
        ]
    },
    "LNAUTOR": {
        "title": "CONSUMER LOANS-AUTO RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNAUTOR",
                        "numerator": "LNAUTO",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNCI": {
        "title": "C&I LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCI"
            }
        ]
    },
    "LNCIR": {
        "title": "C&I LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNCIR",
                        "numerator": "LNCI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNCON": {
        "title": "CONSUMER LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCON"
            }
        ]
    },
    "LNCONR": {
        "title": "CONSUMER LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNCONR",
                        "numerator": "LNCON",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNCONOT1": {
        "title": "CONSUMER LOANS-HOME IMPROVEMENT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCONOT1"
            }
        ]
    },
    "LNCONOTH": {
        "title": "CONSUMER LOANS-OTHER",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCONOTH"
            }
        ]
    },
    "LNCONOTHR": {
        "title": "CONSUMER LOANS-OTHER RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNCONOTHR",
                        "numerator": "LNCONOTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNCRCD": {
        "title": "CONSUMER LOANS-CREDIT CARD PLAN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCRCD"
            }
        ]
    },
    "LNCRCDR": {
        "title": "CONSUMER LOANS-CREDIT CARD PLAN RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNCRCDR",
                        "numerator": "LNCRCD",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNCRCDRP": {
        "title": "LNS-CREDIT CD & RELATED PLAN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCRCDRP"
            }
        ]
    },
    "LNDEP": {
        "title": "DEP INSTITUTION LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNDEP"
            }
        ]
    },
    "LNFG": {
        "title": "FOREIGN GOVT LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNFG"
            }
        ]
    },
    "LNFGR": {
        "title": "FOREIGN GOVT LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNFGR",
                        "numerator": "LNFG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNLS": {
        "title": "LN&LS + UNEARNED INC",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNLS"
            }
        ]
    },
    "LNLSGR": {
        "title": "LOANS AND LEASES-TOTAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNLSGR"
            }
        ]
    },
    "LNLSGR2": {
        "title": "LOANS AND LEASES-TOTAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNLSGR2"
            }
        ]
    },
    "LNLSGRJ": {
        "title": "LOANS AND LEASES-TOTAL ADJUSTED",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNLSGRJ"
            }
        ]
    },
    "LNLSGRR": {
        "title": "LOANS AND LEASES-TOTAL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNLSGRR",
                        "numerator": "LNLSGR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNLSNET": {
        "title": "LOANS AND LEASES-NET",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNLSNET"
            }
        ]
    },
    "LNLSNETR": {
        "title": "LOANS AND LEASES-NET RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNLSNETR",
                        "numerator": "LNLSNET",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNMUNI": {
        "title": "MUNI LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNMUNI"
            }
        ]
    },
    "LNMUNIR": {
        "title": "MUNI LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNMUNIR",
                        "numerator": "LNMUNI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNOTCI": {
        "title": "OTHER LNS & LS-COMM-QBP",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNOTCI"
            }
        ]
    },
    "LNOTCIR": {
        "title": "OTHER LNS & LS-COMM-QBP RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNOTCIR",
                        "numerator": "LNOTCI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNOTHER": {
        "title": "LN TO NONDEP FIN INST & OTH LN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNOTHER"
            }
        ]
    },
    "LNSOTHER": {
        "title": "OTHER LOANS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleAddition",
                    "parameters": {
                        "setField": "LNSOTHER",
                        "additionFields": [
                            "LNOTHER",
                            "LNREPP"
                        ]
                    }
                }
            }
        ]
    },
    "LNSOTHERR": {
        "title": "OTHER LOANS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def LNOTHER = ctx.LNOTHER ?: 0;\ndef LNREPP = ctx.LNREPP ?: 0;\ndef ASSET = ctx.ASSET ?: 0;\nctx.LNSOTHERR = 0;\nif (ASSET > 0) {\n  ctx.LNSOTHERR = ((double)(LNOTHER + LNREPP) / ASSET) * 100;\n}\n"
                    }
                }
            }
        ]
    },
    "LNRE": {
        "title": "RE LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRE"
            }
        ]
    },
    "LNRE2": {
        "title": "RE LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRE2"
            }
        ]
    },
    "LNRECON2": {
        "title": "",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRECON2"
            }
        ]
    },
    "LNREMUL2": {
        "title": "",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNREMUL2"
            }
        ]
    },
    "LNREJ": {
        "title": "RE LOANS ADJUSTED",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNREJ"
            }
        ]
    },
    "LNRE5": {
        "title": "RE LOANS CAVG5",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRE5"
            }
        ]
    },
    "LNRER": {
        "title": "RE LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRER",
                        "numerator": "LNRE",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNREAG": {
        "title": "RE AGRICULTURAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNREAG"
            }
        ]
    },
    "LNRECON5": {
        "title": "RE CONSTRUCTION & LAND DEV-CAV5",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRECON5"
            }
        ]
    },
    "LNREAGR": {
        "title": "RE AGRICULTURAL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNREAGR",
                        "numerator": "LNREAG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRECONS": {
        "title": "RE CONSTRUCTION & LAND DEVELOP",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRECONS"
            }
        ]
    },
    "LNRECONSR": {
        "title": "RE CONSTRUCTION & LAND DEVELOP RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRECONSR",
                        "numerator": "LNRECONS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNREDOM": {
        "title": "RE LOANS-DOM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNREDOM"
            }
        ]
    },
    "LNREDOMR": {
        "title": "RE LOANS-DOM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNREDOMR",
                        "numerator": "LNREDOM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNREFOR": {
        "title": "RE LOANS-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNREFOR"
            }
        ]
    },
    "LNREFORR": {
        "title": "RE LOANS-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNREFORR",
                        "numerator": "LNREFOR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRELOC": {
        "title": "RE 1-4 FAMILY-LINE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRELOC"
            }
        ]
    },
    "LNRELOCR": {
        "title": "RE 1-4 FAMILY-LINE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRELOCR",
                        "numerator": "LNRELOC",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRELOC2": {
        "title": "RE 1-4 FAMILY-LINE2",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRELOC2"
            }
        ]
    },
    "LNRELOC5": {
        "title": "RE 1-4 FAMILY-LINE-CAVG5",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRELOC5"
            }
        ]
    },
    "LNREMULT": {
        "title": "RE MULTIFAMILY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNREMULT"
            }
        ]
    },
    "LNREMUL5": {
        "title": "RE MULTIFAMILY-CAVG5",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNREMUL5"
            }
        ]
    },
    "LNREMULTR": {
        "title": "RE MULTIFAMILY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNREMULTR",
                        "numerator": "LNREMULT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRENRES": {
        "title": "RE NONFARM NONRESIDENTIAL PROP",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRENRES"
            }
        ]
    },
    "LNRENRE5": {
        "title": "RE NONFARM NONRESIDENTIAL CAVG5",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRENRE5"
            }
        ]
    },
    "LNRENRESR": {
        "title": "RE NONFARM NONRESIDENTIAL PROP RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRENRESR",
                        "numerator": "LNRENRES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNREPP": {
        "title": "PREPAID TAXES & INS ON MTG LNS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNREPP"
            }
        ]
    },
    "LNRERES": {
        "title": "RE 1-4 FAMILY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRERES"
            }
        ]
    },
    "LNRERESR": {
        "title": "RE 1-4 FAMILY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRERESR",
                        "numerator": "LNRERES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRERES2": {
        "title": "RE 1-4 FAMILY2",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRERES2"
            }
        ]
    },
    "LNRERES5": {
        "title": "RE 1-4 FAMILY-CAVG5",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRERES5"
            }
        ]
    },
    "LNRESRE": {
        "title": "ALLOWANCE FOR RE LOAN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRESRE"
            }
        ]
    },
    "LS": {
        "title": "LEASES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LS"
            }
        ]
    },
    "LSR": {
        "title": "LEASES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LSR",
                        "numerator": "LS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "MI": {
        "title": "INSURED SAVINGS BANK FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "MI"
            }
        ]
    },
    "MTGLS": {
        "title": "MORTGAGE INDEBTEDNESS & CAP LS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "MTGLS"
            }
        ]
    },
    "N": {
        "title": "NATIONAL BANK FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "N"
            }
        ]
    },
    "NALNLS": {
        "title": "NONACCRUAL-LOANS & LEASES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NALNLS"
            }
        ]
    },
    "NC": {
        "title": "NONINSURED COMMERCIAL INST FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NC"
            }
        ]
    },
    "NCLNLS": {
        "title": "TOTAL N/C-LOANS & LEASES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NCLNLS"
            }
        ]
    },
    "NETIMIN": {
        "title": "NET INC - ATTRIB TO MINORITY INT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NETIMIN"
            }
        ]
    },
    "NETIMINR": {
        "title": "NET INC - ATTRIB TO MINORITY INT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NETIMINR",
                        "numerator": "NETIMIN",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NETIMINQ": {
        "title": "NET INC - ATTRIB TO MINORITY INT QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NETIMINQ"
            }
        ]
    },
    "NETIMINQR": {
        "title": "NET INC - ATTRIB TO MINORITY INT QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NETIMINQR",
                        "numerator": "NETIMINQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NETINBM": {
        "title": "NET INC - BANK & MINORITY INT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NETINBM"
            }
        ]
    },
    "NETINBMR": {
        "title": "NET INC - BANK & MINORITY INT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NETINBMR",
                        "numerator": "NETINBM",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NETINBMQ": {
        "title": "NET INC - BANK & MINORITY INT QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NETINBMQ"
            }
        ]
    },
    "NETINBXA": {
        "title": "NET INCOME BEFORE TAXES ANNUALLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NETINBXA"
            }
        ]
    },
    "NETIBXQA": {
        "title": "",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NETIBXQA"
            }
        ]
    },
    "NETINBMQR": {
        "title": "NET INC - BANK & MINORITY INT QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NETINBMQR",
                        "numerator": "NETINBMQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NEWINST": {
        "title": "NEW INSTITUTION FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NEWINST"
            }
        ]
    },
    "NFAA": {
        "title": "NUMBER OF FIDUCIARY ACCOUNTS AND RELATED ASSET ACCOUNTS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleAddition",
                    "parameters": {
                        "setField": "NFAA",
                        "additionFields": [
                            "TTNANUM",
                            "TTNMNUM"
                        ]
                    }
                }
            }
        ]
    },
    "NIM": {
        "title": "NET INTEREST INCOME",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NIM"
            }
        ]
    },
    "NIMR": {
        "title": "NET INTEREST INCOME RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NIMR",
                        "numerator": "NIM",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NIMQ": {
        "title": "NET INTEREST INCOME QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NIMQ"
            }
        ]
    },
    "NIMQA": {
        "title": "NET INTEREST INCOME QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NIMQA"
            }
        ]
    },
    "NIMA": {
        "title": "NET INTEREST INCOME ANNUALLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NIMA"
            }
        ]
    },
    "NIMQR": {
        "title": "NET INTEREST INCOME QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NIMQR",
                        "numerator": "NIMQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NM": {
        "title": "NONMEMBER INSURED INST FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NM"
            }
        ]
    },
    "NONII": {
        "title": "TOTAL NONINTEREST INCOME",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NONII"
            }
        ]
    },
    "NONIIR": {
        "title": "TOTAL NONINTEREST INCOME RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NONIIR",
                        "numerator": "NONII",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NONIX": {
        "title": "TOTAL NONINTEREST EXPENSE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NONIX"
            }
        ]
    },
    "NONIXR": {
        "title": "TOTAL NONINTEREST EXPENSE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NONIXR",
                        "numerator": "NONIX",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NONIXQ": {
        "title": "TOTAL NONINTEREST EXPENSE QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NONIXQ"
            }
        ]
    },
    "NONIXQA": {
        "title": "TOTAL NONINTEREST EXPENSE QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NONIXQA"
            }
        ]
    },
    "NONIXQR": {
        "title": "TOTAL NONINTEREST EXPENSE QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NONIXQR",
                        "numerator": "NONIXQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NS": {
        "title": "NONINSURED SAVINGS INST FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NS"
            }
        ]
    },
    "NTLNLS": {
        "title": "TOTAL LN&LS NET CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTLNLS"
            }
        ]
    },
    "NTLNLSCOR": {
        "title": "TOTAL LN&LS NET CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTLNLSCOR",
                        "numerator": "NTLNLS",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTLNLSQ": {
        "title": "TOTAL LN&LS NET CHARGE-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTLNLSQ"
            }
        ]
    },
    "NTLNLSQA": {
        "title": "TOTAL LN&LS NET CHARGE-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTLNLSQA"
            }
        ]
    },
    "NTLNLSCOQR": {
        "title": "TOTAL LN&LS NET CHARGE-OFFS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTLNLSCOQR",
                        "numerator": "NTLNLSQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTR": {
        "title": "NONTRANSACTION-TOTAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTR"
            }
        ]
    },
    "NTRR": {
        "title": "NONTRANSACTION-TOTAL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NTRR",
                        "numerator": "NTR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NTRIPC": {
        "title": "NONTRANSACTION-IPC",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRIPC"
            }
        ]
    },
    "NTRIPCR": {
        "title": "NONTRANSACTION-IPC RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NTRIPCR",
                        "numerator": "NTRIPC",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NTRMUNI": {
        "title": "NONTRANSACTION-MUNI",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRMUNI"
            }
        ]
    },
    "NTRMUNIR": {
        "title": "NONTRANSACTION-MUNI RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NTRMUNIR",
                        "numerator": "NTRMUNI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NTRTIME": {
        "title": "TIME DEPOSITS-TOTAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRTIME"
            }
        ]
    },
    "NTRTMLG": {
        "title": "TIME DEPOSITS OVER $100M",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRTMLG"
            }
        ]
    },
    "NTRTMLGJ": {
        "title": "AMT TOTAL TIME DEP MORE THAN $250,000",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRTMLGJ"
            }
        ]
    },
    "NTRTMLGJR": {
        "title": "AMT TOTAL TIME DEP MORE THAN $250,000 RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NTRTMLGJR",
                        "numerator": "NTRTMLGJ",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NTRTMMED": {
        "title": "AMT TIME DEP OF $250,000 OR LESS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRTMMED"
            }
        ]
    },
    "NTRTMMEDR": {
        "title": "AMT TIME DEP OF $250,000 OR LESS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NTRTMMEDR",
                        "numerator": "NTRTMMED",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NTRUSGOV": {
        "title": "NONTRANSACTION-U.S. GOVERNMENT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRUSGOV"
            }
        ]
    },
    "NTRUSGOVR": {
        "title": "NONTRANSACTION-U.S. GOVERNMENT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NTRUSGOVR",
                        "numerator": "NTRUSGOV",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NTIRTA": {
        "title": "RETAINED EARNINGS ANUALLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTIRTA"
            }
        ]
    },
    "NTTOT": {
        "title": "TOTAL LN & LS LOSS NET CHG-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTTOT"
            }
        ]
    },
    "NUMEMP": {
        "title": "NUMBER OF FULL TIME EMPLOYEES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NUMEMP"
            }
        ]
    },
    "OA": {
        "title": "OTHER ASSETS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OA"
            }
        ]
    },
    "OCCDIST": {
        "title": "OCC DISTRICT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OCCDIST"
            }
        ]
    },
    "OCCDISTDESC": {
        "title": "OCC DISTRICT DESC",
        "description": "",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OCCDISTDESC"
            }
        ]
    },
    "OI": {
        "title": "INSURED IBA OFFICE FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OI"
            }
        ]
    },
    "OTHEQ": {
        "title": "Other Equity",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OTHEQ"
            }
        ]
    },
    "OLMIN": {
        "title": "OTHER LIAB & MINOR IN SUBS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OLMIN"
            }
        ]
    },
    "ORE": {
        "title": "OTHER REAL ESTATE OWNED",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ORE"
            }
        ]
    },
    "ORER": {
        "title": "OTHER REAL ESTATE OWNED RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ORER",
                        "numerator": "ORE",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OTHBFHLB": {
        "title": "OTHER LIABILITIES-FHLB",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OTHBFHLB"
            }
        ]
    },
    "OTHBFHLBR": {
        "title": "OTHER LIABILITIES-FHLB RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OTHBFHLBR",
                        "numerator": "OTHBFHLB",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OTHBOR": {
        "title": "OTHER BORROWED MONEY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OTHBOR"
            }
        ]
    },
    "OTHBRF": {
        "title": "OTH BORROWED FUNDS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleAddition",
                    "parameters": {
                        "setField": "OTHBRF",
                        "additionFields": [
                            "TTL",
                            "OTHBOR",
                            "MTGLS"
                        ]
                    }
                }
            }
        ]
    },
    "OTHBRFR": {
        "title": "OTH BORROWED FUNDS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OTHBRFR",
                        "numerator": "OTHBRF",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OTBFH1L": {
        "title": "FHLB ADV MAT REP ONE YR OR LESS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OTBFH1L"
            }
        ]
    },
    "OTBFH1LR": {
        "title": "FHLB ADV MAT REP ONE YR OR LESS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OTBFH1LR",
                        "numerator": "OTBFH1L",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OTBFH1T3": {
        "title": "FHLB ADV MAT REP ONE YR THROUGH THREE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OTBFH1T3"
            }
        ]
    },
    "OTBFH1T3R": {
        "title": "FHLB ADV MAT REP ONE YR THROUGH THREE",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OTBFH1T3R",
                        "numerator": "OTBFH1T3",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OTBFH3T5": {
        "title": "FHLB ADV MAT REP THREE THROUGH FIVE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OTBFH3T5"
            }
        ]
    },
    "OTBFH3T5R": {
        "title": "FHLB ADV MAT REP THREE THROUGH FIVE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OTBFH3T5R",
                        "numerator": "OTBFH3T5",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OTBFHOV5": {
        "title": "FHLB ADV MAT REP OVER FIVE YEARS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OTBFHOV5"
            }
        ]
    },
    "OTBFHOV5R": {
        "title": "FHLB ADV MAT REP OVER FIVE YEARS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OTBFHOV5R",
                        "numerator": "OTBFHOV5",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OTHBFH1L": {
        "title": "FHLB ADV WITH REMAINING MAT ONE YR OR LESS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OTHBFH1L"
            }
        ]
    },
    "OTHBFH1LR": {
        "title": "FHLB ADV WITH REMAINING MAT ONE YR OR LESS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OTHBFH1LR",
                        "numerator": "OTHBFH1L",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OTBFHSTA": {
        "title": "FHLB STRUCTURED ADV",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OTBFHSTA"
            }
        ]
    },
    "OTBFHSTAR": {
        "title": "FHLB STRUCTURED ADV",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OTBFHSTAR",
                        "numerator": "OTBFHSTA",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OTBOT1L": {
        "title": "OTH BORR MAT OR NEXT REPRICING ONE YR OR LESS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OTBOT1L"
            }
        ]
    },
    "OTBOT1LR": {
        "title": "OTH BORR MAT OR NEXT REPRICING ONE YR OR LESS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OTBOT1LR",
                        "numerator": "OTBOT1L",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OTBOT1T3": {
        "title": "OTH BORR MAT OR NEXT REPRICING ONE YR THROUGH THREE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OTBOT1T3"
            }
        ]
    },
    "OTBOT1T3R": {
        "title": "OTH BORR MAT OR NEXT REPRICING ONE YR THROUGH THREE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OTBOT1T3R",
                        "numerator": "OTBOT1T3",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OTBOT3T5": {
        "title": "OTH BORR MAT OR NEXT REPRICING THREE YR THROUGH FIVE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OTBOT3T5"
            }
        ]
    },
    "OTBOT3T5R": {
        "title": "OTH BORR MAT OR NEXT REPRICING THREE YR THROUGH FIVE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OTBOT3T5R",
                        "numerator": "OTBOT3T5",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OTBOTOV5": {
        "title": "OTH BORR MAT OR NEXT REPRICING OVER FIVE YRS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OTBOTOV5"
            }
        ]
    },
    "OTBOTOV5R": {
        "title": "OTH BORR MAT OR NEXT REPRICING OVER FIVE YRS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OTBOTOV5R",
                        "numerator": "OTBOTOV5",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OTHBOT1L": {
        "title": "OTH BORR MAT REMAINING MAT OF ONE YR OR LESS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OTHBOT1L"
            }
        ]
    },
    "OTHBOT1LR": {
        "title": "OTH BORR MAT REMANING MAT OF ONE YR OR LESS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OTHBOT1LR",
                        "numerator": "OTHBOT1L",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "ALLOTHL": {
        "title": "ALL OTHER LIABILITIES",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleAddition",
                    "parameters": {
                        "setField": "ALLOTHL",
                        "additionFields": [
                            "OLMIN",
                            "ACEPT",
                            "LLPFDSTK"
                        ]
                    }
                }
            }
        ]
    },
    "ALLOTHLR": {
        "title": "ALL OTHER LIABILITIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ALLOTHLR",
                        "numerator": "ALLOTHL",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3LNLS": {
        "title": "30-89 DAYS P/D-LOANS & LEASES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3LNLS"
            }
        ]
    },
    "P9LNLS": {
        "title": "90+ DAYS P/D-LOANS & LEASES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9LNLS"
            }
        ]
    },
    "QBPRCOML": {
        "title": "QBP COMMERCIAL BANK REGION",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "QBPRCOML"
            }
        ]
    },
    "QBPRCOMLDESC": {
        "title": "QBP COMMERCIAL BANK REGION DESC",
        "description": "",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "QBPRCOMLDESC"
            }
        ]
    },
    "QBPRSAVB": {
        "title": "QBP BIF FUND SAVINGS REGION",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "QBPRSAVB"
            }
        ]
    },
    "QBPRSAVS": {
        "title": "QBP SAVING SAIF FUND REGION",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "QBPRSAVS"
            }
        ]
    },
    "REGAGNT": {
        "title": "PRIMARY REGULATING AGENCY",
        "description": "",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "REGAGNT"
            }
        ]
    },
    "S10T250B": {
        "title": "ASSETS 10B TO 250B FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "S10T250B"
            }
        ]
    },
    "SB": {
        "title": "SAVINGS BANK FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SB"
            }
        ]
    },
    "SC": {
        "title": "SECURITIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SC"
            }
        ]
    },
    "SCR": {
        "title": "SECURITIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCR",
                        "numerator": "SC",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCAGE": {
        "title": "U.S. AGENCY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCAGE"
            }
        ]
    },
    "SCASPNHA": {
        "title": "U.S. AGENCY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCASPNHA"
            }
        ]
    },
    "SCASPNAF": {
        "title": "U.S. AGENCY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCASPNAF"
            }
        ]
    },
    "SCASPNSUM": {
        "title": "NON-MORT BACKED ISSUES BY US GOVT OR SPONSORED AGENCIES",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleAddition",
                    "parameters": {
                        "setField": "SCASPNSUM",
                        "additionFields": [
                            "SCASPNHA",
                            "SCASPNAF"
                        ]
                    }
                }
            }
        ]
    },
    "SCASPNSUMR": {
        "title": "NON-MORT BACKED ISSUES BY US GOVT OR SPONSORED AGENCIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def SCASPNHA = ctx.SCASPNHA ?: 0;\ndef SCASPNAF = ctx.SCASPNAF ?: 0;\ndef ASSET = ctx.ASSET ?: 0;\nctx.SCASPNSUMR = 0;\nif (ASSET > 0) {\n  ctx.SCASPNSUMR = ((double)(SCASPNHA + SCASPNAF) / ASSET) * 100;\n}\n"
                    }
                }
            }
        ]
    },
    "SCDEQ": {
        "title": "DOMESTIC SEC*DEBT & EQUITY - CON",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCDEQ"
            }
        ]
    },
    "SCDOMO": {
        "title": "OTHER DOMESTIC DEBT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCDOMO"
            }
        ]
    },
    "SCDOMOR": {
        "title": "OTHER DOMESTIC DEBT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCDOMOR",
                        "numerator": "SCDOMO",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCEQ": {
        "title": "EQUITY SECURITIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCEQ"
            }
        ]
    },
    "SCFDEQ": {
        "title": "FOREIGN DEBT & EQUITY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCFDEQ"
            }
        ]
    },
    "SCFORD": {
        "title": "FOREIGN DEBT SECURITIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCFORD"
            }
        ]
    },
    "SCFORDR": {
        "title": "FOREIGN DEBT SECURITIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCFORDR",
                        "numerator": "SCFORD",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCMTGBK": {
        "title": "MORTGAGE BACKED SECURITIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCMTGBK"
            }
        ]
    },
    "SCMTGBKR": {
        "title": "MORTGAGE BACKED SECURITIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCMTGBKR",
                        "numerator": "SCMTGBK",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCMUNI": {
        "title": "MUNICIPAL SECURITIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCMUNI"
            }
        ]
    },
    "SCMUNIR": {
        "title": "MUNICIPAL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCMUNIR",
                        "numerator": "SCMUNI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCMV": {
        "title": "SECURITIES-MV",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCMV"
            }
        ]
    },
    "SCODPC": {
        "title": "RES-OTH DOM DEBT*PRIV CERTS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCODPC"
            }
        ]
    },
    "SCODPCR": {
        "title": "RES-OTH DOM DEBT*PRIV CERTS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCODPCR",
                        "numerator": "SCODPC",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCRES": {
        "title": "CONTRA-ASSETS TO SECURITIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCRES"
            }
        ]
    },
    "SCUS": {
        "title": "U.S. TREASURY & AGENCY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCUS"
            }
        ]
    },
    "SCUSR": {
        "title": "U.S. TREASURY & AGENCY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCUSR",
                        "numerator": "SCUS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCUSA": {
        "title": "U.S. AGENCY ALL OTHER",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCUSA"
            }
        ]
    },
    "SCUST": {
        "title": "U.S. TREASURY SECURITIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCUST"
            }
        ]
    },
    "SCUSTR": {
        "title": "U.S. TREASURY SECURITIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCUSTR",
                        "numerator": "SCUST",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SL": {
        "title": "SAVINGS AND LOAN FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SL"
            }
        ]
    },
    "SM": {
        "title": "STATE MEMBER BANK FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SM"
            }
        ]
    },
    "STALP": {
        "title": "FIPS STATE ALPHA CODE",
        "description": "",
        "type": "string",
        "x-elastic-type": "keyword",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "STALP"
            }
        ]
    },
    "STCHRTR": {
        "title": "STATE CHARTER FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "STCHRTR"
            }
        ]
    },
    "STNAME": {
        "title": "STATE NAME",
        "description": "",
        "type": "string",
        "x-elastic-type": "keyword",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "STNAME"
            }
        ]
    },
    "STNUM": {
        "title": "FIPS STATE NUMBER",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "STNUM"
            }
        ]
    },
    "SUBLLPF": {
        "title": "SUB. DEBT & L/L PREFERRED STK",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SUBLLPF"
            }
        ]
    },
    "SUBND": {
        "title": "SUBORDINATED NOTES & DEBENTURES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SUBND"
            }
        ]
    },
    "SZ25": {
        "title": "ASSETS UNDER 25M FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ25"
            }
        ]
    },
    "SZ100": {
        "title": "ASSETS UNDER 100M FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ100"
            }
        ]
    },
    "SZ100MP": {
        "title": "ASSETS OVER 100M FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ100MP"
            }
        ]
    },
    "SZ100T3": {
        "title": "ASSETS 100M TO 300M FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ100T3"
            }
        ]
    },
    "SZ100T5": {
        "title": "ASSETS 100M TO 500M FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ100T5"
            }
        ]
    },
    "SZ100T1B": {
        "title": "ASSETS 100M TO 1B FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ100T1B"
            }
        ]
    },
    "SZ10BP": {
        "title": "ASSETS OVER 10B FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ10BP"
            }
        ]
    },
    "SZ1BP": {
        "title": "ASSETS OVER 1B FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ1BP"
            }
        ]
    },
    "SZ1BT10B": {
        "title": "ASSETS 1B TO 10B FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ1BT10B"
            }
        ]
    },
    "SZ1BT3B": {
        "title": "ASSETS 1B TO 3B FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ1BT3B"
            }
        ]
    },
    "SZ1BT5B": {
        "title": "ASSETS 1B TO 5B FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ1BT5B"
            }
        ]
    },
    "SZ250BP": {
        "title": "ASSETS OVER 250B FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ250BP"
            }
        ]
    },
    "SZ25T50": {
        "title": "ASSETS 25M TO 50M FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ25T50"
            }
        ]
    },
    "SZ300T5": {
        "title": "ASSETS 300M TO 500M FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ300T5"
            }
        ]
    },
    "SZ3BT10B": {
        "title": "ASSETS 3B TO 10B FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ3BT10B"
            }
        ]
    },
    "SZ500T1B": {
        "title": "ASSETS 500M TO 1B FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ500T1B"
            }
        ]
    },
    "SZ50T100": {
        "title": "ASSETS 50M TO 100M FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ50T100"
            }
        ]
    },
    "SZ5BP": {
        "title": "ASSETS OVER 5B FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ5BP"
            }
        ]
    },
    "TFRA": {
        "title": "TOTAL FIDUCIARY AND RELATED ASSETS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleAddition",
                    "parameters": {
                        "setField": "TFRA",
                        "additionFields": [
                            "TTMA",
                            "TTNMA"
                        ]
                    }
                }
            }
        ]
    },
    "TRADE": {
        "title": "TRADING ACCOUNTS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRADE"
            }
        ]
    },
    "TRADEL": {
        "title": "TRADING LIABILITIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRADEL"
            }
        ]
    },
    "TRADELR": {
        "title": "TRADING LIABILITIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "TRADELR",
                        "numerator": "TRADEL",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "TRADER": {
        "title": "TRADING ACCOUNTS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "TRADER",
                        "numerator": "TRADE",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "TRN": {
        "title": "TRANSACTION-TOTAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRN"
            }
        ]
    },
    "TRNR": {
        "title": "TRANSACTION-TOTAL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "TRNR",
                        "numerator": "TRN",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "TRNIPC": {
        "title": "TRANSACTION-IPC",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRNIPC"
            }
        ]
    },
    "TRNIPCOC": {
        "title": "TRAN-IPC-OFFICIAL CHECKS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRNIPCOC"
            }
        ]
    },
    "TRNIPCOCR": {
        "title": "TRAN-IPC-OFFICIAL CHECKS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "TRNIPCOCR",
                        "numerator": "TRNIPCOC",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "TRNMUNI": {
        "title": "TRANSACTION-MUNI",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRNMUNI"
            }
        ]
    },
    "TRNMUNIR": {
        "title": "TRANSACTION-MUNI RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "TRNMUNIR",
                        "numerator": "TRNMUNI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "TRNUSGOV": {
        "title": "TRANSACTION-U.S. GOVERNMENT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRNUSGOV"
            }
        ]
    },
    "TRNUSGOVR": {
        "title": "TRANSACTION-U.S. GOVERNMENT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "TRNUSGOVR",
                        "numerator": "TRNUSGOV",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "TS": {
        "title": "TIME & SAVINGS DEPOSITS-TOTAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TS"
            }
        ]
    },
    "TSR": {
        "title": "TIME & SAVINGS DEPOSITS-TOTAL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "TSR",
                        "numerator": "TS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "TTL": {
        "title": "TT&L NOTE OPTION",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TTL"
            }
        ]
    },
    "TTLOTBOR": {
        "title": "TT&L & OTHER BORROWINGS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TTLOTBOR"
            }
        ]
    },
    "UNINC": {
        "title": "UNEARNED INCOME",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UNINC"
            }
        ]
    },
    "USA": {
        "title": "USA LOCATED INSTITUTION",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "USA"
            }
        ]
    },
    "UYAMTG": {
        "title": "UNAMORTIZED YIELD ADJ-MTG LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UYAMTG"
            }
        ]
    },
    "ABCUBK": {
        "title": "ASST-BCK UNUSED COMMIT - RELATED",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ABCUBK"
            }
        ]
    },
    "ABCUBKR": {
        "title": "ASST-BCK UNUSED COMMIT - RELATED RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ABCUBKR",
                        "numerator": "ABCUBK",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "ABCUOTH": {
        "title": "ASSET-BACK UNUSED COMMIT - OTHER",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ABCUOTH"
            }
        ]
    },
    "ABCUOTHR": {
        "title": "ASSET-BACK UNUSED COMMIT - OTHER RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ABCUOTHR",
                        "numerator": "ABCUOTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "ABCXBK": {
        "title": "ASSET-BACK CREDIT EX-RELATED",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ABCXBK"
            }
        ]
    },
    "ABCXBKR": {
        "title": "ASSET-BACK CREDIT EX-RELATED RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ABCXBKR",
                        "numerator": "ABCXBK",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "ABCXOTH": {
        "title": "ASSET-BACK CREDIT EX-OTHER",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ABCXOTH"
            }
        ]
    },
    "ABCXOTHR": {
        "title": "ASSET-BACK CREDIT EX-OTHER RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ABCXOTHR",
                        "numerator": "ABCXOTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "ASCEOTH": {
        "title": "C.E. RECOURSE NOT SECUR. - OTH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ASCEOTH"
            }
        ]
    },
    "ASCEOTHR": {
        "title": "C.E. RECOURSE NOT SECUR. - OTH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ASCEOTHR",
                        "numerator": "ASCEOTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "ASCERES": {
        "title": "C.E. RECOURSE NOT SECUR. - RES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ASCERES"
            }
        ]
    },
    "ASCERESR": {
        "title": "C.E. RECOURSE NOT SECUR. - RES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ASCERESR",
                        "numerator": "ASCERES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "ASDROTH": {
        "title": "SOLD W/RECOURSE N/SECUR. - OTH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ASDROTH"
            }
        ]
    },
    "ASDROTHR": {
        "title": "SOLD W/RECOURSE N/SECUR. - OTH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ASDROTHR",
                        "numerator": "ASDROTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "ASDRRES": {
        "title": "SOLD W/RECOURSE N/SECUR.- RES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ASDRRES"
            }
        ]
    },
    "ASDRRESR": {
        "title": "SOLD W/RECOURSE N/SECUR.- RES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ASDRRESR",
                        "numerator": "ASDRRES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "ASSET2": {
        "title": "TOTAL ASSETS-CAVG2",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ASSET2"
            }
        ]
    },
    "ASSET5": {
        "title": "TOTAL ASSETS-CAVG5",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ASSET5"
            }
        ]
    },
    "ASSETFOR": {
        "title": "TOTAL ASSETS-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ASSETFOR"
            }
        ]
    },
    "ASSTLT": {
        "title": "LONG-TERM ASSETS (5+ YEARS)-QBP",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ASSTLT"
            }
        ]
    },
    "ASSTLTR": {
        "title": "LONG-TERM ASSETS (5+ YEARS) RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ASSTLTR",
                        "numerator": "ASSTLT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "ASTEMPM": {
        "title": "ASSETS PER EMPLOYEE IN MILLION",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ASTEMPM"
            }
        ]
    },
    "AVASSETJ": {
        "title": "AVERAGE ASSETS-ADJUSTED-PCA",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "AVASSETJ"
            }
        ]
    },
    "AVASSETJR": {
        "title": "AVERAGE ASSETS-ADJUSTED-PCA RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "AVASSETJR",
                        "numerator": "AVASSETJ",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "BROINS": {
        "title": "BROKERED DEP-INSURED",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "BROINS"
            }
        ]
    },
    "BROINSR": {
        "title": "BROKERED DEP-INSURED RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "BROINSR",
                        "numerator": "BROINS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "CALLYMD": {
        "title": "REPORT DATE (CCYYMMDD)",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CALLYMD"
            }
        ]
    },
    "CHBALFOR": {
        "title": "CASH & DUE FROM DEP INST-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CHBALFOR"
            }
        ]
    },
    "CHBALNI": {
        "title": "NONINTEREST-BEARING CASH & DUE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CHBALNI"
            }
        ]
    },
    "CHBALNIR": {
        "title": "NONINTEREST-BEARING CASH & DUE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "CHBALNIR",
                        "numerator": "CHBALNI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "CHCIC": {
        "title": "CASH ITEMS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CHCIC"
            }
        ]
    },
    "CHCICR": {
        "title": "CASH ITEMS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "CHCICR",
                        "numerator": "CHCIC",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "CHCOIN": {
        "title": "CURRENCY & COIN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CHCOIN"
            }
        ]
    },
    "CHCOINR": {
        "title": "CURRENCY & COIN RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "CHCOINR",
                        "numerator": "CHCOIN",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "CHFLA": {
        "title": "NET OPERATING CASH FLOW-ANN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CHFLA"
            }
        ]
    },
    "CHFLQ": {
        "title": "NET OPERATING CASH FLOW-ANN Quarterly",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CHFLQ"
            }
        ]
    },
    "CHFRB": {
        "title": "BAL DUE FROM FRB",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CHFRB"
            }
        ]
    },
    "CHFRBR": {
        "title": "BAL DUE FROM FRB RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "CHFRBR",
                        "numerator": "CHFRB",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "CHITEM": {
        "title": "CASH ITEM COLLEC IN DOMESTIC OFFICES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CHITEM"
            }
        ]
    },
    "CHITEMR": {
        "title": "CASH ITEMS COLLEC IN DOMESTIC OFFICES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "CHITEMR",
                        "numerator": "CHITEM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "CHNUS": {
        "title": "BAL DUE FROM BK FOR COUNTRY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CHNUS"
            }
        ]
    },
    "CHNUSR": {
        "title": "BAL DUE FROM BK FOR COUNTRY RATIOS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "CHNUSR",
                        "numerator": "CHNUS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "CHNUSFBK": {
        "title": "BAL DUE FROM FOR BR OF OTH US BK",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CHNUSFBK"
            }
        ]
    },
    "CHUS": {
        "title": "BAL DUE FROM DEP INST U.S.",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CHUS"
            }
        ]
    },
    "CHUSR": {
        "title": "BAL DUE FROM DEP INST U.S. RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "CHUSR",
                        "numerator": "CHUS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "CHUSFBK": {
        "title": "BAL DUE FROM U.S. BR OF FOR BKS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CHUSFBK"
            }
        ]
    },
    "CITY": {
        "title": "CITY",
        "description": "",
        "type": "string",
        "x-elastic-type": "keyword",
        "x-elastic-analyzer": [
            {
                "variable": "autocomplete",
                "analyzer": "autocomplete_analyzer"
            }
        ],
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CITY"
            }
        ]
    },
    "COREDEP": {
        "title": "CORE DEPOSITS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "COREDEP"
            }
        ]
    },
    "COREDEPR": {
        "title": "CORE DEPOSITS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "COREDEPR",
                        "numerator": "COREDEP",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "CRAG": {
        "title": "AGRICULTURAL LOAN RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRAG"
            }
        ]
    },
    "CRAGR": {
        "title": "AGRICULTURAL LOAN RECOVERIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "GRAGR",
                        "numerator": "CRAG",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRAGQ": {
        "title": "AGRICULTURAL LOAN RECOVERIES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRAGQ"
            }
        ]
    },
    "CRAGQR": {
        "title": "AGRICULTURAL LOAN RECOVERIES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRAGQR",
                        "numerator": "CRAGQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRAGSM": {
        "title": "AG LOAN RECOVERIES*SMALL BKS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRAGSM"
            }
        ]
    },
    "CRAGSMR": {
        "title": "AAG LOAN RECOVERIES*SMALL BKS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRAGSMR",
                        "numerator": "CRAGSM",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRAGSMQ": {
        "title": "AG LOAN RECOVERIES*SMALL BKS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRAGSMQ"
            }
        ]
    },
    "CRAGSMQR": {
        "title": "AG LOAN RECOVERIES*SMALL BKS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRAGSMQR",
                        "numerator": "CRAGSMQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRAUTO": {
        "title": "AUTO LOANS - RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRAUTO"
            }
        ]
    },
    "CRAUTOR": {
        "title": "AUTO LOANS - RECOVERIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRAUTOR",
                        "numerator": "CRAUTO",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRAUTOQ": {
        "title": "AUTO LOANS - RECOVERIES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRAUTOQ"
            }
        ]
    },
    "CRAUTOQR": {
        "title": "AUTO LOANS - RECOVERIES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRAUTOQR",
                        "numerator": "CRAUTOQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRCI": {
        "title": "COMMERCIAL LOAN RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRCI"
            }
        ]
    },
    "CRCIR": {
        "title": "COMMERCIAL LOAN RECOVERIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRCIR",
                        "numerator": "CRCI",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRCIQ": {
        "title": "COMMERCIAL LOAN RECOVERIES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRCIQ"
            }
        ]
    },
    "CRCIQR": {
        "title": "COMMERCIAL LOAN RECOVERIES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRCIQR",
                        "numerator": "CRCIQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRCINUS": {
        "title": "COMMERCIAL LOAN RECOVERIES NON-U.S.",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRCINUS"
            }
        ]
    },
    "CRCINUSR": {
        "title": "COMMERCIAL LOAN RECOVERIES NON-U.S. RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRCINUSR",
                        "numerator": "CRCINUS",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRCINUSQ": {
        "title": "COMMERCIAL LOAN RECOVERIES NON-U.S. QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRCINUSQ"
            }
        ]
    },
    "CRCINUSQR": {
        "title": "COMMERCIAL LOAN RECOVERIES NON-U.S. QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRCINUSQR",
                        "numerator": "CRCINUSQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRCON": {
        "title": "CONSUMER LOAN RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRCON"
            }
        ]
    },
    "CRCONR": {
        "title": "CONSUMER LOAN RECOVERIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRCONR",
                        "numerator": "CRCON",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRCONQ": {
        "title": "CONSUMER LOAN RECOVERIES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRCONQ"
            }
        ]
    },
    "CRCONQR": {
        "title": "CONSUMER LOAN RECOVERIES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRCONQR",
                        "numerator": "CRCONQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRCONOTH": {
        "title": "OTHER CONSUMER LOAN RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRCONOTH"
            }
        ]
    },
    "CRCONOTHR": {
        "title": "OTHER CONSUMER LOAN RECOVERIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRCONOTHR",
                        "numerator": "CRCONOTH",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRCONOTQ": {
        "title": "OTHER CONSUMER LOAN RECOVERIES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRCONOTQ"
            }
        ]
    },
    "CRCONOTQR": {
        "title": "OTHER CONSUMER LOAN RECOVERIES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRCONOTQR",
                        "numerator": "CRCONOTQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRCRCD": {
        "title": "CREDIT CARD LOAN RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRCRCD"
            }
        ]
    },
    "CRCRCDR": {
        "title": "CREDIT CARD LOAN RECOVERIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRCRCDR",
                        "numerator": "CRCRCD",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRCRCDQ": {
        "title": "CREDIT CARD LOAN RECOVERIES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRCRCDQ"
            }
        ]
    },
    "CRCRCDQR": {
        "title": "CREDIT CARD LOAN RECOVERIES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRCRCDQR",
                        "numerator": "CRCRCDQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRDEP": {
        "title": "DEPOSITORY INST LOAN RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRDEP"
            }
        ]
    },
    "CRDEPR": {
        "title": "DEPOSITORY INST LOAN RECOVERIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRDEPR",
                        "numerator": "CRDEP",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRDEPQ": {
        "title": "DEPOSITORY INST LOAN RECOVERIES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRDEPQ"
            }
        ]
    },
    "CRDEPQR": {
        "title": "DEPOSITORY INST LOAN RECOVERIES Quarterly RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRDEPQR",
                        "numerator": "CRDEPQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRDEPNUS": {
        "title": "FOREIGN DEPS INST LN RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRDEPNUS"
            }
        ]
    },
    "CRDEPNUSR": {
        "title": "FOREIGN DEPS INST LN RECOVERIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRDEPNUSR",
                        "numerator": "CRDEPNUS",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRDEPNUQ": {
        "title": "FOREIGN DEPS INST LN RECOVERIES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRDEPNUQ"
            }
        ]
    },
    "CRDEPNUQR": {
        "title": "FOREIGN DEPS INST LN RECOVERIES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRDEPNUQR",
                        "numerator": "CRDEPNUQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRFORGV": {
        "title": "FOREIGN GOVERNMENT LN RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRFORGV"
            }
        ]
    },
    "CRFORGVR": {
        "title": "FOREIGN GOVERNMENT LN RECOVERIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRFORGVR",
                        "numerator": "CRFORGV",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRFORGVQ": {
        "title": "FOREIGN GOVERNMENT LN RECOVERIES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRFORGVQ"
            }
        ]
    },
    "CRFORGVQR": {
        "title": "FOREIGN GOVERNMENT LN RECOVERIES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRFORGVQR",
                        "numerator": "CRFORGVQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRLS": {
        "title": "LEASE RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRLS"
            }
        ]
    },
    "CRLSR": {
        "title": "LEASE RECOVERIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRLSR",
                        "numerator": "CRLS",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRLSQ": {
        "title": "LEASE RECOVERIES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRLSQ"
            }
        ]
    },
    "CRLSQR": {
        "title": "LEASE RECOVERIES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRLSQR",
                        "numerator": "CRLSQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CROTHER": {
        "title": "ALL OTHER LOAN RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CROTHER"
            }
        ]
    },
    "CROTHERR": {
        "title": "ALL OTHER LOAN RECOVERIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CROTHERR",
                        "numerator": "CROTHER",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CROTHQ": {
        "title": "ALL OTHER LOAN RECOVERIES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CROTHQ"
            }
        ]
    },
    "CROTHQR": {
        "title": "ALL OTHER LOAN RECOVERIES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CROTHQR",
                        "numerator": "CROTHQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRRE": {
        "title": "REAL ESTATE LOAN RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRRE"
            }
        ]
    },
    "CRRER": {
        "title": "REAL ESTATE LOAN RECOVERIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRRER",
                        "numerator": "CRRE",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRREQ": {
        "title": "REAL ESTATE LOAN RECOVERIES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRREQ"
            }
        ]
    },
    "CRREQR": {
        "title": "REAL ESTATE LOAN RECOVERIES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRREQR",
                        "numerator": "CRREQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRREAG": {
        "title": "FARMLAND RE LN RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRREAG"
            }
        ]
    },
    "CRREAGR": {
        "title": "FARMLAND RE LN RECOVERIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRREAGR",
                        "numerator": "CRREAG",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRREAGQ": {
        "title": "FARMLAND RE LN RECOVERIES-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRREAGQ"
            }
        ]
    },
    "CRREAGQR": {
        "title": "FARMLAND RE LN RECOVERIES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRREAGQR",
                        "numerator": "CRREAGQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRRECNFM": {
        "title": "1-4 FAM CONSTRUCT LN RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRRECNFM"
            }
        ]
    },
    "CRRECNOT": {
        "title": "OTHER CONSTRUCT LN RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRRECNOT"
            }
        ]
    },
    "CRRECONQ": {
        "title": "CONSTRUCTION RE LN RECOVER-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRRECONQ"
            }
        ]
    },
    "CRRECONQR": {
        "title": "CONSTRUCTION RE LN RECOVERIES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRRECONQR",
                        "numerator": "CRRECONQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRRECONS": {
        "title": "CONSTRUCTION RE LN RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRRECONS"
            }
        ]
    },
    "CRRECONSR": {
        "title": "CONSTRUCTION RE LN RECOVERIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRRECONSR",
                        "numerator": "CRRECONS",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRREFOR": {
        "title": "REAL ESTATE LN RECOVERIES - FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRREFOR"
            }
        ]
    },
    "CRREFORR": {
        "title": "REAL ESTATE LN RECOVERIES - FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRREFORR",
                        "numerator": "CRREFOR",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRREFORQ": {
        "title": "REAL ESTATE LN RECOVERIES - FOR QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRREFORQ"
            }
        ]
    },
    "CRREFORQR": {
        "title": "REAL ESTATE LN RECOVERIES - FOR QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRREFORQR",
                        "numerator": "CRREFORQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRRELOC": {
        "title": "LINE OF CREDIT RE LN RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRRELOC"
            }
        ]
    },
    "CRRELOCR": {
        "title": "LINE OF CREDIT RE LN RECOVERIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRRELOCR",
                        "numerator": "CRRELOC",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRRELOCQ": {
        "title": "LINE OF CREDIT RE LN RECOVERIES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRRELOCQ"
            }
        ]
    },
    "CRRELOCQR": {
        "title": "LINE OF CREDIT RE LN RECOVERIES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRRELOCQR",
                        "numerator": "CRRELOCQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRREMULQ": {
        "title": "MULTIFAMILY RE LN RECOVERIES-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRREMULQ"
            }
        ]
    },
    "CRREMULQR": {
        "title": "MULTIFAMILY RES RE LN RECOVERIES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRREMULQR",
                        "numerator": "CRREMULQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRREMULT": {
        "title": "MULTIFAMILY RES RE LN RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRREMULT"
            }
        ]
    },
    "CRREMULTR": {
        "title": "MULTIFAMILY RES RE LN RECOVERIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRREMULTR",
                        "numerator": "CRREMULT",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRRENRES": {
        "title": "NONFARM NONRES RE LN RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRRENRES"
            }
        ]
    },
    "CRRENRESR": {
        "title": "NONFARM NONRES RE LN RECOVERIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRRENRESR",
                        "numerator": "CRRENRES",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRRENROT": {
        "title": "OTHER NONFARM NONRES RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRRENROT"
            }
        ]
    },
    "CRRENROW": {
        "title": "OWN-OCCUP NONFARM NONRES RECOV",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRRENROW"
            }
        ]
    },
    "CRRENRSQ": {
        "title": "NONFARM NONRES RE LN RECOVER-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRRENRSQ"
            }
        ]
    },
    "CRRENRSQR": {
        "title": "NONFARM NONRES RE LN RECOVER-QTR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRRENRSQR",
                        "numerator": "CRRENRSQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRRENUS": {
        "title": "NON-U.S. RE LN RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRRENUS"
            }
        ]
    },
    "CRRENUSR": {
        "title": "NON-U.S. RE LN RECOVERIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRRENUSR",
                        "numerator": "CRRENUS",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRRENUSQ": {
        "title": "NON-U.S. RE LN RECOVERIES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRRENUSQ"
            }
        ]
    },
    "CRRENUSQR": {
        "title": "NON-U.S. RE LN RECOVERIES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRRENUSQR",
                        "numerator": "CRRENUSQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRRERES": {
        "title": "RE LOANS 1-4 FAMILY RECOVERIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRRERES"
            }
        ]
    },
    "CRRERESR": {
        "title": "RE LOANS 1-4 FAMILY RECOVERIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRRERESR",
                        "numerator": "CRRERES",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRRERESQ": {
        "title": "RE LOANS 1-4 FAMILY RECOVER-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRRERESQ"
            }
        ]
    },
    "CRRERESQR": {
        "title": "RE LOANS 1-4 FAMILY RECOVERIES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRRERESQR",
                        "numerator": "CRRERESQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRRERSF2": {
        "title": "RE LOAN 1-4 FAM JR LIEN-RECOVER",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRRERSF2"
            }
        ]
    },
    "CRRERSF2R": {
        "title": "RE LOAN 1-4 FAM JR LIEN-RECOVER RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRRERSF2R",
                        "numerator": "CRRERSF2",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRRERS2Q": {
        "title": "RE LOAN 1-4 FAM JR LIEN-RECOVER QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRRERS2Q"
            }
        ]
    },
    "CRRERS2QR": {
        "title": "RE LOAN 1-4 FAM JR LIEN-RECOVER QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRRERS2QR",
                        "numerator": "CRRERS2Q",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRRERSFM": {
        "title": "RE LOAN 1-4 FAM FIRST LIEN-RECOV",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRRERSFM"
            }
        ]
    },
    "CRRERSFMR": {
        "title": "RE LOAN 1-4 FAM FIRST LIEN-RECOV RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRRERSFMR",
                        "numerator": "CRRERSFM",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRRERSFQ": {
        "title": "RE LOAN 1-4 FAM FIRST LIEN-RECOV QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CRRERSFQ"
            }
        ]
    },
    "CRRERSFQR": {
        "title": "RE LOAN 1-4 FAM FIRST LIEN-RECOV QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRRERSFQR",
                        "numerator": "CRRERSFQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CRREOFFDOM": {
        "title": "RE LOAN RECOVERIES DOMESTIC OFFICES",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleAddition",
                    "parameters": {
                        "setField": "CRREOFFDOM",
                        "additionFields": [
                            "CRRECONS",
                            "CRREAG",
                            "CRRERES",
                            "CRREMULT",
                            "CRRENRES"
                        ]
                    }
                }
            }
        ]
    },
    "CRREOFFDOMR": {
        "title": "RE LOAN RECOVERIES DOMESTIC OFFICES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "CRREOFFDOMR",
                        "numerator": "CRREOFFDOM",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "CRREOFFDOMQ": {
        "title": "RE LOAN RECOVERIES DOMESTIC OFFICES QUARTERLY",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleAddition",
                    "parameters": {
                        "setField": "CRREOFFDOMQ",
                        "additionFields": [
                            "CRRECONQ",
                            "CRREAGQ",
                            "CRRERESQ",
                            "CRREMULQ",
                            "CRRENRSQ"
                        ]
                    }
                }
            }
        ]
    },
    "CRREOFFDOMQR": {
        "title": "RE LOAN RECOVERIES DOMESTIC OFFICES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "CRREOFFDOMQR",
                        "numerator": "CRREOFFDOMQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "CTDERBEN": {
        "title": "CR DER (NET)-PURCHASE PROTECT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CTDERBEN"
            }
        ]
    },
    "CTDERBENR": {
        "title": "CR DER (NET)-PURCHASE PROTECT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "CTDERBENR",
                        "numerator": "CTDERBEN",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "CTDERGTY": {
        "title": "CR DER(NET) - SOLD PROTECTION",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CTDERGTY"
            }
        ]
    },
    "CTDERGTYR": {
        "title": "CR DER(NET) - SOLD PROTECTION RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "CTDERGTYR",
                        "numerator": "CTDERGTY",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DEPBEFEX": {
        "title": "TOTAL DEPOSIT LIAB BEF EXCLUSION",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPBEFEX"
            }
        ]
    },
    "DEPCSBQ": {
        "title": "ESTIMATED ASSESSABLE DEPOSITS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPCSBQ"
            }
        ]
    },
    "DEPCSBQR": {
        "title": "ESTIMATED ASSESSABLE DEPOSITS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "DEPCSBQR",
                        "numerator": "DEPCSBQ",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DEPDASTR": {
        "title": "TOT DOMESTIC DEPOSIT / ASSET",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPDASTR"
            }
        ]
    },
    "DEPDASQR": {
        "title": "TOT DOMESTIC DEPOSIT / ASSET QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleDivision",
                    "parameters": {
                        "setField": "DEPDASQR",
                        "numerator": "DEPDOM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DEPFBKF": {
        "title": "FOREIGN BANKS-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPFBKF"
            }
        ]
    },
    "DEPFBKFR": {
        "title": "FOREIGN BANKS-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "DEPFBKFR",
                        "numerator": "DEPFBKF",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DEPFGOVF": {
        "title": "FOREIGN GOVERNMENTS-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPFGOVF"
            }
        ]
    },
    "DEPFGOVFR": {
        "title": "FOREIGN GOVERNMENTS-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "DEPFGOVFR",
                        "numerator": "DEPFGOVF",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DEPIDOM": {
        "title": "INTEREST-BEARING DEP-DOM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPIDOM"
            }
        ]
    },
    "DEPIDOMR": {
        "title": "INTEREST-BEARING DEP-DOM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "DEPIDOMR",
                        "numerator": "DEPIDOM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DEPINS": {
        "title": "ESTIMATED INSURED DEPOSITS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPINS"
            }
        ]
    },
    "DEPINSR": {
        "title": "ESTIMATED INSURED DEPOSITS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "DEPINSR",
                        "numerator": "DEPINS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DEPLGAMT": {
        "title": "AMT DEP ACC GREATER THAN $250,000",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPLGAMT"
            }
        ]
    },
    "DEPLGAMTR": {
        "title": "AMT DEP ACC GREATER THAN $250,000 RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "DEPLGAMTR",
                        "numerator": "DEPLGAMT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DEPLGB": {
        "title": "NUM DEP ACC GREATER THAN $250,000",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPLGB"
            }
        ]
    },
    "DEPLGRA": {
        "title": "AMT OF RETIREMENT DEP ACC OF MORE THAN $250,000",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPLGRA"
            }
        ]
    },
    "DEPLGRAR": {
        "title": "AMT OF RETIREMENT DEP ACC OF MORE THAN $250,000 RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "DEPLGRAR",
                        "numerator": "DEPLGRA",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DEPLGRN": {
        "title": "NUM OF RETIREMENT DEP ACC MORE THAN $250,000",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPLGRN"
            }
        ]
    },
    "DEPLSNB": {
        "title": "DEP THRU LIST SVC NOT BROKERED",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPLSNB"
            }
        ]
    },
    "DEPLSNBR": {
        "title": "DEP THRU LIST SVC NOT BROKERED RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "DEPLSNBR",
                        "numerator": "DEPLSNB",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DEPNIDOM": {
        "title": "NONINTEREST-BEARING DEP-DOM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPNIDOM"
            }
        ]
    },
    "DEPNIDOMR": {
        "title": "NONINTEREST-BEARING DEP-DOM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "DEPNIDOMR",
                        "numerator": "DEPNIDOM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DEPSMAMT": {
        "title": "AMT DEP ACC AT $250,000 OR LESS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPSMAMT"
            }
        ]
    },
    "DEPSMAMTR": {
        "title": "AMT DEP ACC AT $250,000 OR LESS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "DEPSMAMTR",
                        "numerator": "DEPSMAMT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DEPSMB": {
        "title": "NUM DEP ACC EQUAL OR LESS THAN EQUAL TO $250,000",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPSMB"
            }
        ]
    },
    "DEPSMRA": {
        "title": "AMT RETIREMENT DEP ACC OF $250,000 OR LESS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPSMRA"
            }
        ]
    },
    "DEPSMRAR": {
        "title": "AMT RETIREMENT DEP ACC OF $250,000 OR LESS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "DEPSMRAR",
                        "numerator": "DEPSMRA",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DEPSMRN": {
        "title": "NUM RETIREMENT DEP ACC OF $250,000",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPSMRN"
            }
        ]
    },
    "DEPUNA": {
        "title": "EST UNINSURED DEP IN DOM-OFF IN INSURED BRANCHES IN US TERR AND POSSESSIONS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPUNA"
            }
        ]
    },
    "DEPUNAR": {
        "title": "EST UNINSURED DEP IN DOM-OFF IN INSURED BRANCHES IN US TERR AND POSSESSIONS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "DEPUNAR",
                        "numerator": "DEPUNA",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DEPUSBKF": {
        "title": "U.S. BANKS&OTH.US INST-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPUSBKF"
            }
        ]
    },
    "DEPUSBKFR": {
        "title": "U.S. BANKS&OTH.US INST-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "DEPUSBKFR",
                        "numerator": "DEPUSBKF",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DEPUSMF": {
        "title": "U.S.GOVT & ST & POL SUBS-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DEPUSMF"
            }
        ]
    },
    "DEPUSMFR": {
        "title": "U.S.GOVT & ST & POL SUBS-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "DEPUSMFR",
                        "numerator": "DEPUSMF",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "DRAG": {
        "title": "AGRICULTURAL LOAN CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRAG"
            }
        ]
    },
    "DRAGR": {
        "title": "AGRICULTURAL LOAN CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRAGR",
                        "numerator": "DRAG",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRAGQ": {
        "title": "AGRICULTURAL LOAN CHARGE-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRAGQ"
            }
        ]
    },
    "DRAGQR": {
        "title": "AGRICULTURAL LOAN CHARGE-OFFS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRAGQR",
                        "numerator": "DRAGQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRAGSM": {
        "title": "AG LOAN CHARGE-OFFS*SMALL BKS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRAGSM"
            }
        ]
    },
    "DRAGSMR": {
        "title": "AG LOAN CHARGE-OFFS*SMALL BKS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRAGSMR",
                        "numerator": "DRAGSM",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRAGSMQ": {
        "title": "AG LOAN CHARGE-OFFS*SMALL BKS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRAGSMQ"
            }
        ]
    },
    "DRAGSMQR": {
        "title": "AG LOAN CHARGE-OFFS*SMALL BKS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRAGSMQR",
                        "numerator": "DRAGSMQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRAUTO": {
        "title": "AUTO LOANS - CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRAUTO"
            }
        ]
    },
    "DRAUTOR": {
        "title": "AUTO LOANS - CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRAUTOR",
                        "numerator": "DRAUTO",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRAUTOQ": {
        "title": "AUTO LOANS - CHARGE-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRAUTOQ"
            }
        ]
    },
    "DRAUTOQR": {
        "title": "AUTO LOANS - CHARGE-OFFS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRAUTOQR",
                        "numerator": "DRAUTOQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRCI": {
        "title": "COMMERCIAL LOAN CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRCI"
            }
        ]
    },
    "DRCIR": {
        "title": "COMMERCIAL LOAN CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRCIR",
                        "numerator": "DRCI",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRCIQ": {
        "title": "COMMERCIAL LOAN CHARGE-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRCIQ"
            }
        ]
    },
    "DRCIQR": {
        "title": "COMMERCIAL LOAN CHARGE-OFFS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRCIQR",
                        "numerator": "DRCIQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRCINUS": {
        "title": "COMMERCIAL LOAN CHARGE-OFFS NON-U.S.",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRCINUS"
            }
        ]
    },
    "DRCINUSR": {
        "title": "COMMERCIAL LOAN CHARGE-OFFS NON-U.S. RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRCINUSR",
                        "numerator": "DRCINUS",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRCINUSQ": {
        "title": "COMMERCIAL LOAN CHARGE-OFFS NON-U.S. QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRCINUSQ"
            }
        ]
    },
    "DRCINUSQR": {
        "title": "COMMERCIAL LOAN CHARGE-OFFS NON-U.S. QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRCINUSQR",
                        "numerator": "DRCINUSQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRCON": {
        "title": "CONSUMER LOAN CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRCON"
            }
        ]
    },
    "DRCONR": {
        "title": "CONSUMER LOAN CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRCONR",
                        "numerator": "DRCON",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRCONQ": {
        "title": "CONSUMER LOAN CHARGE-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRCONQ"
            }
        ]
    },
    "DRCONQR": {
        "title": "CONSUMER LOAN CHARGE-OFFS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRCONQR",
                        "numerator": "DRCONQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRCONOTH": {
        "title": "OTHER CONSUMER LOAN CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRCONOTH"
            }
        ]
    },
    "DRCONOTHR": {
        "title": "OTHER CONSUMER LOAN CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRCONOTHR",
                        "numerator": "DRCONOTH",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRCONOTQ": {
        "title": "OTHER CONSUMER LOAN CHARGE-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRCONOTQ"
            }
        ]
    },
    "DRCONOTQR": {
        "title": "OTHER CONSUMER LOAN CHARGE-OFFS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRCONOTQR",
                        "numerator": "DRCONOTQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRCRCD": {
        "title": "CREDIT CARD LOAN CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRCRCD"
            }
        ]
    },
    "DRCRCDR": {
        "title": "CREDIT CARD LOAN CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRCRCDR",
                        "numerator": "DRCRCD",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRCRCDQ": {
        "title": "CREDIT CARD LOAN CHARGE-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRCRCDQ"
            }
        ]
    },
    "DRCRCDQR": {
        "title": "CREDIT CARD LOAN CHARGE-OFFS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRCRCDQR",
                        "numerator": "DRCRCDQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRDEP": {
        "title": "DEPOSITORY INST LOAN CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRDEP"
            }
        ]
    },
    "DRDEPR": {
        "title": "DEPOSITORY INST LOAN CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRDEPR",
                        "numerator": "DRDEP",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRDEPQ": {
        "title": "DEPOSITORY INST LOAN CHARGE-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRDEPQ"
            }
        ]
    },
    "DRDEPQR": {
        "title": "DEPOSITORY INST LOAN CHARGE-OFFS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRDEPQR",
                        "numerator": "DRDEPQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRDEPNUS": {
        "title": "FOREIGN DEPS INST LN CHG-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRDEPNUS"
            }
        ]
    },
    "DRDEPNUSR": {
        "title": "FOREIGN DEPS INST LN CHG-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRDEPNUSR",
                        "numerator": "DRDEPNUS",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRDEPNUQ": {
        "title": "FOREIGN DEPS INST LN CHG-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRDEPNUQ"
            }
        ]
    },
    "DRDEPNUQR": {
        "title": "FOREIGN DEPS INST LN CHG-OFFS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRDEPNUQR",
                        "numerator": "DRDEPNUQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRFORGV": {
        "title": "FOREIGN GOVERNMENT LN CHG-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRFORGV"
            }
        ]
    },
    "DRFORGVR": {
        "title": "FOREIGN GOVERNMENT LN CHG-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRFORGVR",
                        "numerator": "DRFORGV",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRFORGVQ": {
        "title": "FOREIGN GOVERNMENT LN CHG-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRFORGVQ"
            }
        ]
    },
    "DRFORGVQR": {
        "title": "FOREIGN GOVERNMENT LN CHG-OFFS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRFORGVQR",
                        "numerator": "DRFORGVQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRLS": {
        "title": "LEASE CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRLS"
            }
        ]
    },
    "DRLSR": {
        "title": "LEASE CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRLSR",
                        "numerator": "DRLS",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRLSQ": {
        "title": "LEASE CHARGE-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRLSQ"
            }
        ]
    },
    "DRLSQR": {
        "title": "LEASE CHARGE-OFFS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRLSQR",
                        "numerator": "DRLSQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DROTHER": {
        "title": "ALL OTHER LOAN CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DROTHER"
            }
        ]
    },
    "DROTHERR": {
        "title": "ALL OTHER LOAN CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DROTHERR",
                        "numerator": "DROTHER",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DROTHQ": {
        "title": "ALL OTHER LOAN CHARGE-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DROTHQ"
            }
        ]
    },
    "DROTHQR": {
        "title": "ALL OTHER LOAN CHARGE-OFFS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DROTHQR",
                        "numerator": "DROTHQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRRE": {
        "title": "REAL ESTATE LOAN CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRRE"
            }
        ]
    },
    "DRRER": {
        "title": "REAL ESTATE LOAN CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRRER",
                        "numerator": "DRRE",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRREQ": {
        "title": "REAL ESTATE LOAN CHARGE-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRREQ"
            }
        ]
    },
    "DRREQR": {
        "title": "REAL ESTATE LOAN CHARGE-OFFS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRREQR",
                        "numerator": "DRREQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRREAG": {
        "title": "FARMLAND RE LN CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRREAG"
            }
        ]
    },
    "DRREAGR": {
        "title": "FARMLAND RE LN CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRREAGR",
                        "numerator": "DRREAG",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRREAGQ": {
        "title": "FARMLAND RE LN CHG-OFFS-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRREAGQ"
            }
        ]
    },
    "DRREAGQR": {
        "title": "FARMLAND RE LN CHARGE-OFFS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRREAGQR",
                        "numerator": "DRREAGQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRRECNFM": {
        "title": "1-4 FAM CONSTRUCT LN CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRRECNFM"
            }
        ]
    },
    "DRRECNOT": {
        "title": "OTHER CONSTRUCT LN CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRRECNOT"
            }
        ]
    },
    "DRRECONQ": {
        "title": "CONSTRUCTION RE LN CHG-OFFS-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRRECONQ"
            }
        ]
    },
    "DRRECONQR": {
        "title": "CONSTRUCTION RE LN CHARGE-OFFS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRRECONQR",
                        "numerator": "DRRECONQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRRECONS": {
        "title": "CONSTRUCTION RE LN CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRRECONS"
            }
        ]
    },
    "DRRECONSR": {
        "title": "CONSTRUCTION RE LN CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRRECONSR",
                        "numerator": "DRRECONS",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRREFOR": {
        "title": "REAL ESTATE LOAN CHRG-OFFS-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRREFOR"
            }
        ]
    },
    "DRREFORR": {
        "title": "REAL ESTATE LOAN CHRG-OFFS-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRREFORR",
                        "numerator": "DRREFOR",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRREFORQ": {
        "title": "REAL ESTATE LOAN CHRG-OFFS-FOR QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRREFORQ"
            }
        ]
    },
    "DRREFORQR": {
        "title": "REAL ESTATE LOAN CHRG-OFFS-FOR QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRREFORQR",
                        "numerator": "DRREFORQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRRELOC": {
        "title": "LINE OF CREDIT RE LN CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRRELOC"
            }
        ]
    },
    "DRRELOCR": {
        "title": "LINE OF CREDIT RE LN CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRRELOCR",
                        "numerator": "DRRELOC",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRRELOCQ": {
        "title": "LINE OF CREDIT RE LN CHARGE-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRRELOCQ"
            }
        ]
    },
    "DRRELOCQR": {
        "title": "LINE OF CREDIT RE LN CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRRELOCQR",
                        "numerator": "DRRELOCQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRREMULQ": {
        "title": "MULTIFAMILY RE LN CHG-OFFS-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRREMULQ"
            }
        ]
    },
    "DRREMULQR": {
        "title": "MULTIFAMILY RES RE LN CHARGE-OFF QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRREMULQR",
                        "numerator": "DRREMULQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRREMULT": {
        "title": "MULTIFAMILY RES RE LN CHARGE-OFF",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRREMULT"
            }
        ]
    },
    "DRREMULTR": {
        "title": "MULTIFAMILY RES RE LN CHARGE-OFF RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRREMULTR",
                        "numerator": "DRREMULT",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRRENRES": {
        "title": "NONFARM NONRES RE LN CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRRENRES"
            }
        ]
    },
    "DRRENRESR": {
        "title": "NONFARM NONRES RE LN CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRRENRESR",
                        "numerator": "DRRENRES",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRRENROT": {
        "title": "OTHER NONFARM NONRES RE CHG-OFF",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRRENROT"
            }
        ]
    },
    "DRRENROW": {
        "title": "OWN-OCCUP NONFARM NONRES CHG-OFF",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRRENROW"
            }
        ]
    },
    "DRRENRSQ": {
        "title": "NONFARM NONRES RE LN CHG-OFF-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRRENRSQ"
            }
        ]
    },
    "DRRENRSQR": {
        "title": "NONFARM NONRES RE LN CHARGE-OFFS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRRENRSQR",
                        "numerator": "DRRENRSQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRRENUS": {
        "title": "NON-U.S. RE LN CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRRENUS"
            }
        ]
    },
    "DRRENUSR": {
        "title": "NON-U.S. RE LN CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRRENUSR",
                        "numerator": "DRRENUS",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRRENUSQ": {
        "title": "NON-U.S. RE LN CHARGE-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRRENUSQ"
            }
        ]
    },
    "DRRENUSQR": {
        "title": "NON-U.S. RE LN CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRRENUSQR",
                        "numerator": "DRRENUSQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRRERES": {
        "title": "RE LOANS 1-4 FAMILY CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRRERES"
            }
        ]
    },
    "DRRERESR": {
        "title": "RE LOANS 1-4 FAMILY CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRRERESR",
                        "numerator": "DRRERES",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRRERESQ": {
        "title": "RE LOANS 1-4 FAMILY CHG-OFFS-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRRERESQ"
            },
            {
                "file": "RISVIEW",
                "field": "DRRERESQ"
            }
        ]
    },
    "DRRERESQR": {
        "title": "RE LOANS 1-4 FAMILY CHARGE-OFFS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRRERESQR",
                        "numerator": "DRRERESQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRRERSF2": {
        "title": "RE LN 1-4 FAM JR LIEN-CHG-OFF",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRRERSF2"
            }
        ]
    },
    "DRRERSF2R": {
        "title": "RE LN 1-4 FAM JR LIEN-CHG-OFF RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRRERSF2R",
                        "numerator": "DRRERSF2",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRRERS2Q": {
        "title": "RE LN 1-4 FAM JR LIEN-CHG-OFF QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRRERS2Q"
            }
        ]
    },
    "DRRERS2QR": {
        "title": "RE LN 1-4 FAM JR LIEN-CHG-OFF QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRRERS2QR",
                        "numerator": "DRRERS2Q",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRRERSFM": {
        "title": "RE LN 1-4 FAM FIRST LIEN-CHG-OFF",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRRERSFM"
            }
        ]
    },
    "DRRERSFMR": {
        "title": "RE LN 1-4 FAM FIRST LIEN-CHG-OFF RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRRERSFMR",
                        "numerator": "DRRERSFM",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRRERSFQ": {
        "title": "RE LN 1-4 FAM FIRST LIEN-CHG-OFF QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "DRRERSFQ"
            }
        ]
    },
    "DRRERSFQR": {
        "title": "RE LN 1-4 FAM FIRST LIEN-CHG-OFF QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRRERSFQR",
                        "numerator": "DRRERSFQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "DRREOFFDOM": {
        "title": "REAL ESTATE LOAN CHARGE-OFFS DOMESTIC OFFICES",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleAddition",
                    "parameters": {
                        "setField": "DRREOFFDOM",
                        "additionFields": [
                            "DRRECONS",
                            "DRREAG",
                            "DRRERES",
                            "DRREMULT",
                            "DRRENRES"
                        ]
                    }
                }
            }
        ]
    },
    "DRREOFFDOMR": {
        "title": "REAL ESTATE LOAN CHARGE-OFFS DOMESTIC OFFICES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "DRREOFFDOMR",
                        "numerator": "DRREOFFDOM",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "DRREOFFDOMQ": {
        "title": "REAL ESTATE LOAN CHARGE-OFFS DOMESTIC OFFICES QUARTERLY",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleAddition",
                    "parameters": {
                        "setField": "DRREOFFDOMQ",
                        "additionFields": [
                            "DRRECONQ",
                            "DRREAGQ",
                            "DRRERESQ",
                            "DRREMULQ",
                            "DRRENRSQ"
                        ]
                    }
                }
            }
        ]
    },
    "DRREOFFDOMQR": {
        "title": "REAL ESTATE LOAN CHARGE-OFFS DOMESTIC OFFICES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "DRREOFFDOMQR",
                        "numerator": "DRREOFFDOMQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "EDCM": {
        "title": "EQUITY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EDCM"
            }
        ]
    },
    "EDCMR": {
        "title": "EQUITY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "EDCMR",
                        "numerator": "EDCM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "EEFF": {
        "title": "EFFICIENCY RATIO EXPENSE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EEFF"
            }
        ]
    },
    "EEFFQ": {
        "title": "EFFICIENCY RATIO EXPENSE QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EEFFQ"
            }
        ]
    },
    "EEFFR": {
        "title": "EFFICIENCY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "EEFFR",
                        "numerator": "EEFF",
                        "denominator": "IEFF"
                    }
                }
            }
        ]
    },
    "EEFFQR": {
        "title": "EFFICIENCY QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EEFFQR"
            }
        ]
    },
    "EFFDATE": {
        "title": "EFFECTIVE DATE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EFFDATE"
            }
        ]
    },
    "EINTGW": {
        "title": "GOODWILL IMPAIRMENT LOSSES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EINTGW"
            }
        ]
    },
    "EINTGWR": {
        "title": "GOODWILL IMPAIRMENT LOSSES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "EINTGWR",
                        "numerator": "EINTGW",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "EINTGWQ": {
        "title": "GOODWILL IMPAIRMENT LOSSES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EINTGWQ"
            }
        ]
    },
    "EINTGWQR": {
        "title": "GOODWILL IMPAIRMENT LOSSES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "EINTGWQR",
                        "numerator": "EINTGWQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "EINTOTH": {
        "title": "AMORT & IMPAIR LOSSES OTH INTAN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EINTOTH"
            }
        ]
    },
    "EINTOTHR": {
        "title": "AMORT & IMPAIR LOSSES OTH INTAN RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "EINTOTHR",
                        "numerator": "EINTOTH",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "EINTOTHQ": {
        "title": "AMORT & IMPAIR LOSSES OTH INTAN QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EINTOTHQ"
            }
        ]
    },
    "EINTOTHQR": {
        "title": "AMORT & IMPAIR LOSSES OTH INTAN QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "EINTOTHQR",
                        "numerator": "EINTOTHQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "ELNANTR": {
        "title": "LOAN LOSS PROV/NT CHG-OFFS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ELNANTR",
                        "numerator": "ELNLOS",
                        "denominator": "NTTOT"
                    }
                }
            }
        ]
    },
    "ELNANTRQ": {
        "title": "LOAN LOSS PROV/NT CHG-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ELNANTRQ"
            }
        ]
    },
    "ELNATRA": {
        "title": "ELNATRA",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ELNATRA"
            }
        ]
    },
    "ELNATRY": {
        "title": "CREDIT LOSS PROV/AVE ASSETS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ELNATRY"
            }
        ]
    },
    "ELNATRYQ": {
        "title": "CREDIT LOSS PROV/AVE ASSETS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ELNATRYQ"
            }
        ]
    },
    "ENCEAUTO": {
        "title": "CR EXPOSURE-ENHANCEMENTS - AUTO",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ENCEAUTO"
            }
        ]
    },
    "ENCEAUTOR": {
        "title": "CR EXPOSURE-ENHANCEMENTS - AUTO RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ENCEAUTOR",
                        "numerator": "ENCEAUTO",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "ENCECI": {
        "title": "CR EXPOSURE - ENHANCEMENTS - CI",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ENCECI"
            }
        ]
    },
    "ENCECIR": {
        "title": "CR EXPOSURE - ENHANCEMENTS - CI RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ENCECIR",
                        "numerator": "ENCECI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "ENCECON": {
        "title": "CR EXPOSURE - ENHANCEMENTS - CON",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ENCECON"
            }
        ]
    },
    "ENCECONR": {
        "title": "CR EXPOSURE - ENHANCEMENTS - CON RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ENCECONR",
                        "numerator": "ENCECON",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "ENCEOTH": {
        "title": "CR EXPOSURE - ENHANCEMENTS - OTH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ENCEOTH"
            }
        ]
    },
    "ENCEOTHR": {
        "title": "CR EXPOSURE - ENHANCEMENTS - OTH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ENCEOTHR",
                        "numerator": "ENCEOTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "ENCERES": {
        "title": "CR EXPOSURE - ENHANCEMENTS - RES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ENCERES"
            }
        ]
    },
    "ENCERESR": {
        "title": "CR EXPOSURE - ENHANCEMENTS - RES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ENCERESR",
                        "numerator": "ENCERES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "EOTHINT": {
        "title": "OTHER INTEREST EXPENSE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EOTHINT"
            }
        ]
    },
    "EOTHINTR": {
        "title": "OTHER INTEREST EXPENSE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "EOTHINTR",
                        "numerator": "EOTHINT",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "EOTHINTQ": {
        "title": "OTHER INTEREST EXPENSE QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EOTHINTQ"
            }
        ]
    },
    "EOTHINTQR": {
        "title": "OTHER INTEREST EXPENSE QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "EOTHINTQR",
                        "numerator": "EOTHINTQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "EQ5": {
        "title": "TOTAL BANK EQUITY CAPITAL-CAVG5",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQ5"
            }
        ]
    },
    "EQCBHCTR": {
        "title": "TRANSACTIONS WITH BHC",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQCBHCTR"
            }
        ]
    },
    "EQCBHCTRR": {
        "title": "TRANSACTIONS WITH BHC RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "EQCBHCTRR",
                        "numerator": "EQCBHCTR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "EQCCOMPI": {
        "title": "OTHER COMPREHENSIVE INCOME",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQCCOMPI"
            }
        ]
    },
    "EQCCOMPIR": {
        "title": "OTHER COMPREHENSIVE INCOME RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "EQCCOMPIR",
                        "numerator": "EQCCOMPI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "EQCDIVA": {
        "title": "CASH DIVIDENDS ON COMM & PFD-ANN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQCDIVA"
            }
        ]
    },
    "EQCMRG": {
        "title": "CHANGES DUE TO MERGERS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQCMRG"
            }
        ]
    },
    "EQCMRGR": {
        "title": "CHANGES DUE TO MERGERS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "EQCMRGR",
                        "numerator": "EQCMRG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "EQCPREV": {
        "title": "BK EQ CAP MOST RECENTLY REPORTED",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQCPREV"
            }
        ]
    },
    "EQCPREVR": {
        "title": "BK EQ CAP MOST RECENTLY REPORTED RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "EQCPREVR",
                        "numerator": "EQCPREV",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "EQCREST": {
        "title": "ACCOUNTING CHANGES & CORRECTIONS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQCREST"
            }
        ]
    },
    "EQCRESTR": {
        "title": "ACCOUNTING CHANGES & CORRECTIONS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "EQCRESTR",
                        "numerator": "EQCREST",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "EQCSTKRX": {
        "title": "SALE OF CAPITAL STOCK",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQCSTKRX"
            }
        ]
    },
    "EQCSTKRXR": {
        "title": "SALE OF CAPITAL STOCK RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "EQCSTKRXR",
                        "numerator": "EQCSTKRX",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "EQCSXQ": {
        "title": "SALE OF CAPITAL STOCK QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQCSXQ"
            }
        ]
    },
    "EQCSXQR": {
        "title": "SALE OF CAPITAL STOCK QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "EQCSXQR",
                        "numerator": "EQCSXQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "EQCTRSTX": {
        "title": "TREASURY STOCK TRANSACTIONS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQCTRSTX"
            }
        ]
    },
    "EQCTRSTXR": {
        "title": "TREASURY STOCK TRANSACTIONS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "EQCTRSTXR",
                        "numerator": "EQCTRSTX",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "EQTOT": {
        "title": "TOTAL EQUITY CAPITAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "EQTOT"
            }
        ]
    },
    "EQTOTR": {
        "title": "TOTAL EQUITY CAPITAL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "EQTOTR",
                        "numerator": "EQTOT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "EQV": {
        "title": "BANK EQUITY CAPITAL/ASSETS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "EQV",
                        "numerator": "EQ",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "EQQR": {
        "title": "BANK EQUITY CAPITAL/ASSETS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleDivision",
                    "parameters": {
                        "setField": "EQQR",
                        "numerator": "EQ",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "ERNAST": {
        "title": "TOTAL EARNING ASSETS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ERNAST"
            }
        ]
    },
    "ERNAST2": {
        "title": "TOTAL EARNING ASSETS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ERNAST2"
            }
        ]
    },
    "ERNAST5": {
        "title": "TOTAL EARNING ASSETS-CAVG5I",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ERNAST5"
            }
        ]
    },
    "ERNASTR": {
        "title": "EARNING ASSETS / TOTAL ASSETS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ERNASTR"
            }
        ]
    },
    "ESTYMD": {
        "title": "ESTABLISHED DATE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ESTYMD"
            }
        ]
    },
    "ENDEFYMD": {
        "title": "INACTIVE DATE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ORG_END_NUM_DTE"
            }
        ]
    },
    "ORG_END_NUM_DTE": {
        "title": "INACTIVE DATE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ORG_END_NUM_DTE"
            }
        ]
    },
    "ETTLOTMG": {
        "title": "TT&L",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ETTLOTMG"
            }
        ]
    },
    "FORMTFR": {
        "title": "THRIFT FINANCIAL REPORT FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "FORMTFR"
            }
        ]
    },
    "FX": {
        "title": "FOREIGN EXCHANGE-TOTAL CONTRACTS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "FX"
            }
        ]
    },
    "FXR": {
        "title": "FOREIGN EXCHANGE-TOTAL CONTRACTS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "FXR",
                        "numerator": "FX",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "FXFFC": {
        "title": "FOR EXCH-FUTURES & FORWARD CONTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "FXFFC"
            }
        ]
    },
    "FXFFCR": {
        "title": "FOR EXCH-FUTURES & FORWARD CONTR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "FXFFCR",
                        "numerator": "FXFFC",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "FXNVS": {
        "title": "FOR EXCHANGE-SWAPS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "FXNVS"
            }
        ]
    },
    "FXNVSR": {
        "title": "FOR EXCHANGE-SWAPS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "FXNVSR",
                        "numerator": "FXNVS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "FXPOC": {
        "title": "FOR EXCH-PUR OPTION CONTRACTS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "FXPOC"
            }
        ]
    },
    "FXPOCR": {
        "title": "FOR EXCH-PUR OPTION CONTRACTS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "FXPOCR",
                        "numerator": "FXPOC",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "FXSPOT": {
        "title": "SPOT FOREIGN EXCHANGE CONTRACTS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "FXSPOT"
            }
        ]
    },
    "FXSPOTR": {
        "title": "SPOT FOREIGN EXCHANGE CONTRACTS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "FXSPOTR",
                        "numerator": "FXSPOT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "FXWOC": {
        "title": "FOR EXCH-WRITTEN OPTION CONTRACT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "FXWOC"
            }
        ]
    },
    "FXWOCR": {
        "title": "FOR EXCH-WRITTEN OPTION CONTRACT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "FXWOCR",
                        "numerator": "FXWOC",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "IBEFTXQ": {
        "title": "INC BEFORE INC TAXS & DISC-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IBEFTXQ"
            }
        ]
    },
    "IBEFXTR": {
        "title": "INCOME BEFORE DISC OPR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IBEFXTR"
            }
        ]
    },
    "IBEFXTRR": {
        "title": "INCOME BEFORE DISC OPR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "IBEFXTRR",
                        "numerator": "IBEFXTR",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "IBEFXTRQ": {
        "title": "INCOME BEFORE DISC OPR QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IBEFXTRQ"
            }
        ]
    },
    "IEFF": {
        "title": "EFFICIENCY RATIO INCOME",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IEFF"
            }
        ]
    },
    "IEFFQ": {
        "title": "EFFICIENCY RATIO INCOME QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IEFFQ"
            }
        ]
    },
    "IBEFXTRQR": {
        "title": "INCOME BEFORE DISC OPR QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "IBEFXTRQR",
                        "numerator": "IBEFXTRQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "IFIDUC": {
        "title": "FIDUCIARY ACTIVITIES INCOME",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IFIDUC"
            }
        ]
    },
    "IFIDUCR": {
        "title": "FIDUCIARY ACTIVITIES INCOME RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "IFIDUCR",
                        "numerator": "IFIDUC",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "IFIDUCQ": {
        "title": "FIDUCIARY ACTIVITIES INCOME-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IFIDUCQ"
            }
        ]
    },
    "IFIDUCQR": {
        "title": "FIDUCIARY ACTIVITIES INCOME-QTR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "IFIDUCQR",
                        "numerator": "IFIDUCQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "IGLCMEX": {
        "title": "TRADING ACCOUNT-COMMODITY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IGLCMEX"
            }
        ]
    },
    "IGLCMEXR": {
        "title": "TRADING ACCOUNT-COMMODITY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "IGLCMEXR",
                        "numerator": "IGLCMEX",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "IGLCMEXQ": {
        "title": "TRADING ACCOUNT-COMMODITY QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IGLCMEXQ"
            }
        ]
    },
    "IGLCMEXQR": {
        "title": "TRADING ACCOUNT-COMMODITY RATIO QUARTERLY",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "IGLCMEXQR",
                        "numerator": "IGLCMEXQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "IGLCREX": {
        "title": "TRADING REVENUE- CREDIT EXPOSURE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IGLCREX"
            }
        ]
    },
    "IGLCREXR": {
        "title": "TRADING REVENUE- CREDIT EXPOSURE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "IGLCREXR",
                        "numerator": "IGLCREX",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "IGLCREXQ": {
        "title": "TRADING REVENUE- CREDIT EXPOSURE QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IGLCREXQ"
            }
        ]
    },
    "IGLCREXQR": {
        "title": "TRADING REVENUE- CREDIT EXPOSURE QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "IGLCREXQR",
                        "numerator": "IGLCREXQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "IGLEDEX": {
        "title": "TRADING ACCOUNT-EQ DERIVATIVE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IGLEDEX"
            }
        ]
    },
    "IGLEDEXR": {
        "title": "TRADING ACCOUNT-EQ DERIVATIVE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "IGLEDEXR",
                        "numerator": "IGLEDEX",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "IGLEDEXQ": {
        "title": "TRADING ACCOUNT-EQ DERIVATIVE QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IGLEDEXQ"
            }
        ]
    },
    "IGLEDEXQR": {
        "title": "TRADING ACCOUNT-EQ DERIVATIVE QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "IGLEDEXQR",
                        "numerator": "IGLEDEXQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "IGLFXEX": {
        "title": "TRADING ACCOUNT-FOREIGN EXCHANGE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IGLFXEX"
            }
        ]
    },
    "IGLFXEXR": {
        "title": "RADING ACCOUNT-FOREIGN EXCHANGE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "IGLFXEXR",
                        "numerator": "IGLFXEX",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "IGLFXEXQ": {
        "title": "TRADING ACCOUNT-FOREIGN EXCHANGE QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IGLFXEXQ"
            }
        ]
    },
    "IGLFXEXQR": {
        "title": "RADING ACCOUNT-FOREIGN EXCHANGE QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "IGLFXEXQR",
                        "numerator": "IGLFXEXQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "IGLRTEX": {
        "title": "TRADING ACCOUNT-INTEREST RATE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IGLRTEX"
            }
        ]
    },
    "IGLRTEXR": {
        "title": "TRADING ACCOUNT-INTEREST RATE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "IGLRTEXR",
                        "numerator": "IGLRTEX",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "IGLRTEXQ": {
        "title": "TRADING ACCOUNT-INTEREST RATE QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IGLRTEXQ"
            }
        ]
    },
    "IGLRTEXQR": {
        "title": "TRADING ACCOUNT-INTEREST RATE QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "IGLRTEXQR",
                        "numerator": "IGLRTEXQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "IGLSECQ": {
        "title": "SECURITIES GAINS AND LOSSES-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IGLSECQ"
            }
        ]
    },
    "IGLTRAD": {
        "title": "TRADING REVENUES-TOTAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IGLTRAD"
            }
        ]
    },
    "IGLTRADR": {
        "title": "TRADING REVENUES-TOTAL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "IGLTRADR",
                        "numerator": "IGLTRAD",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "IGLTRDQ": {
        "title": "TRADING REVENUE-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IGLTRDQ"
            }
        ]
    },
    "IGLTRDQR": {
        "title": "TRADING REVENUE-QTR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "IGLTRDQR",
                        "numerator": "IGLTRDQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "IINSCOM": {
        "title": "INSURANCE COMMISSIONS & FEES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IINSCOM"
            }
        ]
    },
    "IINSCOMR": {
        "title": "INSURANCE COMMISSIONS & FEES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "IINSCOMR",
                        "numerator": "IINSCOM",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "IINSCOMQ": {
        "title": "INSURANCE COMMISSIONS & FEES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IINSCOMQ"
            }
        ]
    },
    "IINSCOMQR": {
        "title": "INSURANCE COMMISSIONS & FEES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "IINSCOMQR",
                        "numerator": "IINSCOMQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "IINSOTH": {
        "title": "INSURANCE COM+FEES-OTHER",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IINSOTH"
            }
        ]
    },
    "IINSOTHR": {
        "title": "INSURANCE COM+FEES-OTHER RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "IINSOTHR",
                        "numerator": "IINSOTH",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "IINSOTHQ": {
        "title": "INSURANCE COM+FEES-OTHER QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IINSOTHQ"
            }
        ]
    },
    "IINSOTHQR": {
        "title": "INSURANCE COM+FEES-OTHER QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "IINSOTHQR",
                        "numerator": "IINSOTHQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "IINSUND": {
        "title": "INSURANCE UNDERWRITNG INCOME",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IINSUND"
            }
        ]
    },
    "IINSUNDR": {
        "title": "INSURANCE UNDERWRITNG INCOME RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "IINSUNDR",
                        "numerator": "IINSUND",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "IINSUNDQ": {
        "title": "INSURANCE UNDERWRITNG INCOME QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IINSUNDQ"
            }
        ]
    },
    "IINSUNDQR": {
        "title": "INSURANCE UNDERWRITNG INCOME QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "IINSUNDQR",
                        "numerator": "IINSUNDQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "IINVFEE": {
        "title": "INVEST BANK",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IINVFEE"
            }
        ]
    },
    "IINVFEER": {
        "title": "INVEST BANK RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "IINVFEER",
                        "numerator": "IINVFEE",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "IINVFEEQ": {
        "title": "INVEST BANK QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IINVFEEQ"
            }
        ]
    },
    "IINVFEEQR": {
        "title": "INVEST BANK QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "IINVFEEQR",
                        "numerator": "IINVFEEQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "INSAGNT1": {
        "title": "PRIMARY INSURER",
        "description": "",
        "type": "string",
        "x-elastic-type": "keyword",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INSAGNT1"
            }
        ]
    },
    "INTANGCC": {
        "title": "PURCH CC REL & NONMTG SER ASTS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INTANGCC"
            }
        ]
    },
    "INTANGW": {
        "title": "GOODWILL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INTANGW"
            }
        ]
    },
    "INTANGWR": {
        "title": "GOODWILL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "INTANGWR",
                        "numerator": "INTANGW",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "INTANMSR": {
        "title": "MORTGAGE SERVICING ASSETS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INTANMSR"
            }
        ]
    },
    "INTANMSRR": {
        "title": "MORTGAGE SERVICING ASSETS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "INTANMSRR",
                        "numerator": "INTANMSR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "INTANOTH": {
        "title": "OTHER IDENTIFIABLE INTANG ASSETS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INTANOTH"
            }
        ]
    },
    "INTANOTHR": {
        "title": "OTHER IDENTIFIABLE INTANG ASSETS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "INTANOTHR",
                        "numerator": "INTANOTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "INTINCYQ": {
        "title": "INTEREST INCOME/EARNING ASSETS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INTINCYQ"
            }
        ]
    },
    "INTINCA": {
        "title": "TOTAL INTEREST INCOME ANNUAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INTINCA"
            }
        ]
    },
    "IOTNII": {
        "title": "OTHER NONINTEREST INCOME",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IOTNII"
            }
        ]
    },
    "IOTNIIR": {
        "title": "OTHER NONINTEREST INCOME RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "IOTNIIR",
                        "numerator": "IOTNII",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "IOTNIIQ": {
        "title": "OTHER NONINTEREST INCOME QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IOTNIIQ"
            }
        ]
    },
    "IOTNIIQR": {
        "title": "OTHER NONINTEREST INCOME QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "IOTNIIQR",
                        "numerator": "IOTNIIQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "ISECZ": {
        "title": "SECURITIZATION INCOME",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ISECZ"
            }
        ]
    },
    "ISECZR": {
        "title": "SECURITIZATION INCOME RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "ISECZR",
                        "numerator": "ISECZ",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "ISECZQ": {
        "title": "SECURITIZATION INCOME QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ISECZQ"
            }
        ]
    },
    "ISECZQR": {
        "title": "SECURITIZATION INCOME QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "ISECZQR",
                        "numerator": "ISECZQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "ISERCHGQ": {
        "title": "SERVICE CHARGE ON DEP ACCTS-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ISERCHGQ"
            }
        ]
    },
    "ISERCHGQR": {
        "title": "SERVICE CHARGE ON DEPOSIT ACCTS-QTR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "ISERCHGQR",
                        "numerator": "ISERCHGQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "ISERFEE": {
        "title": "SERVICING FEES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ISERFEE"
            }
        ]
    },
    "ISERFEER": {
        "title": "SERVICING FEES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "ISERFEER",
                        "numerator": "ISERFEE",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "ISERFEEQ": {
        "title": "SERVICING FEES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ISERFEEQ"
            }
        ]
    },
    "ISERFEEQR": {
        "title": "SERVICING FEES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "ISERFEEQR",
                        "numerator": "ISERFEEQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "IVENCAP": {
        "title": "VENTURE CAPITAL REVENUE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IVENCAP"
            }
        ]
    },
    "IVENCAPR": {
        "title": "VENTURE CAPITAL REVENUE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "IVENCAPR",
                        "numerator": "IVENCAP",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "IVENCAPQ": {
        "title": "VENTURE CAPITAL REVENUE QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "IVENCAPQ"
            }
        ]
    },
    "IVENCAPQR": {
        "title": "VENTURE CAPITAL REVENUE QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "IVENCAPQR",
                        "numerator": "IVENCAPQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "LAG": {
        "title": "AG LOANS - LOSS SHARE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LAG"
            }
        ]
    },
    "LAGR": {
        "title": "AG LOANS - LOSS SHARE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LAGR",
                        "numerator": "LAG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LCI": {
        "title": "C&I LOANS - LOSS SHARE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LCI"
            }
        ]
    },
    "LCIR": {
        "title": "C&I LOANS - LOSS SHARE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LCIR",
                        "numerator": "LCI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LCON": {
        "title": "CONSUMER LOANS - LOSS SHARE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LCON"
            }
        ]
    },
    "LCONR": {
        "title": "CONSUMER LOANS - LOSS SHARE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LCONR",
                        "numerator": "LCON",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LIABFOR": {
        "title": "TOTAL LIABILITIES-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LIABFOR"
            }
        ]
    },
    "LNAG1": {
        "title": "AGRICULTURAL LOANS-UNDER 100-$",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNAG1"
            }
        ]
    },
    "LNAG1R": {
        "title": "AGRICULTURAL LOANS-UNDER 100-$ RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNAG1R",
                        "numerator": "LNAG1",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNAG2": {
        "title": "AGRICULTURAL LOANS-100-250-$",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNAG2"
            }
        ]
    },
    "LNAG2R": {
        "title": "AGRICULTURAL LOANS-100-250-$ RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNAG2R",
                        "numerator": "LNAG2",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNAG3": {
        "title": "AGRICULTURAL LOANS-250-500-$",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNAG3"
            }
        ]
    },
    "LNAG3R": {
        "title": "AGRICULTURAL LOANS-250-500-$ RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNAG3R",
                        "numerator": "LNAG3",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNAG4": {
        "title": "AGRICULTURAL LOANS-UNDER 500-$",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNAG4"
            }
        ]
    },
    "LNAG4R": {
        "title": "AGRICULTURAL LOANS-UNDER 500-$ RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNAG4R",
                        "numerator": "LNAG4",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNAG5": {
        "title": "AG LOANS-CAVG5",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNAG5"
            }
        ]
    },
    "LNAG22": {
        "title": "AG LOANS-CAVG2",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNAG22"
            }
        ]
    },
    "LNAG1N": {
        "title": "AGRICULTURAL LOANS-UNDER 100-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNAG1N"
            }
        ]
    },
    "LNAG1NR": {
        "title": "AGRICULTURAL LOANS-UNDER 100-NUM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNAG1NR",
                        "numerator": "LNAG1N",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNAG2N": {
        "title": "AGRICULTURAL LOANS-100-250-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNAG2N"
            }
        ]
    },
    "LNAG2NR": {
        "title": "AGRICULTURAL LOANS-100-250-NUM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNAG2NR",
                        "numerator": "LNAG2N",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNAG3N": {
        "title": "AGRICULTURAL LOANS-250-500-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNAG3N"
            }
        ]
    },
    "LNAG3NR": {
        "title": "AGRICULTURAL LOANS-250-500-NUM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNAG3NR",
                        "numerator": "LNAG3N",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNAG4N": {
        "title": "AGRICULTURAL LOANS-UNDER 500-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNAG4N"
            }
        ]
    },
    "LNAG4NR": {
        "title": "AGRICULTURAL LOANS-UNDER 500-NUM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNAG4NR",
                        "numerator": "LNAG4N",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNAGFOR": {
        "title": "AGRICULTURAL LOANS-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNAGFOR"
            }
        ]
    },
    "LNAGFORR": {
        "title": "AGRICULTURAL LOANS-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleDivision",
                    "parameters": {
                        "setField": "LNAGFORR",
                        "numerator": "LNAGFOR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNATRESR": {
        "title": "LOAN LOSS RESERVE/GROSS LN&LS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNATRESR",
                        "numerator": "LNATRES",
                        "denominator": "LNLSGR"
                    }
                }
            }
        ]
    },
    "LNAUTO2": {
        "title": "CONSUMER LOANS - AUTO - CAVG2",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNAUTO2"
            }
        ]
    },
    "LNAUTO5": {
        "title": "CONSUMER LOANS - AUTO - CAVG5",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNAUTO5"
            }
        ]
    },
    "LNCI1": {
        "title": "C&I LOANS-UNDER-100-$",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCI1"
            }
        ]
    },
    "LNCI1R": {
        "title": "C&I LOANS-UNDER-100-$ RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNCI1R",
                        "numerator": "LNCI1",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNCI2": {
        "title": "C&I LOANS-100-250-$",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCI2"
            }
        ]
    },
    "LNCI2R": {
        "title": "C&I LOANS-100-250-$ RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNCI2R",
                        "numerator": "LNCI2",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNCI3": {
        "title": "C&I LOANS-250-1M-$",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCI3"
            }
        ]
    },
    "LNCI3R": {
        "title": "C&I LOANS-250-1M-$ RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNCI3R",
                        "numerator": "LNCI3",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNCI4": {
        "title": "C&I LOANS-UNDER-1M-$",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCI4"
            }
        ]
    },
    "LNCI4R": {
        "title": "C&I LOANS-UNDER-1M-$ RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNCI4R",
                        "numerator": "LNCI4",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNCI5": {
        "title": "C&I LOANS-CAVG5",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCI5"
            }
        ]
    },
    "LNCI22": {
        "title": "C&I LOANS-CAVG2",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCI22"
            }
        ]
    },
    "LNCI1N": {
        "title": "C&I LOANS-UNDER-100-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCI1N"
            }
        ]
    },
    "LNCI1NR": {
        "title": "C&I LOANS-UNDER-100-NUM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNCI1NR",
                        "numerator": "LNCI1N",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNCI2N": {
        "title": "C&I LOANS-100-250-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCI2N"
            }
        ]
    },
    "LNCI2NR": {
        "title": "C&I LOANS-250-1M-NUM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNCI2NR",
                        "numerator": "LNCI2N",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNCI3N": {
        "title": "C&I LOANS-250-1M-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCI3N"
            }
        ]
    },
    "LNCI3NR": {
        "title": "C&I LOANS-250-1M-NUM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNCI3NR",
                        "numerator": "LNCI3N",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNCI4N": {
        "title": "C&I LOANS-UNDER-1M-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCI4N"
            }
        ]
    },
    "LNCI4NR": {
        "title": "C&I LOANS-UNDER-1M-NUM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNCI4NR",
                        "numerator": "LNCI4N",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNCIFOR": {
        "title": "C&I LOANS-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCIFOR"
            }
        ]
    },
    "LNCIFORR": {
        "title": "C&I LOANS-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleDivision",
                    "parameters": {
                        "setField": "LNCIFORR",
                        "numerator": "LNCIFOR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNCINUS": {
        "title": "C&I LOANS-NON-U.S. DOMICILE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCINUS"
            }
        ]
    },
    "LNCINUSF": {
        "title": "C&I LOANS-NON-U.S. DOMICILE-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCINUSF"
            }
        ]
    },
    "LNCINUSFR": {
        "title": "C&I LOANS-NON-U.S. DOMICILE-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleDivision",
                    "parameters": {
                        "setField": "LNCINUSFR",
                        "numerator": "LNCINUSF",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNCOMRE": {
        "title": "COMMERCIAL RE LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCOMRE"
            }
        ]
    },
    "LNCOMRER": {
        "title": "COMMERCIAL RE LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNCOMRER",
                        "numerator": "LNCOMRE",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNCOMRE2": {
        "title": "COMMERCIAL RE LOANS2",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCOMRE2"
            }
        ]
    },
    "LNCOMRE5": {
        "title": "COMMERCIAL RE LOANS CAVG5",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCOMRE5"
            }
        ]
    },
    "LNCON2": {
        "title": "CONSUMER LOANS-CAVG2",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCON2"
            }
        ]
    },
    "LNCON5": {
        "title": "CONSUMER LOANS-CAVG5",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCON5"
            }
        ]
    },
    "LNCONFOR": {
        "title": "CONSUMER LOANS-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCONFOR"
            }
        ]
    },
    "LNCONFORR": {
        "title": "CONSUMER LOANS-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleDivision",
                    "parameters": {
                        "setField": "LNCONFORR",
                        "numerator": "LNCONFOR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNCONORP": {
        "title": "OTHER CONSUMER & RELATED PLANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCONORP"
            }
        ]
    },
    "LNCONOT2": {
        "title": "OTHER CONSUMER LOANS-CAVG2",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCONOT2"
            }
        ]
    },
    "LNCONOT5": {
        "title": "OTHER CONSUMER LOANS-CAVG5",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCONOT5"
            }
        ]
    },
    "LNCONRP": {
        "title": "CONSUMER LNS-RELATED PLANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCONRP"
            }
        ]
    },
    "LNCONRPR": {
        "title": "CONSUMER LNS-RELATED PLANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNCONRPR",
                        "numerator": "LNCONRP",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNCONTRA": {
        "title": "OTHER CONTRA ACCOUNTS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCONTRA"
            }
        ]
    },
    "LNCONTRAR": {
        "title": "OTHER CONTRA ACCOUNTS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNCONTRAR",
                        "numerator": "LNCONTRA",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNCRCD2": {
        "title": "CREDIT CARD PLANS-CAVG2",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCRCD2"
            }
        ]
    },
    "LNCRCD5": {
        "title": "CREDIT CARD PLANS-CAVG5",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNCRCD5"
            }
        ]
    },
    "LNDEPAC": {
        "title": "TOTAL DEP INST LNS & ACCEPT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNDEPAC"
            }
        ]
    },
    "LNDEPACD": {
        "title": "TOTAL DEP INST LNS & ACCEPT-DOM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNDEPACD"
            }
        ]
    },
    "LNDEPAOBK": {
        "title": "LOANS TO DEPOSITORY INSTITUTIONS AND ACCEPTANCE OF OTHER BANKS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleSubtraction",
                    "parameters": {
                        "setField": "LNDEPOABK",
                        "subtractionFields": [
                            "LNDEPAC",
                            "LNDEPACD"
                        ]
                    }
                }
            }
        ]
    },
    "LNDEPAOBKR": {
        "title": "LOANS TO DEPOSITORY INSTITUTIONS AND ACCEPTANCE OF OTHER BANKS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def LNDEPAC = ctx.LNDEPAC ?: 0;\ndef LNDEPACD = ctx.LNDEPACD ?: 0;\ndef ASSET = ctx.ASSET ?: 0;\nctx.LNDEPAOBKR = 0;\nif(ASSET > 0) {\n  ctx.LNDEPAOBKR = ((double)(LNDEPAC - LNDEPACD) / ASSET);\n}\n"
                    }
                }
            }
        ]
    },
    "LNDEPCB": {
        "title": "DEP INST LNS-COMMERCIAL BANKS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNDEPCB"
            }
        ]
    },
    "LNDEPCBF": {
        "title": "DEP INST LNS-COMMERCIAL BK-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNDEPCBF"
            }
        ]
    },
    "LNDEPCBFR": {
        "title": "DEP INST LNS-COMMERCIAL BK-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNDEPCBFR",
                        "numerator": "LNDEPCBF",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNDEPFC": {
        "title": "DEP INST LNS-FOR COUNTRY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNDEPFC"
            }
        ]
    },
    "LNDEPFCF": {
        "title": "DEP INST LNS-FOR COUNTRY-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNDEPFCF"
            }
        ]
    },
    "LNDEPFCFR": {
        "title": "DEP INST LNS-FOR COUNTRY-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNDEPFCFR",
                        "numerator": "LNDEPFCF",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNDEPFUS": {
        "title": "DEP INST LNS-FOR COUNTRY-U.S. BR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNDEPFUS"
            }
        ]
    },
    "LNDEPUS": {
        "title": "DEP INST LNS-OTH U.S. INST",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNDEPUS"
            }
        ]
    },
    "LNDEPUSB": {
        "title": "DEP INST LNS-COM BKS-U.S.BRANCH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNDEPUSB"
            }
        ]
    },
    "LNDEPUSF": {
        "title": "DEP INST LNS-OTH U.S. INST-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNDEPUSF"
            }
        ]
    },
    "LNDEPUSFR": {
        "title": "DEP INST LNS-OTH U.S. INST-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNDEPUSFR",
                        "numerator": "LNDEPUSF",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNEXAMT": {
        "title": "EXECUTIVE OFFICER LOANS-AMOUNT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNEXAMT"
            }
        ]
    },
    "LNEXAMTR": {
        "title": "EXECUTIVE OFFICER LOANS-AMOUNT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNEXAMTR",
                        "numerator": "LNEXAMT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNFGFOR": {
        "title": "FOREIGN GOVT LOANS-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNFGFOR"
            }
        ]
    },
    "LNFGFORR": {
        "title": "FOREIGN GOVT LOANS-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNFGFORR",
                        "numerator": "LNFGFOR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNLSDEPR": {
        "title": "NET LOANS & LEASES/DEPOSITS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNLSDEPR",
                        "numerator": "LNLSNET",
                        "denominator": "DEP"
                    }
                }
            }
        ]
    },
    "LNLSDEQR": {
        "title": "NET LOANS & LEASES/DEPOSITS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleDivision",
                    "parameters": {
                        "setField": "LNLSDEQR",
                        "numerator": "LNLSNET",
                        "denominator": "DEP"
                    }
                }
            }
        ]
    },
    "LNLSFOR": {
        "title": "LN&LS + UNEARNED INC-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNLSFOR"
            }
        ]
    },
    "LNLSFORR": {
        "title": "LN&LS + UNEARNED INC-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNLSFORR",
                        "numerator": "LNLSFOR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNLSGR5": {
        "title": "LOANS AND LEASES-TOTAL-CAVG5",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNLSGR5"
            }
        ]
    },
    "LNLSGRF": {
        "title": "LOANS AND LEASES-TOTAL-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNLSGRF"
            }
        ]
    },
    "LNLSGRFR": {
        "title": "LOANS AND LEASES-TOTAL-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNLSGRFR",
                        "numerator": "LNLSGRF",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNLSNTV": {
        "title": "NET LOANS & LEASES/ASSETS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNLSNTV"
            }
        ]
    },
    "LNLSNTQR": {
        "title": "NET LOANS & LEASES/ASSETS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleDivision",
                    "parameters": {
                        "setField": "LNLSNTQR",
                        "numerator": "LNLSNET",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNLSNQR": {
        "title": "NET LOANS & LEASES/ASSETS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleDivision",
                    "parameters": {
                        "setField": "LNLSNQR",
                        "numerator": "LNLSNET",
                        "denominator": "COREDEP"
                    }
                }
            }
        ]
    },
    "LNLSSALE": {
        "title": "LOANS & LEASES HELD FOR RESALE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNLSSALE"
            }
        ]
    },
    "LNLSSALER": {
        "title": "LOANS & LEASES HELD FOR RESALE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNLSSALER",
                        "numerator": "LNLSSALE",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNPLEDGE": {
        "title": "PLEDGED LOANS AND LEASES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNPLEDGE"
            }
        ]
    },
    "LNPLEDGER": {
        "title": "PLEDGED LOANS AND LEASES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNPLEDGER",
                        "numerator": "LNPLEDGE",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNMUNIF": {
        "title": "MUNI LOANS-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNMUNIF"
            }
        ]
    },
    "LNMUNIFR": {
        "title": "MUNI LOANS-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNMUNIFR",
                        "numerator": "LNMUNIF",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNOT1T3": {
        "title": "ALL OTHER LNS & LS * 1-3 YEARS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNOT1T3"
            }
        ]
    },
    "LNOT1T3R": {
        "title": "ALL OTHER LNS & LS * 1-3 YEARS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNOT1T3R",
                        "numerator": "LNOT1T3",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNOT3LES": {
        "title": "ALL OTHER LNS & LS*3 MO OR LESS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNOT3LES"
            }
        ]
    },
    "LNOT3LESR": {
        "title": "ALL OTHER LNS & LS*3 MO OR LESS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNOT3LESR",
                        "numerator": "LNOT3LES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNOT3T5": {
        "title": "ALL OTHER LNS & LS * 3-5 YEARS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNOT3T5"
            }
        ]
    },
    "LNOT3T5R": {
        "title": "ALL OTHER LNS & LS * 3-5 YEARS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNOT3T5R",
                        "numerator": "LNOT3T5",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNOT3T12": {
        "title": "ALL OTHER LNS & LS * 3-12 MONS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNOT3T12"
            }
        ]
    },
    "LNOT3T12R": {
        "title": "ALL OTHER LNS & LS * 3-12 MONS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNOT3T12R",
                        "numerator": "LNOT3T12",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNOT5T15": {
        "title": "ALL OTHER LNS & LS * 5-15 YEARS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNOT5T15"
            }
        ]
    },
    "LNOT5T15R": {
        "title": "ALL OTHER LNS & LS * 5-15 YEARS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNOT5T15R",
                        "numerator": "LNOT5T15",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNOTCI2": {
        "title": "OTHER LOANS & LEASES-QBP-CAVG2",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNOTCI2"
            }
        ]
    },
    "LNOTCI5": {
        "title": "OTHER LOANS & LEASES-QBP-CAVG5",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNOTCI5"
            }
        ]
    },
    "LNOTHERF": {
        "title": "LN TO NONDEP FIN INST & OTH-FGN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNOTHERF"
            }
        ]
    },
    "LNOTHERFR": {
        "title": "LN TO NONDEP FIN INST & OTH-FGN RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNOTHERFR",
                        "numerator": "LNOTHERF",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNOTOV15": {
        "title": "ALL OTHER LNS & LS * OVER 15 YRS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNOTOV15"
            }
        ]
    },
    "LNOTOV15R": {
        "title": "ALL OTHER LNS & LS * OVER 15 YRS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNOTOV15R",
                        "numerator": "LNOTOV15",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNREAG1": {
        "title": "RE AGRICULTURAL-UNDER 100-$",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNREAG1"
            }
        ]
    },
    "LNREAG1R": {
        "title": "RE AGRICULTURAL-UNDER 100-$ RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNREAG1R",
                        "numerator": "LNREAG1",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNREAG2": {
        "title": "RE AGRICULTURAL-100-250-$",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNREAG2"
            }
        ]
    },
    "LNREAG2R": {
        "title": "RE AGRICULTURAL-100-250-$ RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNREAG2R",
                        "numerator": "LNREAG2",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNREAG3": {
        "title": "RE AGRICULTURAL-250-500-$",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNREAG3"
            }
        ]
    },
    "LNREAG3R": {
        "title": "RE AGRICULTURAL-250-500-$ RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNREAG3R",
                        "numerator": "LNREAG3",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNREAG4": {
        "title": "RE AGRICULTURAL-UNDER 500-$",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNREAG4"
            }
        ]
    },
    "LNREAG4R": {
        "title": "RE AGRICULTURAL-UNDER 500-$ RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNREAG4R",
                        "numerator": "LNREAG4",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNREAG1N": {
        "title": "RE AGRICULTURAL-UNDER 100-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNREAG1N"
            }
        ]
    },
    "LNREAG1NR": {
        "title": "RE AGRICULTURAL-UNDER 100-NUM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNREAG1NR",
                        "numerator": "LNREAG1N",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNREAG2N": {
        "title": "RE AGRICULTURAL-100-250-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNREAG2N"
            }
        ]
    },
    "LNREAG2NR": {
        "title": "RE AGRICULTURAL-100-250-NUM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNREAG2NR",
                        "numerator": "LNREAG2N",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNREAG3N": {
        "title": "RE AGRICULTURAL-250-500-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNREAG3N"
            }
        ]
    },
    "LNREAG3NR": {
        "title": "RE AGRICULTURAL-250-500-NUM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNREAG3NR",
                        "numerator": "LNREAG3N",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNREAG4N": {
        "title": "RE AGRICULTURAL-UNDER 500-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNREAG4N"
            }
        ]
    },
    "LNREAG4NR": {
        "title": "RE AGRICULTURAL-UNDER 500-NUM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNREAG4NR",
                        "numerator": "LNREAG4N",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRECNFM": {
        "title": "1-4 FAM RE CONSTRUCTION LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRECNFM"
            }
        ]
    },
    "LNRECNFMR": {
        "title": "1-4 FAM RE CONSTRUCTION LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRECNFMR",
                        "numerator": "LNRECNFM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRECNOT": {
        "title": "OTHER RE CONSTRUCTION & LAND LN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRECNOT"
            }
        ]
    },
    "LNRECNOTR": {
        "title": "OTHER RE CONSTRUCTION & LAND LN",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRECNOTR",
                        "numerator": "LNRECNOT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNREOTH2": {
        "title": "ALL OTHER RE OWNED-1-4 FAMILY2",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNREOTH2"
            }
        ]
    },
    "LNREOTH5": {
        "title": "RE 1-4 FAMILY OTHER LOANS CAVG5",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNREOTH5"
            }
        ]
    },
    "LNRENR1": {
        "title": "RE NONFARM NONRES-UNDER 100-$",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRENR1"
            }
        ]
    },
    "LNRENR1R": {
        "title": "RE NONFARM NONRES-UNDER 100-$ RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRENR1R",
                        "numerator": "LNRENR1",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRENR2": {
        "title": "RE NONFARM NONRES-100-250-$",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRENR2"
            }
        ]
    },
    "LNRENR2R": {
        "title": "RE NONFARM NONRES-100-250-$ RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRENR2R",
                        "numerator": "LNRENR2",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRENR3": {
        "title": "RE NONFARM NONRES-250-1M-$",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRENR3"
            }
        ]
    },
    "LNRENR3R": {
        "title": "RE NONFARM NONRES-250-1M-$ RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRENR3R",
                        "numerator": "LNRENR3",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRENR4": {
        "title": "RE NONFARM NONRES-UNDER 1M-$",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRENR4"
            }
        ]
    },
    "LNRENR4R": {
        "title": "RE NONFARM NONRES-UNDER 1M-$ RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRENR4R",
                        "numerator": "LNRENR4",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRENR1N": {
        "title": "RE NONFARM NONRES-UNDER 100-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRENR1N"
            }
        ]
    },
    "LNRENR1NR": {
        "title": "RE NONFARM NONRES-UNDER 100-NUM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRENR1NR",
                        "numerator": "LNRENR1N",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRENR2N": {
        "title": "RE NONFARM NONRES-100-250-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRENR2N"
            }
        ]
    },
    "LNRENR2NR": {
        "title": "RE NONFARM NONRES-100-250-NUM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRENR2NR",
                        "numerator": "LNRENR2N",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRENR3N": {
        "title": "RE NONFARM NONRES-250-1M-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRENR3N"
            }
        ]
    },
    "LNRENR3NR": {
        "title": "RE NONFARM NONRES-250-1M-NUM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRENR3NR",
                        "numerator": "LNRENR3N",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRENR4N": {
        "title": "RE NONFARM NONRES-UNDER 1M-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRENR4N"
            }
        ]
    },
    "LNRENR4NR": {
        "title": "RE NONFARM NONRES-UNDER 1M-NUM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRENR4NR",
                        "numerator": "LNRENR4N",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRENROT": {
        "title": "OTHER NONFARM NONRES RE LNS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRENROT"
            }
        ]
    },
    "LNRENROTR": {
        "title": "OTHER NONFARM NONRES RE LNS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRENROTR",
                        "numerator": "LNRENROT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRENROW": {
        "title": "OWNER-OCC NONFARM NONRES RE LNS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRENROW"
            }
        ]
    },
    "LNRENROWR": {
        "title": "OWNER-OCC NONFARM NONRES RE LNS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRENROWR",
                        "numerator": "LNRENROW",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRENUS": {
        "title": "RE LNS-NON US ADDRESSEES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRENUS"
            }
        ]
    },
    "LNRENUSR": {
        "title": "RE LNS-NON US ADDRESSEES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRENUSR",
                        "numerator": "LNRENUS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRERSF1": {
        "title": "RE 1-4 FAMILY-FIRST LIENS-ADJUST",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRERSF1"
            }
        ]
    },
    "LNRERSF1R": {
        "title": "RE 1-4 FAMILY-FIRST LIENS-ADJUST RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRERSF1R",
                        "numerator": "LNRERSF1",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRERSF2": {
        "title": "RE 1-4 FAMILY-SECOND LIENS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRERSF2"
            }
        ]
    },
    "LNRERSF2R": {
        "title": "RE 1-4 FAMILY-SECOND LIENS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRERSF2R",
                        "numerator": "LNRERSF2",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRERSFM": {
        "title": "RE 1-4 FAMILY-FIRST LIENS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRERSFM"
            }
        ]
    },
    "LNRERSFMR": {
        "title": "RE 1-4 FAMILY-FIRST LIENS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRERSFMR",
                        "numerator": "LNRERSFM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRESNCR": {
        "title": "LOAN LOSS RESERVE/N/C LOANS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRESNCR",
                        "numerator": "LNATRESJ",
                        "denominator": "NCLNLS"
                    }
                }
            }
        ]
    },
    "LNRS1T3": {
        "title": "RE 1-4 FAMILY * 1-3 YEARS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRS1T3"
            }
        ]
    },
    "LNRS1T3R": {
        "title": "RE 1-4 FAMILY * 1-3 YEARS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRS1T3R",
                        "numerator": "LNRS1T3",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRS3LES": {
        "title": "RE 1-4 FAMILY * 3 MONS OR LESS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRS3LES"
            }
        ]
    },
    "LNRS3LESR": {
        "title": "RE 1-4 FAMILY * 3 MONS OR LESS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRS3LESR",
                        "numerator": "LNRS3LES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRS3T5": {
        "title": "RE 1-4 FAMILY * 3-5 YEARS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRS3T5"
            }
        ]
    },
    "LNRS3T5R": {
        "title": "RE 1-4 FAMILY * 3-5 YEARS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRS3T5R",
                        "numerator": "LNRS3T5",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRS3T12": {
        "title": "RE 1-4 FAMILY * 3-12 MONTHS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRS3T12"
            }
        ]
    },
    "LNRS3T12R": {
        "title": "RE 1-4 FAMILY * 3-12 MONTHS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRS3T12R",
                        "numerator": "LNRS3T12",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRS5T15": {
        "title": "RE 1-4 FAMILY * 5-15 YEARS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRS5T15"
            }
        ]
    },
    "LNRS5T15R": {
        "title": "RE 1-4 FAMILY * 5-15 YEARS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRS5T15R",
                        "numerator": "LNRS5T15",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNRSOV15": {
        "title": "RE 1-4 FAMILY * OVER 15 YEARS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNRSOV15"
            }
        ]
    },
    "LNRSOV15R": {
        "title": "RE 1-4 FAMILY * OVER 15 YEARS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNRSOV15R",
                        "numerator": "LNRSOV15",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LNSB": {
        "title": "SMALL BUSINESS LNS SOLD-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNSB"
            }
        ]
    },
    "LNSBR": {
        "title": "SMALL BUSINESS LNS SOLD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNSBR"
            }
        ]
    },
    "LNSERV": {
        "title": "PRIN BAL- LNS SERVICE FOR OTHERS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LNSERV"
            }
        ]
    },
    "LNSERVR": {
        "title": "PRIN BAL- LNS SERVICE FOR OTHERS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LNSERVR",
                        "numerator": "LNSERV",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LOCCOM": {
        "title": "COMMERCIAL LETTERS OF CREDIT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LOCCOM"
            }
        ]
    },
    "LOCCOMR": {
        "title": "COMMERCIAL LETTERS OF CREDIT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LOCCOMR",
                        "numerator": "LOCCOM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LOCFPSB": {
        "title": "FIN & PERFORM STANDBY LOC",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LOCFPSB"
            }
        ]
    },
    "LOCFPSBR": {
        "title": "FIN & PERFORM STANDBY LOC RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LOCFPSBR",
                        "numerator": "LOCFPSB",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LOCFPSBK": {
        "title": "FIN & PERFORM STANDBY LOC-CONVEY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LOCFPSBK"
            }
        ]
    },
    "LOCFPSBKR": {
        "title": "FIN & PERFORM STANDBY LOC-CONVEY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LOCFPSBKR",
                        "numerator": "LOCFPSBK",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LOCFSB": {
        "title": "FINANCIAL STANDBY LOC",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LOCFSB"
            }
        ]
    },
    "LOCFSBR": {
        "title": "FINANCIAL STANDBY LOC RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LOCFSBR",
                        "numerator": "LOCFSB",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LOCFSBK": {
        "title": "FINANCIAL STANDBY LOC-CONVEYED",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LOCFSBK"
            }
        ]
    },
    "LOCFSBKR": {
        "title": "FINANCIAL STANDBY LOC-CONVEYED RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LOCFSBKR",
                        "numerator": "LOCFSBK",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LOCPSB": {
        "title": "PERFORMANCE STANDBY LOC",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LOCPSB"
            }
        ]
    },
    "LOCPSBR": {
        "title": "PERFORMANCE STANDBY LOC RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LOCPSBR",
                        "numerator": "LOCPSB",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LOCPSBK": {
        "title": "PERFORMANCE STANDBY LOC-CONVEYED",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LOCPSBK"
            }
        ]
    },
    "LOCPSBKR": {
        "title": "PERFORMANCE STANDBY LOC-CONVEYED RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LOCPSBKR",
                        "numerator": "LOCPSBK",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LOREGTY": {
        "title": "ORE PROTECTED - LOSS SHARE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LOREGTY"
            }
        ]
    },
    "LOREGTYR": {
        "title": "ORE PROTECTED - LOSS SHARE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LOREGTYR",
                        "numerator": "LOREGTY",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LOTH": {
        "title": "ALL OTHER LN & LS - LOSS SHARE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LOTH"
            }
        ]
    },
    "LOTHR": {
        "title": "ALL OTHER LN & LS - LOSS SHARE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LOTHR",
                        "numerator": "LOTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LREAG": {
        "title": "RE FARMLAND LN - LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LREAG"
            }
        ]
    },
    "LREAGR": {
        "title": "RE FARMLAND LN - LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LREAGR",
                        "numerator": "LREAG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LRECONS": {
        "title": "RE CONSTRUCT LN - LOSS SHARE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LRECONS"
            }
        ]
    },
    "LRECONSR": {
        "title": "RE CONSTRUCT LN - LOSS SHARE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LRECONSR",
                        "numerator": "LRECONS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LREMULT": {
        "title": "RE MULTIFAMILY LN-LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LREMULT"
            }
        ]
    },
    "LREMULTR": {
        "title": "RE MULTIFAMILY LN-LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LREMULTR",
                        "numerator": "LREMULT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LRENRES": {
        "title": "RE NONFARM NONRES LN - LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LRENRES"
            }
        ]
    },
    "LRENRESR": {
        "title": "RE NONFARM NONRES LN - LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LRENRESR",
                        "numerator": "LRENRES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LRERES": {
        "title": "RE 1-4 FAMILY LNS - LOSS SHARE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LRERES"
            }
        ]
    },
    "LRERESR": {
        "title": "RE 1-4 FAMILY LNS - LOSS SHARE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LRERESR",
                        "numerator": "LRERES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LSALNLS": {
        "title": "CARRY AMT LOSS SHARE-LNLS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LSALNLS"
            }
        ]
    },
    "LSALNLSR": {
        "title": "CARRY AMT LOSS SHARE-LNLS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LSALNLSR",
                        "numerator": "LSALNLS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LSAOA": {
        "title": "CARRY AMT LOSS SHARE -OTH ASSET",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LSAOA"
            }
        ]
    },
    "LSAOAR": {
        "title": "CARRY AMT LOSS SHARE -OTH ASSET RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LSAOAR",
                        "numerator": "LSAOA",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LSAORE": {
        "title": "CARRY AMT LOSS SHARE- ORE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LSAORE"
            }
        ]
    },
    "LSAORER": {
        "title": "CARRY AMT LOSS SHARE- ORE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LSAORER",
                        "numerator": "LSAORE",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LSASCDBT": {
        "title": "CARRY AMT LOSS SHARE -DEBT SEC",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LSASCDBT"
            }
        ]
    },
    "LSASCDBTR": {
        "title": "CARRY AMT LOSS SHARE -DEBT SEC RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LSASCDBTR",
                        "numerator": "LSASCDBT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "LSFOR": {
        "title": "LEASES-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LSFOR"
            }
        ]
    },
    "LSFORR": {
        "title": "LEASES-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "LSFORR",
                        "numerator": "LSFOR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "MSA": {
        "title": "FIPS MSA CODE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "MSA"
            }
        ]
    },
    "MSRECE": {
        "title": "OUT PRIN BAL MORT W/ RECOURSE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "MSRECE"
            }
        ]
    },
    "MSRECER": {
        "title": "OUT PRIN BAL MORT W/ RECOURSE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "MSRECER",
                        "numerator": "MSRECE",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "MSRESFCL": {
        "title": "1-4 FM SERVICED IN FORECLOSURE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "MSRESFCL"
            }
        ]
    },
    "MSRESFCLR": {
        "title": "1-4 FM SERVICED IN FORECLOSURE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "MSRESFCLR",
                        "numerator": "MSRESFCL",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "MSRNRECE": {
        "title": "OUT PRIN BAL MORT W/ NO RECOURSE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "MSRNRECE"
            }
        ]
    },
    "MSRNRECER": {
        "title": "OUT PRIN BAL MORT W/ NO RECOURSE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "MSRNRECER",
                        "numerator": "MSRNRECE",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NAAG": {
        "title": "NONACCRUAL-AGRICULTURAL LNS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NAAG"
            }
        ]
    },
    "NAAGR": {
        "title": "NONACCRUAL-AGRICULTURAL LNS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NAAGR",
                        "numerator": "NAAG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NAAGSM": {
        "title": "NONACCRUAL-AG LNS*SMALL BKS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NAAGSM"
            }
        ]
    },
    "NAAGSMR": {
        "title": "NONACCRUAL-AG LNS*SMALL BKS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NAAGSMR",
                        "numerator": "NAAGSM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NAASSET": {
        "title": "NONACCRUAL-TOTAL ASSETS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NAASSET"
            }
        ]
    },
    "NAASSETR": {
        "title": "NONACCRUAL-AG LNS*SMALL BKS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NAASSETR",
                        "numerator": "NAASSET",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NAAUTO": {
        "title": "NONACCRUAL AUTO LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NAAUTO"
            }
        ]
    },
    "NAAUTOR": {
        "title": "NONACCRUAL AUTO LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NAAUTOR",
                        "numerator": "NAAUTO",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NACI": {
        "title": "NONACCRUAL-C&I LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NACI"
            }
        ]
    },
    "NACIR": {
        "title": "NONACCRUAL-C&I LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NACIR",
                        "numerator": "NACI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NACINUS": {
        "title": "NONACCRUAL-C&I*NON-U.S.",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NACINUS"
            }
        ]
    },
    "NACINUSR": {
        "title": "NONACCRUAL-C&I*NON-U.S. RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NACINUSR",
                        "numerator": "NACINUS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NACON": {
        "title": "NONACCRUAL-CONSUMER LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NACON"
            }
        ]
    },
    "NACONR": {
        "title": "NONACCRUAL-CONSUMER LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NACONR",
                        "numerator": "NACON",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NACONOTH": {
        "title": "NONACCRUAL-OTHER CONSUMER",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NACONOTH"
            }
        ]
    },
    "NACONOTHR": {
        "title": "NONACCRUAL-OTHER CONSUMER RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NACONOTHR",
                        "numerator": "NACONOTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NACRCD": {
        "title": "NONACCRUAL-CREDIT CARD PLANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NACRCD"
            }
        ]
    },
    "NACRCDR": {
        "title": "NONACCRUAL-CREDIT CARD PLANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NACRCDR",
                        "numerator": "NACRCD",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NADEP": {
        "title": "NONACCRUAL-DEP INST LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NADEP"
            }
        ]
    },
    "NADEPR": {
        "title": "NONACCRUAL-DEP INST LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NADEPR",
                        "numerator": "NADEP",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NADEPNUS": {
        "title": "NONACCRUAL-DEP INST*NON U.S.",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NADEPNUS"
            }
        ]
    },
    "NADEPNUSR": {
        "title": "NONACCRUAL-DEP INST*NON U.S. RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NADEPNUSR",
                        "numerator": "NADEPNUS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NAFG": {
        "title": "NONACCRUAL-FOREIGN GOVT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NAFG"
            }
        ]
    },
    "NAFGR": {
        "title": "NONACCRUAL-FOREIGN GOVT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NAFGR",
                        "numerator": "NAFG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NAGTY": {
        "title": "NONACCRUAL-GTY LN&LS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NAGTY"
            }
        ]
    },
    "NAGTYR": {
        "title": "NONACCRUAL -GTY LN&LS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NAGTYR",
                        "numerator": "NAGTY",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NAGTYGNM": {
        "title": "NONACCRUAL REBOOKED GNMA LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NAGTYGNM"
            }
        ]
    },
    "NAGTYGNMR": {
        "title": "NONACCRUAL REBOOKED GNMA LNS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NAGTYGNMR",
                        "numerator": "NAGTYGNM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NAGTYPAR": {
        "title": "NONACCRUAL-PART GTY LN&LS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NAGTYPAR"
            }
        ]
    },
    "NAGTYPARR": {
        "title": "NONACCRUAL-PART GTY LN&LS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NAGTYPARR",
                        "numerator": "NAGTYPAR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NALAG": {
        "title": "NONACCRUAL AG LOANS-LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NALAG"
            }
        ]
    },
    "NALAGR": {
        "title": "NONACCRUAL AG LOANS-LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NALAGR",
                        "numerator": "NALAG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NALCI": {
        "title": "NONACCRUAL C&I LNS-LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NALCI"
            }
        ]
    },
    "NALCIR": {
        "title": "NONACCRUAL C&I LNS-LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NALCIR",
                        "numerator": "NALCI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NALCON": {
        "title": "NONACCRUAL CONSUMER LN -LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NALCON"
            }
        ]
    },
    "NALCONR": {
        "title": "NONACCRUAL CONSUMER LN -LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NALCONR",
                        "numerator": "NALCON",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NALGTY": {
        "title": "NONACCR PROTECT (GTY)-LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NALGTY"
            }
        ]
    },
    "NALGTYR": {
        "title": "NONACCRUAL PROTECT (GTY)-LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NALGTYR",
                        "numerator": "NALGTY",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NALNSALE": {
        "title": "NONACCRUAL-L&L HELD FOR SALE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NALNSALE"
            }
        ]
    },
    "NALNSALER": {
        "title": "NONACCRUAL-L&L HELD FOR SALE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NALNSALER",
                        "numerator": "NALNSALE",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NALOTH": {
        "title": "NONACCRUAL OTHER LNS-LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NALOTH"
            }
        ]
    },
    "NALOTHR": {
        "title": "NONACCRUAL OTHER LNS-LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NALOTHR",
                        "numerator": "NALOTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NALREAG": {
        "title": "NONACCRUAL RE FARM-LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NALREAG"
            }
        ]
    },
    "NALREAGR": {
        "title": "NONACCRUAL RE FARM LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NALREAGR",
                        "numerator": "NALREAG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NALRECON": {
        "title": "NONACCRUAL CONSTR LN -LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NALRECON"
            }
        ]
    },
    "NALRECONR": {
        "title": "NONACCRUAL CONSTR LN -LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NALRECONR",
                        "numerator": "NALRECON",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NALREMUL": {
        "title": "NONACCRUAL MULTIFAM - LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NALREMUL"
            }
        ]
    },
    "NALREMULR": {
        "title": "NONACCRUAL MULTIFAM - LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NALREMULR",
                        "numerator": "NALREMUL",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NALRENRS": {
        "title": "NONACCRUAL NFNR LN - LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NALRENRS"
            }
        ]
    },
    "NALRENRSR": {
        "title": "NONACCRUAL NFNR LN - LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NALRENRSR",
                        "numerator": "NALRENRS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NALRERES": {
        "title": "NONACCRUAL 1-4 FM LN-LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NALRERES"
            }
        ]
    },
    "NALRERESR": {
        "title": "NONACCRUAL 1-4 FM LN-LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NALRERESR",
                        "numerator": "NALRERES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NALS": {
        "title": "NONACCRUAL-LEASES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NALS"
            }
        ]
    },
    "NALSR": {
        "title": "NONACCRUAL-LEASES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NALSR",
                        "numerator": "NALS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NALTOT": {
        "title": "NONACCRUAL TOTAL LOANS - LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NALTOT"
            }
        ]
    },
    "NALTOTR": {
        "title": "NONACCRUAL TOTAL LOANS - LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NALTOTR",
                        "numerator": "NALTOT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NAME": {
        "title": "INSTITUTION NAME",
        "description": "",
        "type": "string",
        "x-elastic-type": "keyword",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NAME"
            }
        ]
    },
    "NAMEFULL": {
        "title": "INSTITUTION FULL NAME",
        "description": "",
        "type": "string",
        "x-elastic-type": "keyword",
        "x-elastic-analyzer": [
            {
                "variable": "raw",
                "analyzer": "whitespace_analyzer"
            },
            {
                "variable": "autocomplete",
                "analyzer": "autocomplete_analyzer"
            }
        ],
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NAMEFULL"
            }
        ]
    },
    "NAOTHLN": {
        "title": "NONACCRUAL-ALL OTHER LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NAOTHLN"
            }
        ]
    },
    "NAOTHLNR": {
        "title": "NONACCRUAL-ALL OTHER LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NAOTHLNR",
                        "numerator": "NAOTHLN",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NARE": {
        "title": "NONACCRUAL-REAL ESTATE LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NARE"
            }
        ]
    },
    "NARER": {
        "title": "NONACCRUAL-REAL ESTATE LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NARER",
                        "numerator": "NARE",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NAREAG": {
        "title": "NONACCRUAL-RE*FARMLAND",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NAREAG"
            }
        ]
    },
    "NAREAGR": {
        "title": "NONACCRUAL-RE*FARMLAND RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NAREAGR",
                        "numerator": "NAREAG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NARECNFM": {
        "title": "NONACCRUAL 1-4 FAM CONSTRUCT LN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NARECNFM"
            }
        ]
    },
    "NARECNFMR": {
        "title": "NONACCRUAL 1-4 FAM CONSTRUCT LN RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NARECNFMR",
                        "numerator": "NARECNFM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NARECNOT": {
        "title": "NONACCRUAL OTHER CONSTR & LAND",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NARECNOT"
            }
        ]
    },
    "NARECNOTR": {
        "title": "NONACCRUAL OTHER CONSTR & LAND RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NARECNOTR",
                        "numerator": "NARECNOT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NARECONS": {
        "title": "NONACCRUAL-RE*CONSTRUCTION",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NARECONS"
            }
        ]
    },
    "NARECONSR": {
        "title": "NONACCRUAL-RE*CONSTRUCTION RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NARECONSR",
                        "numerator": "NARECONS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NAREFOR": {
        "title": "NONACCRUAL-RE*FOREIGN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NAREFOR"
            }
        ]
    },
    "NAREFORR": {
        "title": "NONACCRUAL-RE*FOREIGN RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NAREFORR",
                        "numerator": "NAREFOR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NARELOC": {
        "title": "NONACCRUAL-RE*1-4 FAM LINES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NARELOC"
            }
        ]
    },
    "NARELOCR": {
        "title": "NONACCRUAL-RE*1-4 FAM LINES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NARELOCR",
                        "numerator": "NARELOC",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NAREMULT": {
        "title": "NONACCRUAL-RE*MULTIFAMILY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NAREMULT"
            }
        ]
    },
    "NAREMULTR": {
        "title": "NONACCRUAL-RE*MULTIFAMILY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NAREMULTR",
                        "numerator": "NAREMULT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NARENRES": {
        "title": "NONACCRUAL-RE*NONFARM NONRES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NARENRES"
            }
        ]
    },
    "NARENRESR": {
        "title": "NONACCRUAL-RE*NONFARM NONRES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NARENRESR",
                        "numerator": "NARENRES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NARENROT": {
        "title": "NONACCRUAL OTHER NONFARM NONRES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NARENROT"
            }
        ]
    },
    "NARENROTR": {
        "title": "NONACCRUAL OTHER NONFARM NONRES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NARENROTR",
                        "numerator": "NARENROT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NARENROW": {
        "title": "NONACCRUAL 0WN-OCC NONFRM NONRS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NARENROW"
            }
        ]
    },
    "NARENROWR": {
        "title": "NONACCRUAL OWN-OCC NONFRM NONRS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NARENROWR",
                        "numerator": "NARENROW",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NARENUS": {
        "title": "NONACCRUAL-RE*NON-U.S.",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NARENUS"
            }
        ]
    },
    "NARENUSR": {
        "title": "NONACCRUAL-RE*NON-U.S. RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NARENUSR",
                        "numerator": "NARENUS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NARERES": {
        "title": "NONACCRUAL-RE*1-4 FAMILY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NARERES"
            }
        ]
    },
    "NARERESR": {
        "title": "NONACCRUAL-RE*1-4 FAMILY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NARERESR",
                        "numerator": "NARERES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NARERSF2": {
        "title": "NONACCRUAL-RE*1-4 JUNIOR LIEN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NARERSF2"
            }
        ]
    },
    "NARERSF2R": {
        "title": "NONACCRUAL-RE*1-4 JN LIEN RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NARERSF2R",
                        "numerator": "NARERSF2",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NARERSFM": {
        "title": "NONACCRUAL-RE*1-4 IST LIEN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NARERSFM"
            }
        ]
    },
    "NARERSFMR": {
        "title": "NONACCRUAL-RE*1-4 IST LIEN RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NARERSFMR",
                        "numerator": "NARERSFM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NARSCI": {
        "title": "NONACCRUAL RESTRUCT C&I LN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NARSCI"
            }
        ]
    },
    "NARSCONS": {
        "title": "NONACCR RESTRUCT CONSTRUCTION",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NARSCONS"
            }
        ]
    },
    "NARSLNFM": {
        "title": "NONACCRUAL RESTRU LN- 1-4 FAM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NARSLNFM"
            }
        ]
    },
    "NARSLNFMR": {
        "title": "NONACCRUAL RESTRU LN- 1-4 FAM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NARSLNFMR",
                        "numerator": "NARSLNFM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NARSLNLS": {
        "title": "NONACCRUAL RESTRU LN EXCL 1-4 FM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NARSLNLS"
            }
        ]
    },
    "NARSLNLSR": {
        "title": "NONACCRUAL RESTRU LN EXCL 1-4 FM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NARSLNLSR",
                        "numerator": "NARSLNLS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NARSLNLT": {
        "title": "NONACCRUAL RESTRUCT LN- TOTAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NARSLNLT"
            }
        ]
    },
    "NARSLNLTR": {
        "title": "NONACCRUAL RESTRUCT LN- TOTAL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NARSLNLTR",
                        "numerator": "NARSLNLT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NARSMULT": {
        "title": "NONACCRUAL RESTRUCT MULTIFAMILY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NARSMULT"
            }
        ]
    },
    "NARSNRES": {
        "title": "NONACCR RESTRUCTURED NFNR LN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NARSNRES"
            }
        ]
    },
    "NARSOTH": {
        "title": "NONACCRUAL RESTRUCT ALL OTH LN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NARSOTH"
            }
        ]
    },
    "NASCDEBT": {
        "title": "NONACCRUAL-DEBT SECURITIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NASCDEBT"
            }
        ]
    },
    "NASCDEBTR": {
        "title": "NONACCRUAL-DEBT SECURITIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NASCDEBTR",
                        "numerator": "NASCDEBT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NCAG": {
        "title": "TOTAL N/C-AGRICULTURAL LNS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NCAG"
            }
        ]
    },
    "NCAUTO": {
        "title": "N/C AUTO LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NCAUTO"
            }
        ]
    },
    "NCCI": {
        "title": "TOTAL N/C-C&I LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NCCI"
            }
        ]
    },
    "NCCOMRER": {
        "title": "NC COMMERCIAL RE/COMMERCIAL RE",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NCCOMRER",
                        "numerator": "NCCOMRE",
                        "denominator": "LNCOMRE"
                    }
                }
            }
        ]
    },
    "NCCOMRE": {
        "title": "NC COMMERCIAL RE/COMMERCIAL RE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NCCOMRE"
            }
        ]
    },
    "NCCOMREQR": {
        "title": "NC COMMERCIAL RE/COMMERCIAL RE QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NCCOMREQR",
                        "numerator": "NCCOMRE",
                        "denominator": "LNCOMRE",
                        "noMultiplier": True
                    }
                }
            }
        ]
    },
    "NCCON": {
        "title": "TOTAL N/C-CONSUMER LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NCCON"
            }
        ]
    },
    "NCCONOTH": {
        "title": "TOTAL N/C-OTHER CONSUMER",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NCCONOTH"
            }
        ]
    },
    "NCCRCD": {
        "title": "TOTAL N/C CREDIT CARD PLANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NCCRCD"
            }
        ]
    },
    "NCDEP": {
        "title": "TOTAL N/C-DEP INST LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NCDEP"
            }
        ]
    },
    "NCFG": {
        "title": "TOTAL N/C-FOREIGN GOVT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NCFG"
            }
        ]
    },
    "NCGTYPAR": {
        "title": "TOTAL N/C-PART GTY LN&LS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NCGTYPAR"
            }
        ]
    },
    "NCLNLSR": {
        "title": "N/C LNS & LS/GROSS LNS & LS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NCLNLSR",
                        "numerator": "NCLNLS",
                        "denominator": "LNLSGRJ"
                    }
                }
            }
        ]
    },
    "NCLS": {
        "title": "TOTAL N/C-LEASES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NCLS"
            }
        ]
    },
    "NCOTHLN": {
        "title": "TOTAL N/C-ALL OTHER LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NCOTHLN"
            }
        ]
    },
    "NCRE": {
        "title": "TOTAL N/C REAL ESTATE LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NCRE"
            }
        ]
    },
    "NCRECONR": {
        "title": "N/C CONST REAL ESTATE/CONST RE",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NCRECONR",
                        "numerator": "NCRECONS",
                        "denominator": "LNRECONS"
                    }
                }
            }
        ]
    },
    "NCRECONS": {
        "title": "TOTAL N/C CONST REAL ESTATE CONSTRUCTION",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NCRECONS"
            }
        ]
    },
    "NCRELOC": {
        "title": "TOTAL N/C-RE 1-4 FAMILY LINES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NCRELOC"
            }
        ]
    },
    "NCRELOCR": {
        "title": "N/C HOME EQUITY/HOME EQUITY",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NCRELOCR",
                        "numerator": "NCRELOC",
                        "denominator": "LNRELOC"
                    }
                }
            }
        ]
    },
    "NCREMULR": {
        "title": "N/C MULTIFAMLY RE/MULTIFAMLY RE",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NCREMULR",
                        "numerator": "NCREMULT",
                        "denominator": "LNREMULT"
                    }
                }
            }
        ]
    },
    "NCREMULT": {
        "title": "TOTAL N/C MULTIFAMLY RE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NCREMULT"
            }
        ]
    },
    "NCRENRER": {
        "title": "N/C NONFARM NONRES RE/NONRES RE",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NCRENRER",
                        "numerator": "NCRENRES",
                        "denominator": "LNRENRES"
                    }
                }
            }
        ]
    },
    "NCRENRES": {
        "title": "TOTAL N/C NONFARM NONRES RE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NCRENRES"
            }
        ]
    },
    "NCRER": {
        "title": "N/C REAL ESTATE LNS/REAL ESTATE",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NCRER",
                        "numerator": "NCRE",
                        "denominator": "LNREJ"
                    }
                }
            }
        ]
    },
    "NCREREOR": {
        "title": "N/C 1-4 OTHER RE/1-4 OTHER RE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NCREREOR"
            }
        ]
    },
    "NCRERES": {
        "title": "N/C 1-4 FAMILY RE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NCRERES"
            }
        ]
    },
    "NCRERESR": {
        "title": "N/C 1-4 FAMILY RE/1-4 FAMILY RE",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NCRERESR",
                        "numerator": "NCRERES",
                        "denominator": "LNRERES"
                    }
                }
            }
        ]
    },
    "NETGNAST": {
        "title": "NET G/L ON SALES OF FIX ASSETS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NETGNAST"
            }
        ]
    },
    "NETGNASTR": {
        "title": "NET G/L ON SALES OF FIX ASSETS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NETGNASTR",
                        "numerator": "NETGNAST",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTGLFXAQ": {
        "title": "NET G/L ON SALES OF FIX ASSETS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTGLFXAQ"
            }
        ]
    },
    "NTGLFXAQR": {
        "title": "NET G/L ON SALES OF FIX ASSETS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTGLFXAQR",
                        "numerator": "NTGLFXAQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NETGNSLN": {
        "title": "NET G/L ON SALES OF LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NETGNSLN"
            }
        ]
    },
    "NETGNSLNR": {
        "title": "NET G/L ON SALES OF LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NETGNSLNR",
                        "numerator": "NETGNSLN",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTGLLNQ": {
        "title": "NET G/L ON SALES OF LOANS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTGLLNQ"
            }
        ]
    },
    "NTGLLNQR": {
        "title": "NET G/L ON SALES OF LOANS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTGLLNQR",
                        "numerator": "NTGLLNQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NETGNSRE": {
        "title": "NET G/L ON OTHER RE OWNED",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NETGNSRE"
            }
        ]
    },
    "NETGNSRER": {
        "title": "NET G/L ON OTHER RE OWNED RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NETGNSRER",
                        "numerator": "NETGNSRE",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTGLREQ": {
        "title": "NET G/L ON OTHER RE OWNED QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTGLREQ"
            }
        ]
    },
    "NTGLREQR": {
        "title": "NET G/L ON OTHER RE OWNED QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTGLREQR",
                        "numerator": "NTGLREQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NETINCA": {
        "title": "NET INCOME- BANK- ANN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NETINCA"
            }
        ]
    },
    "NIMY": {
        "title": "NET INTEREST MARGIN",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NIMY",
                        "numerator": "NIMA",
                        "denominator": "ERNAST5"
                    }
                }
            }
        ]
    },
    "NIMYQ": {
        "title": "NET INTEREST MARGIN QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NIMYQ"
            }
        ]
    },
    "NOIJ": {
        "title": "NET OPERATING INCOME-ADJ",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NOIJ"
            }
        ]
    },
    "NOIJR": {
        "title": "NET OPERATING INCOME-ADJ RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NOIJR",
                        "numerator": "NOIJ",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NOIJY": {
        "title": "NET OPERATING INCOME-ADJ/ASSETS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NOIJY",
                        "numerator": "NOIJA",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NOIJYQ": {
        "title": "NET OPERATING INCOME-ADJ/ASSETS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NOIJYQ"
            }
        ]
    },
    "NOIJA": {
        "title": "NET OPERATING INCOME-ADJ ANNUALLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NOIJA"
            }
        ]
    },
    "NOIJQ": {
        "title": "NET OPERATING INCOME-ADJ QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NOIJQ"
            }
        ]
    },
    "NOIJQA": {
        "title": "NET OPERATING INCOME-ADJ QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NOIJQA"
            }
        ]
    },
    "NOIJQR": {
        "title": "NET OPERATING INCOME-ADJ QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NOIJQR",
                        "numerator": "NOIJQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NONIIAY": {
        "title": "NONINTEREST INC/AVERAGE ASSETS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NONIIAY"
            }
        ]
    },
    "NONIIAYQ": {
        "title": "NONINTEREST INC/AVERAGE ASSETS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NONIIAYQ"
            }
        ]
    },
    "NONIIA": {
        "title": "TOTAL NONINTEREST INCOME ANNUALLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NONIIA"
            }
        ]
    },
    "NONIIQ": {
        "title": "TOTAL NONINTEREST INCOME-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NONIIQ"
            }
        ]
    },
    "NONIIQA": {
        "title": "TOTAL NONINTEREST INCOME-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NONIIQA"
            }
        ]
    },
    "NONIIQR": {
        "title": "TOTAL NONINTEREST INCOME-QTR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NONIIQR",
                        "numerator": "NONIIQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NONIXAY": {
        "title": "NONINTEREST EXP/AVERAGE ASSETS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NONIXAY",
                        "numerator": "NONIXA",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NONIXAYQ": {
        "title": "NONINTEREST EXP/AVERAGE ASSETS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NONIXAYQ"
            }
        ]
    },
    "NONIXA": {
        "title": "TOTAL NONINTEREST EXPENSE ANNUALLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NONIXA"
            }
        ]
    },
    "NPERF": {
        "title": "NONPERF ASSETS/TOTAL ASSETS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NPERF"
            }
        ]
    },
    "NPERFV": {
        "title": "NONPERF ASSETS/TOTAL ASSETS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NPERFV",
                        "numerator": "NPERF",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NTAG": {
        "title": "AGRICULTURAL LN NET CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTAG"
            }
        ]
    },
    "NTAGR": {
        "title": "AGRICULTURAL LN NET CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTAGR",
                        "numerator": "NTAG",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTAGA": {
        "title": "AGRICULTURAL LN NET-CHG-ANN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTAGA"
            }
        ]
    },
    "NTAGQ": {
        "title": "AG LOAN NET CHARGE-OFFS-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTAGQ"
            }
        ]
    },
    "NTAGQR": {
        "title": "AG LOAN NET CHARGE-OFFS-QTR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTAGQR",
                        "numerator": "NTAGQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTAGSM": {
        "title": "AG LN NET CHARGE-OFFS*SMALL BKS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTAGSM"
            }
        ]
    },
    "NTAGSMR": {
        "title": "AG LN NET CHARGE-OFFS*SMALL BKS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTAGSMR",
                        "numerator": "NTAGSM",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTAGSMQ": {
        "title": "AG LN NET CHARGE-OFFS*SMALL BKS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTAGSMQ"
            }
        ]
    },
    "NTAGSMQR": {
        "title": "AG LN NET CHARGE-OFFS*SMALL BKS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTAGSMQR",
                        "numerator": "NTAGSMQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTAUTO": {
        "title": "AUTO LOANS - NET CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTAUTO"
            }
        ]
    },
    "NTAUTOR": {
        "title": "AUTO LOANS - NET CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTAUTOR",
                        "numerator": "NTAUTO",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTAUTOA": {
        "title": "AUTO LNS - NET CHG-OFFS - ANN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTAUTOA"
            }
        ]
    },
    "NTAUTOQ": {
        "title": "AUTO LNS - NET CHG-OFFS - QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTAUTOQ"
            }
        ]
    },
    "NTAUTOLNQR": {
        "title": "AUTO LNS - NET CHG-OFFS - QTR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTAUTOLNQR",
                        "numerator": "NTAUTOQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTAUTOQR": {
        "title": "AUTO LN-CHG-OFF- QTR/AUTO LN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTAUTOQR"
            }
        ]
    },
    "NTCI": {
        "title": "COMMERCIAL LOAN NET CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTCI"
            }
        ]
    },
    "NTCIR": {
        "title": "COMMERCIAL LOAN NET CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTCIR",
                        "numerator": "NTCI",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTCIA": {
        "title": "COMMERCIAL LOAN NET-CHG-ANN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTCIA"
            }
        ]
    },
    "NTCINUS": {
        "title": "NON-U.S.COMMERCIAL LN NET CHG-OF",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTCINUS"
            }
        ]
    },
    "NTCINUSR": {
        "title": "NON-U.S.COMMERCIAL LN NET CHG-OF RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTCINUSR",
                        "numerator": "NTCINUS",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTCINUSQ": {
        "title": "NON-U.S.COMMERCIAL LN NET CHG-OF QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTCINUSQ"
            }
        ]
    },
    "NTCINUSQR": {
        "title": "NON-U.S.COMMERCIAL LN NET CHG-OF QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTCINUSQR",
                        "numerator": "NTCINUSQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTCIQ": {
        "title": "COMMERCIAL LOAN NET-CHG-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTCIQ"
            }
        ]
    },
    "NTCIQR": {
        "title": "COMMERCIAL LOAN NET-CHG-QTR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTCIQR",
                        "numerator": "NTCIQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTCOMRER": {
        "title": "COMMERCIAL RE CHG-OFF/COMM RE LN",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NTCOMRER",
                        "numerator": "NTCOMREA",
                        "denominator": "LNCOMRE5"
                    }
                }
            }
        ]
    },
    "NTCOMREQ": {
        "title": "COMMERCIAL RE CHG-OFF/COMM RE LN QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTCOMREQ"
            }
        ]
    },
    "NTCOMREA": {
        "title": "COMMERCIAL RE LN CHG-ANN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTCOMREA"
            }
        ]
    },
    "NTCON": {
        "title": "CONSUMER LOAN NET CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTCON"
            }
        ]
    },
    "NTCONR": {
        "title": "CONSUMER LOAN NET CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTCONR",
                        "numerator": "NTCON",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTCONA": {
        "title": "CONSUMER LOAN NET-CHG-ANN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTCONA"
            }
        ]
    },
    "NTCONOTA": {
        "title": "OTHER CONSUMER LOAN NET-CHG-ANN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTCONOTA"
            }
        ]
    },
    "NTCONOTH": {
        "title": "OTHER CONSUMER LN NET CHARGE-OFF",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTCONOTH"
            }
        ]
    },
    "NTCONOTHR": {
        "title": "OTHER CONSUMER LN NET CHARGE-OFF RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTCONOTHR",
                        "numerator": "NTCONOTH",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTCONOTQ": {
        "title": "OTHER CONSUMER LN NET-CHG-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTCONOTQ"
            }
        ]
    },
    "NTCONOTQR": {
        "title": "OTHER CONSUMER LN NET-CHG-QTR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTCONOTQR",
                        "numerator": "NTCONOTQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTCONQ": {
        "title": "CONSUMER LOAN NET-CHG-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTCONQ"
            }
        ]
    },
    "NTCONQR": {
        "title": "CONSUMER LOAN NET-CHG-QTR RATIO",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTCONQR"
            }
        ]
    },
    "NTCONTQR": {
        "title": "OTH.CONSUMER CHGOFF-QTR/OTH.CONS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTCONTQR"
            }
        ]
    },
    "NTCRCD": {
        "title": "CREDIT CARD LOAN NET CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTCRCD"
            }
        ]
    },
    "NTCRCDR": {
        "title": "CREDIT CARD LOAN NET CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NNTCRCDR",
                        "numerator": "NTCRCD",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTCRCDA": {
        "title": "CREDIT CARD LOAN NET-CHG-ANN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTCRCDA"
            }
        ]
    },
    "NTCRCDQ": {
        "title": "CREDIT CARD LN NET-CHG-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTCRCDQ"
            }
        ]
    },
    "NTCRCDQR": {
        "title": "CREDIT CARD LN NET-CHG-QTR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTCRCDQR",
                        "numerator": "NTCRCDQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTDEP": {
        "title": "DEPOSITORY INST LOAN NET CHG-OFF",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTDEP"
            }
        ]
    },
    "NTDEPR": {
        "title": "DEPOSITORY INST LOAN NET CHG-OFF RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTDEPR",
                        "numerator": "NTDEP",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTDEPNUS": {
        "title": "FOREIGN DEP INST LN NET CHG-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTDEPNUS"
            }
        ]
    },
    "NTDEPNUSR": {
        "title": "FOREIGN DEP INST LN NET CHG-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTDEPNUSR",
                        "numerator": "NTDEPNUS",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTDEPNUQ": {
        "title": "FOREIGN DEP INST LN NET CHG-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTDEPNUQ"
            }
        ]
    },
    "NTDEPNUQR": {
        "title": "FOREIGN DEP INST LN NET CHG-OFFS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTDEPNUQR",
                        "numerator": "NTDEPNUQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTDEPNUSQ": {
        "title": "FOREIGN DEP INST LN NET CHG-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTDEPNUSR",
                        "numerator": "NTDEPNUS",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTDEPQ": {
        "title": "DEPOSITORY INST LOAN NET-CHG-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTDEPQ"
            }
        ]
    },
    "NTDEPQR": {
        "title": "DEPOSITORY INST LOAN NET-CHG-QTR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTDEPQR",
                        "numerator": "NTDEPQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTFORGV": {
        "title": "FOREIGN GOVT LN NET CHG-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTFORGV"
            }
        ]
    },
    "NTFORGVR": {
        "title": "FOREIGN GOVT LN NET CHG-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTFORGVR",
                        "numerator": "NTFORGV",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTFORGVQ": {
        "title": "FOREIGN GOV LN NET-CHG-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTFORGVQ"
            }
        ]
    },
    "NTFORGVQR": {
        "title": "FOREIGN GOV LN NET-CHG-QTR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTFORGVQR",
                        "numerator": "NTFORGVQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTINCHPP": {
        "title": "NET INCOME-BK-HIGHER-PP",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTINCHPP"
            }
        ]
    },
    "NTINCL": {
        "title": "NET INCOME-BANK- LOSERS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTINCL"
            }
        ]
    },
    "NTINCLQ": {
        "title": "NET INCOME-BK-LOSER-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTINCLQ"
            }
        ]
    },
    "NTLNLSA": {
        "title": "TOTAL LN&LS NET-CHG-ANN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTLNLSA"
            }
        ]
    },
    "NTINQHPP": {
        "title": "",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTINQHPP"
            }
        ]
    },
    "NTLNLSR": {
        "title": "NET CHARGE-OFFS/LOANS & LEASES",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NTLNLSR",
                        "numerator": "NTLNLSA",
                        "denominator": "LNLSGR5"
                    }
                }
            }
        ]
    },
    "NTLNLSQR": {
        "title": "NET CHARGE-OFFS/LOANS & LEASES QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTLNLSQR"
            }
        ]
    },
    "NTLS": {
        "title": "LEASE NET CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTLS"
            }
        ]
    },
    "NTLSR": {
        "title": "LEASE NET CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTLSR",
                        "numerator": "NTLS",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTLSQ": {
        "title": "LEASE NET CHARGE-OFFS-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTLSQ"
            }
        ]
    },
    "NTLSQR": {
        "title": "LEASE NET CHARGE-OFFS-QTR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTLSQR",
                        "numerator": "NTLSQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTOTHER": {
        "title": "ALL OTHER LOAN NET CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTOTHER"
            }
        ]
    },
    "NTOTHERR": {
        "title": "ALL OTHER LOAN NET CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTOTHERR",
                        "numerator": "NTOTHER",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTOTHQ": {
        "title": "ALL OTHER LN NET-CHG-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTOTHQ"
            }
        ]
    },
    "NTOTHQR": {
        "title": "ALL OTHER LN NET-CHG-QTRS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTOTHQR",
                        "numerator": "NTOTHQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTRCDSM": {
        "title": "AMT TIME DEP OF $100,000 OR LESS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRCDSM"
            }
        ]
    },
    "NTRCDSMR": {
        "title": "AMT TIME DEP OF $100,000 OR LESS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NTRCDSMR",
                        "numerator": "NTRCDSM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NTRCOMOT": {
        "title": "NONTRANSACTN-COM BKS & OTH U.S.",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRCOMOT"
            }
        ]
    },
    "NTRCOMOTR": {
        "title": "NONTRANSACTN-COM BKS & OTH U.S RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NTRCOMOTR",
                        "numerator": "NTRCOMOT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NTRE": {
        "title": "REAL ESTATE LOAN NET CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRE"
            }
        ]
    },
    "NTREMUQA": {
        "title": "",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTREMUQA"
            }
        ]
    },
    "NTRECOQA": {
        "title": "",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRECOQA"
            }
        ]
    },
    "NTRELNR": {
        "title": "REAL ESTATE LOAN NET CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTRELNR",
                        "numerator": "NTRE",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTREQ": {
        "title": "REAL ESTATE LOAN NET CHARGE-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTREQ"
            }
        ]
    },
    "NTREQA": {
        "title": "REAL ESTATE LOAN NET CHARGE-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTREQA"
            }
        ]
    },
    "NTRERQ": {
        "title": "REAL ESTATE LOAN NET CHARGE-OFFS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTRERQ",
                        "numerator": "NTREQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTREAG": {
        "title": "FARMLAND RE LN NET CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTREAG"
            }
        ]
    },
    "NTREAGR": {
        "title": "FARMLAND RE LN NET CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTREAGR",
                        "numerator": "NTREAG",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTREAGQ": {
        "title": "FARMLAND RE LN NET-CHG-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTREAGQ"
            }
        ]
    },
    "NTREA": {
        "title": "RE LN NET-CHG-ANN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTREA"
            }
        ]
    },
    "NTREAGQR": {
        "title": "FARMLAND RE LN NET-CHG-QTR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTREAGQR",
                        "numerator": "NTREAGQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTRECNFM": {
        "title": "1-4 FAM CONST LN NET-OFF",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRECNFM"
            }
        ]
    },
    "NTRECNOT": {
        "title": "OTHER CONSTRUCT NET CHG-OFF",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRECNOT"
            }
        ]
    },
    "NTRECONQ": {
        "title": "CONSTRUCTION RE LN NET-CHG-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRECONQ"
            }
        ]
    },
    "NTRECONQR": {
        "title": "CONSTRUCTION RE LN NET-CHG-QTR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTRECONQR",
                        "numerator": "NTRECONQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTRECONS": {
        "title": "CONSTRUCTION RE LN NET CHG-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRECONS"
            }
        ]
    },
    "NTRECOSA": {
        "title": "CONST RE LOANS NET-CHG-ANN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRECOSA"
            }
        ]
    },
    "NTRECONSR": {
        "title": "CONSTRUCTION RE LN NET CHG-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTRECONSR",
                        "numerator": "NTRECONS",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTRECOSR": {
        "title": "CONST RE CHG-OFF/CONST RE LOANS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NTRECOSR",
                        "numerator": "NTRECOSA",
                        "denominator": "LNRECON5"
                    }
                }
            }
        ]
    },
    "NTRECOQR": {
        "title": "CONST RE CHG-OFF/CONST RE LOANS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRECOQR"
            }
        ]
    },
    "NTREFOR": {
        "title": "REAL ESTATE LN NET CHG-OFF-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTREFOR"
            }
        ]
    },
    "NTREFORR": {
        "title": "REAL ESTATE LN NET CHG-OFF-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTREFORR",
                        "numerator": "NTREFOR",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTREFORQ": {
        "title": "REAL ESTATE LN NET CHG-OFF-FOR QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTREFORQ"
            }
        ]
    },
    "NTREFORQR": {
        "title": "REAL ESTATE LN NET CHG-OFF-FOR QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTREFORQR",
                        "numerator": "NTREFORQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTRELOC": {
        "title": "LINE OF CREDIT RE LN NET CHG-OFF",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRELOC"
            }
        ]
    },
    "NTRELOCLNR": {
        "title": "LINE OF CREDIT RE LN NET CHG-OFF RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTRELOCLNR",
                        "numerator": "NTRELOC",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTRELOCQ": {
        "title": "LINE OF CREDIT RE LN NET CHG-OFF QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRELOCQ"
            }
        ]
    },
    "NTRELOCA": {
        "title": "LINE OF CREDIT RE LN NET CHG-OFF ANNUALLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRELOCA"
            }
        ]
    },
    "NTRELOCQR": {
        "title": "LINE OF CREDIT RE LN NET CHG-OFF QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTRELOCQR",
                        "numerator": "NTRELOCQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTRELOCRQ": {
        "title": "HOME EQUITY CHG-OFF/HOME EQ LNS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTRELOCR",
                        "numerator": "NTRELOCA",
                        "denominator": "LNRELOC5",
                        "noMultiplier": True
                    }
                }
            }
        ]
    },
    "NTRELOCR": {
        "title": "HOME EQUITY CHG-OFF/HOME EQ LNS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NTRELOCR",
                        "numerator": "NTRELOCA",
                        "denominator": "LNRELOC5"
                    }
                }
            }
        ]
    },
    "NTREMULQ": {
        "title": "MULTIFAMILY RE LN NET-CHG-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTREMULQ"
            }
        ]
    },
    "NTREMULA": {
        "title": "MULTIFAMILY RES RE LN NET-CHG-ANN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTREMULA"
            }
        ]
    },
    "NTREMULQR": {
        "title": "MULTIFAMILY RE LN NET-CHG-QTR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTREMULQR",
                        "numerator": "NTREMULQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTREMULR": {
        "title": "MULTIFAM RE CHG-OFF/MULTI RE LN",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NTREMULR",
                        "numerator": "NTREMULA",
                        "denominator": "LNREMUL5"
                    }
                }
            }
        ]
    },
    "NTREMUQR": {
        "title": "MULTIFAM RE CHG-OFF/MULTI RE LN QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTREMUQR"
            }
        ]
    },
    "NTREMULT": {
        "title": "MULTIFAMLY RES RE LN NET CHG-OFF",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTREMULT"
            }
        ]
    },
    "NTREMULTR": {
        "title": "MULTIFAMLY RES RE LN NET CHG-OFF RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTREMULTR",
                        "numerator": "NTREMULT",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTRENRES": {
        "title": "NONFARM NONRES RE LN NET CHG-OFF",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRENRES"
            }
        ]
    },
    "NTRENRESR": {
        "title": "NONFARM NONRES RE LN NET CHG-OFF RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTRENRESR",
                        "numerator": "NTRENRES",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTRENROT": {
        "title": "OTHER NONFARM NONRS NET CHG-OFF",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRENROT"
            }
        ]
    },
    "NTRENROW": {
        "title": "OWN OCC NONFRM NONRS NET CHG-OFF",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRENROW"
            }
        ]
    },
    "NTRENRSA": {
        "title": "NONFARM NONRES RE LN NET-CHG-ANN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRENRSA"
            }
        ]
    },
    "NTRENRSQ": {
        "title": "NONFARM NONRES RE LN NET-CHG-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRENRSQ"
            }
        ]
    },
    "NTRENRSQR": {
        "title": "NONFARM NONRES RE LN NET-CHG-QTR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTRENRSQR",
                        "numerator": "NTRENRSQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTRENRSR": {
        "title": "NONRES CHG-OFF/NONRES LOANS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NTRENRSR",
                        "numerator": "NTRENRSA",
                        "denominator": "LNRENRE5"
                    }
                }
            }
        ]
    },
    "NTRENRQR": {
        "title": "NONRES CHG-OFF/NONRES LOANS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRENRQR"
            }
        ]
    },
    "NTRENUS": {
        "title": "NON-U.S. RE LN NET CHARGE-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRENUS"
            }
        ]
    },
    "NTRENUSR": {
        "title": "NON-U.S. RE LN NET CHARGE-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTRENUSR",
                        "numerator": "NTRENUS",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTRENUSQ": {
        "title": "NON-U.S. RE LN NET CHARGE-OFFS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRENUSQ"
            }
        ]
    },
    "NTREOTHA": {
        "title": "OTHER 1-4 FAM RE OTHER LN NET-CHG-ANN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTREOTHA"
            }
        ]
    },
    "NTRENUSQR": {
        "title": "NON-U.S. RE LN NET CHARGE-OFFS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTRENUSQR",
                        "numerator": "NTRENUSQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTREOTHR": {
        "title": "OTHER 1-4 FAM RE CHG-OFF/OTH 1-4",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NTREOTHR",
                        "numerator": "NTREOTHA",
                        "denominator": "LNREOTH5"
                    }
                }
            }
        ]
    },
    "NTREOTHRQR": {
        "title": "OTHER 1-4 FAM RE CHG-OFF/OTH 1-4 QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTREOTHRQR",
                        "numerator": "NTREOTQA",
                        "denominator": "LNREOTH2",
                        "noMultiplier": True
                    }
                }
            }
        ]
    },
    "NTREOTQA": {
        "title": "OTHER 1-4 FAM RE CHG-OFF/OTH 1-4 QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTREOTQA"
            }
        ]
    },
    "NTRER": {
        "title": "RE CHARGE-OFF/RE LOANS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NTRER",
                        "numerator": "NTREA",
                        "denominator": "LNRE5"
                    }
                }
            }
        ]
    },
    "NTREQR": {
        "title": "RE CHARGE-OFF/RE LOANS QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTREQR"
            }
        ]
    },
    "NTRERES": {
        "title": "RE LOANS 1-4 FAMILY NET CHG-OFFS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRERES"
            }
        ]
    },
    "NTRERESLNR": {
        "title": "RE LOANS 1-4 FAMILY NET CHG-OFFS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTRERESLNR",
                        "numerator": "NTRERES",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTRERESQ": {
        "title": "RE LOANS 1-4 FAMILY NET-CHG-QTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRERESQ"
            }
        ]
    },
    "NTRERESA": {
        "title": "RE LOANS 1-4 FAMILY NET-CHG-ANN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRERESA"
            }
        ]
    },
    "NTRERESQR": {
        "title": "RE LOANS 1-4 FAMILY NET-CHG-QTR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTRERESQR",
                        "numerator": "NTRERESQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTRERESR": {
        "title": "1-4 FAM RE CHG-OFF/1-4 FAM LOANS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NTRERESR",
                        "numerator": "NTRERESA",
                        "denominator": "LNRERES5"
                    }
                }
            }
        ]
    },
    "NTRERESRQ": {
        "title": "1-4 FAM RE CHG-OFF/1-4 FAM LOANS QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTRERESRQ",
                        "numerator": "NTRERESQ",
                        "denominator": "LNRERES2"
                    }
                }
            }
        ]
    },
    "NTRERSF2": {
        "title": "RE LN 1-4 FAM JR LIEN-NET C/OFF",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRERSF2"
            }
        ]
    },
    "NTRERSF2R": {
        "title": "RE LN 1-4 FAM JR LIEN-NET C/OFF RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTRERSF2R",
                        "numerator": "NTRERSF2",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTRERS2Q": {
        "title": "RE LN 1-4 FAM JR LIEN-NET C/OFF QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRERS2Q"
            }
        ]
    },
    "NTRERS2QR": {
        "title": "RE LN 1-4 FAM JR LIEN-NET C/OFF QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTRERS2QR",
                        "numerator": "NTRERS2Q",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTRERSFM": {
        "title": "RE LN 1-4FAM IST LIEN-NET C/OFF",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRERSFM"
            }
        ]
    },
    "NTRERSFMR": {
        "title": "RE LN 1-4FAM IST LIEN-NET C/OFF RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTRERSFMR",
                        "numerator": "NTRERSFM",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTRERSFQ": {
        "title": "RE LN 1-4FAM IST LIEN-NET C/OFF QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRERSFQ"
            }
        ]
    },
    "NTRERSFQR": {
        "title": "RE LN 1-4FAM IST LIEN-NET C/OFF QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTRERSFQR",
                        "numerator": "NTRERSFQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTREOFFDOM": {
        "title": "REAL ESTATE LOAN NET CHARGE-OFFS DOMESTIC OFFICES",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleAddition",
                    "parameters": {
                        "setField": "NTREOFFDOM",
                        "additionFields": [
                            "NTRECONS",
                            "NTREAG",
                            "NTRERES",
                            "NTREMULT",
                            "NTRENRES"
                        ]
                    }
                }
            }
        ]
    },
    "NTREOFFDOMR": {
        "title": "REAL ESTATE LOAN NET CHARGE-OFFS DOMESTIC OFFICES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTREOFFDOMR",
                        "numerator": "NTREOFFDOM",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "NTREOFFDOMQ": {
        "title": "REAL ESTATE LOAN NET CHARGE-OFFS DOMESTIC OFFICES QUARTERLY",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleAddition",
                    "parameters": {
                        "setField": "NTREOFFDOMQ",
                        "additionFields": [
                            "NTRECONQ",
                            "NTREAGQ",
                            "NTRERESQ",
                            "NTREMULQ",
                            "NTRENRSQ"
                        ]
                    }
                }
            }
        ]
    },
    "NTREOFFDOMQR": {
        "title": "REAL ESTATE LOAN NET CHARGE-OFFS DOMESTIC OFFICES QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTREOFFDOMQR",
                        "numerator": "NTREOFFDOMQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "NTRFC": {
        "title": "NONTRANSACTION-FOR COUNTRY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRFC"
            }
        ]
    },
    "NTRFCFG": {
        "title": "NONTRANSACTION-FOR CNTRY & GOVT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRFCFG"
            }
        ]
    },
    "NTRFCFGR": {
        "title": "NONTRANSACTION-FOR CNTRY & GOVT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NTRFCFGR",
                        "numerator": "NTRFCFG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NTRFG": {
        "title": "NONTRANSACTION-FOR GOVERNMENT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRFG"
            }
        ]
    },
    "NTRSMMDA": {
        "title": "SAVINGS DEP-MMDA",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRSMMDA"
            }
        ]
    },
    "NTRSMMDAR": {
        "title": "SAVINGS DEP-MMDA RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NTRSMMDAR",
                        "numerator": "NTRSMMDA",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NTRSOTH": {
        "title": "SAVINGS DEP-OTHER",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "NTRSOTH"
            }
        ]
    },
    "NTRSOTHR": {
        "title": "SAVINGS DEP-OTHER RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NTRSOTHR",
                        "numerator": "NTRSOTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OAIENC": {
        "title": "INCOME EARNED NOT COLLECTED",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OAIENC"
            }
        ]
    },
    "OALIFGEN": {
        "title": "LIFE INS ASSETS - GENERAL ACC",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OALIFGEN"
            }
        ]
    },
    "OALIFGENR": {
        "title": "LIFE INS ASSETS - GENERAL ACC RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OALIFGENR",
                        "numerator": "OALIFGEN",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OALIFHYB": {
        "title": "LIFE INS ASSETS - HYBRID ACC",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OALIFHYB"
            }
        ]
    },
    "OALIFHYBR": {
        "title": "LIFE INS ASSETS - HYBRID ACC RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OALIFHYBR",
                        "numerator": "OALIFHYB",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OALIFINS": {
        "title": "LIFE INSURANCE ASSETS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OALIFINS"
            }
        ]
    },
    "OALIFINSR": {
        "title": "LIFE INSURANCE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OALIFINSR",
                        "numerator": "OALIFINS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OALIFSEP": {
        "title": "LIFE INS ASSETS - SEPARATE ACC",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OALIFSEP"
            }
        ]
    },
    "OALIFSEPR": {
        "title": "LIFE INS ASSETS - SEPARATE ACC RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OALIFSEPR",
                        "numerator": "OALIFSEP",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OBSDIR": {
        "title": "OFF-BALANCE SHEET DERIVATIVES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OBSDIR"
            }
        ]
    },
    "OBSDIRR": {
        "title": "OFF-BALANCE SHEET DERIVATIVES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OBSDIRR",
                        "numerator": "OBSDIR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OREAG": {
        "title": "ALL OTHER RE OWNED-FARMLAND",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OREAG"
            }
        ]
    },
    "OREAGR": {
        "title": "ALL OTHER RE OWNED-FARMLAND RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OREAGR",
                        "numerator": "OREAG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "ORECONS": {
        "title": "ALL OTHER RE OWNED-CONST",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ORECONS"
            }
        ]
    },
    "ORECONSR": {
        "title": "ALL OTHER RE OWNED-CONST RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ORECONSR",
                        "numerator": "ORECONS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OREGNMA": {
        "title": "ALL OTHER RE OWNED-GNMA LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OREGNMA"
            }
        ]
    },
    "OREINV": {
        "title": "DIRECT & INDIRECT INVEST IN ORE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OREINV"
            }
        ]
    },
    "OREINVR": {
        "title": "DIRECT & INDIRECT INVEST IN ORE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OREINVR",
                        "numerator": "OREINV",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OREMULT": {
        "title": "ALL OTHER RE OWNED-MULTI",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OREMULT"
            }
        ]
    },
    "OREMULTR": {
        "title": "ALL OTHER RE OWNED-MULTI RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OREMULTR",
                        "numerator": "OREMULT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "ORENRES": {
        "title": "ALL OTHER RE OWNED-NONFARM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ORENRES"
            }
        ]
    },
    "ORENRESR": {
        "title": "ALL OTHER RE OWNED-NONFARM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ORENRESR",
                        "numerator": "ORENRES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OREOTH": {
        "title": "OTHER REAL ESTATE OWNED",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OREOTH"
            }
        ]
    },
    "OREOTHR": {
        "title": "OTHER REAL ESTATE OWNED RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OREOTHR",
                        "numerator": "OREOTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OREOTHF": {
        "title": "OTHER REAL ESTATE OWNED-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OREOTHF"
            }
        ]
    },
    "OREOTHFR": {
        "title": "OTHER REAL ESTATE OWNED-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OREOTHFR",
                        "numerator": "OREOTHF",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "ORERES": {
        "title": "ALL OTHER RE OWNED-1-4 FAMILY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ORERES"
            }
        ]
    },
    "ORERESR": {
        "title": "ALL OTHER RE OWNED 1-4 FAMILIY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ORERESR",
                        "numerator": "ORERES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OTHBORF": {
        "title": "OTHER BORROWED MONEY-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OTHBORF"
            }
        ]
    },
    "OTHFFC": {
        "title": "OTHER-FUTURES & FORWARD CONTRACT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OTHFFC"
            }
        ]
    },
    "OTHFFCR": {
        "title": "OTHER-FUTURES & FORWARD CONTRACT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OTHFFCR",
                        "numerator": "OTHFFC",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OTHNVS": {
        "title": "OTHER-NOTIONAL VALUE SWAPS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OTHNVS"
            }
        ]
    },
    "OTHNVSR": {
        "title": "OTHER-NOTIONAL VALUE SWAPS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OTHNVSR",
                        "numerator": "OTHNVS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OTHOFFBS": {
        "title": "ALL OTH OFF-BALANCE SHEET LIAB",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OTHOFFBS"
            }
        ]
    },
    "OTHOFFBSR": {
        "title": "ALL OTH OFF-BALANCE SHEET LIAB RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OTHOFFBSR",
                        "numerator": "OTHOFFBS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OTHPOC": {
        "title": "OTHER-PURCHASED OPTION CONTRACTS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OTHPOC"
            }
        ]
    },
    "OTHPOCR": {
        "title": "OTHER-PURCHASED OPTION CONTRACT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OTHPOCR",
                        "numerator": "OTHPOC",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OTHWOC": {
        "title": "OTHER-WRITTEN OPTION CONTRACTS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OTHWOC"
            }
        ]
    },
    "OTHWOCR": {
        "title": "OTHER-WRITTEN OPTION CONTRACTS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "OTHWOCR",
                        "numerator": "OTHWOC",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "OTSREGNM": {
        "title": "OTS REGION NAME",
        "description": "",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OTSREGNM"
            }
        ]
    },
    "OWNCRCI": {
        "title": "REC OWN INTEREST SEC - CI",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OWNCRCI"
            }
        ]
    },
    "OWNCRCRD": {
        "title": "REC OWN INTEREST SEC - CRCD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OWNCRCRD"
            }
        ]
    },
    "OWNCRHEL": {
        "title": "REC OWN INTEREST SEC - HEL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OWNCRHEL"
            }
        ]
    },
    "OWNDRCI": {
        "title": "C/O OWN INTEREST SEC - CI",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OWNDRCI"
            }
        ]
    },
    "OWNDRCRD": {
        "title": "C/O OWN INTEREST SEC - CRCD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OWNDRCRD"
            }
        ]
    },
    "OWNDRHEL": {
        "title": "C/O OWN INTEREST SEC - HEL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OWNDRHEL"
            }
        ]
    },
    "OWNLNCI": {
        "title": "LN SECURE HELD IN SEC - CI",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OWNLNCI"
            }
        ]
    },
    "OWNLNCRD": {
        "title": "LN SECURE HELD IN SEC - CRCD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OWNLNCRD"
            }
        ]
    },
    "OWNLNHEL": {
        "title": "LN SECURE HELD IN SEC - HEL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OWNLNHEL"
            }
        ]
    },
    "OWNP3CI": {
        "title": "PD 30-89 OWN INTEREST SEC - CI",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OWNP3CI"
            }
        ]
    },
    "OWNP3CRD": {
        "title": "PD 30-89 OWN INTEREST SEC - CRCD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OWNP3CRD"
            }
        ]
    },
    "OWNP3HEL": {
        "title": "PD30-89 OWN INTEREST SEC - HEL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OWNP3HEL"
            }
        ]
    },
    "OWNP9CI": {
        "title": "PD 90 + OWN INTEREST SEC - CI",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OWNP9CI"
            }
        ]
    },
    "OWNP9CRD": {
        "title": "PD 90 + OWN INTEREST SEC - CRCD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OWNP9CRD"
            }
        ]
    },
    "OWNP9HEL": {
        "title": "PD 90 + OWN INTEREST SEC - HEL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OWNP9HEL"
            }
        ]
    },
    "OWNSCCI": {
        "title": "SEC. SECURE HELD IN RC-B - CI",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OWNSCCI"
            }
        ]
    },
    "OWNSCCRD": {
        "title": "SEC. SECURE HELD IN RC-B - CRCD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OWNSCCRD"
            }
        ]
    },
    "OWNSCHEL": {
        "title": "SEC. SECURE HELD IN RC-B - HEL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "OWNSCHEL"
            }
        ]
    },
    "P3AG": {
        "title": "30-89 DAYS P/D-AGRICULTURAL LNS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3AG"
            }
        ]
    },
    "P3AGR": {
        "title": "30-89 DAYS P/D-AGRICULTURAL LNS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3AGR",
                        "numerator": "P3AG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3AGSM": {
        "title": "30-89 DAYS P/D-AG LNS*SMALL BKS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3AGSM"
            }
        ]
    },
    "P3AGSMR": {
        "title": "30-89 DAYS P/D-AG LNS*SMALL BKS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3AGSMR",
                        "numerator": "P3AGSM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3ASSET": {
        "title": "30-89 DAYS P/D-TOTAL ASSETS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3ASSET"
            }
        ]
    },
    "P3ASSETR": {
        "title": "30-89 DAYS P/D TOTAL ASSETS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3ASSETR",
                        "numerator": "P3ASSET",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3AUTO": {
        "title": "30-89 DAYS P/D AUTO LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3AUTO"
            }
        ]
    },
    "P3AUTOR": {
        "title": "30-89 DAYS P/D AUTO LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3AUTOR",
                        "numerator": "P3AUTO",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3CI": {
        "title": "30-89 DAYS P/D-C&I LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3CI"
            }
        ]
    },
    "P3CIR": {
        "title": "30-89 DAYS P/D-C&I LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3CIR",
                        "numerator": "P3CI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3CINUS": {
        "title": "30-89 DAYS P/D-C&I*NON-U.S.",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3CINUS"
            }
        ]
    },
    "P3CINUSR": {
        "title": "30-89 DAYS P/D-C&I*NON-U.S. RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3CINUSR",
                        "numerator": "P3CINUS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3CON": {
        "title": "30-89 DAYS P/D-CONSUMER LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3CON"
            }
        ]
    },
    "P3CONR": {
        "title": "30-89 DAYS P/D-CONSUMER LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3CONR",
                        "numerator": "P3CON",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3CONOTH": {
        "title": "30-89 DAYS P/D-OTHER CONSUMER",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3CONOTH"
            }
        ]
    },
    "P3CONOTHR": {
        "title": "30-89 DAYS P/D-OTHER CONSUMER RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3CONOTHR",
                        "numerator": "P3CONOTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3CRCD": {
        "title": "30-89 DAYS P/D-CREDIT CARD PLANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3CRCD"
            }
        ]
    },
    "P3CRCDR": {
        "title": "30-89 DAYS P/D-CREDIT CARD PLANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3CRCDR",
                        "numerator": "P3CRCD",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3DEP": {
        "title": "30-89 DAYS P/D-DEP INST LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3DEP"
            }
        ]
    },
    "P3DEPR": {
        "title": "30-89 DAYS P/D-DEP INST LOANS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3DEPR",
                        "numerator": "P3DEP",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3DEPNUS": {
        "title": "30-89 DAYS P/D-DEP INST*NON U.S.",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3DEPNUS"
            }
        ]
    },
    "P3DEPNUSR": {
        "title": "30-89 DAYS P/D-DEP INST*NON U.S.",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3DEPNUSR",
                        "numerator": "P3DEPNUS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3FG": {
        "title": "30-89 DAYS P/D-FOREIGN GOVT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3FG"
            }
        ]
    },
    "P3FGR": {
        "title": "30-89 DAYS P/D-FOREIGN GOVT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3FGR",
                        "numerator": "P3FG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3GTY": {
        "title": "30-89 DAYS P/D-GTY LN&LS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3GTY"
            }
        ]
    },
    "P3GTYR": {
        "title": "30-89 DAYS P/D-GTY LN&LS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3GTYR",
                        "numerator": "P3GTY",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3GTYGNM": {
        "title": "30-89 DAY P/D-REBOOKED GNMA LNS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3GTYGNM"
            }
        ]
    },
    "P3GTYGNMR": {
        "title": "30-89 DAY P/D-REBOOKED GNMA LNS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3GTYGNMR",
                        "numerator": "P3GTYGNM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3GTYPAR": {
        "title": "30-89 DAYS P/D-PART GTY LN&LS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3GTYPAR"
            }
        ]
    },
    "P3GTYPARR": {
        "title": "30-89 DAYS P/D-PART GTY LN&LS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3GTYPARR",
                        "numerator": "P3GTYPAR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3LAG": {
        "title": "30-89 DAY P/D AG LOANS-LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3LAG"
            }
        ]
    },
    "P3LAGR": {
        "title": "30-89 DAY P/D AG LOANS-LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3LAGR",
                        "numerator": "P3LAG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3LCI": {
        "title": "30-89 DAYS P/D C&I LNS-LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3LCI"
            }
        ]
    },
    "P3LCIR": {
        "title": "30-89 DAYS P/D C&I LNS-LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3LCIR",
                        "numerator": "P3LCI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3LCON": {
        "title": "30-89 D P/D CONSUMER -LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3LCON"
            }
        ]
    },
    "P3LCONR": {
        "title": "30-89 D P/D CONSUMER -LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3LCONR",
                        "numerator": "P3LCON",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3LGTY": {
        "title": "30-89 P/D PROTECT (GTY)-LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3LGTY"
            }
        ]
    },
    "P3LGTYR": {
        "title": "30-89 P/D PROTECT (GTY)-LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3LGTYR",
                        "numerator": "P3LGTY",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3LNSALE": {
        "title": "30-89 DAYS P/D-L&L HELD FOR SALE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3LNSALE"
            }
        ]
    },
    "P3LNSALER": {
        "title": "30-89 DAYS P/D-L&L HELD FOR SALE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3LNSALER",
                        "numerator": "P3LNSALE",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3LOTH": {
        "title": "30-89 DAYS P/D OTH LNS-LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3LOTH"
            }
        ]
    },
    "P3LOTHR": {
        "title": "30-89 DAYS P/D OTH LNS-LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3LOTHR",
                        "numerator": "P3LOTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3LREAG": {
        "title": "30-89 DAY P/D RE FARM-LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3LREAG"
            }
        ]
    },
    "P3LREAGR": {
        "title": "30-89 DAY P/D RE FARM-LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3LREAGR",
                        "numerator": "P3LREAG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3LRECON": {
        "title": "30-89 P/D CONSTRUCTION -LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3LRECON"
            }
        ]
    },
    "P3LRECONR": {
        "title": "30-89 P/D CONSTRUCTION -LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3LRECONR",
                        "numerator": "P3LRECON",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3LREMUL": {
        "title": "30-89 DAY P/D MULTIFAM -LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3LREMUL"
            }
        ]
    },
    "P3LREMULR": {
        "title": "30-89 DAY P/D MULTIFAM -LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3LREMULR",
                        "numerator": "P3LREMUL",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3LRENRS": {
        "title": "30-89 P/D NONFRM NONRS -LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3LRENRS"
            }
        ]
    },
    "P3LRENRSR": {
        "title": "30-89 P/D NONFRM NONRS -LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3LRENRSR",
                        "numerator": "P3LRENRS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3LRERES": {
        "title": "30-89 D P/D 1-4 FAMILY -LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3LRERES"
            }
        ]
    },
    "P3LRERESR": {
        "title": "30-89 P/D 1-4 FAMILY -LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3LRERESR",
                        "numerator": "P3LRERES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3LS": {
        "title": "30-89 DAYS P/D-LEASES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3LS"
            }
        ]
    },
    "P3LSR": {
        "title": "30-89 DAYS P/D-LEASES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3LSR",
                        "numerator": "P3LS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3LTOT": {
        "title": "30-89 D P/D TOTAL LOANS-LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3LTOT"
            }
        ]
    },
    "P3LTOTR": {
        "title": "30-89 DAYS P/D-TOTAL LOANS-LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3LTOTR",
                        "numerator": "P3LTOT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3OTHLN": {
        "title": "30-89 DAYS P/D-ALL OTHER LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3OTHLN"
            }
        ]
    },
    "P3OTHLNR": {
        "title": "30-89 DAYS P/D-ALL OTHER LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3OTHLNR",
                        "numerator": "P3OTHLN",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3RE": {
        "title": "30-89 DAYS P/D-REAL ESTATE LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3RE"
            }
        ]
    },
    "P3RER": {
        "title": "30-89 DAYS P/D-REAL ESTATE LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3RER",
                        "numerator": "P3RE",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3REAG": {
        "title": "30-89 DAYS P/D-RE*FARMLAND",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3REAG"
            }
        ]
    },
    "P3REAGR": {
        "title": "30-89 DAYS P/D-RE*FARMLAND",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3REAGR",
                        "numerator": "P3REAG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3RECNFM": {
        "title": "30-89 DAYS P/D 1-4 FAM CONSTR LN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3RECNFM"
            }
        ]
    },
    "P3RECNFMR": {
        "title": "30-89 DAYS P/D 1-4 FAM CONSTR LN",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3RECNFMR",
                        "numerator": "P3RECNFM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3RECNOT": {
        "title": "30-89 DAYS P/D OTH CONSTR & LAND",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3RECNOT"
            }
        ]
    },
    "P3RECNOTR": {
        "title": "30-89 DAYS P/D OTH CONSTR & LAND",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3RECNOTR",
                        "numerator": "P3RECNOT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3RECONS": {
        "title": "30-89 DAYS P/D-RE*CONSTRUCTION",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3RECONS"
            }
        ]
    },
    "P3RECONSR": {
        "title": "30-89 DAYS P/D-RE*CONSTRUCTION",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3RECONSR",
                        "numerator": "P3RECON",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3REFOR": {
        "title": "30-89 DAYS P/D-RE*FOREIGN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3REFOR"
            }
        ]
    },
    "P3REFORR": {
        "title": "30-89 DAYS P/D-RE*FOREIGN RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3REFORR",
                        "numerator": "P3REFOR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3RELOC": {
        "title": "30-89 DAYS P/D-RE*1-4 FAM LINES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3RELOC"
            }
        ]
    },
    "P3RELOCR": {
        "title": "30-89 DAYS P/D-RE*1-4 FAM LINES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3RELOCR",
                        "numerator": "P3RELOC",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3REMULT": {
        "title": "30-89 DAYS P/D-RE*MULTIFAMILY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3REMULT"
            }
        ]
    },
    "P3REMULTR": {
        "title": "30-89 DAYS P/D-RE*MULTIFAMILY",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3REMULTR",
                        "numerator": "P3REMULT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3RENRES": {
        "title": "30-89 DAYS P/D-RE*NONFARM NONRES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3RENRES"
            }
        ]
    },
    "P3RENRESR": {
        "title": "30-89 DAYS P/D-RE*NONFARM NONRES",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3RENRESR",
                        "numerator": "P3RENREN",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3RENROT": {
        "title": "30-89 DAYS P/D OTH NONFRM NONRES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3RENROT"
            }
        ]
    },
    "P3RENROTR": {
        "title": "30-89 DAYS P/D OTH NONFRM NONRES",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3RENROTR",
                        "numerator": "P3RENROT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3RENROW": {
        "title": "30-89 DAYS P/D 0WN-OCC NONF NONRS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3RENROW"
            }
        ]
    },
    "P3RENROWR": {
        "title": "30-89 DAYS P/D OWN-OCC NONF NONRS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3RENROWR",
                        "numerator": "P3RENROW",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3RENUS": {
        "title": "30-89 DAYS P/D-RE*NON-U.S.",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3RENUS"
            }
        ]
    },
    "P3RENUSR": {
        "title": "30-89 DAYS P/D-RE*NON-U.S.",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3RENUSR",
                        "numerator": "P3RENUS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3RERES": {
        "title": "30-89 DAYS P/D-RE*1-4 FAMILY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3RERES"
            }
        ]
    },
    "P3RERESR": {
        "title": "30-89 DAYS P/D-RE*1-4 FAMILY",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3RERESR",
                        "numerator": "P3RERES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3RERSF2": {
        "title": "30-89 DAYS P/D-RE*1-4 JN LIEN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3RERSF2"
            }
        ]
    },
    "P3RERSF2R": {
        "title": "30-89 DAYS P/D-RE*1-4 JN LIEN RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3RERSF2R",
                        "numerator": "P3RERSF2",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3RERSFM": {
        "title": "30-89 DAYS P/D-RE*1-4 IST LIEN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3RERSFM"
            }
        ]
    },
    "P3RERSFMR": {
        "title": "30-89 DAYS P/D-RE*1-4 IST LIEN RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3RERSFMR",
                        "numerator": "P3RERSFM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3RSCI": {
        "title": "30-89 DAY P/D RESTRUCT C&I LN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3RSCI"
            }
        ]
    },
    "P3RSCONS": {
        "title": "30-89 P/D RESTRUCT CONSTRUCTION",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3RSCONS"
            }
        ]
    },
    "P3RSLNFM": {
        "title": "30-89 DAY P/D RESTR LN- 1-4 FAM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3RSLNFM"
            }
        ]
    },
    "P3RSLNFMR": {
        "title": "30-89 DAY P/D RESTR LN- 1-4 FAM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3RSLNFMR",
                        "numerator": "P3RSLNFM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3RSLNLS": {
        "title": "30-89 D P/D RESTR LN EXCL1-4 FM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3RSLNLS"
            }
        ]
    },
    "P3RSLNLSR": {
        "title": "30-89 D P/D RESTR LN EXCL1-4 FM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3RSLNLSR",
                        "numerator": "P3RSLNLS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3RSLNLT": {
        "title": "30-89 DAY P/D RESTR LN- TOTAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3RSLNLT"
            }
        ]
    },
    "P3RSLNLTR": {
        "title": "30-89 DAY P/D RESTR LN- TOTAL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3RSLNLTR",
                        "numerator": "P3RSLNLT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P3RSMULT": {
        "title": "30-89 D P/D RESTRUCT MULTIFAM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3RSMULT"
            }
        ]
    },
    "P3RSNRES": {
        "title": "30-89 DAY P/D RESTRUCT NFNR LN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3RSNRES"
            }
        ]
    },
    "P3RSOTH": {
        "title": "30-89 D P/D RESTRUCT ALL OTH LN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3RSOTH"
            }
        ]
    },
    "P3SCDEBT": {
        "title": "30-89 DAYS P/D-DEBT SECURITIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P3SCDEBT"
            }
        ]
    },
    "P3SCDEBTR": {
        "title": "30-89 DAYS P/D-DEBT SECURITIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P3SCDEBTR",
                        "numerator": "P3SCDEBT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9AG": {
        "title": "90+ DAYS P/D-AGRICULTURAL LNS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9AG"
            }
        ]
    },
    "P9AGR": {
        "title": "90+ DAYS P/D-AGRICULTURAL LNS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9AGR",
                        "numerator": "P9AG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9AGSM": {
        "title": "90+ DAYS P/D-AG LNS*SMALL BKS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9AGSM"
            }
        ]
    },
    "P9AGSMR": {
        "title": "90+ DAYS P/D-AG LNS*SMALL BKS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9AGSMR",
                        "numerator": "P9AGSM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9ASSET": {
        "title": "90+ DAYS P/D-TOTAL ASSETS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9ASSET"
            }
        ]
    },
    "P9ASSETR": {
        "title": "90+ DAYS P/D-TOTAL ASSETS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9ASSETR",
                        "numerator": "P9ASSET",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9AUTO": {
        "title": "90+ DAYS P/D AUTO LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9AUTO"
            }
        ]
    },
    "P9AUTOR": {
        "title": "90+ DAYS P/D AUTO LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9AUTOR",
                        "numerator": "P9AUTO",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9CI": {
        "title": "90+ DAYS P/D-C&I LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9CI"
            }
        ]
    },
    "P9CIR": {
        "title": "90+ DAYS P/D-C&I LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9CIR",
                        "numerator": "P9CI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9CINUS": {
        "title": "90+ DAYS P/D-C&I*NON-U.S.",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9CINUS"
            }
        ]
    },
    "P9CINUSR": {
        "title": "90+ DAYS P/D-C&I*NON-U.S. RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9CINUSR",
                        "numerator": "P9CINUS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9CON": {
        "title": "90+ DAYS P/D-CONSUMER LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9CON"
            }
        ]
    },
    "P9CONR": {
        "title": "90+ DAYS P/D-CONSUMER LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9CONR",
                        "numerator": "P9CON",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9CONOTH": {
        "title": "90+ DAYS P/D-OTHER CONSUMER",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9CONOTH"
            }
        ]
    },
    "P9CONOTHR": {
        "title": "90+ DAYS P/D-OTHER CONSUMER RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9CONOTHR",
                        "numerator": "P9CONOTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9CRCD": {
        "title": "90+ DAYS P/D-CREDIT CARD PLANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9CRCD"
            }
        ]
    },
    "P9CRCDR": {
        "title": "90+ DAYS P/D-CREDIT CARD PLANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9CRCDR",
                        "numerator": "P9CRCD",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9DEP": {
        "title": "90+ DAYS P/D-DEP INST LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9DEP"
            }
        ]
    },
    "P9DEPR": {
        "title": "90+ DAYS P/D-DEP INST LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9DEPR",
                        "numerator": "P9DEP",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9DEPNUS": {
        "title": "90+ DAYS P/D-DEP INST*NON U.S.",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9DEPNUS"
            }
        ]
    },
    "P9DEPNUSR": {
        "title": "90+ DAYS P/D-DEP INST*NON U.S. RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9DEPNUSR",
                        "numerator": "P9DEPNUS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9FG": {
        "title": "90+ DAYS P/D-FOREIGN GOVT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9FG"
            }
        ]
    },
    "P9FGR": {
        "title": "90+ DAYS P/D-FOREIGN GOVT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9FGR",
                        "numerator": "P9FG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9GTY": {
        "title": "90+ DAYS P/D-GTY LN&LS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9GTY"
            }
        ]
    },
    "P9GTYR": {
        "title": "90+ DAYS P/D-GTY LN&LS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9GTYR",
                        "numerator": "P9GTY",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9GTYGNM": {
        "title": "90+ DAYS P/D-REBOOKED GNMA LNS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9GTYGNM"
            }
        ]
    },
    "P9GTYGNMR": {
        "title": "90+ DAY P/D-REBOOKED GNMA LNS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9GTYGNMR",
                        "numerator": "P9GTYGNM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9GTYPAR": {
        "title": "90+ DAYS P/D-PART GTY LN&LS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9GTYPAR"
            }
        ]
    },
    "P9GTYPARR": {
        "title": "90+ DAYS P/D-PART GTY LN&LS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9GTYPARR",
                        "numerator": "P9GTYPAR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9LAG": {
        "title": "90+ DAYS P/D AG LOANS-LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9LAG"
            }
        ]
    },
    "P9LAGR": {
        "title": "90+ DAYS P/D AG LOANS-LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9LAGR",
                        "numerator": "P9LAG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9LCI": {
        "title": "90+DAYS P/D C&I LNS-LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9LCI"
            }
        ]
    },
    "P9LCIR": {
        "title": "90+ DAYS P/D C&I LNS-LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9LCIR",
                        "numerator": "P9LCI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9LCON": {
        "title": "90+ D P/D CONSUMER LN - LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9LCON"
            }
        ]
    },
    "P9LCONR": {
        "title": "90+ D P/D CONSUMER LN - LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9LCONR",
                        "numerator": "P9LCON",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9LGTY": {
        "title": "90+ D P/D PROTECT (GTY)-LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9LGTY"
            }
        ]
    },
    "P9LGTYR": {
        "title": "90+ D P/D PROTECT (GTY)-LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9LGTYR",
                        "numerator": "P9LGTY",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9LNSALE": {
        "title": "90 DAYS P/D-L&L HELD FOR SALE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9LNSALE"
            }
        ]
    },
    "P9LNSALER": {
        "title": "90+ DAYS P/D-L&L HELD FOR SALE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9LNSALER",
                        "numerator": "P9LNSALE",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9LOTH": {
        "title": "90+ DAYS P/D OTHER LNS-LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9LOTH"
            }
        ]
    },
    "P9LOTHR": {
        "title": "90+ DAYS P/D OTHER LNS-LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9LOTHR",
                        "numerator": "P9LOTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9LREAG": {
        "title": "90+ DAY P/D RE FARM-LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9LREAG"
            }
        ]
    },
    "P9LREAGR": {
        "title": "90+ DAY P/D RE FARM-LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9LREAGR",
                        "numerator": "P9LREAG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9LRECON": {
        "title": "90+ D P/D CONSTRUCTION -LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9LRECON"
            }
        ]
    },
    "P9LRECONR": {
        "title": "90+ D P/D CONSTRUCTION -LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9LRECONR",
                        "numerator": "P9LRECON",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9LREMUL": {
        "title": "90+ DAY P/D MULTIFAM - LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9LREMUL"
            }
        ]
    },
    "P9LREMULR": {
        "title": "90+ DAY P/D MULTIFAM - LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9LREMULR",
                        "numerator": "P9LREMUL",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9LRENRS": {
        "title": "90+ D P/D NFNR - LOSS SHARE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9LRENRS"
            }
        ]
    },
    "P9LRENRSR": {
        "title": "90+ D P/D NFNR - LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9LRENRSR",
                        "numerator": "P9LRENRS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9LRERES": {
        "title": "90+ D P/D 1-4 FAMILY - LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9LRERES"
            }
        ]
    },
    "P9LRERESR": {
        "title": "90+ D P/D 1-4 FAMILY - LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9LRERESR",
                        "numerator": "P9LRERES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9LS": {
        "title": "90+ DAYS P/D-LEASES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9LS"
            }
        ]
    },
    "P9LSR": {
        "title": "90+ DAYS P/D-LEASES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9LSR",
                        "numerator": "P9LS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9LTOT": {
        "title": "90+ D P/D TOTAL LOANS - LOSS SH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9LTOT"
            }
        ]
    },
    "P9LTOTR": {
        "title": "90+ D P/D TOTAL LOANS - LOSS SH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9LTOTR",
                        "numerator": "P9LTOT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9OTHLN": {
        "title": "90+ DAYS P/D-ALL OTHER LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9OTHLN"
            }
        ]
    },
    "P9OTHLNR": {
        "title": "90+ DAYS P/D-ALL OTHER LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9OTHLNR",
                        "numerator": "P9OTHLN",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9RE": {
        "title": "90+ DAYS P/D-REAL ESTATE LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9RE"
            }
        ]
    },
    "P9RER": {
        "title": "90+ DAYS P/D-REAL ESTATE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9RER",
                        "numerator": "P9RE",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9REAG": {
        "title": "90+ DAYS P/D-RE*FARMLAND",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9REAG"
            }
        ]
    },
    "P9REAGR": {
        "title": "90+ DAYS P/D-RE*FARMLAND",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9REAGR",
                        "numerator": "P9REAG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9RECNFM": {
        "title": "90+ DAYS P/D 1-4 FAM CONSTRUC LN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9RECNFM"
            }
        ]
    },
    "P9RECNFMR": {
        "title": "90+ DAYS P/D 1-4 FAM CONSTRUC LN RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9RECNFMR",
                        "numerator": "P9RECNFM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9RECNOT": {
        "title": "90+ DAYS P/D OTHER CONSTR & LAND",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9RECNOT"
            }
        ]
    },
    "P9RECNOTR": {
        "title": "90+ DAYS P/D OTHER CONSTR & LAND RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9RECNOTR",
                        "numerator": "P9RECNOT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9RECONS": {
        "title": "90+ DAYS P/D-RE*CONSTRUCTION",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9RECONS"
            }
        ]
    },
    "P9RECONSR": {
        "title": "90+ DAYS P/D-RE*CONSTRUCTION RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9RECONSR",
                        "numerator": "P9RECONS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9REFOR": {
        "title": "90 + DAYS P/D-RE*FOREIGN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9REFOR"
            }
        ]
    },
    "P9REFORR": {
        "title": "90+ DAYS P/D-RE*FOREIGN RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9REFORR",
                        "numerator": "P9REFOR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9RELOC": {
        "title": "90+ DAYS P/D-RE*1-4 FAM LINES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9RELOC"
            }
        ]
    },
    "P9RELOCR": {
        "title": "90+ DAYS P/D-RE*1-4 FAM LINES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9RELOCR",
                        "numerator": "P9RELOC",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9REMULT": {
        "title": "90+ DAYS P/D-RE*MULTIFAMILY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9REMULT"
            }
        ]
    },
    "P9REMULTR": {
        "title": "90+ DAYS P/D-RE*MULTIFAMILY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9REMULTR",
                        "numerator": "P9REMULT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9RENRES": {
        "title": "90+ DAYS P/D-RE*NONFARM NONRES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9RENRES"
            }
        ]
    },
    "P9RENRESR": {
        "title": "90+ DAYS P/D-RE*NONFARM NONRES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9RENRESR",
                        "numerator": "P9RENRES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9RENROT": {
        "title": "90+ DAYS P/D OTHER NONFRM NONRES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9RENROT"
            }
        ]
    },
    "P9RENROTR": {
        "title": "90+ DAYS P/D OTHER NONFRM NONRES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9RENROTR",
                        "numerator": "P9RENROT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9RENROW": {
        "title": "90+ DAYS P/D 0WN-OCC NONFR NONRS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9RENROW"
            }
        ]
    },
    "P9RENROWR": {
        "title": "90+ DAYS P/D OWN-OCC NONFR NONRS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9RENROWR",
                        "numerator": "P9RENROW",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9RENUS": {
        "title": "90+ DAYS P/D-RE*NON-U.S.",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9RENUS"
            }
        ]
    },
    "P9RENUSR": {
        "title": "90+ DAYS P/D-RE*NON-U.S.",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9RENUSR",
                        "numerator": "P9RENUS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9RERES": {
        "title": "90+ DAYS P/D-RE*1-4 FAMILY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9RERES"
            }
        ]
    },
    "P9RERESR": {
        "title": "90+ DAYS P/D-RE*1-4 FAMILY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9RERESR",
                        "numerator": "P9RERES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9RERSF2": {
        "title": "90+ DAYS P/D-RE*1-4 JN LIEN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9RERSF2"
            }
        ]
    },
    "P9RERSF2R": {
        "title": "90+ DAYS P/D-RE*1-4 JN LIEN RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9RERSF2R",
                        "numerator": "P9RERSF2",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9RERSFM": {
        "title": "90+ DAYS P/D-RE*1-4 IST LIEN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9RERSFM"
            }
        ]
    },
    "P9RERSFMR": {
        "title": "90+ DAYS P/D-RE*1-4 IST LIEN RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9RERSFMR",
                        "numerator": "P9RERSFM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9RSCI": {
        "title": "90+ DAY P/D RESTRUCT C&I LN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9RSCI"
            }
        ]
    },
    "P9RSCONS": {
        "title": "90+ D P/D RESTRUCT CONSTRUCTION",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9RSCONS"
            }
        ]
    },
    "P9RSLNFM": {
        "title": "90+ DAYS P/D RESTR LN- 1-4 FAM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9RSLNFM"
            }
        ]
    },
    "P9RSLNFMR": {
        "title": "90+ DAYS P/D RESTR LN- 1-4 FAM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9RSLNFMR",
                        "numerator": "P9RSLNFM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9RSLNLS": {
        "title": "90+ DAY P/D RESTRU LN EXCL 1-4 FM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9RSLNLS"
            }
        ]
    },
    "P9RSLNLSR": {
        "title": "90+ DAY P/D RESTRU LN EXCL 1-4 FM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9RSLNLSR",
                        "numerator": "P9RSLNLS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9RSLNLT": {
        "title": "90+ DAY P/D RESTR LN- TOTAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9RSLNLT"
            }
        ]
    },
    "P9RSLNLTR": {
        "title": "90+ DAY P/D RESTR LN- TOTAL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9RSLNLTR",
                        "numerator": "P9RSLNLT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "P9RSMULT": {
        "title": "90+ DAY P/D RESTRUCT MULTIFAM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9RSMULT"
            }
        ]
    },
    "P9RSNRES": {
        "title": "90+ DAY P/D RESTRUCT NFNR LN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9RSNRES"
            }
        ]
    },
    "P9RSOTH": {
        "title": "90+ D P/D RESTRUCT ALL OTH LN",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9RSOTH"
            }
        ]
    },
    "P9SCDEBT": {
        "title": "90+ DAYS P/D-DEBT SECURITIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "P9SCDEBT"
            }
        ]
    },
    "P9SCDEBTR": {
        "title": "90+ DAYS P/D-DEBT SECURITIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "P9SCDEBTR",
                        "numerator": "P9SCDEBT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "PARTACQU": {
        "title": "PARTICIPATIONS ACQUIRED",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "PARTACQU"
            }
        ]
    },
    "PARTCONV": {
        "title": "PARTICIPATIONS CONVEYED",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "PARTCONV"
            }
        ]
    },
    "PARTCONVR": {
        "title": "PARTICIPATIONS CONVEYED RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "PARTCONVR",
                        "numerator": "PARTCONV",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "RB2LNRES": {
        "title": "ALLOWANCE FOR L&L IN TIER 2",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RB2LNRES"
            }
        ]
    },
    "RB2LNRESR": {
        "title": "ALLOWANCE FOR L&L IN TIER 2 RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "RB2LNRESR",
                        "numerator": "RB2LNRES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "RBC": {
        "title": "RBC-TOTAL-PCA",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RBC"
            }
        ]
    },
    "RBCT1": {
        "title": "TIER 1 RBC-PCA",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RBCT1"
            }
        ]
    },
    "RBCT2": {
        "title": "RBC-TIER2-PCA",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RBCT2"
            }
        ]
    },
    "RBCT2R": {
        "title": "RBC-TIER2-PCA RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "RBCT2R",
                        "numerator": "RBCT2",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "RBCT1C": {
        "title": "RC-R COMMON EQ TIER 1 CAPITAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RBCT1C"
            }
        ]
    },
    "RBCT1CER": {
        "title": "COMMON EQUITY TIER 1 RATIO",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RBCT1CER"
            }
        ]
    },
    "RBCT1J": {
        "title": "TIER 1 RBC ADJUSTED LLR - PCA",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RBCT1J"
            }
        ]
    },
    "RBCT1JR": {
        "title": "TIER 1 RBC ADJUSTED LLR - PCA RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "RBCT1JR",
                        "numerator": "RBCT1J",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "RBC1AAJ": {
        "title": "LEVERAGE RATIO-PCA",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "RBC1AAJ",
                        "numerator": "RBCT1",
                        "denominator": "AVASSETJ"
                    }
                }
            }
        ]
    },
    "RBC1AAQR": {
        "title": "LEVERAGE RATIO-PCA QUARTERLY",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleDivision",
                    "parameters": {
                        "setField": "RBC1AAQR",
                        "numerator": "RBCT1",
                        "denominator": "AVASSETJ"
                    }
                }
            }
        ]
    },
    "RBC1RWAJ": {
        "title": "TIER 1 RBC RATIO-PCA",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RBC1RWAJ"
            }
        ]
    },
    "RBCRWAJ": {
        "title": "TOTAL RBC RATIO-PCA",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "RBCRWAJ",
                        "numerator": "RBC",
                        "denominator": "RWAJT"
                    }
                }
            }
        ]
    },
    "RBCRWAQR": {
        "title": "TOTAL RBC QUARTERLY RATIO-PCA",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleDivision",
                    "parameters": {
                        "setField": "RBCRWAQR",
                        "numerator": "RBC",
                        "denominator": "RWAJT"
                    }
                }
            }
        ]
    },
    "REPOPURF": {
        "title": "REPURCHASE AGREEMENT-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "REPOPURF"
            }
        ]
    },
    "REPOSLDF": {
        "title": "REVERSE REPURCHASE AGREEMENT-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "REPOSLDF"
            }
        ]
    },
    "ROEINJR": {
        "title": "RETAINED EARNINGS/AVG BK EQUITY",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ROEINJR",
                        "numerator": "NTIRTA",
                        "denominator": "EQ5"
                    }
                }
            }
        ]
    },
    "RSCI": {
        "title": "RESTRUCTURED LN - C&I",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RSCI"
            }
        ]
    },
    "RSCONS": {
        "title": "RESTRUCTURED LN - CONSTRUCTION",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RSCONS"
            }
        ]
    },
    "RSLNLS": {
        "title": "RESTRUCTURED LN EXCL 1-4 FM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RSLNLS"
            }
        ]
    },
    "RSLNLSR": {
        "title": "RESTRUCTURED LN EXCL 1-4 FM RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "RSLNLSR",
                        "numerator": "RSLNLS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "RSLNLTOT": {
        "title": "RESTRUCTURED LOANS - TOTAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RSLNLTOT"
            }
        ]
    },
    "RSLNLTOTR": {
        "title": "RESTRUCTURED LOANS - TOTAL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "RSLNLTOTR",
                        "numerator": "RSLNLTOT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "RSLNREFM": {
        "title": "RESTRUCTURED LOANS - 1-4 FAMILY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RSLNREFM"
            }
        ]
    },
    "RSLNREFMR": {
        "title": "RESTRUCTURED LOANS - 1-4 FAMILY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "RSLNREFMR",
                        "numerator": "RSLNREFM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "RSMULT": {
        "title": "RESTRUCTURED LN - MULTIFAMILY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RSMULT"
            }
        ]
    },
    "RSNRES": {
        "title": "RESTRUCT LN - NONFARM NONRES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RSNRES"
            }
        ]
    },
    "RSOTHER": {
        "title": "RESTRUCTURED LN - ALL OTHER",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RSOTHER"
            }
        ]
    },
    "RSSDID": {
        "title": "FEDERAL RESERVE ID NUMBER",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RSSDID"
            }
        ]
    },
    "RT": {
        "title": "INTEREST RATE-TOTAL CONTRACTS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RT"
            }
        ]
    },
    "RTR": {
        "title": "CR DER (NET)-PURCHASE PROTECT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "RTR",
                        "numerator": "RT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "RTFFC": {
        "title": "INT RATE-FUTURES & FORWARD CONTR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RTFFC"
            }
        ]
    },
    "RTFFCR": {
        "title": "INT RATE-FUTURES & FORWARD CONTR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "RTFFCR",
                        "numerator": "RTFFC",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "RTNVS": {
        "title": "INT RATE-SWAPS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RTNVS"
            }
        ]
    },
    "RTNVSR": {
        "title": "INT RATE-SWAP RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "RTNVSR",
                        "numerator": "RTNVS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "RTPOC": {
        "title": "INT RATE-PUR OPTION CONTRACTS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RTPOC"
            }
        ]
    },
    "RTPOCR": {
        "title": "INT RATE-PUR OPTION CONTRACTS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "RTPOCR",
                        "numerator": "RTPOC",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "RTWOC": {
        "title": "INT RATE-WRITTEN OPTION CONTRACT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RTWOC"
            }
        ]
    },
    "RTWOCR": {
        "title": "INT RATE-WRITTEN OPTION CONTRACT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "RTWOCR",
                        "numerator": "RTWOC",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "RWAJ": {
        "title": "RWA-ADJUST-PCA-T1 & CET1 RATIO",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RWAJ"
            }
        ]
    },
    "RWAJT": {
        "title": "RWA-ADJUSTED-PCA-TOTAL RBC RAT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "RWAJT"
            }
        ]
    },
    "RWAJTR": {
        "title": "RWA-ADJUSTED-PCA-TOTAL RBC RAT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "RWAJTR",
                        "numerator": "RWAJT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCABS": {
        "title": "ABS-TOTAL-B/S",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCABS"
            }
        ]
    },
    "SCABSR": {
        "title": "ABS-TOTAL-B/S RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCABSR",
                        "numerator": "SCABS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCAF": {
        "title": "SECURITIES-AF",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCAF"
            }
        ]
    },
    "SCAFR": {
        "title": "SECURITIES-AF RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCAFR",
                        "numerator": "SCAF",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCAOT": {
        "title": "U.S. AGENCY ALL OTH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCAOT"
            }
        ]
    },
    "SCCMMB": {
        "title": "COMMERCIAL MBS - TOTAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCCMMB"
            }
        ]
    },
    "SCCMOG": {
        "title": "OTHER COMMERCIAL MBS-GOVT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCCMOG"
            }
        ]
    },
    "SCCMOGR": {
        "title": "OTHER COMMERCIAL MBS-GOVT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCCMOGR",
                        "numerator": "SCCMOG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCCMOT": {
        "title": "OTHER COMMERCIAL MBS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCCMOT"
            }
        ]
    },
    "SCCMOTR": {
        "title": "OTHER COMMERCIAL MBS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCCMOTR",
                        "numerator": "SCCMOT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCCMPT": {
        "title": "COMMERCIAL MBS PASS-THROUGH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCCMPT"
            }
        ]
    },
    "SCCMPTR": {
        "title": "COMMERCIAL MBS PASS-THROUGH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleDivision",
                    "parameters": {
                        "setField": "SCCMPTR",
                        "numerator": "SCCMPT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCCOL": {
        "title": "U.S. AGENCY COLLATERAL MTG-RES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCCOL"
            }
        ]
    },
    "SCCOLR": {
        "title": "U.S. AGENCY COLLATERAL MTG-RES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCOOLR",
                        "numerator": "SCCOL",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCCPTG": {
        "title": "COMM MBS PASS-THRU-GOVT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCCPTG"
            }
        ]
    },
    "SCCPTGR": {
        "title": "COMM MBS PASS-THRU-GOVT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCCPTGR",
                        "numerator": "SCCPTG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCEQFV": {
        "title": "EQ SEC READILY DET FV",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCEQFV"
            }
        ]
    },
    "SCEQFVR": {
        "title": "EQ SEC READILY DET FV RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCEQFVR",
                        "numerator": "SCEQFV",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCFMN": {
        "title": "U.S. AGENCY ISSUED*FNMA-RES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCFMN"
            }
        ]
    },
    "SCFMNR": {
        "title": "U.S. AGENCY ISSUED*FNMA-RES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCFMNR",
                        "numerator": "SCFMN",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCGNM": {
        "title": "U.S. AGENCY GTY BY GNMA",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCGNM"
            }
        ]
    },
    "SCGNMR": {
        "title": "U.S. AGENCY GTY BY GNMA RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCGNMR",
                        "numerator": "SCGNM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCGTY": {
        "title": "U.S. AGENCY ISSUED OR GTY-RES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCGTY"
            }
        ]
    },
    "SCGTYR": {
        "title": "U.S. AGENCY ISSUED OR GTY-RES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCGTYR",
                        "numerator": "SCGTY",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCHA": {
        "title": "SECURITIES-HA",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCHA"
            }
        ]
    },
    "SCHAR": {
        "title": "SECURITIES-HA RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCHAR",
                        "numerator": "SCHA",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCHTMRES": {
        "title": "LESS ALLOW FOR CREDIT LOSSES ON HELD TO MATURITY DEBT SECURITIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCHTMRES"
            }
        ]
    },
    "SCHTMRESR": {
        "title": "LESS ALLOW FOR CREDIT LOSSES ON HELD TO MATURITY DEBT SECURITIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCHTMRESR",
                        "numerator": "SCHTMRES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCLENT": {
        "title": "SECURITIES LENT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCLENT"
            }
        ]
    },
    "SCLENTR": {
        "title": "SECURITIES LENT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCLENTR",
                        "numerator": "SCLENT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCNM1T3": {
        "title": "NONMTG DEBT SEC * 1-3 YEARS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCNM1T3"
            }
        ]
    },
    "SCNM1T3R": {
        "title": "NONMTG DEBT SEC * 1-3 YEARS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCNM1T3R",
                        "numerator": "SCNM1T3",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCNM3LES": {
        "title": "NONMTG DEBT SEC*3 MONS OR LESS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCNM3LES"
            }
        ]
    },
    "SCNM3LESR": {
        "title": "NONMTG DEBT SEC*3 MONS OR LESS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCNM3LESR",
                        "numerator": "SCNM3LES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCNM3T5": {
        "title": "NONMTG DEBT SEC * 3-5 YEARS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCNM3T5"
            }
        ]
    },
    "SCNM3T5R": {
        "title": "NONMTG DEBT SEC * 3-5 YEARS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCNM3T5R",
                        "numerator": "SCNM3T5",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCNM3T12": {
        "title": "NONMTG DEBT SEC * 3-12 MONTHS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCNM3T12"
            }
        ]
    },
    "SCNM3T12R": {
        "title": "NONMTG DEBT SEC * 3-12 MONTHS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCNM3T12R",
                        "numerator": "SCNM3T12",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCNM5T15": {
        "title": "NONMTG DEBT SEC * 5-15 YEARS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCNM5T15"
            }
        ]
    },
    "SCNM5T15R": {
        "title": "NONMTG DEBT SEC * 5-15 YEARS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCNM5T15R",
                        "numerator": "SCNM5T15",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCNMOV15": {
        "title": "NONMTG DEBT SEC * OVER 15 YEARS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCNMOV15"
            }
        ]
    },
    "SCNMOV15R": {
        "title": "NONMTG DEBT SEC * OVER 15 YEARS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCNMOV15R",
                        "numerator": "SCNMOV15",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCO3YLES": {
        "title": "OTH MORTGAGE SEC * 3 YR OR LESS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCO3YLES"
            }
        ]
    },
    "SCO3YLESR": {
        "title": "OTH MORTGAGE SEC * 3 YR OR LESS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCO3YLESR",
                        "numerator": "SCO3YLES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SC1LES": {
        "title": "Fixed and floating rate debt securities (included above) with remaining maturity of one year or less",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SC1LES"
            }
        ]
    },
    "SC1LESR": {
        "title": "Fixed and floating rate debt securities (included above) with remaining maturity of one year or less ratio",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SC1LESR",
                        "numerator": "SC1LES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCODOT": {
        "title": "OTH DOM DEBT*ALL OTHER",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCODOT"
            }
        ]
    },
    "SCODOTR": {
        "title": "OTH DOM DEBT*ALL OTHER RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCODOTR",
                        "numerator": "SCODOT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCODPI": {
        "title": "CMO PRIV ISSUED",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCODPI"
            }
        ]
    },
    "SCODPIR": {
        "title": "CMO PRIV ISSUED RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCODPIR",
                        "numerator": "SCODPI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCOOV3Y": {
        "title": "OTH MORTGAGE SEC * OVER 3 YRS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCOOV3Y"
            }
        ]
    },
    "SCOOV3YR": {
        "title": "OTH MORTGAGE SEC * OVER 3 YRS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCOOV3YR",
                        "numerator": "SCOOV3Y",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCPLEDGE": {
        "title": "PLEDGED SECURITIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCPLEDGE"
            }
        ]
    },
    "SCPLEDGER": {
        "title": "PLEDGED SECURITIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCPLEDGER",
                        "numerator": "SCPLEDGE",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCPT1T3": {
        "title": "MTG PASS-THRU SEC * 1-3 YEARS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCPT1T3"
            }
        ]
    },
    "SCPT1T3R": {
        "title": "MTG PASS-THRU SEC * 1-3 YEARS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCPT1T3R",
                        "numerator": "SCPT1T3",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCPT3LES": {
        "title": "MTG PASS-THRU SEC*3 MON OR LESS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCPT3LES"
            }
        ]
    },
    "SCPT3LESR": {
        "title": "MTG PASS-THRU SEC*3 MON OR LESS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCPT3LES",
                        "numerator": "SCPT3LESR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCPT3T5": {
        "title": "MTG PASS-THRU SEC * 3-5 YEARS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCPT3T5"
            }
        ]
    },
    "SCPT3T5R": {
        "title": "MTG PASS-THRU SEC * 3-5 YEARS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCPT3T5R",
                        "numerator": "SCPT3T5",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCPT3T12": {
        "title": "MTG PASS-THRU SEC * 3-12 MONTHS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCPT3T12"
            }
        ]
    },
    "SCPT3T12R": {
        "title": "MTG PASS-THRU SEC * 3-12 MONTHS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCPT3T12R",
                        "numerator": "SCPT3T12",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCPT5T15": {
        "title": "MTG PASS-THRU SEC * 5-15 YEARS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCPT5T15"
            }
        ]
    },
    "SCPT5T15R": {
        "title": "MTG PASS-THRU SEC * 5-15 YEARS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCPT5T15R",
                        "numerator": "SCPT5T15",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCPTOV15": {
        "title": "MTG PASS-THRU SEC * OVER 15 YRS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCPTOV15"
            }
        ]
    },
    "SCPTOV15R": {
        "title": "MTG PASS-THRU SEC * OVER 15 YRS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCPTOV15R",
                        "numerator": "SCPTOV15",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCRDEBT": {
        "title": "DEBT SECURITIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCRDEBT"
            }
        ]
    },
    "SCRDEBTR": {
        "title": "DEBT SECURITIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCRDEBTR",
                        "numerator": "SCRDEBT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCSFP": {
        "title": "STRUCTURED FIN PROD - TOTAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCSFP"
            }
        ]
    },
    "SCSFPR": {
        "title": "STRUCTURED FIN PROD - TOTAL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCSFPR",
                        "numerator": "SCSFP",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCSNHAA": {
        "title": "STRUCTURED NOTES AMORTIZED COST",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCSNHAA"
            }
        ]
    },
    "SCSNHAAR": {
        "title": "STRUCTURED NOTES AMORTIZED COST RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCSNHAAR",
                        "numerator": "SCSNHAA",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCSNHAF": {
        "title": "STRUCTURED NOTES-FAIR VALUE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCSNHAF"
            }
        ]
    },
    "SCSNHAFR": {
        "title": "STRUCTURED NOTES-FAIR VALUE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SCSNHAFR",
                        "numerator": "SCSNHAF",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SCSPN": {
        "title": "U.S. AGENCY GOVT SPONSORED",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SCSPN"
            }
        ]
    },
    "SZ30AUTO": {
        "title": "30-89 PD LN-SECURITIZATION-AUTO",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ30AUTO"
            }
        ]
    },
    "SZ30AUTOR": {
        "title": "30-89 PD LN-SECURITIZATION-AUTO RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZ30AUTOR",
                        "numerator": "SZ30AUTO",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZ30CI": {
        "title": "30-89 PD LN-SECURITIZATION-CI",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ30CI"
            }
        ]
    },
    "SZ30CIR": {
        "title": "30-89 PD LN-SECURITIZATION-CI RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZ30CIR",
                        "numerator": "SZ30CI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZ30CON": {
        "title": "30-89 PD LN-SECURITIZATION-CON",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ30CON"
            }
        ]
    },
    "SZ30CONR": {
        "title": "30-89 PD LN-SECURITIZATION-CON RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZ30CONR",
                        "numerator": "SZ30CON",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZ30CRCD": {
        "title": "30-89 PD LN-SECURITIZATION-CRCD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ30CRCD"
            }
        ]
    },
    "SZ30CRCDR": {
        "title": "30-89 PD LN-SECURITIZATION-CRCD RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZ30CRCDR",
                        "numerator": "SZ30CRCD",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZ30HEL": {
        "title": "30-89 PD LN-SECURITIZATION-HEL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ30HEL"
            }
        ]
    },
    "SZ30HELR": {
        "title": "30-89 PD LN-SECURITIZATION-HEL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZ30HELR",
                        "numerator": "SZ30HEL",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZ30OTH": {
        "title": "30-89 PD LN-SECURITIZATION-OTH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ30OTH"
            }
        ]
    },
    "SZ30OTHR": {
        "title": "30-89 PD LN-SECURITIZATION-OTH RATIO",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZ30OTHR",
                        "numerator": "SZ30OTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZ30RES": {
        "title": "30-89 PD LN-SECURITIZATION -RES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ30RES"
            }
        ]
    },
    "SZ30RESR": {
        "title": "30-89 PD LN-SECURITIZATION -RES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZ30RESR",
                        "numerator": "SZ30RES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZ90AUTO": {
        "title": "90 + PD LN-SECURITIZATION-AUTO",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ90AUTO"
            }
        ]
    },
    "SZ90AUTOR": {
        "title": "90 + PD LN-SECURITIZATION-AUTO RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZ90AUTOR",
                        "numerator": "SZ90AUTO",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZ90CI": {
        "title": "90 + PD LN-SECURITIZATION-CI",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ90CI"
            }
        ]
    },
    "SZ90CIR": {
        "title": "90 + PD LN-SECURITIZATION-CI RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZ90CIR",
                        "numerator": "SZ90CI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZ90CON": {
        "title": "90 + PD LN-SECURITIZATION-CON",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ90CON"
            }
        ]
    },
    "SZ90CONR": {
        "title": "90 + PD LN-SECURITIZATION-CON RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZ90CONR",
                        "numerator": "SZ90CON",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZ90CRCD": {
        "title": "90 + PD LN-SECURITIZATION-CRCD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ90CRCD"
            }
        ]
    },
    "SZ90CRCDR": {
        "title": "90 + PD LN-SECURITIZATION-CRCD RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZ90CRCDR",
                        "numerator": "SZ90CRCD",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZ90HEL": {
        "title": "90+ PD LN-SECURITIZATION-HEL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ90HEL"
            }
        ]
    },
    "SZ90HELR": {
        "title": "90+ PD LN-SECURITIZATION-HEL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZ90HELR",
                        "numerator": "SZ90HEL",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZ90OTH": {
        "title": "90 + PD LN-SECURITIZATION-OTH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ90OTH"
            }
        ]
    },
    "SZ90OTHR": {
        "title": "90 + PD LN-SECURITIZATION-OTH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZ90OTHR",
                        "numerator": "SZ90OTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZ90RES": {
        "title": "90 + PD LN-SECURITIZATION-RES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZ90RES"
            }
        ]
    },
    "SZ90RESR": {
        "title": "90 + PD LN-SECURITIZATION-RES RATION",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZ90RESR",
                        "numerator": "SZ90RES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZCRAUTO": {
        "title": "REC ASSET SECURITIZATION-AUTO",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZCRAUTO"
            }
        ]
    },
    "SZCRAUTOR": {
        "title": "REC ASSET SECURITIZATION-AUTO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZCRAUTOR",
                        "numerator": "SZCRAUTO",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZCRCDFE": {
        "title": "OUTSTDG CC FEES IN SECURITZD CC",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZCRCDFE"
            }
        ]
    },
    "SZCRCDFER": {
        "title": "OUTSTDG CC FEES IN SECURITZD CC RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZCRCDFER",
                        "numerator": "SZCRCDFE",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZCRCI": {
        "title": "REC ASSET SECURITIZATION-CI",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZCRCI"
            }
        ]
    },
    "SZCRCIR": {
        "title": "REC ASSET SECURITIZATION-CI RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZCRCIR",
                        "numerator": "SZCRCI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZCRCON": {
        "title": "REC ASSET SECURITIZATION-CON",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZCRCON"
            }
        ]
    },
    "SZCRCONR": {
        "title": "REC ASSET SECURITIZATION-CON RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZCRCONR",
                        "numerator": "SZCRCON",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZCRCRCD": {
        "title": "REC ASSET SECURITIZATION - CRCD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZCRCRCD"
            }
        ]
    },
    "SZCRCRCDR": {
        "title": "REC ASSET SECURITIZATION - CRCD RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZCRCRCDR",
                        "numerator": "SZCRCRCD",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZCRHEL": {
        "title": "RE PRIN SEC ASSET SOLD-HEL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZCRHEL"
            }
        ]
    },
    "SZCRHELR": {
        "title": "RE PRIN SEC ASSET SOLD-HEL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZCRHELR",
                        "numerator": "SZCRHEL",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZCROTH": {
        "title": "REC ASSET SECURITIZATION-",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZCROTH"
            }
        ]
    },
    "SZCROTHR": {
        "title": "REC ASSET SECURITIZATION- RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZCROTHR",
                        "numerator": "SZCROTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZCRRES": {
        "title": "REC ASSET SECURITIZATION-RES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZCRRES"
            }
        ]
    },
    "SZCRRESR": {
        "title": "REC ASSET SECURITIZATION-RES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZCRRESR",
                        "numerator": "SZCRRES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZDRAUTO": {
        "title": "C/O ON ASSET SECURITIZATION-AUTO",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZDRAUTO"
            }
        ]
    },
    "SZDRAUTOR": {
        "title": "C/O ON ASSET SECURITIZATION-AUTO RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZDRAUTOR",
                        "numerator": "SZDRAUTO",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZDRCI": {
        "title": "C/O ON ASSET SECURITIZATION-CI",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZDRCI"
            }
        ]
    },
    "SZDRCIR": {
        "title": "C/O ON ASSET SECURITIZATION-CI RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZDRCIR",
                        "numerator": "SZDRCI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZDRCON": {
        "title": "C/O ON ASSET SECURITIZATION-CON",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZDRCON"
            }
        ]
    },
    "SZDRCONR": {
        "title": "C/O ON ASSET SECURITIZATION-CON RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZDRCONR",
                        "numerator": "SZDRCON",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZDRCRCD": {
        "title": "C/O ON ASSET SECURITIZATION-CRCD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZDRCRCD"
            }
        ]
    },
    "SZDRCRCDR": {
        "title": "C/O ON ASSET SECURITIZATION-CRCD RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZDRCRCDR",
                        "numerator": "SZDRCRCD",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZDRHEL": {
        "title": "C/O ON ASSET SECURITIZATION-HEL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZDRHEL"
            }
        ]
    },
    "SZDRHELR": {
        "title": "C/O ON ASSET SECURITIZATION-HEL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZDRHELR",
                        "numerator": "SZDRHEL",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZDROTH": {
        "title": "C/O ON ASSET SECURITIZATION-OTH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZDROTH"
            }
        ]
    },
    "SZDROTHR": {
        "title": "C/O ON ASSET SECURITIZATION-OTH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZDROTHR",
                        "numerator": "SZDROTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZDRRES": {
        "title": "C/O ON ASSET SECURITIZATION-RES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZDRRES"
            }
        ]
    },
    "SZISLAUT": {
        "title": "CR EXP ON SECURITIZATN - AUTO",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZISLAUT"
            }
        ]
    },
    "SZISLAUTR": {
        "title": "CR EXP ON SECURITIZATN - AUTO RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZISLAUTR",
                        "numerator": "SZISLAUT",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZISLCCD": {
        "title": "CR EXP ON SECURITIZATN - CRCD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZISLCCD"
            }
        ]
    },
    "SZISLCCDR": {
        "title": "CR EXP ON SECURITIZATN - CRCD RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZISLCCDR",
                        "numerator": "SZISLCCD",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZISLCI": {
        "title": "CR EXP ON SECURITIZATN -CI",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZISLCI"
            }
        ]
    },
    "SZISLCIR": {
        "title": "CR EXP ON SECURITIZATN -CI RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZISLCIR",
                        "numerator": "SZISLCI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZISLCON": {
        "title": "CR EXP ON SECURITIZATN - CON",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZISLCON"
            }
        ]
    },
    "SZISLCONR": {
        "title": "CR EXP ON SECURITIZATN - CON RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZISLCONR",
                        "numerator": "SZISLCON",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZISLHEL": {
        "title": "CR EXP ON SECURITIZATN - HEL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZISLHEL"
            }
        ]
    },
    "SZISLHELR": {
        "title": "CR EXP ON SECURITIZATN - HEL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZISLRESR",
                        "numerator": "SZISLRES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZISLOTH": {
        "title": "CR EXP ON SECURITIZATN -OTH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZISLOTH"
            }
        ]
    },
    "SZISLOTHR": {
        "title": "CR EXP ON SECURITIZATN -OTH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZISLOTHR",
                        "numerator": "SZISLOTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZISLRES": {
        "title": "CR EXP ON SECURITIZATION RES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZISLRES"
            }
        ]
    },
    "SZISLRESR": {
        "title": "CR EXP ON SECURITIZATION RES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZISLRESR",
                        "numerator": "SZISLRES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZLAUTO": {
        "title": "RE PRIN SEC ASSET SOLD - AUTO",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZLAUTO"
            }
        ]
    },
    "SZLAUTOR": {
        "title": "RE PRIN SEC ASSET SOLD - AUTO RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZLAUTOR",
                        "numerator": "SZLAUTO",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZLNCI": {
        "title": "RE PRIN SEC ASSET SOLD - CI",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZLNCI"
            }
        ]
    },
    "SZLNCIR": {
        "title": "RE PRIN SEC ASSET SOLD - CI RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZLNCIR",
                        "numerator": "SZLNCI",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZLNCON": {
        "title": "RE PRIN SEC ASSET SOLD - CONS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZLNCON"
            }
        ]
    },
    "SZLNCONR": {
        "title": "RE PRIN SEC ASSET SOLD - CONS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZLNCONR",
                        "numerator": "SZLNCON",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZLNCRCD": {
        "title": "RE PRIN SEC ASSET SOLD - CRCD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZLNCRCD"
            }
        ]
    },
    "SZLNCRCDR": {
        "title": "RE PRIN SEC ASSET SOLD - CRCD RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZLNCRCDR",
                        "numerator": "SZLNCRCD",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZLNHEL": {
        "title": "RE PRIN SEC ASSET SOLD - HEL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZLNHEL"
            }
        ]
    },
    "SZLNHELR": {
        "title": "RE PRIN SEC ASSET SOLD - HEL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZLNHELR",
                        "numerator": "SZLNHEL",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZLNOTH": {
        "title": "RE PRIN SEC ASSET SOLD - OTH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZLNOTH"
            }
        ]
    },
    "SZLNOTHR": {
        "title": "RE PRIN SEC ASSET SOLD - OTH RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZLNOTHR",
                        "numerator": "SZLNOTH",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZLNRES": {
        "title": "RE PRIN SEC ASSET SOLD-RES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZLNRES"
            }
        ]
    },
    "SZLNRESR": {
        "title": "RE PRIN SEC ASSET SOLD-RES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "SZLNRESR",
                        "numerator": "SZLNRES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "SZUCAUTO": {
        "title": "COMMITS FOR LIQUIDITY  - AUTO",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZUCAUTO"
            }
        ]
    },
    "SZUCCI": {
        "title": "COMMITS FOR LIQUIDITY  - CI",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZUCCI"
            }
        ]
    },
    "SZUCCON": {
        "title": "COMMITS FOR LIQUIDITY  - CON",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZUCCON"
            }
        ]
    },
    "SZUCCRCD": {
        "title": "COMMITS FOR LIQUIDITY  - CRCD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZUCCRCD"
            }
        ]
    },
    "SZUCHEL": {
        "title": "COMMITS FOR LIQUIDITY - HEL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZUCHEL"
            }
        ]
    },
    "SZUCOTH": {
        "title": "COMMITS FOR LIQUIDITY  - OTH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZUCOTH"
            }
        ]
    },
    "SZUCRES": {
        "title": "COMMITS FOR LIQUIDITY  - RES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "SZUCRES"
            }
        ]
    },
    "TCAMA": {
        "title": "CORP TRUST-MANAGED-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCAMA"
            }
        ]
    },
    "TCAMANUM": {
        "title": "CORP TRUST-MANAGED-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCAMANUM"
            }
        ]
    },
    "TCANMA": {
        "title": "CORP TRUST-NON-MANAGED-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCANMA"
            }
        ]
    },
    "TCANMNUM": {
        "title": "CORP TRUST-NON-MANAGED-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCANMNUM"
            }
        ]
    },
    "TCANUM": {
        "title": "CORP TRUST-TRUSTEESHIPS-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCANUM"
            }
        ]
    },
    "TCANUMD": {
        "title": "CORP & MUNI-TRUSTEE-DEFAULT-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCANUMD"
            }
        ]
    },
    "TCAPAO": {
        "title": "CORP TRUST-TRUSTEESHIPS-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCAPAO"
            }
        ]
    },
    "TCAPAOD": {
        "title": "CORP & MUNI-TRUSTEE-DEFAULT-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCAPAOD"
            }
        ]
    },
    "TCATNUM": {
        "title": "CORP TRUST-TRANSFER-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCATNUM"
            }
        ]
    },
    "TCDEMV": {
        "title": "CIFS -DOM EQUITY-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCDEMV"
            }
        ]
    },
    "TCDENUM": {
        "title": "CIFS -DOM EQUITY-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCDENUM"
            }
        ]
    },
    "TCIEMV": {
        "title": "CIFS -INTL/GLOBAL-EQ-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCIEMV"
            }
        ]
    },
    "TCIENUM": {
        "title": "CIFS -INTL/GLOBAL-EQ-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCIENUM"
            }
        ]
    },
    "TCMBMV": {
        "title": "CIFS-MUNICIPAL BOND-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCMBMV"
            }
        ]
    },
    "TCMBNUM": {
        "title": "CIFS-MUNICIPAL BOND-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCMBNUM"
            }
        ]
    },
    "TCSBMV": {
        "title": "CIFS -STOCK/BOND-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCSBMV"
            }
        ]
    },
    "TCSBNUM": {
        "title": "CIFS -STOCK/BOND-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCSBNUM"
            }
        ]
    },
    "TCSNMA": {
        "title": "CUST AND SAFE ACCT-NON-MAN-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCSNMA"
            }
        ]
    },
    "TCSNMNUM": {
        "title": "CUST AND SAFE ACCT-NON-MAN-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCSNMNUM"
            }
        ]
    },
    "TCSOMV": {
        "title": "CIFS-SPECIALTY/OTHER-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCSOMV"
            }
        ]
    },
    "TCSONUM": {
        "title": "CIFS-SPECIALTY/OTHER-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCSONUM"
            }
        ]
    },
    "TCSTMV": {
        "title": "CIFS-SHORT TERM INV-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCSTMV"
            }
        ]
    },
    "TCSTNUM": {
        "title": "CIFS-SHORT TERM INV-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCSTNUM"
            }
        ]
    },
    "TCTBMV": {
        "title": "CIFS - TAXABLE BOND-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCTBMV"
            }
        ]
    },
    "TCTBNUM": {
        "title": "CIFS - TAXABLE BOND-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCTBNUM"
            }
        ]
    },
    "TCTOTMV": {
        "title": "CIFS-TOTAL-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCTOTMV"
            }
        ]
    },
    "TCTOTNUM": {
        "title": "CIFS-TOTAL-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TCTOTNUM"
            }
        ]
    },
    "TEBMA": {
        "title": "EMP BENE-DEF BENE-MANAGE-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TEBMA"
            }
        ]
    },
    "TEBMANUM": {
        "title": "EMP BENE-DEF BENE-MANAGED-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TEBMANUM"
            }
        ]
    },
    "TEBNMA": {
        "title": "EMP BENE-DEF BENE-NON-MAN-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TEBNMA"
            }
        ]
    },
    "TEBNMNUM": {
        "title": "EMP BENE-DEF BENE-NON-MAN-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TEBNMNUM"
            }
        ]
    },
    "TECMA": {
        "title": "EMP BENE-CONTRIB-MANAGED-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TECMA"
            }
        ]
    },
    "TECMANUM": {
        "title": "EMP BENE-CONTRI-MANAGED-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TECMANUM"
            }
        ]
    },
    "TECNMA": {
        "title": "EMP BENE-CONTRI-NON-MAN-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TECNMA"
            }
        ]
    },
    "TECNMNUM": {
        "title": "EMP BENE-CONTRI-NON-MANAGE-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TECNMNUM"
            }
        ]
    },
    "TECPS": {
        "title": "EMP BEN & RET TR - COM & PF STK",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TECPS"
            }
        ]
    },
    "TEEQF": {
        "title": "EMP BEN & RET TR - EQ MUT FUND",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TEEQF"
            }
        ]
    },
    "TEI": {
        "title": "EMP BEN & RET TR - INT BEARING",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TEI"
            }
        ]
    },
    "TEMATOT": {
        "title": "EMP BEN & RET TR-TOT MANAGE AST",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TEMATOT"
            }
        ]
    },
    "TEMISC": {
        "title": "EMP BEN & RET TR - MISC ASSET",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TEMISC"
            }
        ]
    },
    "TEMMF": {
        "title": "EMP BEN & RET TR - MONEY MKT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TEMMF"
            }
        ]
    },
    "TENI": {
        "title": "EMP BEN & RET TR - NONINT BEAR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TENI"
            }
        ]
    },
    "TEOTHB": {
        "title": "EMP BEN & RET TR-OTH NOTE & BND",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TEOTHB"
            }
        ]
    },
    "TEOTHF": {
        "title": "EMP BEN & RET TR - OTH MUT FUND",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TEOTHF"
            }
        ]
    },
    "TERE": {
        "title": "EMP BEN & RET TR - REAL ESTATE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TERE"
            }
        ]
    },
    "TEREMTG": {
        "title": "EMP BEN & RET TR - RE MTG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TEREMTG"
            }
        ]
    },
    "TESCMUN": {
        "title": "EMP BEN & RET TR - MUNI",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TESCMUN"
            }
        ]
    },
    "TESCUS": {
        "title": "EMP BEN & RET TR -U.S TREAS & OB",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TESCUS"
            }
        ]
    },
    "TESTO": {
        "title": "EMP BEN & RET TR - SHRT TERM OB",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TESTO"
            }
        ]
    },
    "TETOT": {
        "title": "EXPENSE FIDUCIARY - YTD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TETOT"
            }
        ]
    },
    "TETRF": {
        "title": "EMP BEN & RET TR - TRUST FUND",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TETRF"
            }
        ]
    },
    "TEUF": {
        "title": "EMP BEN & RET TR - UNREG FUNDS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TEUF"
            }
        ]
    },
    "TFEMA": {
        "title": "FOUNDATION & ENDOW-MANAGED-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TFEMA"
            }
        ]
    },
    "TFEMANUM": {
        "title": "FOUNDATION & ENDOW-MANAGED-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TFEMANUM"
            }
        ]
    },
    "TFENMA": {
        "title": "FOUNDATION & END-NON-MANAGE-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TFENMA"
            }
        ]
    },
    "TFENMNUM": {
        "title": "FOUNDATION & END-NON-MANAGE-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TFENMNUM"
            }
        ]
    },
    "TICA": {
        "title": "GR.INC-CORP TRUST & AGENCY-YTD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TICA"
            }
        ]
    },
    "TICS": {
        "title": "GR.INC-CUSTODY-YTD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TICS"
            }
        ]
    },
    "TIEB": {
        "title": "GR.INC-EMP. BENEFIT-BENEFIT-YTD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TIEB"
            }
        ]
    },
    "TIEC": {
        "title": "GR.INC-EMP. BENEFIT- CONTRI-YTD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TIEC"
            }
        ]
    },
    "TIFE": {
        "title": "GR. INC- FOUNDATION & ENDOW-YTD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TIFE"
            }
        ]
    },
    "TIMA": {
        "title": "GR.INC - INVESTMENT AGCY - YTD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TIMA"
            }
        ]
    },
    "TIMMA": {
        "title": "INVESTMENT AGENCY-MANAGED-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TIMMA"
            }
        ]
    },
    "TIMMANUM": {
        "title": "INVESTMENT AGENCY-MANAGED-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TIMMANUM"
            }
        ]
    },
    "TIMNMA": {
        "title": "INVESTMENT AGCY NON-MANAGED-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TIMNMA"
            }
        ]
    },
    "TIMNMNUM": {
        "title": "INVESTMENT AGCY NON-MANAGED-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TIMNMNUM"
            }
        ]
    },
    "TINTRA": {
        "title": "INTRACOMPANY INC FIDUCIARY-YTD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TINTRA"
            }
        ]
    },
    "TIOF": {
        "title": "GR.INC-OTHER FIDUCIARY-YTD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TIOF"
            }
        ]
    },
    "TIOR": {
        "title": "GR.INC-OTHER RETIREMENT -YTD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TIOR"
            }
        ]
    },
    "TIP": {
        "title": "GR.INC-PERSONAL & AG ACCTS-YTD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TIP"
            }
        ]
    },
    "TIR": {
        "title": "GR.INC-RELATED SERV-YTD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TIR"
            }
        ]
    },
    "TITOTF": {
        "title": "TOT FOREIGN OFF GROSS FIDUC-YTD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TITOTF"
            }
        ]
    },
    "TMAF": {
        "title": "FIDUCIARY FGN OFF-MANAGED-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TMAF"
            }
        ]
    },
    "TMAFNUM": {
        "title": "FIDUCIARY FGN OFF-MANAGED-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TMAFNUM"
            }
        ]
    },
    "TMASMF": {
        "title": "ADVISED/SPONSORED MUT FND -AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TMASMF"
            }
        ]
    },
    "TMASMFN": {
        "title": "ADVISED/SPONSORED MUTAL FND-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TMASMFN"
            }
        ]
    },
    "TNI": {
        "title": "NET FIDUCIARY INCOME -YTD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TNI"
            }
        ]
    },
    "TNL": {
        "title": "NET LOSS FROM FIDUCIARY-YTD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TNL"
            }
        ]
    },
    "TNMAF": {
        "title": "FIDUCIARY FGN OFF-NON-MAN-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TNMAF"
            }
        ]
    },
    "TNMNUMF": {
        "title": "FIDUCIARY FGN OFF-NON-MAN-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TNMNUMF"
            }
        ]
    },
    "TOCPS": {
        "title": "ALL OTH MAN ASSET-COM & PFD STK",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TOCPS"
            }
        ]
    },
    "TOEQF": {
        "title": "ALL OTH MANAGE AST - EQ MUT FND",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TOEQF"
            }
        ]
    },
    "TOFMA": {
        "title": "OTH FIDUCIARY-MANAGED-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TOFMA"
            }
        ]
    },
    "TOFMANUM": {
        "title": "OTH FIDUCIARY-MANAGED-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TOFMANUM"
            }
        ]
    },
    "TOFNMA": {
        "title": "OTH FIDUCIARY NON-MANAGED-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TOFNMA"
            }
        ]
    },
    "TOFNMNUM": {
        "title": "OTH FIDUCIARY-NON-MANAGED-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TOFNMNUM"
            }
        ]
    },
    "TOI": {
        "title": "ALL OTH MANAGE ASSET - INT BEAR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TOI"
            }
        ]
    },
    "TOMATOT": {
        "title": "ALL OTHER MANAGED ASSET- TOTAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TOMATOT"
            }
        ]
    },
    "TOMISC": {
        "title": "ALL OTH MAN ASSET - MISC ASSET",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TOMISC"
            }
        ]
    },
    "TOMMF": {
        "title": "ALL OTH MANAGE AST - MONEY MKT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TOMMF"
            }
        ]
    },
    "TONI": {
        "title": "ALL OTH MAN ASSET - NONINT BEAR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TONI"
            }
        ]
    },
    "TOOTHB": {
        "title": "ALL OTH MAN AST -OTH NOTE & BND",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TOOTHB"
            }
        ]
    },
    "TOOTHF": {
        "title": "ALL OTH MAN ASSET - OTH MUT FND",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TOOTHF"
            }
        ]
    },
    "TORE": {
        "title": "ALL OTH MAN ASSET - REAL ESTATE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TORE"
            }
        ]
    },
    "TOREMTG": {
        "title": "ALL OTHER MANAGE ASSET - RE MTG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TOREMTG"
            }
        ]
    },
    "TORMA": {
        "title": "OTH RETIREMENT-MANAGED-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TORMA"
            }
        ]
    },
    "TORMANUM": {
        "title": "OTH RETIREMENT-MANAGED-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TORMANUM"
            }
        ]
    },
    "TORNMA": {
        "title": "OTH RETIREMENT-NON-MAN-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TORNMA"
            }
        ]
    },
    "TORNMNUM": {
        "title": "OTH RETIREMENT-NON-MAN-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TORNMNUM"
            }
        ]
    },
    "TOSCMUN": {
        "title": "ALL OTHER MANAGED ASSET - MUNI",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TOSCMUN"
            }
        ]
    },
    "TOSCUS": {
        "title": "ALL OTH MAN AST-U.S. TREAS & OB",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TOSCUS"
            }
        ]
    },
    "TOSTO": {
        "title": "ALL OTH MAN AST - SHRT TERM OBL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TOSTO"
            }
        ]
    },
    "TOTRF": {
        "title": "ALL OTH MAN ASSET - TRUST FUND",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TOTRF"
            }
        ]
    },
    "TOUF": {
        "title": "ALL OTH MAN ASSET - UNREG FUNDS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TOUF"
            }
        ]
    },
    "TPICPS": {
        "title": "PER TR & INV AGY- COM & PRF STK",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TPICPS"
            }
        ]
    },
    "TPIEQF": {
        "title": "PER TR & INV AGY - EQ MUT FUND",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TPIEQF"
            }
        ]
    },
    "TPII": {
        "title": "PER TR & INV AGY - INT BEARING",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TPII"
            }
        ]
    },
    "TPIMATOT": {
        "title": "PER TR & INV AGY-TOT MANAGE AST",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TPIMATOT"
            }
        ]
    },
    "TPIMISC": {
        "title": "PER TR & INV AGY - MISC",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TPIMISC"
            }
        ]
    },
    "TPIMMF": {
        "title": "PER TR & INV AGY - MONEY MKT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TPIMMF"
            }
        ]
    },
    "TPINI": {
        "title": "PER TR & INV AGY-NONINT BEARING",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TPINI"
            }
        ]
    },
    "TPIOTHB": {
        "title": "PER TR & INV AGY-OTH NOTE & BND",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TPIOTHB"
            }
        ]
    },
    "TPIOTHF": {
        "title": "PER TR & INV AGY - OTH MUT FUND",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TPIOTHF"
            }
        ]
    },
    "TPIRE": {
        "title": "PER TR & INV AGY - REAL ESTATE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TPIRE"
            }
        ]
    },
    "TPIREMTG": {
        "title": "PER TR & INV AGY - RE MTG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TPIREMTG"
            }
        ]
    },
    "TPISCMUN": {
        "title": "PER TR & INV AGY - MUNI",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TPISCMUN"
            }
        ]
    },
    "TPISCUS": {
        "title": "PER TR & INV AGY-U.S TREAS & OB",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TPISCUS"
            }
        ]
    },
    "TPISTO": {
        "title": "PER TR & INV AGY - SHRT TERM OB",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TPISTO"
            }
        ]
    },
    "TPITRF": {
        "title": "PER TR & INV AGY - TRUST FUND",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TPITRF"
            }
        ]
    },
    "TPIUF": {
        "title": "PER TR & INV AGY- UNREG FUNDS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TPIUF"
            }
        ]
    },
    "TPMA": {
        "title": "MANAGED ASSET-PER & AGEN-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TPMA"
            }
        ]
    },
    "TPMANUM": {
        "title": "MANAGED ASSET - PER&AGEN-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TPMANUM"
            }
        ]
    },
    "TPNMA": {
        "title": "NON-MANAGED - PER&AGEN-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TPNMA"
            }
        ]
    },
    "TPNMNUM": {
        "title": "NON-MANAGED ASSET-PER&AGEN-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TPNMNUM"
            }
        ]
    },
    "TREXER": {
        "title": "TRUST POWERS EXERCISED",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TREXER"
            }
        ]
    },
    "TRFOR": {
        "title": "TRADING ACCOUNTS-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRFOR"
            }
        ]
    },
    "TRHMA": {
        "title": "IRA",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRHMA"
            }
        ]
    },
    "TRHMANUM": {
        "title": "IRA",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRHMANUM"
            }
        ]
    },
    "TRHNMA": {
        "title": "IRA",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRHNMA"
            }
        ]
    },
    "TRHNMNUM": {
        "title": "IRA",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRHNMNUM"
            }
        ]
    },
    "TRLREVAL": {
        "title": "TRADE-DERIVATIVES NEG VAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRLREVAL"
            }
        ]
    },
    "TRLREVALR": {
        "title": "TRADE-DERIVATED NEG VAL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "TRLREVALR",
                        "numerator": "TRLREVAL",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "TRNCBO": {
        "title": "TRANSACTION-COM BKS& OTHER",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRNCBO"
            }
        ]
    },
    "TRNCBOR": {
        "title": "TRANSACTION-COM BKS& OTHER RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "TRNCBOR",
                        "numerator": "TRNCBO",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "TRNFC": {
        "title": "TRANSACTION-FOR COUNTRY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRNFC"
            }
        ]
    },
    "TRNFCFG": {
        "title": "TRANSACTION-FOR COUNTRY & GOVT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRNFCFG"
            }
        ]
    },
    "TRNFCFGR": {
        "title": "TRANSACTION-FOR COUNTRY & GOVT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "TRNFCFGR",
                        "numerator": "TRNFCFG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "TRNFG": {
        "title": "TRANSACTION-FOREIGN GOVERNMENT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRNFG"
            }
        ]
    },
    "TRNNIA": {
        "title": "AMT NON-INTEREST BEARING TRANSACTION ACC MORE THAN $250,000",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRNNIA"
            }
        ]
    },
    "TRNNIAR": {
        "title": "AMT NON-INTEREST BEARING TRANSACTION ACC MORE THAN $250,000",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "TRNNIAR",
                        "numerator": "TRNNIA",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "TRNNIN": {
        "title": "NUM NON-INTEREST BEARING TRANSACTION ACC MORE THAN $250,000",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRNNIN"
            }
        ]
    },
    "TRPOWER": {
        "title": "INSTITUTION HAS TRUST POWER",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRPOWER"
            }
        ]
    },
    "TRREVALD": {
        "title": "TRADE-DERIV POS VAL-DOM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRREVALD"
            }
        ]
    },
    "TRREVALF": {
        "title": "TRADE-DERIV POS VALUE-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TRREVALF"
            }
        ]
    },
    "TRREVALSUM": {
        "title": "REVALUATION GAINS ON OFF-BALANCE SHEET CONTRACTS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleAddition",
                    "parameters": {
                        "setField": "TRREVALSUM",
                        "additionFields": [
                            "TRREVALD",
                            "TRREVALF"
                        ]
                    }
                }
            }
        ]
    },
    "TRREVALSUMR": {
        "title": "REVALUATION GAINS ON OFF-BALANCE SHEET CONTRACTS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def TRREVALD = ctx.TRREVALD ?: 0;\ndef TRREVALF = ctx.SCCPTG ?: 0;\ndef ASSET = ctx.ASSET ?: 0;\nctx.TRREVALSUMR = 0;\nif (ASSET > 0) {\n  ctx.TRREVALSUMR = ((double)(TRREVALD + TRREVALF) / ASSET);\n}\n"
                    }
                }
            }
        ]
    },
    "TTMA": {
        "title": "TOT FIDUCIARY ACCTS-MAN-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TTMA"
            }
        ]
    },
    "TTNANUM": {
        "title": "TOT FIDUCIARY ACCTS-MAN-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TTNANUM"
            }
        ]
    },
    "TTNMA": {
        "title": "TOT FIDUCIARY ACCTS-NON-MAN-AMT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TTNMA"
            }
        ]
    },
    "TTNMNUM": {
        "title": "TOT FIDUCIARY ACCTS-NON-MAN-NUM",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "TTNMNUM"
            }
        ]
    },
    "UC": {
        "title": "UNUSED COMMIT-TOTAL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UC"
            }
        ]
    },
    "UCR": {
        "title": "UNUSED COMMIT-TOTAL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "UCR",
                        "numerator": "UC",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "UCCOMRE": {
        "title": "UNUSED COMMIT-COM RE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UCCOMRE"
            }
        ]
    },
    "UCCOMRER": {
        "title": "UNUSED COMMIT-COM RE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "UCCOMRER",
                        "numerator": "UCCOMRE",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "UCCOMRES": {
        "title": "UNUSED COMMIT-SECURED COM RE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UCCOMRES"
            }
        ]
    },
    "UCCOMRESR": {
        "title": "UNUSED COMMIT-SECURED COM RE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "UCCOMRESR",
                        "numerator": "UCCOMRES",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "UCCOMREU": {
        "title": "UNUSED COMMIT-UNSECURED COM RE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UCCOMREU"
            }
        ]
    },
    "UCCOMREUR": {
        "title": "UNUSED COMMIT-UNSECURED COM RE RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "UCCOMREUR",
                        "numerator": "UCCOMREU",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "UCCRCD": {
        "title": "UNUSED COMMIT-CREDIT CARD LINES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UCCRCD"
            }
        ]
    },
    "UCCRCDR": {
        "title": "UNUSED COMMIT-CREDIT CARD LINES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "UCCRCDR",
                        "numerator": "UCCRCD",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "UCLN": {
        "title": "UNUSED COMMIT-TOTAL LOANS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UCLN"
            }
        ]
    },
    "UCLOC": {
        "title": "UNUSED COMMIT-HOME EQUITY LINES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UCLOC"
            }
        ]
    },
    "UCLOCR": {
        "title": "UNUSED COMMIT-HOME EQUITY LINES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "UCLOCR",
                        "numerator": "UCLOC",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "UCOTHER": {
        "title": "UNUSED COMMIT-ALL OTHER",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UCOTHER"
            }
        ]
    },
    "UCOTHERR": {
        "title": "UNUSED COMMIT-ALL OTHER RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "UCOTHER",
                        "numerator": "UCOTHE",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "UCOVER1": {
        "title": "UNUSED COM-OVER 1 YR-RC-R COL A",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UCOVER1"
            }
        ]
    },
    "UCOVER1R": {
        "title": "UNUSED COM-OVER 1 YR-RC-R COL A RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "UCOVER1R",
                        "numerator": "UCOVER1",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "UCSC": {
        "title": "UNUSED COMMIT-SEC UNDERWRITING",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UCSC"
            }
        ]
    },
    "UCSCR": {
        "title": "UNUSED COMMIT-SEC UNDERWRITING RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "UCSCR",
                        "numerator": "UCSC",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "UCSZAUTO": {
        "title": "UNUSED COMMIT FOR SECUR. - AUTO",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UCSZAUTO"
            }
        ]
    },
    "UCSZCI": {
        "title": "UNUSED COMMIT FOR SECUR. - CI",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UCSZCI"
            }
        ]
    },
    "UCSZCON": {
        "title": "UNUSED COMMIT FOR SECUR. - CON",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UCSZCON"
            }
        ]
    },
    "UCSZCRCD": {
        "title": "UNUSED COMMIT FOR SECUR. - CRCD",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UCSZCRCD"
            }
        ]
    },
    "UCSZHEL": {
        "title": "UNUSED COMMIT FOR SECUR. - HEL",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UCSZHEL"
            }
        ]
    },
    "UCSZOTH": {
        "title": "UNUSED COMMIT FOR SECUR. - OTH",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UCSZOTH"
            }
        ]
    },
    "UCSZRES": {
        "title": "UNUSED COMMIT FOR SECUR. - RES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UCSZRES"
            }
        ]
    },
    "UNINCFOR": {
        "title": "UNEARNED INCOME-FOR",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UNINCFOR"
            }
        ]
    },
    "UNINCFORR": {
        "title": "UNEARNED INCOME-FOR RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "UNINCFORR",
                        "numerator": "UNINCFOR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "VOLIAB": {
        "title": "VOLATILE LIABILITIES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "VOLIAB"
            }
        ]
    },
    "VOLIABR": {
        "title": "VOLATILE LIABILITIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "VOLIABR",
                        "numerator": "VOLIAB",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "ZIP": {
        "title": "ZIP CODE",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ZIP"
            }
        ]
    },
    "LIPNMTG": {
        "title": "NONMORTGAGE LOANS IN PROCESS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "LIPNMTG"
            }
        ]
    },
    "UYANMTG": {
        "title": "UNAMORTIZED YIELD ADJ-NONMTG LNS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UYANMTG"
            }
        ]
    },
    "ILNLS": {
        "title": "LOAN & LEASE INCOME",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "ILNLS"
            }
        ]
    },
    "UNIT": {
        "title": "BANKS UNIT",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UNIT"
            }
        ]
    },
    "PTAXNETINC": {
        "title": "PRE-TAX NET INCOME OPERATING INCOME",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleSubtraction",
                    "parameters": {
                        "setField": "PTAXNETINC",
                        "subtractionFields": [
                            "IBEFTAX",
                            "IGLSEC"
                        ]
                    }
                }
            }
        ]
    },
    "PTAXNETINCR": {
        "title": "PRE-TAX NET INCOME OPERATING INCOME RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "PTAXNETINCR",
                        "numerator": "PTAXNETINC",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "PTAXNETINCQ": {
        "title": "PRE-TAX NET INCOME OPERATING INCOME QUARTERLY",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleSubtraction",
                    "parameters": {
                        "setField": "PTAXNETINCQ",
                        "subtractionFields": [
                            "IBEFTXQ",
                            "IGLSECQ"
                        ]
                    }
                }
            }
        ]
    },
    "PTAXNETINCQR": {
        "title": "PRE-TAX NET INCOME OPERATING INCOME QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "PTAXNETINCQR",
                        "numerator": "PTAXNETINCQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "ADDNONII": {
        "title": "ADDITIONAL NONINTEREST INCOME",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def NONII = ctx.NONII ?: 0;\ndef IFIDUC = ctx.IFIDUC ?: 0;\ndef ISERCHG = ctx.ISERCHG ?: 0;\ndef IGLTRAD = ctx.IGLTRAD ?: 0;\nctx.ADDNONII = NONII - ( IFIDUC + ISERCHG + IGLTRAD );\n"
                    }
                }
            }
        ]
    },
    "ADDNONIIR": {
        "title": "ADDITIONAL NONINTEREST INCOME RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "ADDNONIIR",
                        "numerator": "ADDNONII",
                        "denominator": "ASSET5"
                    }
                }
            }
        ]
    },
    "ADDNONIIQ": {
        "title": "ADDITIONAL NONINTEREST INCOME QUARTERLY",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def NONIIQ = ctx.NONIIQ ?: 0;\ndef IFIDUCQ = ctx.IFIDUCQ ?: 0;\ndef ISERCHGQ = ctx.ISERCHGQ ?: 0;\ndef IGLTRDQ = ctx.IGLTRDQ ?: 0;\nctx.ADDNONIIQ = NONIIQ - ( IFIDUCQ + ISERCHGQ + IGLTRDQ );\n"
                    }
                }
            }
        ]
    },
    "ADDNONIIQR": {
        "title": "ADDITIONAL NONINTEREST INCOME QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "ADDNONIIQR",
                        "numerator": "ADDNONIIQ",
                        "denominator": "ASSET2"
                    }
                }
            }
        ]
    },
    "AVMMLF": {
        "title": "Quarterly average amount of assets purchased under the MMLF and excluded from \u201cTotal assets for the leverage ratio.\u201d",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "AVMMLF"
            }
        ]
    },
    "AVMMLFR": {
        "title": "Quarterly average amount of assets purchased under the MMLF and excluded from \u201cTotal assets for the leverage ratio.\u201d ratio",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "AVMMLFR",
                        "numerator": "AVMMLF",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "AVPPPPLG": {
        "title": "Quarterly average amount of PPP loans pledged to the PPPLF and excluded from \u201cTotal assets for the leverage ratio.\u201d",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "AVPPPPLG"
            }
        ]
    },
    "AVPPPPLGR": {
        "title": "Quarterly average amount of PPP loans pledged to the PPPLF and excluded from \u201cTotal assets for the leverage ratio.\u201d ratio",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "AVPPPPLGR",
                        "numerator": "AVPPPPLG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "MMLFBAL": {
        "title": "Outstanding balance of assets purchased under the Money Market Mutual Fund Liquidity Facility (MMLF).",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "MMLFBAL"
            }
        ]
    },
    "MMLFBALR": {
        "title": "Outstanding balance of assets purchased under the Money Market Mutual Fund Liquidity Facility (MMLF) ratio",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "MMLFBALR",
                        "numerator": "MMLFBAL",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "PPPLFOV1": {
        "title": "Outstanding balance under the PPPLF with a remaining maturity of more than one year",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "PPPLFOV"
            }
        ]
    },
    "PPPLFOV1R": {
        "title": "Outstanding balance under the PPPLF with a remaining maturity of more than one year ratio",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "PPPLFOV1R",
                        "numerator": "PPPLFOV1",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "PPPLNBAL": {
        "title": "Outstanding balance of PPP loans",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "PPPLNBAL"
            }
        ]
    },
    "PPPLNBALR": {
        "title": "Outstanding balance of PPP loans ratio",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "PPPLNBALR",
                        "numerator": "PPPLNBAL",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "PPPLNNUM": {
        "title": "Number of PPP loans outstanding",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "PPPLNNUM"
            }
        ]
    },
    "PPPLNNUMR": {
        "title": "Number of PPP loans outstanding ratio",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "PPPLNNUMR",
                        "numerator": "PPPLNNUM",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "PPPLNPLG": {
        "title": "Outstanding balance of PPP loans pledged to the PPPLF",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "PPPLNPLG"
            }
        ]
    },
    "PPPLNPLGR": {
        "title": "Outstanding balance of PPP loans pledged to the PPPLF ratio",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "PPPLNPLGR",
                        "numerator": "PPPLNPLG",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "PPPLF1LS": {
        "title": "Outstanding balance under the PPPLF with a remaining maturity of one year or less",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "PPPLF1LS"
            }
        ]
    },
    "PPPLF1LSR": {
        "title": "Outstanding balance under the PPPLF with a remaining maturity of one year or less ratio",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "PPPLF1LSR",
                        "numerator": "PPPLF1LS",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "IDNTCIR": {
        "title": "COMMERCIAL & INDUSTRIAL LOANS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "IDNTCIR",
                        "numerator": "NTCIA",
                        "denominator": "LNCI5"
                    }
                }
            }
        ]
    },
    "IDNTCIQR": {
        "title": "COMMERCIAL & INDUSTRIAL LOANS QUARTERLY",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "IDNTCIQR",
                        "numerator": "NTCIQ",
                        "denominator": "LNCI5"
                    }
                }
            }
        ]
    },
    "IDNTCONR": {
        "title": "LOANS TO INDIVIDUALS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "IDNTCONR",
                        "numerator": "NTCONA",
                        "denominator": "LNCON5"
                    }
                }
            }
        ]
    },
    "IDNTCRDR": {
        "title": "CREDIT CARDS & RELATED PLANS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "IDNTCRDR",
                        "numerator": "NTCRCDA",
                        "denominator": "LNCRCD5"
                    }
                }
            }
        ]
    },
    "IDNTCOOR": {
        "title": "OTHER LOANS TO INDIVIDUALS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageMultipleAddition",
                    "parameters": {
                        "setField": "IDNTCOOR",
                        "numFields": [
                            "NTCONOTA",
                            "NTAUTOA"
                        ],
                        "denFields": [
                            "LNCONOT5",
                            "LNAUTO5"
                        ]
                    }
                }
            }
        ]
    },
    "IDNTCOOQR": {
        "title": "OTHER LOANS TO INDIVIDUALS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageMultipleAddition",
                    "parameters": {
                        "setField": "IDNTCOOQR",
                        "multiplier": 4,
                        "numFields": [
                            "NTCONOTQ",
                            "NTAUTOQ"
                        ],
                        "denFields": [
                            "LNCONOT2",
                            "LNAUTO2"
                        ]
                    }
                }
            }
        ]
    },
    "IDNTCRDQR": {
        "title": "CREDIT CARDS & RELATED PLANS QUARTERLY",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "IDNTCRDQR",
                        "numerator": "NTCRCDQ",
                        "denominator": "LNCRCD2"
                    }
                }
            }
        ]
    },
    "IDNTILR": {
        "title": "",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "IDNTILR",
                        "numerator": "NTINCL",
                        "denominator": "INSTCNT"
                    }
                }
            }
        ]
    },
    "IDOTHNII": {
        "title": "",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def NONII = ctx.NONII ?: 0;\ndef IFIDUC = ctx.IFIDUC ?: 0;\ndef ISERCHG = ctx.ISERCHG ?: 0;\ndef IGLTRAD = ctx.IGLTRAD ?: 0;\nctx.IDOTHNII = NONII - ( IFIDUC + ISERCHG + IGLTRAD );\n"
                    }
                }
            }
        ]
    },
    "NTAUTOPR": {
        "title": "AUTOMOBILE LOANS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTAUTOPR",
                        "numerator": "NTAUTOA",
                        "denominator": "LNAUTO5",
                        "noMultiplier": True
                    }
                }
            }
        ]
    },
    "NTCONOTR": {
        "title": "OTHER CONSUMER LOANS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTCONOTR",
                        "numerator": "NTCONOTA",
                        "denominator": "LNCONOT5",
                        "noMultiplier": True
                    }
                }
            }
        ]
    },
    "IDERNCVR": {
        "title": "EARNINGS COVERAGE OF NET LOAN CHARGE-OFFS (X)",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleDivision",
                    "parameters": {
                        "setField": "IDERNCVR",
                        "numerator": "CHFLA",
                        "denominator": "NTLNLSA"
                    }
                }
            }
        ]
    },
    "IDERNCVQR": {
        "title": "Earnings coverage of net loan charge-offs",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleDivision",
                    "parameters": {
                        "setField": "IDERNCVQR",
                        "numerator": "CHFLQ",
                        "denominator": "NTLNLSQ"
                    }
                }
            }
        ]
    },
    "EQCDIVNTINC": {
        "title": "CASH DIVIDENDS TO NET INCOME (YTD ONLY)",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "EQCDIVNTINC",
                        "numerator": "EQCDIVA",
                        "denominator": "NETINCA",
                        "noMultiplier": True
                    }
                }
            }
        ]
    },
    "NACDIR": {
        "title": "NOTIONAL AMOUNT OF CREDIT DERIVATIVES",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleAddition",
                    "parameters": {
                        "setField": "NACDIR",
                        "additionFields": [
                            "CTDERGTY",
                            "CTDERBEN"
                        ]
                    }
                }
            }
        ]
    },
    "NACDIRR": {
        "title": "NOTIONAL AMOUNT OF CREDIT DERIVATIVES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "NACDIRR",
                        "numerator": "NACDIR",
                        "denominator": "ASSET"
                    }
                }
            }
        ]
    },
    "NTCOMREQR": {
        "title": "COMMERCIAL RE CHG-OFF/COMM RE LN QUARTERLY RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageQuarterly",
                    "parameters": {
                        "setField": "NTCOMREQR",
                        "numerator": "NTCOMREQ",
                        "denominator": "LNCOMRE2"
                    }
                }
            }
        ]
    },
    "NTALLOTHNUM": {
        "title": "Net Charge-offs All other loans & leases (including farm) Numerator",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def NTDEP = ctx.NTDEP ?: 0;\ndef NTFORGV = ctx.NTFORGV ?: 0;\ndef NTOTHER = ctx.NTDEP ?: 0;\ndef NTLS = ctx.NTLS ?: 0;\ndef NTAGA = ctx.NTAGA ?: 0;\ndef IDANN = 1;\nif (ctx.REPDTE.lastIndexOf('0331') > -1) {\n  IDANN = 4;\n} else if (ctx.REPDTE.lastIndexOf('0630') > -1) {\n  IDANN = 2;\n} else if (ctx.REPDTE.lastIndexOf('0930') > -1) {\n  IDANN = 1.333;\n}\nctx.NTALLOTHNUM = (((NTDEP + NTFORGV + NTOTHER + NTLS) * IDANN) + NTAGA)\n"
                    }
                }
            }
        ]
    },
    "NTALLOTHDEN": {
        "title": "Net Charge-offs All other loans & leases (including farm) denominator",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleAddition",
                    "parameters": {
                        "setField": "NTALLOTHDEN",
                        "additionFields": [
                            "LNOTCI5",
                            "LNAG5"
                        ]
                    }
                }
            }
        ]
    },
    "NTALLOTHR": {
        "title": "ALL OTHER LOANS & LEASES (INCLUDING FARM)",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageYTD",
                    "parameters": {
                        "setField": "NTALLOTHR",
                        "numerator": "NTALLOTHNUM",
                        "denominator": "NTALLOTHDEN",
                        "noMultiplier": True
                    }
                }
            }
        ]
    },
    "NTALLOTHQR": {
        "title": "Net Charge-offs All other loans & leases (including farm)",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageMultipleAddition",
                    "parameters": {
                        "multiplier": 4,
                        "setField": "NTALLOTHQR",
                        "numFields": [
                            "NTDEPQ",
                            "NTFORGVQ",
                            "NTOTHQ",
                            "NTLSQ",
                            "NTAGQ"
                        ],
                        "denFields": [
                            "LNOTCI2",
                            "LNAG22"
                        ]
                    }
                }
            }
        ]
    },
    "IDNCCOOR": {
        "title": "Other loans to individuals",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageMultipleAddition",
                    "parameters": {
                        "setField": "IDNCCOOR",
                        "numFields": [
                            "NCCONOTH",
                            "NCAUTO"
                        ],
                        "denFields": [
                            "LNCONORP",
                            "LNAUTO"
                        ]
                    }
                }
            }
        ]
    },
    "IDNCOTHR": {
        "title": "All other loans & leases (including farm )",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentageMultipleAddition",
                    "parameters": {
                        "setField": "IDNCOTHR",
                        "numFields": [
                            "NCDEP",
                            "NCFG",
                            "NCOTHLN",
                            "NCLS",
                            "NCAG"
                        ],
                        "denFields": [
                            "LNOTCI",
                            "LNAG"
                        ]
                    }
                }
            }
        ]
    },
    "IDNCCIR": {
        "title": "COMMERCIAL & INDUSTRIAL LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "IDNCCIR",
                        "numerator": "NCCI",
                        "denominator": "LNCI"
                    }
                }
            }
        ]
    },
    "IDNCCONR": {
        "title": "LOANS TO INDIVIDUALS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "IDNCCONR",
                        "numerator": "NCCON",
                        "denominator": "LNCON"
                    }
                }
            }
        ]
    },
    "IDNCCRDR": {
        "title": "CREDIT CARDS & RELATED PLANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "IDNCCRDR",
                        "numerator": "NCCRCD",
                        "denominator": "LNCRCD"
                    }
                }
            }
        ]
    },
    "IDNCATOR": {
        "title": "AUTOMOBILE LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "IDNCATOR",
                        "numerator": "NCAUTO",
                        "denominator": "LNAUTO"
                    }
                }
            }
        ]
    },
    "IDNTATOR": {
        "title": "",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "IDNTATOR",
                        "numerator": "NTAUTOA",
                        "denominator": "LNAUTO5"
                    }
                }
            }
        ]
    },
    "IDNTCOTR": {
        "title": "",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "IDNTCOTR",
                        "numerator": "NTCONOTA",
                        "denominator": "LNCONOT5"
                    }
                }
            }
        ]
    },
    "IDDEPINR": {
        "title": "IDDEPINR",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "IDDEPINR",
                        "numerator": "DEPINS",
                        "denominator": "DEPBEFEX"
                    }
                }
            }
        ]
    },
    "IDDIVNIR": {
        "title": "",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "IDDIVNIR",
                        "numerator": "EQCDIVA",
                        "denominator": "NETINCA"
                    }
                }
            }
        ]
    },
    "IDNCCOTR": {
        "title": "OTHER CONSUMER LOANS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "IDNCCOTR",
                        "numerator": "NCCONOTH",
                        "denominator": "LNCONORP"
                    }
                }
            }
        ]
    },
    "INTINCY": {
        "title": "INTEREST INCOME TO EARNING ASSETS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "INTINCY",
                        "numerator": "INTINCA",
                        "denominator": "ERNAST5"
                    }
                }
            }
        ]
    },
    "IDNCGTPR": {
        "title": "NONCURRENT LOANS WHICH ARE WHOLLY OR PARTIALLY GUARANTEED BY THE U.S. GOVERNMENT RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "IDNCGTPR",
                        "numerator": "NCGTYPAR",
                        "denominator": "NCLNLS"
                    }
                }
            }
        ]
    },
    "IDLNCORR": {
        "title": "NET LOANS AND LEASES TO CORE DEPOSITS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "IDLNCORR",
                        "numerator": "LNLSNET",
                        "denominator": "COREDEP"
                    }
                }
            }
        ]
    },
    "IDT1CnoCB": {
        "title": "ID NO CB FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def RBCT1C = ctx.RBCT1C ?: 0;\ndef CBLRIND = ctx.CBLRIND ?: 0;\ndef INSFDIC = ctx.INSFDIC ?: 0;\ndef IBA = ctx.IBA ?: 0;\nctx.IDT1CnoCB = 0;\nif (INSFDIC === 1 && CBLRIND === 0 && IBA === 0) {\n  ctx.IDT1CnoCB = RBCT1C;\n}\n"
                    }
                }
            }
        ]
    },
    "IDT1JnoCB": {
        "title": "ID NO J CB FLAG",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def RBCT1J = ctx.RBCT1J ?: 0;\ndef CBLRIND = ctx.CBLRIND ?: 0;\ndef INSFDIC = ctx.INSFDIC ?: 0;\ndef IBA = ctx.IBA ?: 0;\nctx.IDT1JnoCB = 0;\nif (INSFDIC === 1 && CBLRIND === 0 && IBA === 0) {\n  ctx.IDT1JnoCB = RBCT1J;\n}\n"
                    }
                }
            }
        ]
    },
    "IDT1CER": {
        "title": "COMMON EQUITY TIER 1 CAPITAL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "IDT1CER",
                        "numerator": "IDT1CnoCB",
                        "denominator": "RWAJ"
                    }
                }
            }
        ]
    },
    "IDT1RWAJR": {
        "title": "TIER 1 RISK-BASED CAPITAL RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "IDT1RWAJR",
                        "numerator": "IDT1JnoCB",
                        "denominator": "RWAJ"
                    }
                }
            }
        ]
    },
    "SCEQNFT": {
        "title": "EQUITY SECURITIES NOT HELD FOR TRADING",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleAddition",
                    "parameters": {
                        "setField": "SCEQNFT",
                        "additionFields": [
                            "SCEQ",
                            "SCEQFV"
                        ]
                    }
                }
            }
        ]
    },
    "SCRMBPI": {
        "title": "PRIV ISSUED RES MORTGAGE-BACKED SECURITIES",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "simpleAddition",
                    "parameters": {
                        "setField": "SCRMBPI",
                        "additionFields": [
                            "SCODPC",
                            "SCODPI"
                        ]
                    }
                }
            }
        ]
    },
    "SCRMBPIR": {
        "title": "PRIV ISSUED RES MORTGAGE-BACKED SECURITIES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def SCODPC = ctx.SCODPC ?: 0;\ndef SCODPI = ctx.SCODPI ?: 0;\ndef ASSET = ctx.ASSET ?: 0;\nctx.SCRMBPIR = 0;\nif (ASSET > 0) {\n  ctx.SCRMBPIR = ((double)(SCODPC + SCODPI) / ASSET);\n}\n"
                    }
                }
            }
        ]
    },
    "SCUSO": {
        "title": "U.S GOVERNMENT OBLIGATIONS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def CALLFORM = ctx.CALLFORM ?: 0;\ndef SCAGE = ctx.SCAGE ?: 0;\ndef SCUST = ctx.SCUST ?: 0;\nif (CALLFORM === 100 && Integer.parseInt(ctx.REPYEAR) < 1996) {\n  ctx.SCUSO = (SCAGE-SCUST);\n} else {\n  ctx.SCUSO = SCAGE;\n}\n"
                    }
                }
            }
        ]
    },
    "SCUSOR": {
        "title": "U.S GOVERNMENT OBLIGATIONS RATIOS",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def CALLFORM = ctx.CALLFORM ?: 0;\ndef SCAGE = ctx.SCAGE ?: 0;\ndef SCUST = ctx.SCUST ?: 0;\ndef ASSET = ctx.ASSET ?: 0;\nctx.SCUSOR = 0;\nif (ASSET > 0) {\n  if (CALLFORM === 100 && Integer.parseInt(ctx.REPYEAR) < 1996) {\n    ctx.SCUSOR = ((double)(SCAGE-SCUST) / ASSET);\n  } else {\n    ctx.SCUSOR = ((double)SCAGE / ASSET);\n  }\n}\n"
                    }
                }
            }
        ]
    },
    "SCCMOS": {
        "title": "OTHER COMM MORTGAGE-BACKED SEC",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def SCCMMB = ctx.SCCMMB ?: 0;\ndef SCCPTG = ctx.SCCPTG ?: 0;\ndef SCCMOG = ctx.SCCMOG ?: 0;\nctx.SCCMOS = SCCMMB - SCCPTG - SCCMOG;\n"
                    }
                }
            }
        ]
    },
    "SCCMOSR": {
        "title": "OTHER COMM MORTGAGE-BACKED SEC",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def SCCMMB = ctx.SCCMMB ?: 0;\ndef SCCPTG = ctx.SCCPTG ?: 0;\ndef SCCMOG = ctx.SCCMOG ?: 0;\ndef ASSET = ctx.ASSET ?: 0;\nctx.SCCMOSR = 0;\nif (ASSET > 0) {\n  ctx.SCCMOSR = ((double)(SCCMMB - SCCPTG - SCCMOG) / ASSET);\n}\n"
                    }
                }
            }
        ]
    },
    "SCTATFR": {
        "title": "ASSETS HELD IN TRADING ACCOUNTS FOR TFR REPORTERS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def SCUS = ctx.SCUS ?: 0;\ndef SCMUNI = ctx.SCMUNI ?: 0;\ndef SCDOMO = ctx.SCDOMO ?: 0;\ndef SCFORD = ctx.SCFORD ?: 0;\ndef SCEQ = ctx.SCEQ ?: 0;\ndef SC = ctx.SC ?: 0;\ndef FORMTFR = ctx.FORMTFR ?: 0;\ndef SCRES = ctx.SCRES ?: 0;\nctx.SCTATFR = "";\nif (Integer.parseInt(ctx.REPYEAR) < 2012 && FORMTFR === 1) {\n  ctx.SCTATFR = SCUS + SCMUNI + SCDOMO + SCFORD + SCEQ - SC - SCRES;\n}\n"
                    }
                }
            }
        ]
    },
    "LNLSGRS": {
        "title": "LOANS AND LEASES, GROSS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def LNLSGR = ctx.LNLSGR ?: 0;\ndef LNCONTRA = ctx.LNCONTRA ?: 0;\ndef UNINC = ctx.UNINC ?: 0;\ndef LNLS = ctx.LNLS ?: 0;\nif (Integer.parseInt(ctx.REPYEAR) < 1996) {\n  ctx.LNLSGRS = LNLSGR + LNCONTRA - UNINC;\n} else { \n  ctx.LNLSGRS = LNLS;\n}\n"
                    }
                }
            }
        ]
    },
    "LNLSGRSR": {
        "title": "LOANS AND LEASES, GROSS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def LNLSGR = ctx.LNLSGR ?: 0;\ndef LNCONTRA = ctx.LNCONTRA ?: 0;\ndef UNINC = ctx.UNINC ?: 0;\ndef LNLS = ctx.LNLS ?: 0;\ndef ASSET = ctx.ASSET ?: 0;\nctx.LNLSGRSR = 0;\nif(ASSET > 0) {\n  if (Integer.parseInt(ctx.REPYEAR) < 1996) {\n    ctx.LNLSGRSR = ((double)(LNLSGR + LNCONTRA - UNINC) / ASSET);\n  } else { \n    ctx.LNLSGRSR = ((double)LNLS / ASSET);\n  }\n}\n"
                    }
                }
            }
        ]
    },
    "AOA": {
        "title": "ALL OTH ASSETS",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def OA = ctx.OA ?: 0;\ndef INVSUB = ctx.INVSUB ?: 0;\ndef INVSUORE = ctx.INVSUORE ?: 0;\ndef CUSLI = ctx.CUSLI ?: 0;\nctx.AOA = 0;\nif (Integer.parseInt(ctx.REPYEAR) > 2009) {\n  ctx.AOA = OA + INVSUB + INVSUORE;\n} else {\n  ctx.AOA = OA + INVSUB + CUSLI\n}\n"
                    }
                }
            }
        ]
    },
    "AOAR": {
        "title": "ALL OTH ASSETS RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def OA = ctx.OA ?: 0;\ndef INVSUB = ctx.INVSUB ?: 0;\ndef INVSUORE = ctx.INVSUORE ?: 0;\ndef ASSET = ctx.ASSET ?: 0;\ndef CUSLI = ctx.CUSLI ?: 0;\nctx.AOAR = 0;\nif (Integer.parseInt(ctx.REPYEAR) > 2009 && ASSET > 0) {\n  ctx.AOAR = ((double)(OA + INVSUB + INVSUORE) / ASSET);\n} else {\n  ctx.AOAR = (((double)(OA + INVSUB + CUSLI) / ASSET) * 100)\n}\n"
                    }
                }
            }
        ]
    },
    "ESTINS": {
        "title": "PERCENTAGE INSURED ESTIMATED",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "percentage",
                    "parameters": {
                        "setField": "ESTINS",
                        "numerator": "DEPINS",
                        "denominator": "DEPBEFEX"
                    }
                }
            }
        ]
    },
    "ESTINSR": {
        "title": "PERCENTAGE INSURED ESTIMATED RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def DEPINS = ctx.DEPINS ?: 0;\ndef DEPBEFEX = ctx.DEPBEFEX ?: 0;\ndef ASSET = ctx.ASSET ?: 0;\nctx.ESTINSR = 0;\nif ( DEPBEFEX > 0 && ASSET > 0 ) {\n  ctx.ESTINSR = ((double)((DEPINS / DEPBEFEX) * 100) / ASSET);\n}\n"
                    }
                }
            }
        ]
    },
    "P3RELNDO": {
        "title": "P/D 30-89 REAL ESTATE LOANS IN DOMESTIC OFFICES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def P3RECONS = ctx.P3RECONS ?: 0;\ndef P3REAG = ctx.P3REAG ?: 0;\ndef P3RERES = ctx.P3RERES ?: 0;\ndef P3REMULT = ctx.P3REMULT ?: 0;\ndef P3RENRES = ctx.P3RENRES ?: 0;\nctx.P3RELNDO = P3RECONS + P3REAG + P3RERES + P3REMULT + P3RENRES;\n"
                    }
                }
            }
        ]
    },
    "P3RELNDOR": {
        "title": "P/D 30-89 REAL ESTATE LOANS IN DOMESTIC OFFICES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def P3RECONS = ctx.P3RECONS ?: 0;\ndef P3REAG = ctx.P3REAG ?: 0;\ndef P3RERES = ctx.P3RERES ?: 0;\ndef P3REMULT = ctx.P3REMULT ?: 0;\ndef P3RENRES = ctx.P3RENRES ?: 0;\ndef ASSET = ctx.ASSET ?: 0;\nctx.P3RELNDOR = 0;\nif ( ASSET > 0 ) {\n  ctx.P3RELNDOR = ((double)(P3RECONS + P3REAG + P3RERES + P3REMULT + P3RENRES) / ASSET);\n}\n"
                    }
                }
            }
        ]
    },
    "P9RELNDO": {
        "title": "90+ REAL ESTATE LOANS IN DOMESTIC OFFICES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def P9RECONS = ctx.P9RECONS ?: 0;\ndef P9REAG = ctx.P9REAG ?: 0;\ndef P9RERES = ctx.P9RERES ?: 0;\ndef P9REMULT = ctx.P9REMULT ?: 0;\ndef P9RENRES = ctx.P9RENRES ?: 0;\nctx.P9RELNDO = P9RECONS + P9REAG + P9RERES + P9REMULT + P9RENRES;\n"
                    }
                }
            }
        ]
    },
    "P9RELNDOR": {
        "title": "90+ REAL ESTATE LOANS IN DOMESTIC OFFICES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def P9RECONS = ctx.P9RECONS ?: 0;\ndef P9REAG = ctx.P9REAG ?: 0;\ndef P9RERES = ctx.P9RERES ?: 0;\ndef P9REMULT = ctx.P9REMULT ?: 0;\ndef P9RENRES = ctx.P9RENRES ?: 0;\ndef ASSET = ctx.ASSET ?: 0;\nctx.P9RELNDOR = 0;\nif ( ASSET > 0 ) {\n  ctx.P9RELNDOR = ((double)(P9RECONS + P9REAG + P9RERES + P9REMULT + P9RENRES) / ASSET);\n}\n"
                    }
                }
            }
        ]
    },
    "NARELNDO": {
        "title": "90+ REAL ESTATE LOANS IN DOMESTIC OFFICES",
        "description": "",
        "type": "number",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def NARECONS = ctx.NARECONS ?: 0;\ndef NAREAG = ctx.NAREAG ?: 0;\ndef NARERES = ctx.NARERES ?: 0;\ndef NAREMULT = ctx.NAREMULT ?: 0;\ndef NARENRES = ctx.NARENRES ?: 0;\nctx.NARELNDO = NARECONS + NAREAG + NARERES + NAREMULT + NARENRES;\n"
                    }
                }
            }
        ]
    },
    "NARELNDOR": {
        "title": "90+ REAL ESTATE LOANS IN DOMESTIC OFFICES RATIO",
        "description": "",
        "type": "number",
        "x-elastic-type": "double",
        "x-source-mapping": [
            {
                "formula": {
                    "type": "raw",
                    "parameters": {
                        "script": "def NARECONS = ctx.NARECONS ?: 0;\ndef NAREAG = ctx.NAREAG ?: 0;\ndef NARERES = ctx.NARERES ?: 0;\ndef NAREMULT = ctx.NAREMULT ?: 0;\ndef NARENRES = ctx.NARENRES ?: 0;\ndef ASSET = ctx.ASSET ?: 0;\nctx.NARELNDOR = 0;\nif ( ASSET > 0 ) {\n  ctx.NARELNDOR = ((double)(NARECONS + NAREAG + NARERES + NAREMULT + NARENRES) / ASSET);\n}\n"
                    }
                }
            }
        ]
    },
    "STCNTY": {
        "title": "State and County Nunber",
        "description": "",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "STCNTY"
            }
        ]
    },
    "CBSA": {
        "title": "Metropolitan Statistical Area",
        "description": "",
        "type": "string",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "CBSA"
            }
        ]
    },
    "INSDATE": {
        "title": "Date of Deposit Insurance",
        "description": "",
        "type": "string",
        "x-elastic-type": "keyword",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "INSDATE"
            }
        ]
    },
    "UPDDATE": {
        "title": "Last Structure Change Process Date",
        "description": "",
        "type": "string",
        "x-elastic-type": "keyword",
        "x-source-mapping": [
            {
                "file": "RISVIEW",
                "field": "UPDDATE"
            }
        ]
    }
}