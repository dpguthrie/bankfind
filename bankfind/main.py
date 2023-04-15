from bankfind.base import BF


def get_failures(filters: str = None, **kwargs):
    """
    Detail on failed financial institutions

    Arguments
    ---------
    filters: str, default None, optional
        Filter for the bank search

    Keyword Arguments
    -----------------
    fields: str, default ALL FIELDS, optional
        Comma delimited list of fields to search
    sort_by: str, default OFFICES, optional
        Field name by which to sort returned data
    sort_order: str, default ASC, optional
        Indicator if ascending (ASC) or descending (DESC)
    limit: int, default 10,000, optional
        Number of records to return.  Maximum is 10,000
    offset: int, default 0, optional
        Offset of page to return
    format: str, default json, optional
        Format of the data to return
    friendly_fields: bool, default False, optional
        Return friendly field names
    """
    return BF()._get_data("failures", filters, **kwargs)


def get_history(filters: str = None, search: str = None, **kwargs):
    """
    Detail on structure change events

    Arguments
    ---------
    filters: str, default None, optional
        Filter for the bank search
    search: str
        Flexible text search against institution records.  Currently, only
        supports name search.  Text search and fuzzy matching is supported
        as well.

    Keyword Arguments
    -----------------
    fields: str, default ALL FIELDS, optional
        Comma delimited list of fields to search
    sort_by: str, default OFFICES, optional
        Field name by which to sort returned data
    sort_order: str, default ASC, optional
        Indicator if ascending (ASC) or descending (DESC)
    limit: int, default 10,000, optional
        Number of records to return.  Maximum is 10,000
    offset: int, default 0, optional
        Offset of page to return
    output: str, default json, optional
        Format of the data to return, json or pandas
    friendly_fields: bool, default False, optional
        Return friendly field names
    """
    return BF()._get_data("history", filters, search, **kwargs)


def get_institutions(filters: str = None, search: str = None, **kwargs):
    """
    List of financial institutions

    Arguments
    ---------
    filters: str, default None, optional
        Filter for the bank search
    search: str
        Flexible text search against institution records.  Currently, only
        supports name search.  Text search and fuzzy matching is supported
        as well.

    Keyword Arguments
    -----------------
    fields: str, default ALL FIELDS, optional
        Comma delimited list of fields to search
    sort_by: str, default OFFICES, optional
        Field name by which to sort returned data
    sort_order: str, default ASC, optional
        Indicator if ascending (ASC) or descending (DESC)
    limit: int, default 10,000, optional
        Number of records to return.  Maximum is 10,000
    offset: int, default 0, optional
        Offset of page to return
    format: str, default json, optional
        Format of the data to return
    friendly_fields: bool, default False, optional
        Return friendly field names
    """
    return BF()._get_data("institutions", filters, search, **kwargs)


def get_locations(filters: str = None, **kwargs):
    """
    List of locations / branches of financial institutions

    Arguments
    ---------
    filters: str, default None, optional
        Filter for the bank search

    Keyword Arguments
    -----------------
    fields: str, default ALL FIELDS, optional
        Comma delimited list of fields to search
    sort_by: str, default OFFICES, optional
        Field name by which to sort returned data
    sort_order: str, default ASC, optional
        Indicator if ascending (ASC) or descending (DESC)
    limit: int, default 10,000, optional
        Number of records to return.  Maximum is 10,000
    offset: int, default 0, optional
        Offset of page to return
    format: str, default json, optional
        Format of the data to return
    friendly_fields: bool, default False, optional
        Return friendly field names
    """
    return BF()._get_data("locations", filters, **kwargs)


def get_summary(filters: str = None, **kwargs):
    """
    Aggregate financial and structure data, subtotaled by year

    Arguments
    ---------
    filters: str, default None, optional
        Filter for the bank search

    Keyword Arguments
    -----------------
    fields: str, default ALL FIELDS, optional
        Comma delimited list of fields to search
    sort_by: str, default OFFICES, optional
        Field name by which to sort returned data
    sort_order: str, default ASC, optional
        Indicator if ascending (ASC) or descending (DESC)
    limit: int, default 10,000, optional
        Number of records to return.  Maximum is 10,000
    offset: int, default 0, optional
        Offset of page to return
    format: str, default json, optional
        Format of the data to return
    friendly_fields: bool, default False, optional
        Return friendly field names
    """
    return BF()._get_data("summary", filters, **kwargs)

def get_financials(filters: str = None, **kwargs):
    """
    Get Financial Information for FDIC Insured Institutions

    Arguments
    ---------
    filters: str, default None, optional
        Filter for the bank search

    Keyword Arguments
    -----------------
    fields: str, default ALL FIELDS, optional
        Comma delimited list of fields to search
    sort_by: str, default OFFICES, optional
        Field name by which to sort returned data
    sort_order: str, default ASC, optional
        Indicator if ascending (ASC) or descending (DESC)
    limit: int, default 10,000, optional
        Number of records to return.  Maximum is 10,000
    offset: int, default 0, optional
        Offset of page to return
    agg_by: str, default blank
        The field(s) by which data will be aggregated.
    agg_term_fields: str, default blank
        The field(s) for which aggregations will be counted for each unique term.
    agg_sum_fields: str, default blank
        The field(s) for which aggregations will be summed or aggregated.
    agg_limit: int,
        The limit on how many aggregated results will be displayed
    format: str, default json, optional
        Format of the data to return
    download: bool, default False
        Whether the data should be downloaded as a file.
    filename: str,
        The filename to use when downloading data
    friendly_fields: bool, default False, optional
        Return friendly field names
    """
    return BF()._get_data("financials", filters, **kwargs)

