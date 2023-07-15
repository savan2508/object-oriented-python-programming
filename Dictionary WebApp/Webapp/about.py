import justpy as jp
from Webapp import layout
from Webapp import page

class About(page.Page):
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-grey-200 h-screen")
        jp.Div(a=div, text="About Me", classes="text-4xl m-2")
        jp.Div(a=div,
               text="Hi, I'm Savan Patel, the developer behind this web application. I created this app to showcase "
                    "my skills in web development using Python as the backend. This project demonstrates my expertise "
                    "in creating a dynamic dictionary app with an instant English word definition feature.",
               classes="text-lg")
        jp.Div(a=div,
               text="In addition to Python, I am a skilled developer proficient in Node.js. I have extensive "
                    "experience in building web applications and working with APIs. The combination of Python and "
                    "Node.js allows me to create robust and scalable web solutions.",
               classes="text-lg")
        jp.A(a=div, text="Visit my website", href="https://savan2508.github.io/savan-website/",
             classes="text-lg mt-4 underline text-blue-500")
        jp.Div(a=div,
               text="On my website, you'll find a collection of my work, including web development projects, "
                    "tutorials, and more.",
               classes="text-lg mt-2")
        jp.Div(a=div,
               text="If you have any inquiries or would like to collaborate on a project, please don't hesitate to "
                    "reach out. You can contact me via email at ",
               classes="text-lg mt-4")
        jp.A(a=div, text="sawanpatel2508@gmail.com", href="mailto:sawanpatel2508@gmail.com",
             classes="text-lg underline text-blue-500")

        return wp
