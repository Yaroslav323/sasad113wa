import discord

discord_token = input("Token Discord: ")

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"User {client.user.name} success connect to Discord")
    
    server_id = input("server Discord: ").strip()
    channel_id = input("chanel Discord: ").strip()

    while True:
        message = input("Text (or 'exit' for exit): ").strip()
        if message.lower() == "exit":
            break

        try:
            server = client.get_guild(int(server_id))
            channel = discord.utils.get(server.channels, id=int(channel_id))
            await channel.send(message)
            print(f"Sent {server.name} in chanel {channel.name}")
        except discord.Forbidden:
            print("Error")
        except discord.HTTPException as e:
            print(f"Error: {str(e)}")
        except discord.NotFound:
            print("Error")
        except ValueError:
            print("Error")

    await client.close()

client.run(discord_token)
