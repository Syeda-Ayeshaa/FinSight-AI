import json
import os

def save_output(data, validation):

    output = {
        "extracted_data": data,
        "validation_result": validation
    }

    # Ensure outputs folder exists
    os.makedirs("outputs", exist_ok=True)

    with open("outputs/extracted_data.json", "w") as f:
        json.dump(output, f, indent=4)