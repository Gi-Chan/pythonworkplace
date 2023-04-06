

class Counter:
    
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
    
    def substract(self):
        self.count -=1

a = Counter()
a.increment()
print("Counter value = ", a.count)

a.substract()
print("Counter value = ", a.count)
