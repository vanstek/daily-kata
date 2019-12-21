#Simple Events
#Level: 5 kyu
'''
Your goal is to write an Event constructor function, which can be used to make event objects.

An event object should work like this:

it has a .subscribe() method, which takes a function and stores it as its handler
it has an .unsubscribe() method, which takes a function and removes it from its handlers
it has an .emit() method, which takes an arbitrary number of arguments and calls all the stored functions with these arguments
'''
class Event():
    
    def __init__(self):
        self._handlers = []
    
    def subscribe(self, handler):
        self._handlers.append(handler)
    
    def unsubscribe(self, handler):
        if handler in self._handlers:
            self._handlers.remove(handler)
        
    def emit(self, *args):
        for h in self._handlers:
            h(*args)
