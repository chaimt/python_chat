from flask import Blueprint
from app.domain import messageApp
from flask import request

message_requests = Blueprint('message_requests', __name__)


@message_requests.route('/chat', methods=['POST'])
def chat_send():
    return messageApp.add_message(request.data).to_json()


@message_requests.route('/chat/<message_id>', methods=['GET'])
def chat_get(message_id):
    return messageApp.peek_message(message_id).to_json()


@message_requests.route('/chat/<message_id>', methods=['DELETE'])
def chat_delete(message_id):
    return messageApp.pop_message(message_id).to_json()