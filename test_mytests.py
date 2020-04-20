import pytest
from dog import Dog

#NOTE: For pytest to pick up this file must name it test_* and method names must begine with test_
#to run test use pytest
def tesxt_answer():
    d = Dog()
    assert(d.me == "dog")