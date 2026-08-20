# With encapsulation implementation
class washing_machine():
    def __init__(self):
        self.__status = False

    def set_value(self,val):
        self.__status = val

    def get_value(self):
           print(self.__status)

    def start(self):
        if self.__status:
             print("Machine Start")

    def stop(self):
         if not self.__status:
              print("Machine Stopped")

wm = washing_machine()
wm.set_value(True)
wm.start()
wm.get_value()
wm.set_value(False)
wm.stop()
wm.get_value()
