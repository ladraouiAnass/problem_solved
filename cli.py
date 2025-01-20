import argparse
import json
import requests
import os

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Consume the Django CLI view.")
    parser.add_argument("falcon_path", help="Path to the falcon.json file.")
    parser.add_argument("empire_path", help="Path to the empire.json file.")
    parser.add_argument("--url", default="http://127.0.0.1:8080/cli_view/", help="URL of the Django CLI view.")

    args = parser.parse_args()

    # Validate file paths
    if not os.path.exists(args.falcon_path):
        print(f"Error: falcon.json file not found at {args.falcon_path}")
        return

    if not os.path.exists(args.empire_path):
        print(f"Error: empire.json file not found at {args.empire_path}")
        return

    try:
        # Load JSON files
        with open(args.falcon_path, 'r') as falcon_file:
            falcon_data = json.load(falcon_file)

        with open(args.empire_path, 'r') as empire_file:
            empire_data = json.load(empire_file)

        # Prepare request payload
        payload = {
            "falcon": falcon_data,
            "empire": empire_data
        }

        # Send POST request to the Django server
        response = requests.post(args.url, json=payload)

        # Display response
        if response.status_code == 200:
            print("Response from server:")
            print(json.dumps(response.json(), indent=4))
        else:
            print(f"Error: Received status code {response.status_code}")
            print(response.text)

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
