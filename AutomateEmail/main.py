import datetime
import time
import yagmail
import pandas
import requests


class NewsFeed:
    base_url = 'https://newsapi.org/v2/everything?'

    """
    1. Go to the newsapi.org website.
    2. Click on the "Get API Key" button in the top right corner of the page.
    3. Sign up for a free account by providing your email address and creating a password. Alternatively, you can sign 
    up using your Google or Facebook account.
    4. Once you have signed up, you will be redirected to your dashboard.
    5. Click on the "API Keys" tab in the top menu.
    6. You will see a default API key already created for you. You can use this key or create a new one by clicking on 
    the "Create API Key" button.
    7. Give your API key a name and select the plan you want to use (the free plan is sufficient for most small 
    projects).
    8. Once you have created your API key, it will be displayed on the dashboard along with its usage statistics.
    9. Copy the API key and use it in your project to make requests to the News API.
    10. Paste the key below as a string(in the quotation mark) to run the program. 
    """

    API_Key = ''

    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = f'{self.base_url}' \
              f'qInTitle={self.interest}&' \
              f'from={self.from_date}' \
              f'to={self.to_date}' \
              'sortBy=popularity&' \
              f'language={self.language}&' \
              f'apiKey={self.API_Key}'

        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        email_body = ''

        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body


while True:
    if datetime.datetime.now().hour == 6 and datetime.datetime.now().minute == 00:

        df = pandas.read_excel('email_list.xlsx')

        """
        If you have gmail account enter in the user_email or Go to the Gmail website at www.gmail.com.
        Click on the "Create account" button.
        Fill out the sign-up form with your first and last name, username (which will be your email address), 
        and password.
        Follow the prompts to enter your phone number for verification and complete the sign-up process.
        Once you have created your Gmail account, go to your account settings by clicking on your profile picture in 
        the top right corner of the Gmail window and selecting "Google Account".
        In the left-hand menu, select "Security".
        Scroll down to the "Signing in to Google" section and click on "App passwords".
        Select the app or device you want to generate an app password for (in this case, your Python script).
        Select your device type and operating system, if applicable.
        Click on "Generate" to create a new app password.
        Copy the app password and use it in your Python script to authenticate with Gmail.
        """
        user_email = ""
        user_password = ""

        today = datetime.datetime.now().strftime('%y-%m-%d')
        yesterday = datetime.datetime.now() - datetime.timedelta(days=1)

        for index, row in df.iterrows():
            news_feed = NewsFeed(interest=row['interest'],
                                 from_date=yesterday.strftime('%y-%m-%d'),
                                 to_date=today,
                                 language='en')
            email = yagmail.SMTP(user=user_email, password=user_password)
            email.send(to=row['email'],
                       subject=f"Hi {row['First Name']}",
                       contents=f"What's up buddy? Your interest is {row['interest']}. "
                                f"Your free news are \n{news_feed.get()}")

    time.sleep(60)
