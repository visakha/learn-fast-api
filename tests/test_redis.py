import redis


def test_valid_id():
    r = redis.StrictRedis('localhost', 6379, encoding="utf-8", decode_responses=True)
    r.mset({'Croatia': 'Zagreb', 'Bahamas': 'Nassau'})
    assert r.get('Bahamas') == 'Nassau'
