```python
import json
from prototype.mobile_interface import UserSchema, user_input
from prototype.touchscreen_input import processInput, displayOutput

class HumanComputerInteraction:
    def __init__(self):
        self.user_schema = UserSchema()
        self.user_input = user_input

    def validate_input(self, input_data):
        errors = self.user_schema.validate(input_data)
        if errors:
            displayOutput("inputError", json.dumps(errors))
            return False
        return True

    def handle_input(self):
        input_data = processInput(self.user_input)
        if self.validate_input(input_data):
            return input_data
        else:
            return None

    def handle_output(self, output_data):
        displayOutput("outputMessage", output_data)

    def interact(self):
        while True:
            input_data = self.handle_input()
            if input_data is None:
                continue
            output_data = self.process_data(input_data)
            self.handle_output(output_data)

    def process_data(self, input_data):
        # This function should be implemented in the child class
        pass
```