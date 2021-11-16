import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from file_to_test import input_function, create_file, print_hello, several_input_function

def test_input_function(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x : "Mark")
    assert input_function() == 'Mark'

def test_create_file(tmpdir):
    p = tmpdir.mkdir("test").join("save.txt")
    create_file(p,"content")
    assert p.read_text(encoding=None) == "content"
    
def test_print_hello(capsys):
    print_hello()
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
  
### tester une fonction avec plusieurs input.

def test_several_input_function(monkeypatch,capsys):
    
    def geninputs():
        inputs = ['Rien', 'Rien', 'Rien Monsieur']
        for i in inputs:
            yield i

    GEN = geninputs()

    monkeypatch.setattr('builtins.input', lambda x : next(GEN))
    assert several_input_function() == 3