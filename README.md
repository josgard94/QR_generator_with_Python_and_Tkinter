# QR_generator_with_Python_and_Tkinter
Share your Wifi connection using a QR. In this project, the Python qrcode library is used to generate a QR code with the necessary information to automatically connect a mobile device to a Wifi network. The QR code generated in this project has an error correction capacity of approximately 25%.

To execute this source code it is necessary to install the qrcode library with the following command:
  
  + pip install qrcode


What is a QR Code?

A Quick Response code is a two-dimensional pictographic code used for its fast readability and comparatively large storage capacity. The code consists of black modules arranged in a square pattern on a white background. The information encoded can be made up of any kind of data (e.g., binary, alphanumeric, or Kanji symbols).


The error_correction parameter controls the error correction used for the QR Code. The following four constants are made available on the qrcode package:

  + ERROR_CORRECT_L		
      +	About 7% or less errors can be corrected.
  + ERROR_CORRECT_M (default)		
      +	About 15% or less errors can be corrected.
  + ERROR_CORRECT_Q		
      +	About 25% or less errors can be corrected.
  + ERROR_CORRECT_H.		
      +	About 30% or less errors can be corrected. 
