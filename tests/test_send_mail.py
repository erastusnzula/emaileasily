import unittest

from emaileasy import email_to, email_subject, email_cc, email_bcc


class GetTestCase(unittest.TestCase):
    def test_get_recipient(self):
        recipients = 'example.gmail.com'
        result = email_to(recipients)
        self.assertEqual(result, 'example.gmail.com')

    def test_get_email_subject(self):
        subject = 'Email subject'
        results = email_subject(subject)
        self.assertEqual(results, "Email subject")

    def test_get_email_cc(self):
        results = email_cc('example.gmail.com')
        self.assertEqual(results, 'example.gmail.com')

    def test_get_email_bcc(self):
        results = email_bcc('example.gmail.com')
        self.assertEqual(results, 'example.gmail.com')


if __name__ == '__main__':
    unittest.main()
