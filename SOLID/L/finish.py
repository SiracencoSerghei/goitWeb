
class Notification:
    def notify(self, message):
        raise NotImplementedError



class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f"Send {message} to email: {self.email}")


class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f"Send {message} sms to phone: {self.phone}")


class NotificationService:
    def __init__(self, notification: Notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)


if __name__ == '__main__':
    person = Contact('Sergio', 'sergio@example.com', '+380245373839')
    notify_sms = SMS(person.phone)
    notify_email = Email(person.email)

    service_SMS = NotificationService(notify_sms)
    service_Email = NotificationService(notify_email)
    service_SMS.send('hello bro')
    service_Email.send("Hello Bro!")
