class EventDispatcher:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_name, callback):
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(callback)
        return lambda: self.listeners[event_name].remove(callback)  # Return an unsubscribe function

    def publish(self, event_name, *args, **kwargs):
        for callback in self.listeners.get(event_name, []):
            callback(*args, **kwargs)
