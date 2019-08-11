
from tagcounterdb import DB

DB.init()

key1 = 'http://some.key'
key2 = 'http://another.key'
value1 = {'check': 111, 'dict': 9999999999999, 'storing': 0}
value2 = {'it': 'should', 'replace': 'the previous one'}

def test_stored():
    DB.set(key1, value1)
    DB.set(key2, value1)
    assert DB.get(key1) == value1
    assert DB.get(key2) == value1

def test_replase():
    DB.set(key1, value1)
    DB.set(key2, value2)
    assert DB.get(key2) == value2
