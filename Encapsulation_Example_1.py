# Example without encapsulation
class washing_machine():
    def __init__(self,process):
        self.process = process

    def start(self):
        print(self.process)

    def stop(self):
        print(self.process)

wm = washing_machine("Machine started")
wm.start()
wm.process = "Machine stop"
print(wm.process)
        