"""
Call SPI - Custom Caller ID
A simple script to make outbound calls with custom caller ID using a telephony SPI.

Update the SPI_API_URL, SPI_API_KEY, and authentication as required for your provider.
"""

import requests
import os

# Example configuration (Replace with your provider's details)
SPI_API_URL = os.getenv("SPI_API_URL", "https://example-spi.com/api/call")
SPI_API_KEY = os.getenv("SPI_API_KEY", "your_api_key_here")

def make_call(to_number: str, from_number: str, message: str):
    """
    Make an outbound call via SPI with a custom caller ID.

    Args:
        to_number (str): The destination phone number (E.164 format).
        from_number (str): The custom caller ID (E.164 format).
        message (str): The message to play or send.

    Returns:
        dict: Response from the SPI provider.
    """
    payload = {
        "to": to_number,
        "from": from_number,
        "message": message
    }
    headers = {
        "Authorization": f"Bearer {SPI_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(SPI_API_URL, json=payload, headers=headers)
    if response.ok:
        print(f"Call to {to_number} initiated successfully with Caller ID {from_number}.")
    else:
        print(f"Failed to initiate call: {response.text}")
    return response.json()


if __name__ == "__main__":
    # Example usage (replace with real values)
    make_call(
        to_number="+1234567890",
        from_number="+10987654321",
        message="Hello, this is a test call from Call SPI."
    )
