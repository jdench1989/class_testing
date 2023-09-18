from lib.string_builder import *

def test_string_builder_add_string():
    builder = StringBuilder()
    builder.add('This is a string')
    assert builder.str == 'This is a string'

def test_string_builder_size():
    builder = StringBuilder()
    builder.add('This is a string')
    assert builder.size() == 16

def test_string_builder_output():
    builder = StringBuilder()
    builder.add('string1')
    builder.add('string2')
    builder.add('string3')
    assert builder.output() == 'string1string2string3'