from django.test import TestCase
from django.core import mail
from django.core.management import call_command
from django.test import SimpleTestCase, override_settings

ADMINS = (('Admin', 'HikeBuddy100@gmail.com'), ('Admin and Manager', 'HikeBuddy100@gmail.com')),
MANAGERS = (('Manager', 'HikeBuddy100@gmail.com'), ('Admin and Manager', 'HikeBuddy100@gmail.com')),


# Create your tests here.
class SendTestEmailManagementCommand(SimpleTestCase):
    """
    Test the sending of a test email using the `sendtestemail` command.
    """

    def test_single_receiver(self):
        """
        The mail is sent with the correct subject and recipient.
        """
        recipient = 'HikeBuddy100@gmail.com'
        call_command('sendtestemail', recipient)
        self.assertEqual(len(mail.outbox), 1)
        mail_message = mail.outbox[0]
        self.assertEqual(mail_message.subject[0:15], 'Test email from')
        self.assertEqual(mail_message.recipients(), [recipient])

    def test_multiple_receivers(self):
        """
        The mail may be sent with multiple recipients.
        """
        recipients = ['HikeBuddy100@gmail.com', 'HikeBuddy100@gmail.com']
        call_command('sendtestemail', recipients[0], recipients[1])
        self.assertEqual(len(mail.outbox), 1)
        mail_message = mail.outbox[0]
        self.assertEqual(mail_message.subject[0:15], 'Test email from')
        self.assertEqual(sorted(mail_message.recipients()), [
            'HikeBuddy100@gmail.com',
            'HikeBuddy100@gmail.com',
        ])




