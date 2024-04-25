import sys
import yaml
from telethon.sync import TelegramClient, events
from discord_webhook import DiscordWebhook, DiscordEmbed

with open("./config.yml", "r") as config_file:
    config = yaml.safe_load(config_file)

    for k, v in config.items():
        if v == '???':
            print(f"You need to provide '{k}' in config.yml")
            sys.exit()

    api_id = config['api_id']
    api_hash = config['api_hash']
    TARGET_CHANNEL_ID = config['TARGET_CHANNEL_ID']
    DISCORD_WEBHOOK_URL = config['DISCORD_WEBHOOK_URL']

with TelegramClient('me', api_id, api_hash) as client:
    print("Logged in successfully!")

    # Get self
    me = client.get_me()
    print(f"Welcome {me.first_name}{' '+me.last_name if me.last_name else ''} (id={me.id})")

    # Fill entity cache
    dialogs = client.get_dialogs()

    # Get the target channel entity
    channel = client.get_entity(TARGET_CHANNEL_ID)

    # On new message in the target channel
    @client.on(events.NewMessage(chats=channel))
    async def handler(event):
        message = event.message

        # Send webhook
        webhook = DiscordWebhook(url=DISCORD_WEBHOOK_URL)
        embed = DiscordEmbed(description=message.message)
        embed.set_footer(text="By YAT2DS")
        embed.set_timestamp(message.date)
        webhook.add_embed(embed)
        response = webhook.execute()

    client.run_until_disconnected()

print("Logged out")