from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageEvent
import openai


gpt = on_command("chat",priority=4)



@gpt.handle()
async def gpt_handle(event:MessageEvent):
    openai.api_key = "YOUR API KEY HERE"
    user_msg=str(event.message)
    user_msg=user_msg[4:]
    msg=[{"role": "user", "content": user_msg}]
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg)
    await gpt.send(message=str(response.choices[0].message.content)[2:],at_sender=True)
    await gpt.finish()
    