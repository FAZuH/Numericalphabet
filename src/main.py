# Numericalphabet 1.0.3
# Made by FAZuH

import Message
import Trainer

while True:
    try:
        Message.user_input()
        Trainer.trainer()
        Message.result()

    except Exception as e:
        Message.print_red(f'Error: {str(e)}')