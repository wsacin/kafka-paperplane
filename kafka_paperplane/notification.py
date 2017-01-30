
from .exceptions import ValidationError
import yajl


MSG_TYPE_CHOICES = {'ALERT', 'LOG', 'TASK', 'WARNING'}


class Notification(object):

    @staticmethod
    def create(msg, msg_type):
        payload = {}

        if msg_type not in MSG_TYPE_CHOICES:
            raise ValidationError(
                'Message types available: {}'
                .format(MSG_TYPE_CHOICES))

        if msg == '':
            raise ValidationError(
                'Notification with an empty message.')

        payload = {
            'message': msg,
            'message_type': msg_type,
        }
        dump = yajl.dumps(payload)
        return bytes(dump.encode('utf-8'))
