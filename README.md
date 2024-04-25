# Yet Another Telegram to Discord Script (YAT2DS)

*Redirects messages from any channel in Telegram to a Discord channel using Discord webhook.*

## Libraries
- Telegram: [LonamiWebs/Telethon](https://github.com/LonamiWebs/Telethon)
- Discord webhook: [lovvskillz/python-discord-webhook](https://github.com/lovvskillz/python-discord-webhook)

## How it works?

The script uses Telegram userbot (or selfbot) which is **NOT** Telegram bot to read messages of any channel from the user.

The main advantage of userbot is that we don't need to add a bot to a channel to read messages but instead we just need to be in the channel.

However, an obvious drawback is that abusing the API can make your account banned instead of a simple bot so make sure you don't break [Telegram's TOS](https://core.telegram.org/api/terms) otherwise your account will be banned (like someone I know personally).

**TLDR**: You can be **banned**, use the script at your own risk.

## Installing and Setup

### Fill `config.yml`

Edit the config file with your own credentials:
- `api_id` and `api_hash` can be obtained by creating a new application from telegram (https://my.telegram.org). They are used to log into your user account.

- `TARGET_CHANNEL_ID` is the id of the Telegram channel you want to redirect. You can get it by looking at the url of the channel using the web version:

  ![Telegram channel id](images/channel_id.png)
  
  *Here the channel id is `2021440294`.*

- `DISCORD_WEBHOOK_URL` allows the script to redirect Telegram messages to a specific Discord channel (without using Discord bot). You can create a new webhook url for the Discord channel you want the messages to be redirected by doing: 
  
  `Edit the channel -> Integrations -> Webhooks -> New webhook`.
  
  It should look like: `https://discord.com/api/webhooks/???/???`.

Once you have all the required credentials, you can run the script.

### First connection

The first time you will run the script, it will ask your phone number and the security code.

After that, it should not ask you since it has created a "session" file (in our case it's named `me.session`).

If you delete or modify this file, you have to authenticate again.

If you change IP, you may need to authenticate again.

### Deploy the script

```shell
# Install dependencies
pip install -r requirements.txt

# Start the script
python main.py

# Start the script and keep it in the background with tmux
tmux # Start a new tmux instance
python main.py # Then CTRL-B + D to detach and you can exit the terminal

# Stop the script in the background
tmux attach # Get the previous tmux instance
# CTRL-C to stop the script
# CTRL-D to exit tmux
```

## Improvement

Currently, the script only redirect **text** from messages.

If I have spare time, I may add support for documents, videos and pictures but feel free to improve it and send me a pull request if you want to contribute to the project.