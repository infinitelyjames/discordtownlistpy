import requests, threading, asyncio

class Threads:
	def newThread(function, args=()):
		new_thread = threading.Thread(target=function, args=args) # error handle threads so they output into log file
		new_thread.start()
		return new_thread

def postGuildCount(guild_count: str, token: str, threaded=True): # runs in background if threaded==True, in case API is slow (took ~1-2 minutes to post during testing, however did speed up)
    def main(guild_count, token):
        url = "https://townlist.xyz/api/bots/stats" # townlist.xyz listing.discordtownshop.com
        headers = {"serverCount": guild_count,"Content-Type": "application/json","Authorization": token}
        requests.post(url, headers=headers)
    if threaded:
        Threads.newThread(lambda: main(guild_count, token))
    else:
        main(guild_count, token)

async def asyncRequest(url: str, method=requests.get):
    loop = asyncio.get_event_loop()
    future_object = loop.run_in_executor(None, method, url)
    response = await future_object
    return response

async def returnBotData(bot_id: str):
    response = await asyncRequest("https://townlist.xyz/api/bots/{0}".format(bot_id))
    return response.json()
