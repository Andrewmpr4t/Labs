import keyboard
from abc import ABC, abstractmethod

class KeyboardListener(ABC):
    @abstractmethod
    def on_key_press(self, key_name):
        pass

class KeyLogger(KeyboardListener):
    def on_key_press(self, key_name):
        print(f"Натиснуто: {key_name}")

class KeyFileLogger(KeyboardListener):
    def __init__(self, file_path="keyboard_log.txt"):
        self.file_path = file_path

    def on_key_press(self, key_name):
        with open(self.file_path, "a", encoding="utf-8") as f:
            f.write(f"{key_name}\n")

class KeyboardSpy:
    def __init__(self):
        self._listeners = []

    def attach(self, listener: KeyboardListener):
        self._listeners.append(listener)

    def notify_listeners(self, key_name):
        for listener in self._listeners:
            listener.on_key_press(key_name)

    def start(self):
        keyboard.on_press(lambda event: self.notify_listeners(event.name))
        keyboard.wait("ctrl+q")

if __name__ == "__main__":
    spy = KeyboardSpy()
    
    spy.attach(KeyLogger())
    spy.attach(KeyFileLogger())
    
    spy.start()