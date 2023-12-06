
class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Email:
    def notify(self, message, email):
        print(f"Send {message} to email: {email}")


class SMS:
    def notify(self, message, phone):
        print(f"Send {message} sms to phone: {phone}")


class NotificationService:
    def __init__(self, contact: Contact, notification: Email | SMS):
        self.contact = contact
        self.notification = notification

    def send(self, message):
        if isinstance(self.notification, Email):
            self.notification.notify(message, self.contact.email)
        elif isinstance(self.notification, SMS):
            self.notification.notify(message, self.contact.phone)
        else:
            raise Exception("The method 'notification' is not supported.")

if __name__ == '__main__':
    person = Contact('Sergio', 'sergio@example.com', '+380245373839')
    service_SMS = NotificationService(person, SMS())
    service_Email = NotificationService(person, Email())
    service_SMS.send('hello bro')
    service_Email.send("Hello Bro!")
