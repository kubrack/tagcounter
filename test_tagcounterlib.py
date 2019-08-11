
import tagcounterlib as tlib

testset = {
        'http://a.tim.ua': {'html': 1, 'head': 1, 'meta': 4, 'title': 1, 'style': 1, 'body': 1, 'table': 1, 'tbody': 1, 'tr': 3, 'td': 3, 'h3': 1, 'b': 7, 'a': 1, 'p': 18, 'br': 4, 'ul': 8, 'li': 27}
}

def test_process():
    for t in testset:
        assert testset[t] == tlib.process_uri(t)
