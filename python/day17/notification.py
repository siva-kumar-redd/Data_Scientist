class Notification:
    pass
class EmailNotification(Notification):
    def send(self):
        print("this is email notification")

class SMSNotification(Notification):
    def send(self):
        print("this is sms notification")

class WhatsAppNotification(Notification):
    def send(self):
        print("this is whatsapp notification")

notify = [EmailNotification(),SMSNotification(),WhatsAppNotification()]

for note in notify:
    note.send()