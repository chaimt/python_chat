import unittest
import datetime

from app.domain.data_structures import MessageApp
from app.domain.data_structures import Message


class TestMessageApp(unittest.TestCase):

    def test_not_eq(self):
        message1 = Message(1, "one", "chaim", datetime.datetime.utcnow())
        message2 = Message(2, "two", "chaim", datetime.datetime.utcnow())
        self.assertNotEqual(message1, message2)

    def test_eq(self):
        time = datetime.datetime.utcnow()
        message1 = Message(1, "one", "chaim", time)
        message2 = Message(2, "two", "chaim", time)
        self.assertEqual(message1, message2)

    def test_empty(self):
        messages = MessageApp()
        self.assertEqual(messages.total_sent(), 0)

    def test_add(self):
        messages = MessageApp()
        message = messages.add_message("test", "chaim")
        self.assertEqual(message.message_id, 1)
        self.assertEqual(message.message, "test")
        self.assertEqual(messages.total_sent(), 1)


if __name__ == '__main__':
    unittest.main()

