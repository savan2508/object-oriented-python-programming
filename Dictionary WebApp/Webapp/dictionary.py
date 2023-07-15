import justpy as jp
import definition
from Webapp import layout
from Webapp import page


class Dictionary(page.Page):
    path = '/dictionary'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-100 h-screen")
        jp.Div(a=div, text="Instant English Dictionary", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the definition of any English word instantly as you type.", classes="text-lg")

        input_div = jp.Div(a=div, classes="grid grid-cols-2")
        input_box = jp.Input(a=input_div, placeholder="Type in a word here...",
                             classes="m-2 bg-gray-100 border-2 border-grey-200 rounded w-64"
                                     "w-64 focus:bg-white focus:outline-none"
                                     "focus:border-purple-500 py-2 px-4")

        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40")
        jp.Button(a=input_div, text="Get Definition", classes="border-2 text-grey-100",
                  click=cls.get_definition, outputdiv=output_div, inputbox=input_box)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        defined = definition.Definition(widget.inputbox.value).get()
        widget.outputdiv.text = " ".join(defined)
