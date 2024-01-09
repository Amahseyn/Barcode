Barcode Reader
This is a simple Python script that uses OpenCV and the pyzbar library to read barcodes from an image.

Prerequisites
Python 3.x
OpenCV (cv2) library
pyzbar library
Numpy library
Installation
Clone the repository or download the script file (barcode_reader.py) to your local machine.

Install the required dependencies by running the following command:

Copy
pip install opencv-python pyzbar numpy
```
Usage
Place the barcode image file in the appropriate location. In this script, the image file is expected to be located at /home/mio/Documents/Barcode/images/Untitled.jpg. Make sure to modify the path to match your specific image file.

Run the script using the following command:

Copy
python barcode_reader.py
```

The script will display the processed image and wait for a key press. Once you press a key, it will print the shape of the image and the mean value of the pixel densities.

It will then apply a threshold to the image based on the pixel densities and display the resulting image. Again, it will wait for a key press.

Finally, it will attempt to decode any barcodes present in the image using the pyzbar library. If a barcode is successfully detected, it will print the data of the first barcode found.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
