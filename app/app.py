import os

import falcon

FAL_VER = os.environ["FAL_VER"]


class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            "quote": ("I've always been more interested in " "the future than in the past."),
            "author": "Farshid Ashouri",
            "version": FAL_VER,
        }

        resp.media = quote


application = falcon.API()
application.add_route("/ping", QuoteResource())
