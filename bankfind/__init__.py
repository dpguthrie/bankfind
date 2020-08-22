"""Python interface to the FDIC's API for publically available bank data"""

__version__ = '0.0.1'


from .main import (get_failures, get_history, get_institutions,  # noqa
                   get_locations, get_summary)
from .metadata import meta_dict  # noqa
