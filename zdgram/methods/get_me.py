import zdgram

class GetMe:
    async def getMe(self: "zdgram.Bot") -> "zdgram.types.User":
        """
        A simple method for testing your bot's authentication token. Requires no parameters. Returns basic information about the bot in form of a User object.

        :return: Returns basic information about the bot in form of a User object
        """
        if "me" in self.cache:
            return self.cache.get('me')
        resp_json = await self.sendRequest(
            method_name="getMe"
        )
        me = zdgram.bot.update_manager._parse(zdgram.bot.user_manager._parse(resp_json.get("result")))
        self.cache.update({"me": me})
        return me

    get_me = getMe