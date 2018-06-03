import datetime

import logging
logger = logging.getLogger(__name__)


class Message:

    def __init__(self, message_id, message, username, timestamp):
        self.message_id = message_id
        self.message = message
        self.username = username
        self.timestamp = timestamp

    def __eq__(self, other):
        return self.timestamp == other.timestamp

    def to_json(self):
        return str({"id": 123, "messages": self.message, "username": self.username, "timestamp": self.timestamp})


class MessageApp:

    def __init__(self):
        self.currentId = 0
        self.messages = {}

    def add_message(self, message, username):
        self.currentId += 1
        self.messages[str(self.currentId)] = Message(self.currentId, message,username, datetime.datetime.utcnow())
        return self.messages[str(self.currentId)]

    def peek_message(self, message_id):
        if message_id in self.messages:
            return self.messages[message_id]
        else:
            return Message(-1, "no such message")

    def pop_message(self, message_id):
        if message_id in self.messages:
            m = self.messages[message_id]
            del self.messages[message_id]
            return m
        else:
            return Message(-1, "no such message")

    def size(self):
        return self.messages.__sizeof__()

    def total_sent(self):
        return self.currentId
