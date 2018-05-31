class LinkedList():

    def __init__(self, val=None, nxt=None, lst=None, *args, **kwargs):

        if isinstance(val, list) and len(val) > 0:
            self.to_llist(val)

        elif isinstance(lst, list) and len(lst) > 0:
            self.to_llist(lst)

        else:
            self.val = val
            self.nxt = nxt

    def push_last(self, val):
        ll = self
        # TODO: optimize, store link to last element
        while ll.nxt != None:
            ll = ll.nxt

        ll.nxt = LinkedList(val)
        return True

    def pop_last(self):
        ll, prev = self, None

        if ll.nxt == None:
            res = ll.val
            self.val = None
            self.nxt = None
            return res

        # TODO: optimize, store link to last element
        while ll.nxt != None:
            prev = ll
            ll = ll.nxt
        # save previous to the end element and return it
        res = ll.val
        prev.nxt = None
        # update linked list in self
        self = ll
        return res

    def to_llist(self, l):
        """Инициализация linked_list с помощью list"""
        res = self
        itr = res
        for i, el in enumerate(l):
            itr.val = el
            itr.nxt = LinkedList()

            if i == len(l) - 1:
                itr.nxt = None
            else:
                itr = itr.nxt

        return res

    def __iter__(self):
        """ преобразование linked_list обратно в list через итератор """
        while 1:
            if self:
                res = self.val
                self = self.nxt
                yield res

            else:
                # raise StopIteration
                return

    def reverse(self):
        """Сформировать linked_list в обратном порядке, вернуть полученный reversed llist"""
        ll = self
        el = None
        N = 0

        while ll.nxt != None:
            cur = LinkedList(ll.val, None)    
            cur.nxt = el

            el = cur
            ll = ll.nxt
            N += 1

        el = LinkedList(ll.val, el)

        return el

    def __str__(self):
        """Вывод linked list в читаемом виде (преобразование в массив)"""
        return "{}".format(list(self))
