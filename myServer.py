#Class Libraries
import discord
import os
import random 
from ec2_metadata import ec2_metadata
from dotenv import load_dotenv

load_dotenv()

#Initialize the Discord bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

#Get the token from the environment variables
token = str(os.getenv('TOKEN'))

#Output to make sure the class libraries work
print('This is my Ec2_metadata.region:', ec2_metadata.region)
print('This is my Ec2_metadata.instance.id:', ec2_metadata.instance_id)


@client.event 
async def on_ready(): 
    # Print a message when the bot is logged in and ready
    print("Logged in as a bot {0.user}".format(client))

@client.event 
async def on_message(message): 
    # Get the username, channel, and message content
    username = str(message.author).split("#")[0] 
    channel = str(message.channel.name) 
    user_message = str(message.content) 

    # Log the message
    print(f'Message {user_message} by {username} on {channel}') 

    # Prevent the bot from replying to itself
    if message.author == client.user: 
        return

    # Check if the message is in the "random" channel
    if channel == "random": 
        # Respond to greetings
        if user_message.lower() == "hello":
            await message.channel.send(f'Hi {username} ') 
            return
        # other string options
        elif user_message.lower() == "aloha": 
            await message.channel.send(f'Mahalo {username}') 

        # Returning instance data for the last conditional statement.
        elif user_message.lower() == "ec2 data": 
            await message.channel.send(f"Your instance data is  {ec2_metadata.instance} Your EC2 Data: {ec2_metadata.region}") 

#Run the bot with the token
client.run(token)
