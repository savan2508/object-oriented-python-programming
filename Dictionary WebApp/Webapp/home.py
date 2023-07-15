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
        jp.Div(a=div, text="This is the Home page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        This is some text, lorem ipsum aojsafjsdoapjfdsoajf
        dafjosdijaofdjaoifjsdio adofjsd afjdos afjdsoaf afdiosajf 
        jfaodsjf afdjsoa jfa osdjaofjsdo aojdioajfsd asiofja sd
        ajosdifajdsoa fsdoajfoidsj aiodfjaso 
        """, classes="text-lg")

        return wp


