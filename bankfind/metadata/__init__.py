from .failure import failure_dict
from .history import history_dict
from .institution import institution_dict
from .location import location_dict
from .summary import summary_dict
from .financials import financials_dict


meta_dict = {
    'failures': failure_dict,
    'history': history_dict,
    'institutions': institution_dict,
    'locations': location_dict,
    'summary': summary_dict,
    'financials': financials_dict
}
