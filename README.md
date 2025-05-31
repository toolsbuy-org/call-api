<p align="center">
  <img src="https://img.icons8.com/ios-filled/100/000000/phone.png" alt="Phone Icon" width="70"/>
  <img src="https://img.icons8.com/color/96/000000/python--v1.png" alt="Python Icon" width="70"/>
</p>

<h1 align="center">Call SPI - Custom Caller ID</h1>

<p align="center">
  <b>Call SPI</b> is a Python application for making automated calls via a telephony Service Provider Interface (SPI), supporting custom caller ID features.
</p>

<p align="center">
  <a href="https://t.me/toolsbuy">
    <img src="https://camo.githubusercontent.com/b6aa193bb6a181fb4d1675178de6e74e31f22cf3d36b5c896f26055373f777ca/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436861742d54656c656772616d2d626c75653f7374796c653d666f722d7468652d6261646765266c6f676f3d74656c656772616d" alt="Telegram" style="max-width: 100%;" />
  </a>
</p>

---

## Features

- 📞 Make automated outbound calls.
- 🆔 Set a custom caller ID for each call.
- 🐍 Easy-to-use Python API.
- ⚙️ Configurable and extensible.

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

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

<p align="center">
  Made with <span style="color: #e25555;">&#10084;</span> for automated communications.
</p>
