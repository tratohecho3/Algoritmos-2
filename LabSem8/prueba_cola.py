from cola import Cola

c = Cola()

print(repr('c.enqueue(3)').center(14), repr(c.enqueue(3)).center(14), repr(c.head).center(14))
print(repr('c.enqueue(5)').center(14), repr(c.enqueue(5)).center(14), repr(c.head).center(14))
print(repr('c.size()').center(14), repr(c.size()).center(14), repr(c.head).center(14))
print(repr('c.enqueue(9)').center(14), repr(c.enqueue(9)).center(14), repr(c.head).center(14))
print(repr('c.dequeue()').center(14), repr(c.dequeue()).center(14), repr(c.head).center(14))
print(repr('c.first()').center(14), repr(c.first()).center(14), repr(c.head).center(14))
print(repr('c.is_empty()').center(14), repr(c.is_empty()).center(14), repr(c.head).center(14))
print(repr('c.dequeue()').center(14), repr(c.dequeue()).center(14), repr(c.head).center(14))
print(repr('c.dequeue()').center(14), repr(c.dequeue()).center(14), repr(c.head).center(14))
print(repr('c.size()').center(14), repr(c.size()).center(14), repr(c.head).center(14))
print(repr('c.is_empty()').center(14), repr(c.is_empty()).center(14), repr(c.head).center(14))
print(repr('c.dequeue()').center(14), repr(c.dequeue()).center(14), repr(c.head).center(14))