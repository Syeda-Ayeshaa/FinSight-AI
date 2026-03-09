import requests

API_KEY = "YOUR_HYPERAPI_KEY"
API_URL = "https://api.hyperbots.com/hyperapi/extract"

def extract_document(file_path):

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    files = {
        "file": open(file_path, "rb")
    }

    try:
        response = requests.post(API_URL, headers=headers, files=files)

        if response.status_code == 200:
            return response.json()

    except:
        pass

    # Mock data fallback (used when API is unavailable)
    return {
        "invoice_id": "INV-001",
        "vendor": "Demo Supplier",
        "items": [
            {"item": "Laptop", "qty": 2, "price": 600},
            {"item": "Mouse", "qty": 5, "price": 20},
            {"item": "Keyboard", "qty": 3, "price": 50}
        ],
        "tax": 100,
        "total": 1550
    }