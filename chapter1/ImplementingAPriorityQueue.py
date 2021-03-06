# Implement queue that sorts items by a given priority and always returns the
# item with the highest priority on each pop operation

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
        
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        # prioridade é negada porque o heapq lista de forma crescente
        self._index += 1
        
    def pop(self):
        return heapq.heappop(self._queue)[-1]
    
class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)
    
q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

q.pop() # vai retornar os items pela ordem de prioridade. Os que tiverem a mesma
        # prioridade serão retornados na sequência que foram postos na lista