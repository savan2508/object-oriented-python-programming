# Automate Email

## Description
This is a Python script that sends a daily email with news articles based on the interests of the recipient. The script uses the News API to retrieve news articles and the Yagmail library to send the email. It reads recipient information and interests from an Excel file.

## Prerequisites
Python 3.x
pandas
requests
yagmail

## Installation
1. Clone the repository:

    bash Copy code
    git clone https://github.com/savan2508/object-oriented-python-programming/tree/master/AutomateEmail
2. Install the required packages:
   bash
   Copy code
   pip install pandas requests yagmail

3. Sign up for a free News API key at https://newsapi.org/ and copy the key into the NewsFeed class in main.py.

4. Sign up for a Gmail account and generate an app password to authenticate with Gmail. Copy the email and password into the user_email and user_password variables in main.py.

5. Update the email_list.xlsx file with the recipients' information and interests.

## Usage
* To run the script, simply execute the following command:

python main.py

* The script will send an email to each recipient listed in email_list.xlsx with news articles based on their interests.

## Code:
* This Python code is used to fetch news articles from the News API based on the user's interests, and send those 
articles to a list of email recipients using the yagmail library.

* First, the necessary libraries are imported: datetime, time, yagmail, pandas, and requests.

* A class called NewsFeed is defined. This class has a base URL for the News API and an API Key attribute that will be 
used to make requests to the API. The NewsFeed class also has an init method that takes in the user's interests, the 
start and end dates for the news articles to be fetched, and the language in which the news articles should be 
returned. The get() method is defined within the class, which constructs a URL for the News API based on the user's 
inputs, sends a request to the News API, and returns a string containing the titles and URLs of the news articles.

* The program then enters an infinite loop using a while loop, which runs continuously until the program is terminated. 
The loop checks if the current time is 6:00 am using the datetime module. If the time is 6:00 am, the program 
proceeds to fetch the list of email recipients from an Excel file using the pandas library.

* The program then generates the news feed for each recipient using the NewsFeed class and sends an email to each 
recipient using yagmail. The email contains the recipient's first name, their interest, and the news articles that 
were fetched from the News API.

* Finally, the program waits for 60 seconds using the time.sleep() method before checking the time again and repeating 
the process. It ensure that the program does not spam the recipients. 

* Overall, this program fetches news articles from the News API and sends them to a list of email recipients based on 
their interests, all while running continuously until the program is terminated.
