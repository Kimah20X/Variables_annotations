'''
10. Duck typing - first element of a sequence

Augment the following code with the correct duck-typed annotations:

# The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
bob@dylan:~$ cat 100-main.py
#!/usr/bin/env python3

safe_first_element =  __import__('100-safe_first_element').safe_first_element

print(safe_first_element.__annotations__)

bob@dylan:~$ ./100-main.py
{'lst': typing.Sequence[typing.Any], 'return': typing.Union[typing.Any, NoneType]}

File: 100-safe_first_element.py
'''

from typing import Sequence, Any, Union
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None

print(safe_first_element.__annotations__)
