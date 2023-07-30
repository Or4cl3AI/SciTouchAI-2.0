import flask
from flask import request, jsonify
from prototype import human_computer_interaction, touchscreen_input, natural_language_processing
from marshmallow import Schema, fields

class UserSchema(Schema):
    user_input = fields.Str(required=True)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Scientific Data Analysis App</h1>
<p>A prototype API for analyzing scientific data.</p>'''

@app.route('/api/v1/resources/analyze', methods=['POST'])
def api_analyze():
    schema = UserSchema()
    try:
        user_data = schema.load(request.form)
        user_input = user_data['user_input']
    except Exception as e:
        return jsonify({'message': 'inputError', 'error': str(e)}), 400

    try:
        processed_input = touchscreen_input.processInput(user_input)
        interaction_result = human_computer_interaction.processInput(processed_input)
        final_result = natural_language_processing.processInput(interaction_result)
    except Exception as e:
        return jsonify({'message': 'inputError', 'error': str(e)}), 400

    return jsonify({'message': 'outputMessage', 'result': final_result})

app.run()