# Numericalphabet v1.0.4
# Made by FAZuH

import Message
import Trainer

print("Available test types: '{}', '{}'' and '{}'".format(*Message.test_types))
while True:
    try:
        Message.user_input()
        Trainer.trainer()
        Message.result()

    except Exception as e:
        Message.print_red(f'Error: {str(e)}')
