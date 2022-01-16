import json

from .errors import NoResultFound

from urllib.request import urlopen, Request
from urllib.error import HTTPError
from random import choice

__all__ = ["Waifu"]


class Waifu:
    """Represents the waifu class. Fetches image urls from `waifu.pics <https://waifu.pics/>`__."""

    base = "https://waifu.pics/api/sfw/"

    @classmethod
    def __image__(cls, url: str) -> str:

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"
        }
        req = Request(url=url, headers=headers)

        try:
            page = urlopen(req)
        except HTTPError as e:
            raise NoResultFound(f"HTTP Error: {e.code}")

        res = json.loads(page.read())

        return res["url"]

    @classmethod
    def random(cls) -> str:
        """Returns waifus from random category"""

        select = choice(["waifu", "shinobu", "megumin", "neko"])
        return cls.__image__(cls.base + select)

    @classmethod
    def random_gif(cls) -> str:
        """Returns a random anime gif"""

        select = choice(
            [
                "bully",
                "cuddle",
                "cry",
                "hug",
                "awoo",
                "kiss",
                "lick",
                "pat",
                "smug",
                "bonk",
                "yeet",
                "blush",
                "smile",
                "wave",
                "highfive",
                "handhold",
                "nom",
                "bite",
                "glomp",
                "slap",
                "kill",
                "kick",
                "happy",
                "wink",
                "poke",
                "dance",
                "cringe",
            ]
        )
        return cls.__image__(cls.base + select)

    @classmethod
    def waifu(cls) -> str:
        """Returns untagged waifus"""

        return cls.__image__(cls.base + "waifu")

    @classmethod
    def shinobu(cls) -> str:
        """Returns waifus from shinobu category"""

        return cls.__image__(cls.base + "shinobu")

    @classmethod
    def megumin(cls) -> str:
        """Returns waifus from megumin category"""

        return cls.__image__(cls.base + "megumin")

    @classmethod
    def neko(cls) -> str:
        """Returns waifus from neko category"""

        return cls.__image__(cls.base + "neko")

    @classmethod
    def bully(cls) -> str:
        """Returns anime bully gifs"""

        return cls.__image__(cls.base + "bully")

    @classmethod
    def cuddle(cls) -> str:
        """Returns anime cuddle gifs"""

        return cls.__image__(cls.base + "cuddle")

    @classmethod
    def cry(cls) -> str:
        """Returns anime cry gifs"""

        return cls.__image__(cls.base + "cry")

    @classmethod
    def hug(cls) -> str:
        """Returns anime hug gifs"""

        return cls.__image__(cls.base + "hug")

    @classmethod
    def awoo(cls) -> str:
        """Returns anime awoo gifs"""

        return cls.__image__(cls.base + "awoo")

    @classmethod
    def kiss(cls) -> str:
        """Returns anime kiss gifs"""

        return cls.__image__(cls.base + "kiss")

    @classmethod
    def lick(cls) -> str:
        """Returns anime lick gifs"""

        return cls.__image__(cls.base + "lick")

    @classmethod
    def pat(cls) -> str:
        """Returns anime pat gifs"""

        return cls.__image__(cls.base + "pat")

    @classmethod
    def smug(cls) -> str:
        """Returns anime smug gifs"""

        return cls.__image__(cls.base + "smug")

    @classmethod
    def bonk(cls) -> str:
        """Returns anime bonk gifs"""

        return cls.__image__(cls.base + "bonk")

    @classmethod
    def yeet(cls) -> str:
        """Returns anime yeet gifs"""

        return cls.__image__(cls.base + "yeet")

    @classmethod
    def blush(cls) -> str:
        """Returns anime blush gifs"""

        return cls.__image__(cls.base + "blush")

    @classmethod
    def smile(cls) -> str:
        """Returns anime wave gifs"""

        return cls.__image__(cls.base + "wave")

    @classmethod
    def highfive(cls) -> str:
        """Returns anime highfive gifs"""

        return cls.__image__(cls.base + "highfive")

    @classmethod
    def handhold(cls) -> str:
        """Returns anime handhold gifs"""

        return cls.__image__(cls.base + "handhold")

    @classmethod
    def nom(cls) -> str:
        """Returns anime nom gifs"""

        return cls.__image__(cls.base + "nom")

    @classmethod
    def bite(cls) -> str:
        """Returns anime bite gifs"""

        return cls.__image__(cls.base + "bite")

    @classmethod
    def glomp(cls) -> str:
        """Returns anime glomp gifs"""

        return cls.__image__(cls.base + "glomp")

    @classmethod
    def slap(cls) -> str:
        """Returns anime slap gifs"""

        return cls.__image__(cls.base + "slap")

    @classmethod
    def kill(cls) -> str:
        """Returns anime kill gifs"""

        return cls.__image__(cls.base + "kill")

    @classmethod
    def kick(cls) -> str:
        """Returns anime kick gifs"""

        return cls.__image__(cls.base + "kick")

    @classmethod
    def happy(cls) -> str:
        """Returns anime happy gifs"""

        return cls.__image__(cls.base + "happy")

    @classmethod
    def wink(cls) -> str:
        """Returns anime wink gifs"""

        return cls.__image__(cls.base + "wink")

    @classmethod
    def poke(cls) -> str:
        """Returns anime pole gifs"""

        return cls.__image__(cls.base + "poke")

    @classmethod
    def dance(cls) -> str:
        """Returns anime dance gifs"""

        return cls.__image__(cls.base + "dance")

    @classmethod
    def cringe(cls) -> str:
        """Returns anime cringe gifs"""

        return cls.__image__(cls.base + "cringe")
