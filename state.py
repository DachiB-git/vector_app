class State:
    observers = []
    state = None

    def __init__(self, state):
        self.state = state

    def notify(self):
        for observer in self.observers:
            observer.update()

    def add_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
