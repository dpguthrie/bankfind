summary_dict = {
    'ALLOTHER': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'All Other Loans',
        'description': 'All Other Loans'
    },
    'alsonew': {
        'type': 'integer',
        'title': 'New Charters to Absorb Another Charter',
        'description': 'New savings institution charter created to absorb any other type of charter in its first quarter of operation.'
    },
    'ASSET': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Assets',
        'description': 'Total Assets On A Consolidated Basis\nNote: For Banks With Foreign Operations Data For March &\nSeptember Of 1973 Through 1975 Are Reported On A\nDomestic Basis'
    },
    'BANKS': {
        'type': 'integer',
        'title': 'Total Commercial Banks (Filing Y/E Call)',
        'description': 'Total Insured Commercial Banks filing 12/31 fincncial report  (See Notes to User for definition of commercial bank)'
    },
    'BKPREM': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Bank Premises and Equipment',
        'description': 'Premises and Fixed Assets\nNote:\n(1) Premises and Fixed Assets (Including Capitalized Leases) On A Consolidated Basis\n(2) For Banks With Foreign Operations Data For March & September Of 1972 Through 1975 Was Reported On A Domestic Basis'
    },
    'BRANCHES': {
        'type': 'integer',
        'title': 'Total Branches',
        'description': 'Branches include all offices of a bank, other than its head office, at which deposits are received, checks paid or money lent. Banking facilities separate from a banking house, banking facilities at government installations, offices, agencies, paying or receiving stations, drive-in facilities and other facilities operated for limited purposes are defined as branches under the FDI Act (see Notes to User)'
    },
    'BRANCHIN': {
        'type': 'integer',
        'title': 'Banks with Branches',
        'description': 'Banks with branches are institutions that operate one or more offices at which deposits are received or other banking business conducted in addition to the main or head office.'
    },
    'BRO': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Memo: Brokered Deposits',
        'description': 'Borrowed Deposits (Represents funds which the reporting bank obtains, directly or indirectly, by or through any deposit broker for deposit into one or more deposit accounts. Includes both those in which the entire beneficial interest in a given bank deposit account or investment is held by a single depositor and those in which deposit broker sells participation in a given bank deposit account or instrument to one or more investors).'
    },
    'BRWDMONY': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Borrowed Funds',
        'description': 'Borrowed Funds - (1969-Present -- Represents Federal Funds purchase. securities sold under agreements to repurchase, demand notes issued to the US Treasury, mortgage indebtedness, liabilities under capitalized leases and all other liabilities for borrowed money. -- 1934-1968 -- Does not include mortgage indebtedness which is netted against bank premsises.)'
    },
    'CB_SI': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'title': 'Commercial Banks (CB) vs. Savings Institution (SI)',
        'description': 'Differentiates the summarised data between the Commercial Banks and the Savings Institutions',
        'options': ['CB', 'SI']
    },
    'chartoth': {
        'type': 'integer',
        'title': 'Charter Transfers from Commercial Banks',
        'description': 'Represents the transfer of a commercial bank to a savings institution charter that meets the definition of a thrift (see Notes to Table SI-1) and has applied for and received FDIC insurance (BIF or SAIF).'
    },
    'CHBAL': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Cash & Due from Depository Institutions',
        'description': 'Total Cash and Balances Due From Depository Institutions Which Include Both Noninterest-Bearing and Interest-Bearing Deposits On A Consolidated Basis\nNote:\n(1): Additional Detail Can Be Found On Schedule Rc-A\n(2) For Banks With Foreign Operations Data For March and September 1972 Through 1975 Are Reported On A Domestic Basis'
    },
    'CHBALI': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Interest Earning Balances',
        'description': 'Interest-Bearing Balances Due From Depository Institutions On A Consolidated Basis\nNote: Additional Detail Can Be Found On Schedule Rc-A'
    },
    'chrtrest': {
        'type': 'integer',
        'title': 'Non-insured Becoming insured',
        'description': 'Represents the transfer of an existing institution that does not have deposit insurance to a savings institution charter with FDIC insurance from BIF or SAIF. Examples of such institutions include Trust Banks and savings institutions with state deposit insurance that apply for and receive FDIC insurance'
    },
    'comboass': {
        'type': 'integer',
        'title': 'Assisted Mergers with Thrifts',
        'description': 'Represents the absorption of a failing savings institution by another savings institution with assistance from either the BIF or SAIF. (Included are RTC Accelerated Resolution Program (ARP) assisted mergers. These institutions were not placed in RTC conservatorship.)'
    },
    'combos': {
        'type': 'integer',
        'title': 'Unassisted Mergers/Consolidations of Thrifts',
        'description': 'Represents the absorption of a savings institution charter by another savings institution without assistance. Both institutions may be owned by the same holding company in a consolidation of affiliates.'
    },
    'CONS': {
        'type': 'integer',
        'title': 'RTC Conservatorships',
        'description': 'Institutions in RTC Conservatorship'
    },
    'CORPBNDS': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Other Debt Securities',
        'description': 'Other Debt Securities'
    },
    'COUNT': {
        'type': 'integer',
        'title': 'Total Savings Institutions (Filing Y/E Call)',
        'description': 'All FDIC Insured Savings Institutions filing a 12/31 financial report'
    },
    'CRLNLS': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Loan & Lease Recoveries',
        'description': 'Total Recoveries Of Loans and Lease Financing Receivables Credited To The Allowance For Loan and Lease Losses\nNote: For Banks With Foreign Operations, Data For December\n1972 Through December 1975 Are Domestic Only'
    },
    'DDT': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Deposits - Domestic Demand',
        'description': 'Total Demand Deposits Included In Total Transaction Accounts Held In Domestic Offices\nNote: For Tfr Filers Between June 1989 Through March 1990 Includes Non-interest Bearing Deposits'
    },
    'DEP': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Deposits',
        'description': 'Total Deposits On A Consolidated Basis\nNote:\n(1) Additional Detail Can Be Found On Schedule Rc-E\n(2) For Banks With Foreign Operations Data For March & September Of 1972 Through 1975 Are Reported On A Domestic Basis'
    },
    'DEPDOM': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Domestic Deposits',
        'description': 'Represents the sum of total deposits, domestic offices only'
    },
    'DEPFOR': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Foreign Deposits',
        'description': 'Represents the sum of total deposits in foreign offices'
    },
    'DEPI': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Interest Bearing Deposits',
        'description': 'Interest-Bearing Consolidated Office Deposits\n\nNote:\n(1) Additional Detail Can Be Found On Schedule Rc-E\n(2) Tfr Filers With Less Than $300 Million In Assets and Risk-Based Capital Ratios In Excess Of 12 Percent Are Not Required To File Schedule Cmr Beginning March 1993, However, When Cmr Data Is Either Incorrect Or Not Filed Fts Assumes That All Deposits Are Interest-Bearing\n(3) Prior To Receipt Of The 75-Day Tfr Tape All Tfr Filers Deposits Are Assumed To Be Interest-Bearing\n(4) For Banks With Foreign Operations Data For March & September Of 1972 Through 1975 Are Reported On A Domestic Basis'
    },
    'DEPIFOR': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Foreign Deposits - Interest Bearing',
        'description': 'Represents any deposit in foreign offices, whether demand, savings or time, on which the bank pays or accrues interest'
    },
    'DEPNI': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Memo: Deposits - Non-interest Bearing',
        'description': 'Represents any deposit on which the bank does not pay or accrue interest'
    },
    'DEPNIFOR': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Foreign Deposits - Non-interest Bearing',
        'description': 'Represents any deposit in foreign offices on which the bank does not pay or accrue interest'
    },
    'DRLNLS': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Loan & Lease Charge-offs',
        'description': 'Total Charged-Off Loans and Lease Financing Receivables Debited To The Allowance For Loan and Lease Losses\nNote: For Banks With Foreign Operations, Data For December 1972 Through December 1975 Are Domestic Only'
    },
    'EAMINTAN': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Memo: Amortization of Intangibles',
        'description': 'Goodwill Impairment Losses and Amortization Expense and Impairment Loss For Other Intangible Assets On A Consolidated Basis\n\nNote:\n(1) Prior To March 2001, Listed As Memoranda Only and Is Included In All Other Non-interest Expense\n(2) Includes Only Amortization Of Goodwill For Tfr Filers'
    },
    'EDEP': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Int Exp - Total Deposits',
        'description': 'Interest Expense On Total Deposits (Domestic and Foreign) On A Consolidated Basis\nNote: For Banks With Foreign Operations, Data For December 1972 Through December 1975 Are Domestic Only'
    },
    'EDEPDOM': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Int Exp - Deposit in Domestic Offices',
        'description': 'Interest Expense On Total Deposits Held In Domestic Offices\nNote: For Banks With Foreign Operations, Data For December 1972 Through December 1975 Are Domestic Only'
    },
    'EDEPFOR': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Int Exp - Deposits in Foreign Offices',
        'description': 'Deposit Interest Expense-For (1976-Present -- Represents all interests on all liabilities reportable as deposits in foreign offices. -- 1934-1975 -- Interest on foregin office deposits is not available. Reports of income were submitted on a domestic only basis.)'
    },
    'EEREPP': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Fed Funds Purchased/Securities Sold',
        'description': 'Represents the gross expenses of all liabilities reportable under this category'
    },
    'EFHLBADV': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Int Exp Oth - Advances From FHLB',
        'description': 'Interest Expense and The Amortization Of Any Related Yield Adjustments On Fhlbank Advances\nNote: Only Reported By Tfr Filers'
    },
    'EFREPP': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Int Exp - Fed Funds Purchased/Securities Sold',
        'description': "Interest Expense On Federal Funds Purchased and Securities Sold Under Agreements To Repurchase On A Consolidated Basis (Prior To March 1997 Was On A Consolidated Basis In Domestic Offices Of The Bank and Of Its Edge and Agreement Subsidiaries, and In Ibf'S)\nNote: For Banks With Foreign Operations, Data For December\n1972 Through December 1975 Are Domestic Only"
    },
    'EINTEXP': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Interest Expense',
        'description': 'Total Interest Expense On A Consolidated Basis\nNote: For Banks With Foreign Operations, Data For December\n1972 Through December 1975 Are Domestic Only'
    },
    'EINTEXP2': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Eintexp2',
        'description': 'Eintexp2'
    },
    'ELNATR': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Provision for Loan & Lease Losses',
        'description': 'Provision For Loan & Lease Losses On A Consolidated Basis\n\nNote:\n(1) Beginning March 2003, Includes The Provision For Allocated Transfer Risk Related To Loans\n(2) From March 1997 To December 2000, Defined As The Provision For Credit Losses & Allocated Transfer Risk Reserve Which Includes The Provision For Off-Balance Sheet Credit Losses For Call Report Filers\n(3) Prior To March 1997, Defined As The Provision For Loan and Lease Losses & Allocated Transfer Risk\n(4) For Tfr Filers, Consists Of The Provision For Loan and Lease Losses\n(5) Reflects Net Provision For Losses On Interest-Bearing Assets For Tfr Filers\n(6) For Banks With Foreign Operations, Data For December 1972 Through December 1975 Are Domestic Only'
    },
    'EOTHNINT': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'All Other Non-interest Expenses',
        'description': 'All Other Non-interest Expense On A Consolidated Basis\n\nNote:\n(1) Prior To March 2001, Included The Amortization Of Intangible Assets For Call Reporters\n(2) Greater Detail Is Provided In Subsequent Data Fields For All Items In Excess Of 10% Of This Item All Other Non-interest Expense On A Consolidated Basis\n(3) Does Not Include Losses On Asset Sales For Tfr Filers Beginning June 1996, Such Gains (Losses) Are Included Net In Non-interest Income\n(4) Includes Loss On Sale Of Securities Held For Investments For Tfr Filers Between March 1984 Through December 1986\n(5) For Banks With Foreign Operations, Data For December 1972 Through December 1975 Are Domestic Only'
    },
    'EPREMAGG': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Occupancy Expense',
        'description': 'Expenses Of Premises and Fixed Assets (Net Of Rental Income and Excluding Salaries and Employee Benefits and Mortgage Interest) On A Consolidated Basis\nNote: For Banks With Foreign Operations, Data For December 1972 Through December 1975 Are Domestic Only'
    },
    'EQ': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Equity',
        'description': 'Represents the sum of all capital accounts'
    },
    'EQCDIV': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Cash Dividends Declared',
        'description': 'Cash Dividends Declared On Common and Preferred Stock On A Consolidated Basis\nNote: For Banks With Foreign Operations, Data For December 1972 Through December 1975 Are Domestic Only'
    },
    'EQCDIVC': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Cash Dividends Declared (Common)',
        'description': 'Cash Dividends Declared On Common Stock On A Consolidated Basis\n\nNote:\n(1) 034 Reporters Only File Data On The December Call\n(2) For Banks With Foreign Operations, Data For December 1972 Through December 1975 Are Domestic Only'
    },
    'EQCDIVP': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Cash Dividends Declared (Preferred)',
        'description': 'Cash Dividends Declared On Preferred Stock On A Consolidated Basis\nNote:\n(1) 034 Reporters Only File Data On The December Call\n(2) For Banks With Foreign Operations, Data For December 1972 Through December 1975 Are Domestic Only'
    },
    'EQCS': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Common Stock',
        'description': 'Common Stock On A Consolidated Basis\nNote: For Banks With Foreign Operations, Data For March & September Of 1972 Through 1975 Are Reported On A Domestic Basis'
    },
    'EQDIV': {
        'type': 'integet',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Cash Divident Declared',
        'description': 'The total of cash dividends declared on all preferred and common stock during the calendar year, regardless of when payable'
    },
    'EQNM': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Equity Capital',
        'description': 'Total Capital (Represents the total of all capital components, including FDIC net worth certificates.)'
    },
    'EQNWCERT': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'FDIC Net Worth Certificates',
        'description': 'Net Worth Certificates Represents The Outstanding Balances Issued To The Fdic In Exchange For Promissory Notes Received From The Fdic On A Consolidated Basis'
    },
    'EQOTHCC': {
        'type': 'integer',
        'title': 'Other Capital',
        'description': 'Other Capital'
    },
    'EQPP': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Perpetual Preferred Stock',
        'description': 'Perpetual Preferred Stock and Related Surplus On A Consolidated Basis\nNote: For Banks With Foreign Operations, Data For March & September Of 1972 Through 1975 Are Reported On A Domestic Basis'
    },
    'EQSUR': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Surplus',
        'description': 'Surplus (Excludes All Surplus Related To Preferred Stock) On A Consolidated Basis\nNote: For Banks With Foreign Operations, Data For March & September Of 1972 Through 1975 Are Reported On A Domestic Basis\n'
    },
    'EQUPTOT': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Undivided Profits',
        'description': 'Undivided Profits, Capital Reserves, Net Unrealized Holding Gains (Losses) On Available-For-Sale Securities and Other Equity Capital Components and/Or\nAccumulated Gains (Losses) On Cash Flow Hedges On A Consolidated Basis\n\nNote:\n(1) Prior To March 1999 Included Undivided Profits, Capital Reserves and Net Unrealized Gains (Losses) On Available-For-Sale Securities\n(2) Prior To March 1994 Included Undivided Profits and Capital Reserves Less Net Unrealized Loss On Marketable Equity Securities\n(3) This Item Includes Net Worth Certificates For Bif Thrifts\n(4) For Banks With Foreign Operations, Data For March & September Of 1972 Through 1975 Are Reported On A Domestic Basis'
    },
    'ESAL': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Employee Salaries and Benefits',
        'description': 'Salaries and Employee Benefits On A Consolidated Basis Note: For Banks With Foreign Operations, Data For December 72 Through December 1975 Are Domestic Only'
    },
    'ESUBND': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Int Exp - Subordinated Notes',
        'description': 'Interest Expense On Subordinated Notes and Debentures On A Consolidated Basis\nNote:\n1. This Item Is Not Reported By Form 51 Filers\n2. For Banks With Foreign Operations, Data For December 1972 Through December 1975 Are Domestic Only'
    },
    'EXTRA': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Net Extraordinary Items',
        'description': 'Discontinued Operations, Net Of Applicable Income Taxes On A Consolidated Basis\n\nNote:\n(1) Prior To March 2016, Defined As Extraordinary Items and and Other Adjustments, Net Of Taxes On A Consolidated Basis\n(2) This Item Does Not Include The Tax Effects Related To Securities Gains and Losses and Extraordinary Items From June 1984 Through December 1985 For Bif Thrifts (Refer To Applicable Income Taxes)\n(3) For Banks With Foreign Operations, Data For December 1972 Through December 1975 Are Domestic Only'
    },
    'FD_BIF': {
        'type': 'integer',
        'title': 'FDIC Supervised, BIF Insured Institutions',
        'description': 'FDIC Supervised, BIF Insured Institutions'
    },
    'FD_SAIF': {
        'type': 'integer',
        'title': 'FDIC supervised, SAIF Insured Institutions',
        'description': 'FDIC supervised SAIF insured institutions'
    },
    'FREPO': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Federal Funds Sold',
        'description': "Federal Funds Sold and Securities Purchased Under Agreements To Resell On A Consolidated Basis\n\nNote:\n(1) Prior To March 1997, Includes Only Federal Funds Sold and Securities Purchased Under Agreements To Resell In Domestic Offices Of The Bank and Of Its Edge and Agreement Subsidiaries, and In Ibf'S\n(2) Prior To March 1998, Includes Only Federal Funds Sold For Tfr Filers\n(3) For Banks With Foreign Operations, Data For March & September Of 1972 Through 1975 Was Reported On A Domestic Basis"
    },
    'FREPP': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Fed Funds & Repos Purchased',
        'description': 'Federal Funds Purchased and Securities Sold Under Agreements To Repurchase On A Consolidated Basis \nNote:\n(1) Prior To March 1998, Includes Only Reverse Repurchase Agreements For Tfr Filers\n(2) For Banks With Foreign Operations Data For March & September Of 1972 Through 1975 Are Reported On A Domestic Basis'
    },
    'ICHBAL': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Int Inc - Balances Due',
        'description': 'Total Interest Income On Balances Due From Depository Institutions On A Consolidated Basis'
    },
    'IFEE': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Fee Income',
        'description': 'Fee Income (Represents service charges on deposit accounts such as maintenance fees, activity charges, administrative charges, overdraft charges and check certification charges; mortgage loans servicing fees plus other fees and charges, including prepayment loan fees, late charges, assumption fees, and amortization of commitment fees.)'
    },
    'IFREPO': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Int Inc - Fed Funds Sold/Securities Purchased',
        'description': 'Interest Income On Federal Funds Sold and Securities Purchased Under Agreements To Resell On A Consolidated Basis\nNote:\n(1) Prior To March 1997 Included Only Income From Domestic Offices Of The Bank and Of Its Edge and Agreement Subsidiaries, and In Ibfs On A Consolidated Basis\n(2) For Banks With Foreign Operations Data For December 1972 Through 1975 Are Domestic Only'
    },
    'IGLSEC': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Securities Gains and Losses',
        'description': 'Realized Gains (Losses) On Held-To-Maturity and Available-For-Sale Debt Securities and Unrealized Holding Gains (Losses) On Equity Securities Not Held For Trading Before Adjustments For Income Taxes On A Consolidated Basis (Also Includes Realized Gains On Equity Securities Until The Institution Adopts Asu 2016-01)\nNote:\n1. Prior To March 2018, Defined As Realized Gains (Losses) On Held-To-Maturity and Available-For-Sale Securities Before Adjustments For Income Taxes On A Consolidated Basis\n2. Beginning In The 2018 Reporting Year, Includes Unrealized Gains (Losses) On Equity Securities For Institutions That Adopted Asu2016-01 and Includes Realized Gains (Losses) On Equity Securities For Institutions That Have Not Yet Adopted Asu2016-01\n3. Prior To March 1994 Defined As Gains (Losses) On Securities Not Held In Trading Accounts \n4. From March 1990 Through March 2009, Includes Gains (Losses) On Assets Held For Sale For Tfr Filers\n5. Includes Gains (Losses) On Loans Held For Investment From March 1984 Through December 1989 For Tfr Filers\n6. Tfr Filers Report Only Gains From March 1984 Through December 1986\n7. For Banks With Foreign Operations Data For December 1972 Through December 1975 Are Domestic Only'
    },
    'ILNDOM': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Int Inc - Domestic Office Loans',
        'description': 'Total Interest and Fees On Loans Held In Domestic Offices\nNote:\n(1) U-Size-Stratum = 0001 Means That Bank Has Total Assets Less Than $25 Million\n(2) U-Size-Stratum = 0002 Means That Bank Has Total Assets Equal To Or Greater Than $25 Million\n(3) For Banks With Foreign Operations, Data For December 1972 Through December 1975 Are Domestic Only'
    },
    'ILNFOR': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Int Inc - Foreign Office Loans',
        'description': "Total Interest and Fees On Loans Held In Foreign Offices, Edge and Agreement Subsidiaries, and Ibf'S"
    },
    'ILNLS': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Int Inc - Total Loans & Leases',
        'description': 'Interest and Fees On Loans and Lease Financing Receivables On A Consolidated Basis\nNote:\n(1) U-Size-Stratum = 0001 Means That Bank Has Total Assets Less Than $25 Million\n(2) U-Size-Stratum = 0002 Means That Bank Has Total Assets Equal To Or Greater Than $25 Million\n(3) For Banks With Foreign Operations, Data For December 1972 Through December 1975 Are Domestic Only'
    },
    'ILNS': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Int Inc - Loans',
        'description': 'Loans (Represents all interest, fees and similar charges levied against or associated with all assets reportable as loans. Includes interest, yield related fees, commitment fees, service charges on loans and discount accretion. (One savings bank with an office in Canada has been reporting on the Domestic & Foregin Consolidated Call Report form (FFIEC 031). It does not, however, indicate any income or expenses related to foregin operations.))'
    },
    'ILS': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Int Inc - Leases',
        'description': 'Total Interest Income From Lease Financing Receivables On A\nConsolidated Basis'
    },
    'INTAN': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Intangible Assets',
        'description': 'Intangible Assets On A Consolidated Basis'
    },
    'INTBAST': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Interest Earning Assets',
        'description': 'Total Interest Earning Assets (Derived See Si-19) - Sc'
    },
    'INTBLIB': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Interest Bearing Liabilities',
        'description': 'Total Interest Bearing Liabilities (Derived See Si-19) - Sc'
    },
    'INTINC': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Interest Income',
        'description': 'Total Interest Income On A Consolidated Basis\nNote: For Banks With Foreign Operations Data For December 1972 Through December 1975 Are Domestic Only'
    },
    'INTINC2': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'INTINC2',
        'description': 'INTINC2'
    },
    'IRAKEOGH': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': "Memo: IRA's and Keogh Plan-Deposits",
        'description': "Individual Retirement Accounts (Ira'S) and Keogh Plan\nAccounts Held In Domestic Offices\nNote: Listed As Memoranda Only"
    },
    'ISC': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Int Inc - Investment Securities',
        'description': 'Total Interest and Dividend Income On: U.S. Treasury Securities, U.S. Government Agency and Corporation Obligations, Securities Issued By States and Political\nSubdivision In The U.S., Other Domestic Debt Securities, Foreign Debt Securities, and Equity Securities (Including Investments In Mutual Funds) On A Consolidated Basis\nNote:\n(1) This Item Includes Interest Income On Deposits For Tfr Filers\n(2) Includes Interest Income On Assets Held In Trading Accounts For Tfr Filers For Two Distinct Periods: (A) March 1984 Through December 1989 and (B) June 1996\nAnd Following Quarters.\n(3) For Banks With Foreign Operations, Data For December 1972 Through December 1975 Are Domestic Only'
    },
    'ISERCHG': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Service Charges on Deposit Accounts',
        'description': 'Represents service charges on deposit accounts in domestic offices such as maintenance fees, activity charges, administrative charges, overdraft charges, and check certification charges'
    },
    'ITAX': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Applicable Income Taxes',
        'description': 'Represents Federal, state and local taxes on income. It does not include taxes relating to securities transactions or extraordinary items'
    },
    'ITAXR': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Pre-Tax Net Operating Income',
        'description': 'Pre-Tax Net Operating Income (Represents Net Interest Income plus Total Non-interest Income less Total Non-interest Expense and the Provision for Loan & Lease Losses.)'
    },
    'ITRADE': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Int Inc - Trading Account Assets',
        'description': 'Interest Income From Assets Held In Trading Accounts On A Consolidated Basis \nNote:\nBeginning March 2017, Reported As An Individual Income Category For Form 031 Filers Only and Is Included As A Component Of Other Interest Income For All Other Report Forms'
    },
    'LIAB': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Liabilities',
        'description': 'Total Liabilities Including Subordinated Notes and Debentures and Limited Life Preferred Stock and Related Surplus On A Consolidated Basis\nNote: Prior To March 2009, This Item Included Noncontrolling (Minority) Interests In Consolidated Subsidiaries For Call Report and Tfr Filers'
    },
    'LIABEQ': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Liabilities and Equity Capital',
        'description': 'Total Liabilities, Limited-Life Preferred Stock, and Equity Capital On A Consolidated Basis Note: For Banks With Foreign Operations Data For March & September Of 1972 Through 1975 Are Reported On A Domestic Basis'
    },
    'liqasstd': {
        'type': 'integer',
        'title': 'Assisted Payouts',
        'description': 'Represents all assisted payouts of FDIC-insured savings institutions that are not in RTC conservatorship.'
    },
    'liqunass': {
        'type': 'integer',
        'title': 'Voluntary Liquidations',
        'description': 'Represents all instances where the owners of a thrift voluntarily surrender their charter with all liabilities including deposits paid down and all assets sold.'
    },
    'LNAG': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Agricultural Loans',
        'description': 'Loans To Finance Agricultural Production and Other Loans To Farmers On A Consolidated Basis\nNote: For Banks With Foreign Operations, Data For All Periods Form December 1972 Through September 1978 Are Domestic Only'
    },
    'LNALLOTH': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'All Other Loans to Individuals',
        'description': 'All Other Loans (1969-Present -- Represents Federal funds purchased, securities sold under agreements to repurchase, demand notes issued to the US Treasury, mortgage indebtedness, liabilities under capitalized leases and all other liabilities for borrowed money. -- 1934-1968 -- Does not include mortgage indebtedness which is netted against bank premises.)'
    },
    'LNATRES': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Allowance for Losses Loans and Leases',
        'description': 'Allowance For Loan and Lease Financing Receivable Losses and Allocated Transfer Risk On A Consolidated Basis\nNote:\n(1) From March 2001 To Dec 2002 Allocated Transfer Riskis Netted From Loans & Not Included As Part Of The Reserve\n(2) Additional Detail Can Be Found On Schedule Ri-B\n(3) For Tfr Filers Between March 1984 Through December 1989 Includes Allowance For Mortgage Pool Securities\n(4) For Banks With Foreign Operations, Data For March & September Of 1972 Through 1975 Was Reported On A Domestic Basis'
    },
    'LNAUTO': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Memo: Loans to Individuals - Auto',
        'description': 'Represents installment loans to purchase private passenger automobiles, both direct loans and purchased paper'
    },
    'LNCI': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Commercial and Industrial Loans',
        'description': 'Commercial and Industrial Loans On A Consolidated Basis Note: For Banks With Foreign Operations, Data For All Periods From December 1972 Through September 1978 Are Domestic Only'
    },
    'LNCON': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Loans to Individuals',
        'description': 'Loans To Individuals For Household, Family, and Other Personal Expenditures (Consumer Loans) On A Consolidated Basis\nNote:\n(1) For Tfr Filers Includes Revolving Loans Secured By 1-4 Family Dwelling Units From March 1984 Through March 1988\n(1) For Banks With Foreign Operations, Data For All Periods From December 1972 Through September 1978 Are Domestic Only'
    },
    'LNCONOT1': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Loans to Individuals - Home Improvement',
        'description': 'Installment Loans To Individuals To Repair and Modernize\nResidential Property Held In Domestic Offices'
    },
    'LNCONOTH': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Loans to Individuals - All Others',
        'description': 'Represents all other loans to individuals for household, family and other personal expenditures. It includes auto loans, both direct and indirect, mobile homes (unless secured by a real estate mortgage), education loans, other installment loans both secured by personal property or unsecured, and single payment loans (time or demand, secured or unsecured)'
    },
    'LNCRCD': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Loans to Individuals - Credit Card Plans',
        'description': 'Credit Cards Related Plans On A Consolidated Basis\n\nNote:\n(1)Prior To March 2001 Includes Credit Cards Related Plans-Loans To Individuals For Household, Family, and Other Personal Expenditures (Consumer Loans) Includes Check Credit and Other Revolving Credit Plans\n(2) For Tfr Filers Between March 1984 Through March 1988 This Figure Includes Home Equity Loans Based On The Creditworthiness Of The Borrower (T-Sc340)\n(3) For Banks With Foreign Operations, Data For All Periods From December 1972 Through September 1978 Are Domestic Only'
    },
    'LNDEP': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Loans to Deposit Institutions',
        'description': 'Loans To Depository Institutions On A Consolidated Basis\nNote: For Banks With Foreign Operations, Data For All Periods From December 1972 Through September 1978 Are Domestic Only\nNote:(1) Beginning March 2001 Includes Acceptances Of Other Banks\n(2) Beginning March 2001, Includes Acceptances Of Other Banks For Ibas'
    },
    'LNLS': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Gross Loans and Leases',
        'description': 'Represents the sum of all components of loans'
    },
    'LNLSGR': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Loans and Leases',
        'description': 'Loans and Lease Financing Receivables, Net Of Unearned Income, On A Consolidated Basis\nNote:\n(1) Additional Detail Can Be Found On Schedule Rc-C\n(2) For Tfr Filers This Item Is Net Of Unamortized Yield Adjustments For Mortgage Pool Securities From March 1984 Through December 1989\n(3) For Banks With Foreign Operations, Data For March & September Of 1972 Through 1975 Was Reported On A Domestic Basis'
    },
    'LNLSNET': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Net Loans and Leases',
        'description': 'Loans and Lease Financing Receivables, Net Of Unearned Income, Allowance, and Reserve On A Consolidated Basis\nNote:\n(1) For Tfr Filers This Item Is Net Of Valuation Allowances and Unamortized Yield Adjustments For Mortgage Pool Securities From March 1984 Through\n(2) For Banks With Foreign Operations, Data For March & September Of 1972 Through 1975 Are Reported On A Domestic Basis'
    },
    'LNMOBILE': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Memo: Loans to Individuals - Mobile Homes',
        'description': "Represents loans to individuals to purchase mobile homes. (If the bank's security interest in the loan was represented by a mortgage or deed of trust, the loan should be included in real estate loans)"
    },
    'LNMUNI': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Loans to States and Politicial Sub-divisions',
        'description': 'Obligations (Other Than Securities and Leases) Of States and Political Subdivisions In The U.S. (Including Nonrated Industrial Development Obligations) On A Consolidated Basis'
    },
    'LNRE': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Real Estate Loans',
        'description': 'Loans Secured By Real Estate On A Consolidated Basis\nNote:\n(1) For Tfr Filers Between March 1984 Through March 1988 This Figure Excludes Home Equity Loans Based On The Creditworthiness Of The Borrower (T-Sc340)\n(2) For Banks With Foreign Operations, Data For All Periods From December 1972 Through September 1978 Are Domestic Only'
    },
    'LNREAG': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'R/E Loan - Farmland',
        'description': 'Represents loans secured by farmland, including improvements, and other land known to be used or usable for agricultural purposes, as evidenced by mortgages or other liens. It includes loans secured by farmland that are guaranteed by the Farmers Home Administration (FHA) or by the Small Business Administration'
    },
    'LNRECONS': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'R/E Loan - Construction & Land Develop',
        'description': 'Construction and Land Development Loans Secured By Real Estate Held In Domestic Offices\nNote: For Tfr Filers Portions Of Lnrecons Were Included In Other Real Estate Loan Categories Prior To March 30, 1986'
    },
    'LNREDOM': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total R/E Loans in Domestic Offices',
        'description': 'Represents the total of all loans secured by real estate in domestic offices (U.S. and other areas)'
    },
    'LNREFOR': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total R/E Loans in Foreign Offices',
        'description': 'Represents all loans secured by real estate in foreign offices'
    },
    'LNRELOC': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Memo: Home Equity Loans',
        'description': 'Revolving, Open-End Loans Secured By 1-4 Family Residential Properties and Extended Under Lines Of Credit Held In Domestic Offices'
    },
    'LNREMULT': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'R/E Loans -  Multifamily',
        'description': 'Multifamily (5 Or More) Residential Properties Secured By Real Estate Held In Domestic Offices'
    },
    'LNRENRES': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'R/E Loan -  Non-farm/Non-residential Prop',
        'description': 'Nonfarm Nonresidential Properties Secured By Real Estate Held In Domestic Offices\nNote: For Tfr Filers This Figure Includes Mortgages On Properties That Are Used For Farming'
    },
    'LNRERES': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'R/E Loan - 1-4 Family',
        'description': 'Total Loans Secured By 1-4 Family Residential Properties Held In Domestic Offices\nNote: For Tfr Filers Between March 1984 Through March 1988 This Figure Excludes Home Equity Loans Based On The Creditworthiness Of The Borrower'
    },
    'LNRESRE': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Memo: Contra Account',
        'description': 'Allowance For Loan Losses On Real Estate Loans On A Consolidated Basis\nNote: For Tfr Filers Includes Allowance For Mortgage Pool Securities Between March 1984 Through December 1989'
    },
    'LNSP': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Memo: Loans to Individuals - Single Payment',
        'description': 'All loans both time or demand, secured or unsecured, to individuals for personal, family or other household expenditures'
    },
    'LS': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Leases',
        'description': 'Lease Financing Receivables (Net Of Unearned Income) On A Consolidated Basis\nNote: For Banks With Foreign Operations, Data For March & September Call Dates Are Domestic Only Through December 1975'
    },
    'MERGERS': {
        'type': 'integer',
        'title': 'Failures: Assisted Merger',
        'description': 'Mergers, consolidations or absorptions entered into as a result of supervisory actions. The transaction may or may not have required FDIC assistance.'
    },
    'MISSADJ': {
        'type': 'integer',
        'title': 'Other Misc. Adjustments',
        'description': 'Represents any FDIC-insured savings institution that did not file a financial report during the year in which the charter was added or deleted.'
    },
    'MTGLS': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Mortgage and Other Borrowings',
        'description': 'Represents mortgage indebtedness and liabilities under capitalized leases'
    },
    'NALNLS': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Non-accrual Loans & Leases',
        'description': 'Total Nonaccrual Loans and Lease Financing Receivables On A Consolidated Basis'
    },
    'NCHGREC': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Net Loans and Leases Charge-offs',
        'description': 'Net Loans and Leases Charge Offs (-- 1984-1989 -- Represents Loan and Lease Charge-offs less Loan and Lease Recoveries. An amount enclosed in paraentheses indicates net recoveries. Not collected by TFR filers. -- 1990-Present -- Represents Loan and Lease Charge-offs less Loan and Lease Recoveries. An amount enclosed in paraentheses indicates net recoveries.)'
    },
    'NCLNLS': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Non-current Loans & Leases',
        'description': 'Total Loans and Lease Financing Receivables 90 Days Or More Past Due and Nonaccrual On A Consolidated Basis\nNote: Includes Delinquent Loans (60 Or More Days Overdue) and Past Due Loans (One Or More Payments Missed) For Tfr Filers Prior To March 1990'
    },
    'NETINC': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Net Income',
        'description': 'Net Income Attributable To The Bank On A Consolidated Basis\nNote: For Banks With Foreign Operations, Data For December 1972 Through December 1975 Are Domestic Only'
    },
    'newcount': {
        'type': 'integer',
        'title': 'New Charters',
        'description': 'Institutions newly chartered by federal or state banking authorities including authorities in the U. S. Territories or possessions.'
    },
    'New_Char': {
        'type': 'integer',
        'title': 'New Charters',
        'description': 'Institutions newly licensed or chartered by the Office of the Comptroller of the Currency (national banks) or by state banking authorities, including banking authorities in the U. S. territories or possessions. Includes de novo institutions as well as charters issued to take over a failing institution.'
    },
    'NEW6_1': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Int Exp - Borrowed Money',
        'description': 'Represents interest expense related to demand notes issued to the U. S. Treasury, mortgage indebtedness, obligations under capitalized leases, and other borrowed money'
    },
    'NEW9_1': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'All Other Assets',
        'description': "Represents all other assets not included in previously mentioned captions. Includes, for the most part, customers' liabilities on acceptances outstanding, income earned not collected as well as any other asset not included above"
    },
    'NEW10_1': {
        'type': 'integer',
        'title': 'Corporate Bonds and Other Securities',
        'description': "Represents all securities, bonds, notes and debentures of domestic and foreign corporations. Also includes privately issued or guaranteed mortgage backed securities and certain detached U.S. Government security coupons held as a result of either their purchase or the bank's stripping them (CATS, TIGRs, COUGARs, LIONs and ETRs)."
    },
    'NEW10_2': {
        'type': 'integer',
        'title': 'Trading Account Securities',
        'description': 'Securities within the scope of ASC Topic 320, Investments – Debt Securities, that a bank has elected to report at fair value under a fair value option with changes in fair value reported in current earnings should be classified as trading securities. (https://www.fdic.gov/regulations/resources/call/crinst/2018-06/031-041-618rc-d-063018.pdf)'
    },
    'NEW10_3': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Memo: Valuation Reserves',
        'description': 'For all years except 1969-1973, investment securities are reflected net of general valuation reserves. Specific reserves are deducted from each security so reserved'
    },
    'NEW11_1': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'All Other Loans',
        'description': "Represents unplanned overdrafts and loans to: brokers and dealers in securities, any borrower for the purpose of purchasing and carrying securities, nonprofit institutions and organizations, individuals for investment purposes, real estate investment trusts, mortgage companies holding companies of depository institutions, insurance companies, finance companies, factors and other financial intermediaries, federally sponsored lending agencies, investment banks, the bank's own trust department, Small Business Investment Companies, foreign governments and official institutions, and any other loan not included in one of the above categories"
    },
    'NEW14_1': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Borrowed Funds',
        'description': 'Represents Federal funds purchased, securities sold under agreements to repurchase, demand notes issued to the US Treasury, mortgage indebtedness, liabilities under capitalized leases and all other liabilities for borrowed money'
    },
    'NEW14_2': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Other Liabilities',
        'description': 'Includes all liabilities not included above and limited life preferred stock'
    },
    'NEW14_3': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Liabilities',
        'description': 'Represents the total of all components of liabilities'
    },
    'NEW14_4': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Undivided Profits',
        'description': 'Represents undivided profits and related accounts'
    },
    'NEW15_1': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Deposits - Individuals, Partnerships and Corporations',
        'description': 'Represents all deposits of individuals, partnerships and corporations in domestic and foreign offices'
    },
    'NEW15_2': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Deposits - U.S. Government',
        'description': 'Represents all deposits of individuals, partnerships and corporations in domestic and foreign offices'
    },
    'NEW15_3': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Deposits - States and Political Subdivisions',
        'description': 'Represents all deposits of states, counties and municipalities in domestic offices. Such deposits, if any, in foreign offices are not separately reported'
    },
    'NEW15_4': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Deposits - All Other',
        'description': 'Represents all other deposits. Includes deposits of financial institutions, both domestic and foreign, deposits of foreign governments and official institutions and certified and official checks. Also includes deposits in foreign offices other than those of individuals, partnerships and corporations'
    },
    'NEW15_5': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Deposits - Domestic Savings',
        'description': 'Represents all savings deposits in domestic offices'
    },
    'NEW15_7': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Domestic Deposits',
        'description': 'Total Domestic Deposits'
    },
    'NEW16_1': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Demand Notes and Other Liabilities',
        'description': 'Represents demand notes issued to the U.S. Treasury (Treasury tax & loan account), and all other borrowings. Includes mortgage indebtedness and liabilities under capitalized leases for Call report filers. Includes FSLIC net worth certificates for TFR filers'
    },
    'NEW16_2': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Interest Bearing Deposits',
        'description': 'Represents any deposit in domestic and foreign offices on which the banks pays or accrues interest'
    },
    'NIM': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Net Interest Income',
        'description': 'Net Interest Income (Total Interest Income Minus Total Interest Expense) On A Consolidated Basis\nNote: For Banks With Foreign Operations, Data For December 1972 Through December 1975 Are Domestic Only'
    },
    'NONII': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Non-interest Income',
        'description': 'Total Non-interest Income On A Consolidated Basis\nNote:\n(1) From March 1990 Through March 2009, Excludes Gains (Losses) On Assets Held For Sale For Tfr Filers, See Tfr Instructions For So430\n(2) Excludes Gains On The Sale Of Loans Held For Investments From March 1984 Through December 1989 For Tfr Filers\n(3) For Banks With Foreign Operations, Data For December 1972 Through December 1975 Are Domestic Only'
    },
    'NONIX': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Non-interest Expense',
        'description': 'Total Non-interest Expense On A Consolidated Basis\nNote:\n(1) Excludes Losses On Asset Sales For Tfr Filers Beginning June 1996\n(2) Includes Loss On Sale Of Mortgage Pool and Other Securities Held For Investment For Tfr Filers From March 1984 Through December 1986\n(3) Excludes Losses On Loans Held For Investment For Tfr Filers From March 1987 Through December 1989\n(4) For Banks With Foreign Operations, Data For December 1972 Through December 1975 Are Domestic Only'
    },
    'NTLNLS': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Net Loan & Lease Charge-offs',
        'description': 'Represents Loan and Lease Charge-offs less Loan and Lease Recoveries. An amount enclosed in parentheses indicates net recoveries. Not collected by TFR filers'
    },
    'NTR': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Memo: Domestic Deposits Non-Transaction',
        'description': "Represents deposits that are not included in the definition of transaction accounts above or that do not satisfy the criteria necessary to be defined as a transaction account. MMDA's are specifically defined as nontransaction accounts"
    },
    'NTRTIME': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Deposits - Domestic Time',
        'description': 'Represents all time certificates of deposit, time open accounts and similar deposits in domestic offices'
    },
    'NTRTMLG': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Memo: Time Deposits (Over $100K)',
        'description': 'Time Deposits Over $100,000 Or More Held In Domestic Offices\nNote:\n(1) Listed As Memoranda Only and Is Included In Total Nontransaction Accounts\n(2) Prior To March 2007, Includes All Deposits (Not Just Time) Greater Than $100,000 For Tfr Filers. Except For December 2006, Includes All Nonretirement Deposits Over\n$100,000 and All Retirement Deposits Over $250,000 For Tfr Filers\n(3) Includes Time Deposits Of $100,000 Or More'
    },
    'NUMEMP': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Number of Full Time Employees',
        'description': 'Number Of Full Time-Equivalent Employees On Payroll At The End Of The Current Period\nNote:\n(1) Listed As Memoranda Only\n(2) For Banks With Foreign Operations Data For March & September Of 1972 Through 1975 Are Reported On A Domestic Basis'
    },
    'OEA': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Other Earning Assests',
        'description': 'Other Earning Assests (-- 1984-1989 -- Represents Federal funds sold and securities purchased under agreements to resell (repurchase agreements). Items not separately reported by TFR filers. They are included in Secruties. -- 1990-Present -- Represents Federal funds sold and securities purchased under agreements to resell (repurchase agreements). Includes only Federal funds sold for TFR filers. Repurchase agreements are included in Securities.)'
    },
    'OFFICES': {
        'type': 'integer',
        'title': 'Offices',
        'description': 'Offices include: Multiple service offices, Military facilities, Drive-in facilities, Loan production offices, Consumer credit offices, Seasonal offices, Administrative offices, Messenger service offices, Supermarket banking offices, and Other offices.'
    },
    'OINTBOR': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Demand Notes and Other Borrowings',
        'description': 'Demand Notes and Other Borrowings (Represents demand notes issued to US Treasury (Treasury tax & loan account), and all other borrowings. Includes mortgage indebtedness and liabilities under capitalized leases for Call report filers. Includes FSLIC net worth certificates for TFR filers.)'
    },
    'OINTEXP': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Other Interest Expenses',
        'description': 'Total Other Interest Expenses (Federal Funds Purchased and Securities Sold -- Represents the gross expense of all liabilities reportable under this category. This item is not reported separately by TFR filers. It is included in Borrowed Money).'
    },
    'OINTINC': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Int Inc - Total Other',
        'description': 'Total Other Interest Income (Represents the total of all Other Interest Income components).'
    },
    'OONONII': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Other Non-interest Income',
        'description': 'Other Non Interest Income (1984-1989 -- Same as Total Other Interest Income except gains on the sale of loans held for investment are excluded for TFR filers. -- 1990- Present -- Represents income derived from the sale of assets held for sale; office building operations; real estate held for investment; REO operations; LOCOM adjustments made to assets held for sale; net income (loss) from investements in service corporations/subsidiaries (other than operating or finance subsidiaires); leasing operations; realized and unrealized gains (losses) on trading assets; gains on the sale of REO real estate held for investment, and loans held for investment; and the amoritization of deferred gains (losses) on asset hedges.)'
    },
    'ORE': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Other Real Estate Owned',
        'description': 'Other Real Estate Owned On A Consolidated Basis\nNote:\n(1) Prior To June 2009, Includes Direct and Indirect Investments In Real Estate\n(2) For Banks With Foreign Operations Data For March & September Of 1972 Through 1975 Was Reported On A Domestic Basis'
    },
    'ORET': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Other Real Estate',
        'description': 'Other Real Estate (Represents other real estate owned net of reserves for losses). Not available for 1997. For 1986 through 1988 ORET = ORE + INVSUORE; for all other years ORET = ORE'
    },
    'OT_BIF': {
        'type': 'integer',
        'title': 'Non FDIC Supervised BIF Insured Institutions',
        'description': 'Non FDIC supervised BIF insured institutions'
    },
    'OT_SAIF': {
        'type': 'integer',
        'title': 'Non FDIC Supervised SAIF Insured Institutions',
        'description': 'Non FDIC supervised SAIF insured institutions'
    },
    'OTHASST': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'All Other Assets',
        'description': 'All Other Assets (Same as Other Real Estate except that investment in service corporations/subsidiaries is reported gross of valuation allowances by TFR filers, and assets held in trading accounts are included in Securities for TFR filers. -- 1990-Present -- Represents all associations assets not previously mentioned. Includes all non real estate repossessed property, investment in service corporations/subsidiaries, property leased to others, income earned but not yet collected, assets held in the trading accounts, and miscellaneous assets) For 2009- present OTHASST = SUM (INVSUB + INVSUORE + CUSLI + OA)'
    },
    'OTHBFHLB': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Advances from FHLB',
        'description': 'Other Liabilities From The Fhlb\nNote:Prior To March 2001 Only Reported On Tfrs'
    },
    'OTHBORR': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Int Exp Oth - Borrowed Money',
        'description': 'Borrowed Money (Represents interest expense related to demand notes issued the US Treasury, mortage indebtedness, obligations under capitalized leases and on other borrowed money.'
    },
    'OTHEQ': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Other Equity',
        'description': 'Represents all equity securities not held for trading: investment in mutual funds, common stock of FNMA, Student Loan Marketing Association, Federal Home Loan Mortgage Corporation, Federal Reserve Bank stock, Federal Home Loan Bank stock, minority interests not meeting the definition of associated companies, "restricted" stock, and other equity securities in both domestic and foreign corporations\n'
    },
    'OTHER': {
        'type': 'integer',
        'title': 'Other',
        'description': 'Withdrawals from FDIC insurance, voluntary liquidations, or conversions to institutions that are not considered commercial banks. Also includes relocation of banks from one state to another.'
    },
    'OTHLIAB': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Other Liabilities',
        'description': 'Other Liabilities (Includes all liabilities not included above and limited life preferred stock. 2001- present -- Includes OTHER LIAB & MINOR IN SUBS).'
    },
    'OTHNBORR': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Borrowed Funds',
        'description': 'Borrowed Funds (Includes federal funds purchased, securities sold under agreements to repurchase (reverse repurchase agreements), demand notes issued to the US Treasury, mortgage indebtedness, liabilities under capitalized leases and all other liabilities for borrowed money. Includes only reverse purchase agreements (securities sold under agreements to repurchase) and FSLIC net worth certificates for TFR filers)'
    },
    'OTLNCNTA': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Less: Other Contra Accounts',
        'description': 'Other Contracts (Represents amount reported by savings institutions that file on the Thrift Financial Report. Contra accounts include accrued interest receivable, unamortized yield adjustments and valuation allowances. Negative amounts reflect unamortized premiums and deferred direct costs exceeding unamortized discounts and deferred loan fees).'
    },
    'PAID_OFF': {
        'type': 'integer',
        'title': 'Failures: Paid Off',
        'description': 'Institutions that were declared insolvent, the insured deposits of which were paid by the FDIC.'
    },
    'P3LNLS': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Loans & Leases P/D 30-89 Days',
        'description': 'Total Loans and Lease Financing Receivables Past Due 30 Through 89 Days and Still Accruing Interest On A Consolidated Basis\nNote:\n(1) Prior To March 2001,This Information On An Institution Level Is Considered Confidential By The Ffiec'
    },
    'P9LNLS': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Loans & Leases P/D 90+ Days',
        'description': 'Total Loans and Lease Financing Receivables Past Due 90 Or More Days and Still Accruing Interest On A Consolidated Basis'
    },
    'PTXNOINC': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Pre-Tax Net Operating Income',
        'description': 'Pre-Tax Net Operating Income'
    },
    'REL_CO': {
        'type': 'integer',
        'title': 'Conversions',
        'description': 'Conversions of existing institutions of any type that meet the definition of commercial banks (see Definition of Total Commercial Banks and have applied for and received FDIC insurance. Also includes bank relocations from one state to another.'
    },
    'SAVINGS': {
        'type': 'integer',
        'title': 'Total Savings Institutions (Total Insured)',
        'description': 'Total Insured Savings Institutions including institutions that did not file a 12/31 fincncial report and other adjustments (See Notes to User).'
    },
    'SC': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Investment Securities (Book Value)',
        'description': 'Total Securities: The Sum Of Held-To-Maturity Securities At Amortized Cost, Available-For-Sale Securities At Fair Value and Equity Securities With Readily Determinable Fair Values Not Held For Trading On A Consolidated Basis\nNote:\n1. Prior To March 2018, Defined As Total Held-To-Maturity At Amortized Cost and Available-For-Sale At Fair Value Securities (Excludes Assets Held In Trading Accounts) On A Consolidated Basis\n2. Beginning In 2018, Includes Equity Securities For Institutions That Have Adopted Asu2016-01 and Those Institutions That Have Not Yet Adopted This Accounting\nStandard\n3. Prior To March 1994 Item Defined As Book Value\n4. Additional Detail Can Be Found On Schedule Rc-B\n5. For Tfr Filers Between March 1984 Through December 1989 Includes Interest-Earning Deposits In Fhlbs, Other Interest-Earning Deposits, Federal Funds Sold and Assets Held In Trading Accounts\n6. For Banks With Foreign Operations Data For March & September Of 1972 Through 1975 Are Reported On A Domestic Basis'
    },
    'SCAGE': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'U.S. Agencies and Corporation Securities',
        'description': 'Total U.S. Government Agency and Corporation Obligations On A Consolidated Basis\nNote:\n1) From June 2009 Through December 2010, This Item Excluded Other Commercial\nMortgage-Backed Securities\n2) Prior To June 2009, This Item Included Other Commercial Mortgage-Backed Securities\n3) Beginning March 1994 Consists Of Held-To-Maturity At Amortized Cost and Available-For-Sale At Fair Value Securities\n4) Includes The Aforementioned Securities Held In Trading Accounts For Tfr Filers\n5) Includes U.S. Treasury Securities For Tfr Filers Between March 1984 Through December 1989 and After March 1996\n6) Does Not Include Mortgage Derivative Securities For Tfr Filers Between March 1984 Through December 1986\n7) For Banks With Foreign Operations, Data For March & September Of 1973 Through 1975 Are Reported On A Domestic Basis'
    },
    'SCEQ': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Equity Securities',
        'description': 'Total Equity Securities Available-For-Sale At Fair Value On A Consolidated Basis\nNote:\n(1) Beginning March 2018 Does Not Include Equity Securities For Institutions That Have Adopted Asu 2016-01 See Sceqfv\n(2) Includes The Aforementioned Securities Held In Trading Accounts For Tfr Filers'
    },
    'SCMTGBK': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Memo: Mortgage Backed Securities',
        'description': 'Mortgage Backed Securities On A Consolidated Basis\nIncludes:\n(1) U.S. Government Agency and Corporation Obligations Issued Or Guaranteed Certificates Of Participation In Pools Of Residential Mortgages,\n(2) U.S. Government Agency and Corporation Obligations Collateralized Mortgage Obligations Issued By Fnma and Fhlmc (Including Remics)\n(3) Other Domestic Debt Securities - Private (I.E., Non-Government-Issued-Or-Guaranteed) Certificates Of Participations In Pools Of Residential Mortgages, and\n(4) Other Domestic Debt Securities - Privately-Issued Collateralized Mortgage Obligations (Including Remics)'
    },
    'SCMUNI': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'States and Political Subdivisions Securities',
        'description': 'Total Securities Issued By States and Political Subdivisions Held-To-Maturity At Amortized Cost and Available-For-Sale At Fair Value On A Consolidated Basis\nNote:\n(1) Prior To March 1994 Item Was Defined As Book Value\n(2) Includes The Aforementioned Securities Held In Trading Accounts For Tfr Filers\n(3) For Banks With Foreign Opeations, Data For March & September Of 1973 Through 1975 Are Reported On A Domestic Basis'
    },
    'SCMV': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Market Values',
        'description': 'Represents the market (fair) value of all investment securities'
    },
    'SCRES': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Less: Contra Accounts',
        'description': 'Contra-Assets To Securities (Reserves)\nNote: For Tfr Filers Only'
    },
    'SCUS': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'U.S. Treasury & Agency',
        'description': 'Total U.S. Treasury Securities and U.S. Government Agency and Corporation Obligations On A Consolidated Basis\nNote:\n1) From June 2009 Through December 2010 This Item Excluded Commercial Mortgage Backed Securities\n2) Prior To June 2009, This Item Included Commercial Mortgage Backed Securities\n3) Beginning March 1994 Consists Of Held-To-Maturity At Amortized Cost and Available-For-Sale At Fair Value Securities\n4) Does Not Include Mortgage Derivative Securities From March 1984 Through December 1986 For Tfr Filers\n5) Includes The Aforementioned Securities Held In Trading Accounts For Tfr Filers\n6) For Banks With Foreign Operations Data For March & September Of 1973 Through 1975 Are Reported On A Domestic Basis'
    },
    'SCUSA': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Securities Of Us Agencies',
        'description': 'Securities Of Us Agencies'
    },
    'SCUST': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'U.S. Treasury Securities',
        'description': 'U.S. Treasury Securities Held-To-Maturity At Amortized Cost and Available-For-Sale At Fair Value On A Consolidated Basis\nNote:\n(1) Beginning June 1996, Tfr Filers No Longer Report U.S. Treasury Securities Separately\n(2) Prior To March 1994 Item Was Defined As Book Value\n(3) Includes The Aforementioned Securities Held In Trading Accounts For Tfr Filers\n(4) For Banks With Foreign Operations, Data For March & September Of 1973 Through 1975 Are Reported On A Domestic Basis'
    },
    'STNAME': {
        'type': 'string',
        'title': 'Locations',
        'description': 'Locations',
        'x-elastic-type': 'keyword'
    },
    'STNUM': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'title': 'State Number',
        'description': 'State Number'
    },
    'SUBLLPF': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Subordinated Notes',
        'description': 'Subordinated Notes and Debentures and Limited-Life Preferred Stock and Related Surplus On A Consolidated Basis\nNote: (1) Banks With Foreign Operations Data For March & September Of 1972 Through 1975 Are Reported On A Domesitc Basis'
    },
    'SUBND': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Subordinated Notes/Debentures',
        'description': 'Represents all notes and debentures subordinated to deposits and all capital notes and debentures'
    },
    'TINTINC': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Int Inc - Total Other',
        'description': 'Total Other Interest Income (Represents the sum of Other Interest Income - Investment Securities, Trading Account Assets, Federal Funds Sold and Securities Purchased, and Balanaces Due from Depository Institutions)'
    },
    'tochrt': {
        'type': 'integer',
        'title': 'Charter Transfers to Commercial Banks',
        'description': 'Represents the charter transfer of existing FDIC-insured savings institutions to an FDIC-insured commercial bank charter.'
    },
    'tofail': {
        'type': 'integer',
        'title': 'Assisted Mergers with Commercial Banks',
        'description': 'Represents the absorption of a failing savings institution by a commercial bank with assistance from either the BIF or SAIF.'
    },
    'TOINTEXP': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Int Exp  - Total Deposits',
        'description': 'Total Other Interest Expense (Represents the sum of all components of Other Interest Expense)'
    },
    'tomerg': {
        'type': 'integer',
        'title': 'Unassisted Mergers with Commercial Banks',
        'description': 'Represents the absorption of a savings institution charter by a commercial bank without assistance.'
    },
    'tortc': {
        'type': 'integer',
        'title': 'Failures Transferred to the RTC',
        'description': 'Represents institutions that were declared failed and placed under RTC conservatorship until a buyer(s) is(are) found or a payout to depositors occurs.'
    },
    'TOTAL': {
        'type': 'integer',
        'title': 'Total Commercial Banks (Total Insured)',
        'description': 'Total Insured Commercial Banks including institutions that did not file a 12/31 fincncial report and other adjustments (See Notes to User)'
    },
    'TOT_FDIC': {
        'type': 'integer',
        'title': 'Total FDIC Supervised Savings Institutions',
        'description': 'Total FDIC Supervised Savings Institutions'
    },
    'TOT_OTS': {
        'type': 'integer',
        'title': 'Total Non FDIC Supervised Savings Institutions',
        'description': 'Total Non FDIC Supervised Savings Institutions'
    },
    'TOT_SAVE': {
        'type': 'integer',
        'x-special-note': 'State level institution count is currently unavailable.',
        'title': 'Total Savings Institutions',
        'description': 'All FDIC Insured Savings Institutions filing a 12/31 financial report'
    },
    'TPD': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Loans and Leases Past Due',
        'description': 'Total Loans and Leases Past Due'
    },
    'TRADE': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Trading Account Assets',
        'description': 'Assets Held In Trading Accounts On A Consolidated Basis\nNote:\n(1) Effective March 1994 Item Reported On A Gross Basis\n(2) Additional Detail Can Be Found On Schedule Rc-D\n(3) For Banks With Foreign Operations Data For March & September Of 1972 Through 1975 Are Reported On A Domestic Basis,\n(4) For Periods 1972 Through 1983 Includes Only Securities'
    },
    'TRADES': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Less: Trading Accounts',
        'description': 'Trading Accounts'
    },
    'TRN': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Memo: Domestic Deposits Transaction',
        'description': "Represents all demand deposits, NOW accounts, ATS accounts, accounts from which payments may be made to third parties by means of an automated teller machine, a remote service unit, or another electronic device, and accounts that permit third party payments through use of checks, drafts, negotiable instruments, or other similar instrument. (MMDA's are specifically excluded from the latter two definitions)"
    },
    'UNASSIST': {
        'type': 'integer',
        'title': 'Unassisted Mergers',
        'description': 'Voluntary mergers, consolidations or absorptions of two or more institutions.'
    },
    'UNINC': {
        'type': 'integer',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Unearned Income',
        'description': 'Unearned Income On Loans On A Consolidated Basis\nNote: For Banks With Foreign Operations, Data For March 1976 Through September 1978 Are Domestic Only'
    },
    'UNIT': {
        'type': 'integer',
        'title': 'Unit Banks',
        'description': 'Unit banks are institutions that are operating only one office at which deposits are received or other banking business is conducted.'
    },
    'YEAR': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'title': 'Year',
        'description': 'Statistics reported as of end of year.'
    }
}
