import json

import justpy as jp
import definition


class Api:
    """
    Handles requests at /api?w=word
    """
    @classmethod
    def serve(cls, req):
        """
            Serves the API request for word definition.

            Args:
                req (justpy.Request): The request object containing the query parameters.

            Returns:
                justpy.WebPage: The response as a JSON string containing the word and its definition.
        """
        wp = jp.WebPage()
        word = req.query_params.get('w')
        defined = definition.Definition(word).get()

        response = {
            "word": word,
            "definition": defined
        }
        wp.html = json.dumps(response)
        return wp

#
# jp.Route("/api", Api.serve)
# jp.justpy()
