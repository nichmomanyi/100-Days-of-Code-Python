from twilio.rest import Client

TWILIO_SID = "AC39b6ca493feb968b2f527c00fd018bca"
TWILIO_AUTH_TOKEN = "3174e8c395e4aeeae0867b3813593c96"
TWILIO_VIRTUAL_NUMBER = "+15134079698"
TWILIO_VERIFIED_NUMBER = "+254715210571"


class NotificationManager:
    class NotificationManager:

        def __init__(self):
            self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

        def send_sms(self, message):
            message = self.client.messages.create(
                body=message,
                from_=TWILIO_VIRTUAL_NUMBER,
                to=TWILIO_VERIFIED_NUMBER,
            )
            # Prints if successfully sent.
            print(message.sid)
