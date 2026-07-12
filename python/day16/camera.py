class Camera:
    def capture(self):
        print("Capturing Image")

class Phone:
    def call(self):
        print("Calling...")

class SmartPhone(Camera,Phone):
    def details_info(self):
        print("this is smart phone")


smartphone = SmartPhone()

smartphone.details_info()
smartphone.call()
smartphone.capture()