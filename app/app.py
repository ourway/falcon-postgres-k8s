"""
main application
"""
import os
from datetime import datetime
from glob import glob

import falcon

from constants import TIME_FORMAT
from db.models import Preferences
from db.session import session_scope
from utils import save_random_image

FAL_VER = os.environ["FAL_VER"]


class QuoteResource:
    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """Handles GET requests"""
        with session_scope() as session:
            data = session.query(Preferences).filter(Preferences.name == "hitcount").scalar()
            if not data:
                obj = Preferences(name="hitcount", value="1", description="just hit counts")
                session.add(obj)
            else:
                new_val = int(data.value) + 1
                data.value = str(new_val)
                session.add(data)

            quote = {
                "quote": ("I've always been more interested in " "the future than in the past."),
                "author": "Farshid Ashouri",
                "version": FAL_VER,
            }

            resp.media = quote


class ServerTimeResource:
    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """Connects to database and fetches server time"""
        with session_scope() as session:
            servertime, *_ = session.execute("select now()").fetchone()
            server_time = datetime.strftime(servertime, TIME_FORMAT)
            result = {"response": server_time}
            resp.media = result


class HitCountResource:
    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """fetches number of hitcounts"""
        with session_scope() as session:
            data = session.query(Preferences.value).filter(Preferences.name == "hitcount").scalar()
            result = {"response": data}
            resp.media = result


class StorageResource:
    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        """fill storage with random data and list files"""
        save_random_image()
        resp.media = {"response": glob("/data/*.jpg")}


application = falcon.API()
application.add_route("/ping", QuoteResource())
application.add_route("/servertime", ServerTimeResource())
application.add_route("/hitcount", HitCountResource())
application.add_route("/storage", StorageResource())
