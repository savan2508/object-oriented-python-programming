# CaloriesCalculator

This is a Python Flask web application that calculates the number of calories needed by an individual based on their weight, height, age, and location's temperature.

The app is defined using Flask, and it has two pages: a home page and a calories form page. The home page is defined by the HomePage class, which inherits from Flask's MethodView class. The get() method of the HomePage class renders the index.html template.

The calories form page is defined by the CaloriesFormPage class, which also inherits from Flask's MethodView class. The get() method of the CaloriesFormPage class creates an instance of the CaloriesForm class and renders the calories_form_page.html template with the form as context. The post() method of the CaloriesFormPage class receives the form data, creates an instance of the Temperature class to get the current temperature in the user's location, and then creates an instance of the Calories class with the user's information and the temperature. Finally, it calculates the number of calories needed by the user and renders the calories_form_page.html template with the form and result as context.

The CaloriesForm class is a subclass of the Form class from the wtforms library. It defines the form fields and a submit button. The calories_form_page.html template renders the form fields and result, if available.

The Temperature and Calories classes are defined in separate Python files (temperature.py and calories.py, respectively) and imported into this file. They handle the logic for getting the temperature and calculating the calories, respectively.

The application can be run using app.run() function call with the debug argument set to True.

# Installation
To run this application, you will need to install the following:

Python 3.x
Flask
wtforms
Clone this repository or download the ZIP file and extract the contents to a directory on your computer.

# Usage
Open your terminal or command prompt and navigate to the directory where the application is located.
Run the following command to start the Flask development server:
Copy code
python app.py
Open your web browser and go to http://localhost:5000/ to access the home page.
Click on the "Calories Form" link to go to the calories form page.
Enter your weight, height, age, country, and city, and click the "Calculate" button to calculate your daily caloric needs.
The app will display your daily caloric needs for the current temperature in the specified country and city.

# Credits
This app was developed by Savan Patel. It uses the following libraries:

Flask
wtforms
