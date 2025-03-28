# 📶 QR Generator with Python and Tkinter

Easily share your Wi-Fi connection using a **QR code** 📱. This project uses Python and the `qrcode` library to generate a QR code containing the necessary credentials to allow a mobile device to automatically connect to a Wi-Fi network.

The QR code generated includes **error correction level Q**, which allows approximately **25%** of the code to be restored if damaged or obscured.

---

## 🚀 Getting Started

To run this project, make sure you have the `qrcode` library installed:

```bash
pip install qrcode
```

## 🧠 What is a QR Code?
A QR (Quick Response) code is a two-dimensional pictographic code known for its fast readability and relatively large storage capacity. The code is made up of black squares (modules) arranged on a white background and can store different types of data:
 - Binary
 - Alphanumeric
 - Kanji symbols
 - And more

## ⚙️ QR Code Error Correction
The qrcode library provides four levels of error correction. These allow a QR code to remain scannable even if partially damaged:
| Constant           | Correction Level       | Description                             |
|--------------------|------------------------|----------------------------------------|
| `ERROR_CORRECT_L`  | Low                    | Recovers ~7% of the data                |
| `ERROR_CORRECT_M`  | Medium (default)       | Recovers ~15% of the data               |
| `ERROR_CORRECT_Q`  | Quartile               | Recovers ~25% of the data               |
| `ERROR_CORRECT_H`  | High                   | Recovers ~30% of the data               |
|
In this project, we use ERROR_CORRECT_Q for a balance between reliability and QR complexity.

## 🖼️ Interface
This app uses Tkinter to provide a graphical interface where users can enter Wi-Fi credentials and instantly generate a QR code ready to scan.

## ⭐ Like this project?
Star it if you found it useful ⭐ and feel free to contribute!
