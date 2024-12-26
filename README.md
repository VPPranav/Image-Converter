# Image-Converter
This project is a web-based Image Editor built using Flask and OpenCV. It allows users to upload images and perform basic image processing tasks such as converting images to grayscale or changing their formats (WEBP, JPG, PNG). The application supports file validation to ensure only allowed image types are processed. 
Detailed Description of the Image Editor Project
This project is a web-based Image Editor developed using the Flask web framework and OpenCV library for image processing. The application enables users to upload images and apply basic operations such as converting images to grayscale and changing their formats (e.g., converting to WEBP, JPG, PNG). The platform is designed to be simple and user-friendly while providing essential image editing functionalities.

Key Features:
Image Upload:

The application allows users to upload images through a user-friendly web interface.
Supported file formats include PNG, WEBP, JPG, JPEG, and GIF.
The application performs file validation to ensure that only these supported formats are uploaded, rejecting any unsupported file types.
Image Processing Operations:

Grayscale Conversion: Users can convert their images into grayscale, making them black-and-white.
Format Conversion: Users can convert images to different formats such as WEBP, JPG, or PNG.
The image processing is handled by OpenCV, a powerful image processing library, which is responsible for reading and manipulating the uploaded images.
File Handling:

The application saves the uploaded images to an uploads folder and stores the processed images in the static folder.
Each processed image is saved with a new filename, indicating the operation performed (e.g., adding "_gray" to the filename for grayscale images).
User Feedback:

After processing an image, the application provides real-time feedback using Flash Messages, notifying the user whether the operation was successful or if any issues occurred during the upload or processing.
Flash messages also contain a clickable link to the processed image, allowing users to view or download it easily.
Simple Navigation:

The app features two main pages: the Home page for uploading and processing images, and the About page providing details about the project.
The web interface is simple yet intuitive, designed with Bootstrap for responsive layout and user experience.
Folder and File Management:

The application ensures that the necessary directories (e.g., uploads and static) are created if they do not already exist, ensuring that file storage is handled correctly.
Images are securely saved using secure_filename from the Werkzeug library to prevent security issues related to file names.
Deployment:

The Flask application runs locally on a development server (default port 5001), allowing users to interact with the tool via a browser. It can be easily deployed to a production environment with minimal changes.
