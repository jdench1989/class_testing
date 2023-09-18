from lib.gratitudes import *

def test_gratitudes_returns_empty():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "

def test_gratitudes_add_strings():
    gratitudes = Gratitudes()
    gratitudes.add('nice weather')
    gratitudes.add('friends')
    gratitudes.add('family')
    assert gratitudes.format() == "Be grateful for: nice weather, friends, family"

def test_gratitudes_empty_string():
    gratitudes = Gratitudes()
    gratitudes.add('nice weather')
    gratitudes.add('')
    assert gratitudes.format() == "Be grateful for: nice weather, "