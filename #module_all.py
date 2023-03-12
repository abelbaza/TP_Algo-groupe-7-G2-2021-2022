#module de tout
import ctypes
class Module:
    """le module contenant toutes les classes ainsi que leurs méthodes"""
    def __init__(self):
        self._data = []
        self._n = 0 # count actual elements
        self._capacity = 1 # default array capacity
        self._A = self._make_array(self._capacity)
        self._head = None
        self._size = 0
        self._tail = None
    
    def __len__(self):
        """Return the number of
        elements in the queue/list"""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

#reverse_file

def reverse_file(filename):
    """Overwrite given file with its contents
    line-by-line reversed"""
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip("\n"))
        original.close()
# now we overwrite with contents in LIFO order
    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()

#is_matched

def is_matched(expr):
    """Return true if all delimiters are
    properly match; False otherwise."""
    lefty ='({[' #opening delimiters
    reighty = ')}]' # respective closing delimiters
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in reighty:
            if S.is_empty():
                return False
            if reighty.index(c) != lefty.index(S.pop()):
               return False
    return S.is_empty()

#is_matched_html

def is_matched_html(raw):
    """Return True if all HTML tags are
    properly match; False otherwise."""
    S = ArrayStack
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
    tag = raw[j+1:k]
    if not tag.startswith("/"):
        S.push(tag)
    else:
        if S.is_empty():
            return False
        if tag[1:] != S.pop():
            return False
        j=raw.find('<', k+1)
    return S.is_empty()

#insert

def insert(self, k, value):
    """Insert value at index k, shifting
    subsequent values rightward."""
# (for simplicity, we assume 0<=k<=n in this version
    if self._n == self._capacity: # not enough room
        self._resize(2*self._capacity) # so doluble capacity
        for j in range(self._A[j-1]):# shift rightmost
            self._A[j] = self._A[j-1] # store newest element
            self._n += 1

#insertion_sort

def insertion_sort(A):
    """ Sort list of comparables elements
    into an increasing order """
    for k in range(1, len(A)): # from 1 to n-1
        cur = A[k] # current element to be inserted
        j=k # find correct index j for current
        while j>0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
            A[j] = cur

#Remove

def remove(self, value):
    """Remove first occurence of value
    (or raise ValueError)."""
# note we do not consider shrinking
# the dynamic array in this version
    for k in range(self._n):
        if self._A[k] == value:
# found a match!
            for j in range(k, self._n - 1):
# shift elements to fill gap
                self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None
# help garbage collection
                self._n -= 1
# we have one less item
        return
# exit immediately
        raise ValueError('value not found')

#tableau dynamique


class DynamicArray(Module):
    """ A dynamic array class as a simplified Python list """
    
# low-level array
    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n
    def __getitem__(self, k):
        """Return the item at position k"""
        if not 0 <= k < self._n:
            raise IndexError("invalid index")
            return self._A[k] # retreive from array
    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:
    # not enough room
            self._resize(2*self._capacity)
    # so double capacity
            self._A[self._n] = obj
            self._n += 1
    def _resize(self, c):
        """Resize internal array to capacity c"""
        B= self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
            self._A = B
            self._capacity = c
    def _make_array(self,c):
        """Return new array with capacity c."""
        return (c*ctypes.py_object)()

#LinkedSatck

class LinkedStack(Module):
    """LIFO Stack implementation using
    a singly linked list for storage"""
# ------------ nested _Node class -----------
    class _Node:
        """ Lightweight, nonpublic class
        for storing a singly linked node."""
        __slots__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next
# stack methods
    def __len__(self):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head)
        self._size += 1
    def top(self):
        """ Return (but not remove) the element
        at the top of the stack
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise empty('Stack is empty')
        return self._head._element
    def pop(self):
        """Remove and return the element
        at the top of the stack (LIFO)"""
        """Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1

#ArrayStack

class ArrayStack(Module):
    """ LIFO stack implementation using
    a Python list as underlying storage"""
    
    def __len__(self):
        """Return the number of
        elements in the stack"""
        return len(self._data)
    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0
    def push(self, e):
        """Add element e to top of the stack"""
        self._data.append(e)
    def top(self):
        """Return (but not remove) the
        element at the top of the stack"""
        """Raise Empty Exception if the stack is empty"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    def pop(self):
        """Remove and return the element
        from the top of the stack (i.e. LIFO).
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

#LinkedQueue

class LinkedQueue(Module):
    """FIFO queue implementation using
    a singly linked list for storage """
    class _Node:
        """ Lightweight, nonpublic class
        for storing a singly linked node."""
        __slots__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def first(self):
        """Return (but not remove)
        the element at the front of the queue"""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

#CircularQueue

class CircularQueue(Module):
    """Queue implementation using
    circularly linked list for storage"""

    class _Node:
        """Lightweight, nonpublic class
        for storing a singly linked node
        (omitted here; identical to that
        of LinkedStack._Node)"""

    def first(self):
        """Return (but not remove)
        the element at the front of
        the queue. Raise Empty
        exception if the queue is empty."""
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        """Remove and return the first
        element of the queue (FIFO).
        Raise Empty exception if the
        queue is empty."""
        if self._isempty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
            self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        """Add an element to the back
        of the queue."""
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = self._tail._next
            self._tail_next = newest
            self._tail = newest
            self._size += 1
    
    def rotate(self):
        """Rotate front element to
        the back of the queue."""
        if self._size >0:
            self._tail = self._tail._next

#DoublyLinkedBase

class _DoublyLinkedBase(Module):
    """ A base class providing a doubly
    linked list representation"""

    class _Node:
        """Ligthweight, nonpublic class
        for storing q doubly linked node"""
        __slot__= 'element', '\_prev' , '\_next'
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing
        nodes and return new node."""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size +=1
        return newest

    def _delete_node(self, node):
        """Delete nosentinel node from
        the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predeccessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None

#LinkedDequeue


class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation
    based on a doubly linked list """

    def first(self):
        """Return (but not remove) the element
        at the front of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element

    def last(self):
        """Return (but not remove) the
        element at the back of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header_next)

    def delete_first(self):
        """Remove and return the element from the
        front of the deque.
        Raise Empty exception if deque is empty."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete._node(self._header._next)

    def delete_last(self):
        """Remove and return the element from the
        back of the deque.
        Raise Empty exception if deque is empty."""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)
