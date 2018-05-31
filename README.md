# linked_list_reverse
Python implementation of classic linked list structure with method to get reversed linked list within O(N) complexity.

Functionality:
1. Initialize linked list via val/nxt attributes or via passing a list to constructor
```
l = LinkedList(1, None)
l = LinkedList([1, 2, 3, {"N"}])
```

2. Push/pop last element of linked list:
```
>>> ll = LinkedList([1, 2, 3, {"N"}])
>>> print(ll.pop_last())
{"N"}
>>> print(ll)
[1, 2, 3]

>>> ll = LinkedList([1, 2])
>>> print(ll.push_last(3))
True
>>> print(ll)
[1, 2, 3]
```

3. Get reversed linked list:
```
>>> from linked_list_reverse import LinkedList
>>> l = LinkedList([1, 2, 3])
>>> list(l.reverse())
[3, 2, 1]
>>> list(l.reverse().reverse())
[1, 2, 3]
```

# Run tests:
```
/linked_list_reverse$ python ./tests.py -v
test_init_all_variants (__main__.LinkedListTest) ... ok
test_init_empty_llist (__main__.LinkedListTest) ... ok
test_push_pop (__main__.LinkedListTest) ... ok
test_reverse (__main__.LinkedListTest) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.034s

OK
```
