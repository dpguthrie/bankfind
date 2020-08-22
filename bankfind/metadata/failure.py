failure_dict = {
    'NAME': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'title': 'Institution Name',
        'description': "This is the legal name of the institution. When available, the Institution's name links to useful information for the customers and vendors of these institutions. This information includes press releases, information about the acquiring institution, (if applicable), how your accounts and loans are affected, and how vendors can file claims against the receivership."
    },
    'CERT': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'title': 'Cert',
        'description': 'The certificate number assigned by the FDIC used to identify institutions and for the issuance of insurance certificates. By clicking on this number, you will link to the Institution Directory (ID) system which will provide the last demographic and financial data filed by the selected institution.'
    },
    'FIN': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'title': 'FIN',
        'description': 'Financial Institution Number (FIN) is a unique number assigned to the institution as an Assistance Agreement, Conservatorship, Bridge Bank or Receivership.'
    },
    'CITYST': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'title': 'Location',
        'description': 'The city and state (or territory) of the headquarters of the institution.'
    },
    'FAILDATE': {
        'type': 'string',
        'format': 'date-time',
        'title': 'Effective Date',
        'description': 'The date that the failed / assisted institution ceased to exist as a privately held going concern. For institutions that entered into government ownership, such as FDIC Bridge Banks and RTC conservatorships, this is the date that they entered into such ownership.'
    },
    'FAILYR': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'title': 'Year',
        'description': 'The 4-digit year that the failed / assisted institution ceased to exist as a privately held going concern. For institutions that entered into government ownership, such as FDIC Bridge Banks and RTC conservatorships, this is the date that they entered into such ownership.'
    },
    'SAVR': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'title': 'Insurance Fund',
        'description': 'Before 1989, there were two federal deposit insurance funds, one administered by the FDIC, which insured deposits in commercial banks and state-chartered savings banks, and another administered by the Federal Savings and Loan Insurance Corporation (FSLIC), which insured deposits in state- and federally-chartered savings associations. In 1989, the Financial Institutions Reform, Recovery and Enforcement Act (FIRREA) specified that thereafter the FDIC would be the federal deposit insurer of all banks and savings associations and would administer both the FDIC fund, which was renamed the Bank Insurance Fund (BIF) and the replacement for the insolvent FSLIC fund, which was called the Savings Association Insurance Fund (SAIF). Although it was created in 1989, the SAIF was not responsible for savings association failures until 1996. From 1989 through 1995, savings association failures were the responsibility of the Resolution Trust Corporation (RTC). In February 2006, The Federal Deposit Insurance Reform Act of 2005 provided for the merger of the BIF and the SAIF into a single Deposit Insurance Fund (DIF). Necessary technical and conforming changes to the law were made under The Federal Deposit Insurance Reform Conforming Amendments Act of 2005. The merger of the funds was effective on March 31, 2006. For additional information about deposit insurance fund and legislation, go to http://www.fdic.gov/deposit/insurance/index.html.',
        'options': ['BIF', 'RTC', 'FSLIC', 'SAIF', 'DIF', 'FDIC']
    },
    'RESTYPE1': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'title': 'Transaction Type',
        'description': "Institutions have been resolved through several different types of transactions. The transaction types outlined below can be grouped into three general categories, based upon the method employed to protect insured depositors and how each transaction affects a failed / assisted institution's charter. In most assistance transactions, insured and uninsured depositors are protected, the failed / assisted institution remains open and its charter survives the resolution process. In purchase and assumption transactions, the failed / assisted institution's insured deposits are transferred to a successor institution, and its charter is closed. In most of these transactions, additional liabilities and assets are also transferred to the successor institution. In payoff transactions, the deposit insurer - the FDIC or the former Federal Savings and Loan Insurance Corporation - pays insured depositors, the failed / assisted institution's charter is closed, and there is no successor institution. For a more complete description of resolution transactions and the FDIC's receivership activities, see Managing the Crisis: The FDIC and RTC Experience, a study prepared by the FDIC's Division of Resolutions and Receiverships. Copies are available from the FDIC's Public Information Center.\nCategory 1 - Institution's charter survives\nA/A\t- Assistance Transactions. These include: 1) transactions where assistance was provided to the acquirer, who purchased the entire institution. For a few FSLIC transactions, the acquirer purchased the entire bridge bank - type entity, but certain other assets were moved into a liquidating receivership prior to the sale, and 2) open bank assistance transactions, including those where assistance was provided under a systemic risk determination (in such cases any costs that exceed the amounts estimated under the least cost resolution requirement would be recovered through a special assessment on all FDIC-insured institutions).\nREP -\tReprivatization, management takeover with or without assistance at takeover, followed by a sale with or without additional assistance.\nCategory 2 - Institution's charter is terminated, insured deposits plus some assets and other liabilities are transferred to a successor charter\nP&A - Purchase and Assumption, where some or all of the deposits, certain other liabilities and a portion of the assets (sometimes all of the assets) were sold to an acquirer. It was not determined if all of the deposits (PA) or only the insured deposits (PI) were assumed.\nPA - Purchase and Assumption, where the insured and uninsured deposits, certain other liabilities and a portion of the assets were sold to an acquirer.\nPI - Purchase and Assumption of the insured deposits only, where the traditional P&A was modified so that only the insured deposits were assumed by the acquiring institution.\nIDT - Insured Deposit Transfer, where the acquiring institution served as a paying agent for the insurer, established accounts on their books for depositors, and often acquired some assets as well. Includes ABT (asset-backed transfer, a FSLIC transaction that is very similar to an IDT).\nMGR - An institution where FSLIC took over management and generally provided financial assistance. FSLIC closed down before the institution was sold.\nCategory 3\nPO - Payout, where the insurer paid the depositors directly and placed the assets in a liquidating receivership. Note: Includes transactions where the FDIC established a Deposit Insurance National Bank to facilitate the payout process.",
        'options': ['A/A', 'REP', 'P&A', 'PA', 'PI', 'IDT', 'MGR', 'PO']
    },
    'CHCLASS1': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'title': 'Charter Class',
        'description': "The FDIC assigns classification codes indicating an institution's charter type (commercial bank, savings bank, or savings association), its chartering agent (state or federal government), its Federal Reserve membership status (member or nonmember), and its primary federal regulator (state-chartered institutions are subject to both federal and state supervision). These codes are:\nN - National chartered commercial bank supervised by the Office of the Comptroller of the Currency;\nSM - State charter Fed member commercial bank supervised by the Federal Reserve;\nNM - State charter Fed nonmember commercial bank supervised by the FDIC;\nSA - State or federal charter savings association supervised by the Office of Thrift Supervision or Office of the Comptroller of the Currency;\nSB - State charter savings bank supervised by the FDIC.",
        'options': ['N', 'SM', 'NM', 'SA', 'SB']
    },
    'RESTYPE': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'title': 'Resolution',
        'description': 'The given institution has failure stature or it can be assistance has been provided by FDIC in merging with other institution.',
        'options': ['Failure', 'Assistance']
    },
    'QBFDEP': {
        'type': 'number',
        'x-elastic-type': 'double',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Deposits',
        'description': 'Total including demand deposits, money market deposits, other savings deposits, time deposits and deposits in foreign offices as of the last Call Report or Thrift Financial Report filed by the institution prior to the effective date. Note this does not necessarily reflect total deposits on the last report filed because in some cases reports were filed after the effective date.'
    },
    'QBFASSET': {
        'type': 'number',
        'x-elastic-type': 'double',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Total Assets',
        'description': 'The Total assets owned by the institution including cash, loans, securities, bank premises and other assets as of the last Call Report or Thrift Financial Report filed by the institution prior to the effective date. Note this does not necessarily reflect total assets on the last report filed because in some cases reports were filed after the effective date. This total does not include off-balance-sheet accounts.'
    },
    'COST': {
        'type': 'number',
        'x-elastic-type': 'double',
        'x-number-unit': 'Thousands of US Dollars',
        'title': 'Estimated Loss',
        'description': 'The estimated loss is the difference between the amount disbursed from the Deposit Insurance Fund (DIF) to cover obligations to insured depositors and the amount estimated to be ultimately recovered from the liquidation of the receivership estate. Estimated losses reflect unpaid principal amounts deemed unrecoverable and do not reflect interest that may be due on the DIF\'s administrative or subrogated claims should its principal be repaid in full.\nNotes:\nComprehensive data on estimated losses are not available for FDIC-insured failures prior to 1986, or for FSLIC-insured failures from 1934-88. Estimated loss is presented as "N/A" in years for which comprehensive information is not available.\nEstimated Loss data was previously referred to as \'Estimated Cost\' in past releases of the Historical Statistic on Banking. For RTC receiverships, the \'Estimated Cost\' included an allocation of FDIC corporate revenue and expense items such as interest expense on Federal Financing Bank debt, interest expense on escrowed funds and interest revenue on advances to receiverships. Other FDIC receiverships did not include such an allocation. To maintain consistency with FDIC receiverships, the RTC allocation is no longer reflected in the estimated loss amounts for failed / assisted institutions that were resolved through RTC receiverships.\nBeginning with the release of 2007 information, the \'Estimated Loss\' in the Historical Statistics on Banking is presented and defined consistently with the aggregate Estimated Receivership Loss for FRF-RTC institutions and Estimated Losses for FDIC receiverships that are reported in the FDIC\'s Annual Report. The estimated loss is obtained from the FDIC\'s Failed Bank Cost Analysis (FBCA) report and the RTC Loss report. The FBCA provides data for receiverships back to 1986. The RTC Loss Report provides similar data back to 1989. \nQuestions regarding Estimated Loss should be sent to DOFBusinessCenter@fdic.gov. \nAlso, for more detail regarding resolution transactions and the FDIC\'s receivership activities, see Managing the Crisis: The FDIC and RTC Experience, a historical study prepared by the FDIC\'s Division of Resolutions and Receiverships. Copies are available from the FDIC\'s Public Information Center.'
    },
    'PSTALP': {
        'type': 'string',
        'x-elastic-type': 'keyword',
        'title': 'State',
        'description': 'Two-character alphanumeric code for US state or Territory'
    }
}
