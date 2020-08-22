from io import StringIO
import urllib.parse

import pandas as pd
import requests
from requests.models import Response

from bankfind.metadata import meta_dict


class BF:

    DEFAULTS = {
        'institutions': {
            'sort_by': 'OFFICES',
            'sort_order': 'ASC',
            'limit': 10000,
            'offset': 0,
            'format': 'json',
            'search': True
        },
        'locations': {
            'sort_by': 'NAME',
            'sort_order': 'ASC',
            'limit': 10000,
            'offset': 0,
            'format': 'json',
            'search': False
        },
        'history': {
            'sort_by': 'PROCDATE',
            'sort_order': 'DESC',
            'limit': 10000,
            'offset': 0,
            'format': 'json',
            'search': True
        },
        'summary': {
            'sort_by': 'YEAR',
            'sort_order': 'DESC',
            'limit': 10000,
            'offset': 0,
            'format': 'json',
            'search': False
        },
        'failures': {
            'sort_by': 'FAILDATE',
            'sort_order': 'DESC',
            'limit': 10000,
            'offset': 0,
            'format': 'json',
            'search': False
        }
    }

    def __init__(self):
        pass

    def _construct_params(
            self,
            key: str,
            filters: str = None,
            search: str = None,
            **kwargs):
        d = self.DEFAULTS[key]
        params = {
            'sort_by': kwargs.get('sort_by', d['sort_by']),
            'sort_order': kwargs.get(
                'sort_order', d['sort_order']),
            'limit': kwargs.get('limit', d['limit']),
            'offset': kwargs.get('offset', d['offset']),
            'format': 'csv' if kwargs.get('output') == 'pandas' else 'json',
            'download': 'false',
            'fields': kwargs.get(
                'fields', ','.join(list(meta_dict[key].keys())))
        }
        if filters:
            params.update({'filters': filters})
        if search and d['search']:
            params.update({'search': search})
        return params

    def _friendly_fields(self, key, data, dataframe=True):
        meta = meta_dict[key]
        if isinstance(data, list):
            data = pd.DataFrame([i['data'] for i in data])
        data.columns = data.columns.map(
            dict((k, meta[k]['title'])
                 for k in meta.keys() if k in data.columns))
        if dataframe:
            return data
        return data.to_dict(orient='records')

    def _to_json(
            self,
            key: str,
            response: Response,
            friendly_fields: bool = False):
        json_data = response.json()
        if friendly_fields:
            json_data['data'] = self._friendly_fields(
                key, json_data['data'], dataframe=False)
        else:
            json_data['data'] = [i['data'] for i in json_data['data']]
        return json_data

    def _to_pandas(
            self,
            key: str,
            response: Response,
            friendly_fields: bool = False):
        df = pd.read_csv(StringIO(response.text))
        if friendly_fields:
            df = self._friendly_fields(key, df)
        return df

    def _get_data(
            self,
            key: str,
            filters: str = None,
            search: str = None,
            **kwargs):
        params = self._construct_params(key, filters, search, **kwargs)
        r = requests.get(
            f"https://banks.data.fdic.gov/api/{key}",
            params=urllib.parse.urlencode(params)
        )
        if r.ok:
            return getattr(self, f"_to_{kwargs.get('output', 'json')}")(
                key, r, kwargs.get('friendly_fields', False))
        return r
