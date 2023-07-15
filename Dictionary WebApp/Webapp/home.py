import justpy as jp
from Webapp import layout
from Webapp import page


class Home(page.Page):
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-grey-200 h-screen p-2")
        jp.Div(a=div, text="Welcome to the Dictionary Webapp!", classes="text-4xl m-2")
        jp.Div(a=div,
               text="This web application provides an instant English dictionary where you can get the definition of "
                    "any English word as you type.",
               classes="text-lg")
        jp.Div(a=div,
               text="If you want to access the dictionary, please use the navigation bar to explore the different "
                    "pages.",
               classes="text-lg")
        jp.Div(a=div,
               text="Alternatively, you can also use the Dictionary Webapp API to retrieve word definitions "
                    "programmatically.",
               classes="text-lg")
        jp.A(a=div, text="API Documentation", href="/documentation", classes="text-lg text-blue-500 underline")

        return wp


