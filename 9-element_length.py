'''
9.
Let's duck type an iterable object

Annotate
the
below
function’s
parameters and
return values
with the appropriate types


def element_length(lst):
    return [(i, len(i)) for i in lst]


bob @ dylan: ~$ cat
9 - main.py
# !/usr/bin/env python3

element_length = __import__('9-element_length').element_length

print(element_length.__annotations__)

bob @ dylan: ~$./ 9 - main.py
{'lst': typing.Iterable[typing.Sequence], 'return': typing.List[typing.Tuple[typing.Sequence, int]]}

File: 9 - element_length.py
'''

from typing import Iterable, Sequence, Tuple, List

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]

print(element_length.__annotations__)