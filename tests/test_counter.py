from lib.counter import *

def test_counter_increments():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."
    counter.add(20)
    assert counter.report() == "Counted to 25 so far."
    counter.add(10)
    assert counter.report() == "Counted to 35 so far."

def test_counter_zero():
    counter = Counter()
    counter.add(0)
    assert counter.report() == "Counted to 0 so far."

def test_counter_negative_values():
    counter = Counter()
    counter.add(100)
    assert counter.report() == "Counted to 100 so far."
    counter.add(-10)
    assert counter.report() == "Counted to 90 so far."
    counter.add(-50)
    assert counter.report() == "Counted to 40 so far."