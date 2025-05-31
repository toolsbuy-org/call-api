<p align="center">
  <img src="assets/logo.png" alt="Call SPI Logo" width="120"/>
</p>

<h1 align="center">Call SPI - Custom Caller ID</h1>

<p align="center">
  <img src="assets/phone_icon.png" alt="Phone Icon" width="60"/>
  <img src="assets/callerid_icon.png" alt="Caller ID Icon" width="60"/>
</p>

<p align="center">
  <b>Call SPI</b> is a simple Python application for making automated calls via a telephony Service Provider Interface (SPI), supporting custom caller ID features.
</p>

---

## Features

- Make automated outbound calls.
- Set a custom caller ID for each call.
- Easy-to-use Python API.
- Configurable and extensible.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/call-spi.git
   cd call-spi
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Edit `main.py` with your SPI provider credentials and desired call parameters.

```python
from main import make_call

make_call(
    to_number="+1234567890",
    from_number="+10987654321",  # Custom caller ID
    message="Hello, this is a test call from Call SPI."
)
```

## Configuration

- Update your SPI provider API credentials in `main.py`.
- Set the default caller ID and message as needed.

## Assets

- **Logo:** ![Logo](assets/logo.png)
- **Phone Icon:** ![Phone Icon](assets/phone_icon.png)
- **Caller ID Icon:** ![Caller ID Icon](assets/callerid_icon.png)

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

<p align="center">
  Made with ❤️ for automated communications.
</p>
