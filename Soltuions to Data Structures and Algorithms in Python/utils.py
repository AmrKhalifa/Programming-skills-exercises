





class _DoublyLinkedBase:
    class _Node:
        __slots__='_element', '_prev', '_next'
        
        def __init__(self, element, prev, nxt):
            self._element = element 
            self._prev = prev
            self._next = nxt 
            
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer 
        self._trailer._prev = self._header
        self._size = 0 
        
    def __len__(self): 
        return self._size 
    
    def is_empty(self):
        return self._size == 0 
    
    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest 
        self._size += 1
        return newest 
    
    def _delete_node(self, node):
        predecessor = node._prev 
        successor = node._next 
        predecessor._next = successor 
        successor._prev = predecessor 
        self._size -= 1
        element = node._element 
        node._prev = node._next = node._element = None
        return element 

class PositionalList(_DoublyLinkedBase):
    def __init__(self):
        super().__init__() 
        
    class Position: 
        def __init__(self, container, node):
            self._container = container 
            self._node = node 
            
        def element(self):
            return self._node._element 
        def __eq__(self, other): 
            return type(other) is type(self) and other._node is self._node
        def __ne__(self, other):
            return not(self==other)
    
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper position type')
        if p._container is not self:
            raise ValueError('p does not belong to this type')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node 
    
    def _make_position(self, node):
        if (node is self._header) or (node is self._trailer):
            return None
        else:
            return self.Position(self, node)
        
    def first(self):
        return self._make_position(self._header._next)
    
    def last(self):
        return self._make_position(self._trailer._prev)
    
    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        cursor = self.first() 
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
            
    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)
    
    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)
    
    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)
    
    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)
    
    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)
    
    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)
    
    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element 
        original._element = e
        return old_value