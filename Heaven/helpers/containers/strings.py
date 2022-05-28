class Strings(object):
    def stat_string(self):
        return f"""
			**Dex:** Stats

			**Location:** /home/stats

			**Name:** {self.UserName()}
			**{self.BotName()} version:** {self.assistant_version}
			**Python version:** {self.python_version}
			**Pyrogram version:** {self.pyrogram_version}
			**Database:** {self.db_status()}
			**Uptime:** {self.uptime()}
			**User Bio:** {self.UserBio()}
			"""

    def closed_menu_string(self):
        return f"""
			Welcome to Heaven World.
			This is your Helpdex, Tap on open button to get more buttons which will help you to understand & operate your userbot & assistant.

			• Menu is closed
			"""
