from . import Command
from .. import utils
import requests
import json


class Xkcd(Command):
    names = ["xkcd"]
    description = "Gets a relevant xkcd"
    needsContent = False

    async def execute_command(self, client, msg, content):
        # if len(content) == 0:

        response = json.loads(
            str(
                requests.post(
                    "https://relevant-xkcd-backend.herokuapp.com/search",
                    data={"search": content},
                )
            )
        )

        print(response)

        await utils.delay_send(msg.channel, response, 1)
