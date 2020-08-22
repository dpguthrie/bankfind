import bankfind as bf


def test_institutions():
    data = bf.get_institutions(
        filters="STALP:CO AND ACTIVE:1",
        search="NAME: AMG",
    )
    assert len(data['data']) == 1


def test_locations():
    data = bf.get_locations(
        filters="CERT:57295"
    )
    assert len(data['data']) >= 7


def test_history():
    data = bf.get_history(
        filters="CERT:57295",
        output='pandas',
        friendly_fields=True
    )
    assert len(data) >= 18


def test_summary():
    df = bf.get_summary(
        filters='CB_SI:CB AND ASSET:[10000000000 TO *] AND YEAR:["2018" TO "2019"]',
        output='pandas')
    assert len(df) >= 4


def test_failures():
    data = bf.get_failures(
        filters='PSTALP:CO AND FAILYR:["2008" TO "2011"]',
        sort_by='COST',
        sort_order='DESC',
        friendly_fields=True)
    assert len(data['data']) == 9


def test_bad_request():
    response = bf.get_institutions(sort_by="BAD_SORT_BY_FIELD")
    assert response.status_code == 400
