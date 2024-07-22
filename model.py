# minimal_example.py
import chainlit as cl

@cl.on_chat_start
async def start():
    msg = cl.Message(content="Bot is ready. What's your query?")
    await msg.send()

@cl.on_message
async def main(message: cl.Message):
    await cl.Message(content=f"You said: {message.content}").send()

# Run this minimal example