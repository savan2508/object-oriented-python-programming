# Webcam Photo Sharer

This code uses the Kivy library to create a graphical user interface (GUI) application with two screens: CameraScreen and ImageScreen. The CameraScreen allows the user to start and stop the webcam, capture an image, and move to the ImageScreen. The ImageScreen allows the user to generate a shareable link for the captured image, copy the link to the clipboard, and open the link in a web browser.

The GUI is defined in a KV file, frontend.kv, which is loaded using the Builder module. The KV file defines the layout and widgets for the screens and their functionality.

The CameraScreen class contains methods for starting and stopping the webcam, capturing an image, and moving to the ImageScreen. The start() method sets the camera play flag to True to start the webcam and updates the camera button text. The stop() method sets the camera play flag to False to stop the webcam and updates the camera button text. The capture() method creates a filename based on the current time, exports the camera texture to a PNG file with the filename, and moves to the ImageScreen with the captured image.

The ImageScreen class contains methods for creating a shareable link, copying the link to the clipboard, and opening the link in a web browser. The create_link() method gets the filename of the captured image from the CameraScreen, creates a FileSharer object with the filepath, generates a shareable link using the share() method, and displays the link in the ImageScreen. The copy_link() method copies the link to the clipboard using the Clipboard module, or displays an error message if the link hasn't been created yet. The open_link() method opens the link in a web browser using the webbrowser module, or displays an error message if the link hasn't been created yet.

The RootWidget class is a subclass of ScreenManager, which manages the screens and their transitions. The RunApp class is the main application class, which builds and runs the GUI.

Overall, this code provides a simple way to capture an image from a webcam and share it online via a generated link. However, there is no security or authentication implemented for the file sharing, so use with caution.

# Features
Start and stop the webcam

Capture an image from the webcam

Generate a shareable link for the captured image

Copy the link to the clipboard

Open the link in a web browser

# Requirements 
Python 3.x

Kivy library

filesharer library

webbrowser module

# Installation
Clone this repository to your local machine.

Install the required dependencies using pip install -r requirements.txt.

Run the application using python main.py.

# Usage
Start the webcam by clicking the "Start Camera" button.

Capture an image by clicking the "Capture" button.

Move to the ImageScreen by clicking the "Share" button.

Generate a shareable link by clicking the "Create Link" button.

Copy the link to the clipboard by clicking the "Copy Link" button.

Open the link in a web browser by clicking the "Open Link" button.

# Security
Please note that this application does not provide any security or authentication for the shared files. Use at your own risk.

# Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues if you find any bugs or have any feature requests.
