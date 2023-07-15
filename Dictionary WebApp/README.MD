# Dictionary Webapp

This is a web application built using the JustPy library and Pandas for data handling. It provides an instant English dictionary where users can get the definition of any English word as they type.

## Usage

### Windows Users

If you're a Windows user, you can simply download the `DictionaryWebapp.exe` file from the repository. Running this executable will start the web application locally on your machine. You can access it by opening your web browser and visiting [http://127.0.0.1:8001/](http://127.0.0.1:8001/).

### Mac and Linux Users

If you're using Mac or Linux, you can clone this repository to your local machine by executing the following command in your terminal:


Once the repository is cloned, navigate to the project directory and run the `main.py` file:


This will start the web application on your local machine. You can access it by opening your web browser and visiting [http://127.0.0.1:8001/](http://127.0.0.1:8001/).

## Installation

To install the necessary dependencies, use the following command:


This will install the required Python libraries (`justpy` and `pandas`) needed to run the web application.

## Documentation

The code in this repository consists of several modules and classes that make up the Dictionary Webapp. Here's a brief overview of the code structure:

- `main.py`: This is the entry point of the application. Running this file starts the JustPy server and serves the web application.
    * This code sets up routes for different pages in a web application using the JustPy framework. It imports the necessary modules and classes and then registers routes for pages that inherit from the page.Page base class. The routes are registered using the jp.Route function, which takes the path and the serve function of each page as arguments.

The registered pages include Home, About, and Dictionary. The Home page is served when the root path ("/") is accessed, the About page is served when the path "/about" is accessed, and the Dictionary page is served when the path "/dictionary" is accessed.

The jp.justpy(port=8001) line starts the JustPy server on port 8001, making the web application accessible through that port.

- `Webapp`: This directory contains the core logic of the web application.
  - `page.py`: Defines the base class for web pages and contains the routing logic.
  - `home.py`: Implements the Home page, which is served at the root path ("/").
    * This code defines the Home page class that also inherits from page.Page. It sets the path attribute to "/", indicating that this page should be served when the root path is accessed. The serve method is a class method that serves as the entry point for this page. It creates a JustPy QuasarPage instance, defines the layout and content for the page, and returns the QuasarPage instance, which will be rendered by JustPy.
  - `about.py`: Implements the About page, which is served at "/about".
  - `dictionary.py`: Implements the Dictionary page, which is served at "/dictionary".
    * This code defines the Dictionary page class that inherits from page.Page. It sets the path attribute to "/dictionary", indicating that this page should be served when that path is accessed.
    * The serve method is a class method that serves as the entry point for this page. It creates a JustPy QuasarPage instance and defines the layout and content for the page. It returns the QuasarPage instance, which will be rendered by JustPy. 
    * The get_definition method is a static method that handles the logic for retrieving the definition of a word. It takes a widget and msg as arguments. It uses the definition.Definition class to retrieve the definition of the word entered in the inputbox widget. It then sets the text of the outputdiv widget to display the definition.
  - `layout.py`: Contains the layout components used in the web application.
    * This code defines the DefaultLayout class, which is a subclass of jp.QLayout from the JustPy framework. It overrides the __init__ method to customize the layout. The DefaultLayout class sets up a header, toolbar, and drawer components using the Quasar framework. It provides a method move_drawer to handle toggling the drawer's visibility when a button is clicked.
  - `definition.py`: Defines the `Definition` class used for retrieving word definitions.
- `data.csv`: This CSV file contains the word definitions used by the application.
- `DictionaryWebapp.exe`: The Windows executable file for running the web application.

### API

The Dictionary Webapp also provides an API for retrieving word definitions programmatically. You can make a GET request to the `/api` endpoint with the `w` query parameter specifying the word for which you want the definition. The API will return a JSON response containing the word and its definition.

To use the API, refer to the API documentation section for detailed information on the API endpoint and usage.

## API Documentation

For detailed information on how to use the API and its endpoints, please refer to the [API Documentation](API_DOCUMENTATION.md) file.

## Contributing

## Contributing

Contributions to this repository are welcome. If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

---

Enjoy using the Dictionary Webapp! If you have any questions or need further assistance, please don't hesitate to reach out at sawanpatel2508@gmail.com.

