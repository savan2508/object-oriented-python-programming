import justpy as jp
import definition
from Webapp import layout
from Webapp import page


class Documentation(page.Page):
    path = '/documentation'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        jp.Div(a=container, text="Instant Dictionary API", classes="text-4xl m-2")
        jp.Div(a=container, text="Get Definition of words", classes="text-lg")
        jp.Hr(a=container)

        # Word Definition API section
        jp.Div(a=container, text="Word Definition API", classes="text-2xl m-2")
        jp.P(a=container,
             text="The Word Definition API provides a simple way to retrieve definitions for English words.")
        jp.P(a=container,
             text="You can use this API by making a GET request to the `/api` endpoint with the `w` query parameter "
                  "specifying the word for which you want the definition.")

        # Endpoint section
        jp.Div(a=container, text="Endpoint", classes="text-lg font-semibold mt-4")
        jp.Code(a=container, text="/api?w=word", classes="bg-gray-100 p-2 rounded")
        jp.P(a=container,
             text="The `/api` endpoint accepts a `w` query parameter to specify the word for which you want the "
                  "definition.")

        # Parameters section
        jp.Div(a=container, text="Parameters", classes="text-lg font-semibold mt-4")
        jp.Table(a=container, classes="table-auto border-collapse")
        jp.Tr(a=container, classes="bg-gray-200")
        jp.Th(a=container, text="Parameter", classes="px-4 py-2 border")
        jp.Th(a=container, text="Type", classes="px-4 py-2 border")
        jp.Th(a=container, text="Description", classes="px-4 py-2 border")
        jp.Tr(a=container)
        jp.Td(a=container, text="w", classes="px-4 py-2 border")
        jp.Td(a=container, text="string", classes="px-4 py-2 border")
        jp.Td(a=container, text="The word to get the definition for.", classes="px-4 py-2 border")

        # Example Request section
        jp.Div(a=container, text="Example Request", classes="text-lg font-semibold mt-4")
        jp.Code(a=container, text="GET /api?w=example", classes="bg-gray-100 p-2 rounded")

        # Example Response section
        jp.Div(a=container, text="Example Response", classes="text-lg font-semibold mt-4")
        jp.Code(a=container, text='''{
          "word": "example",
          "definition": [
            "A thing characteristic of its kind or illustrating a general rule."
          ]
        }''', classes="bg-gray-100 p-2 rounded")

        return wp