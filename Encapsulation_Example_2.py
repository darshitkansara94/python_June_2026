# With encapsulation implementation
class washing_machine():
    def __init__(self):
        self.__status = False

    def start(self):
        if not self.__status: # status  = True
            print("Machine started")
            # self.__status = True

    def stop(self):
        # self.__status = True
        if not self.__status:
            print("Machine is not started")
            # self.__status = False

    

wm = washing_machine() # Status = False
wm.start()
wm.stop()
wm.__status = True
print("This is end of program")