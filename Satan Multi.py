import os
import json
import requests
import random
import time
import datetime
import colorama
from colorama import Fore, Style
import discord
from discord import Webhook, SyncWebhook
from discord.ext import commands
from pystyle import Colors, Colorate, Center

colorama.init()

class DiscordMultiTool:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {'Authorization': ''}
        self.token = ''
        self.bot_token = ''
        self.webhook_url = ''
        
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def banner(self):
        self.clear()
        banner = """
   ██████  ▄▄▄     ▄▄▄█████▓ ▄▄▄       ███▄    █ 
▒██    ▒ ▒████▄   ▓  ██▒ ▓▒▒████▄     ██ ▀█   █ 
░ ▓██▄   ▒██  ▀█▄ ▒ ▓██░ ▒░▒██  ▀█▄  ▓██  ▀█ ██▒
  ▒   ██▒░██▄▄▄▄██░ ▓██▓ ░ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
▒██████▒▒ ▓█   ▓██▒ ▒██▒ ░  ▓█   ▓██▒▒██░   ▓██░
▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░ ▒ ░░    ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
░ ░▒  ░ ░  ▒   ▒▒ ░   ░      ▒   ▒▒ ░░ ░░   ░ ▒░
░  ░  ░    ░   ▒    ░        ░   ▒      ░   ░ ░ 
      ░        ░  ░              ░  ░         ░ 
                                                
                                       
        """
        print(Colorate.Horizontal(Colors.red_to_black, Center.XCenter(banner)))
        print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter("Satan Multi | Open Source\n")))
        
    def set_token(self):
        self.token = input(f"{Fore.RED}Enter Discord Token: {Style.RESET_ALL}")
        self.headers['Authorization'] = self.token
        
    def set_bot_token(self):
        self.bot_token = input(f"{Fore.RED}Enter Bot Token: {Style.RESET_ALL}")
        
    def set_webhook(self):
        self.webhook_url = input(f"{Fore.RED}Enter Webhook URL: {Style.RESET_ALL}")
        
    def token_info(self):
        try:
            r = self.session.get('https://discord.com/api/v9/users/@me', headers=self.headers)
            if r.status_code == 200:
                user = r.json()
                print(f"\n{Fore.GREEN}Token Information:{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Username: {user['username']}#{user['discriminator']}")
                print(f"Email: {user['email']}")
                print(f"Phone: {user['phone']}")
                print(f"ID: {user['id']}")
                print(f"2FA Enabled: {user['mfa_enabled']}")
                print(f"Verified: {user['verified']}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Invalid Token!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def token_nuker(self, server_id):
        try:
            guild = discord.Guild(id=server_id)
            for channel in guild.channels:
                channel.delete()
            for role in guild.roles:
                role.delete()
            for emoji in guild.emojis:
                emoji.delete()
            print(f"{Fore.GREEN}Successfully nuked server!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def token_joiner(self, invite_code):
        try:
            r = self.session.post(f'https://discord.com/api/v9/invites/{invite_code}', headers=self.headers)
            if r.status_code == 200:
                print(f"{Fore.GREEN}Successfully joined server!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Failed to join server!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def token_leaver(self, server_id):
        try:
            r = self.session.delete(f'https://discord.com/api/v9/users/@me/guilds/{server_id}', headers=self.headers)
            if r.status_code == 204:
                print(f"{Fore.GREEN}Successfully left server!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Failed to leave server!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def token_login(self):
        try:
            client = discord.Client()
            @client.event
            async def on_ready():
                print(f"{Fore.GREEN}Logged in as {client.user.name}#{client.user.discriminator}{Style.RESET_ALL}")
                await client.close()
            client.run(self.token, bot=False)
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def token_to_id(self):
        try:
            r = self.session.get('https://discord.com/api/v9/users/@me', headers=self.headers)
            if r.status_code == 200:
                user = r.json()
                print(f"\n{Fore.GREEN}User ID: {user['id']}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Invalid Token!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def token_server_raid(self, server_id, message, amount):
        try:
            guild = discord.Guild(id=server_id)
            for i in range(int(amount)):
                for channel in guild.text_channels:
                    channel.send(message)
            print(f"{Fore.GREEN}Successfully raided server!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def token_spammer(self, user_id, message, amount):
        try:
            user = discord.User(id=user_id)
            for i in range(int(amount)):
                user.send(message)
            print(f"{Fore.GREEN}Successfully spammed user!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def token_delete_friends(self):
        try:
            r = self.session.get('https://discord.com/api/v9/users/@me/relationships', headers=self.headers)
            if r.status_code == 200:
                friends = r.json()
                for friend in friends:
                    self.session.delete(f'https://discord.com/api/v9/users/@me/relationships/{friend["id"]}', headers=self.headers)
                print(f"{Fore.GREEN}Successfully deleted all friends!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Failed to get friends list!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def token_block_friends(self):
        try:
            r = self.session.get('https://discord.com/api/v9/users/@me/relationships', headers=self.headers)
            if r.status_code == 200:
                friends = r.json()
                for friend in friends:
                    self.session.put(f'https://discord.com/api/v9/users/@me/relationships/{friend["id"]}', 
                                    json={'type': 2}, headers=self.headers)
                print(f"{Fore.GREEN}Successfully blocked all friends!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Failed to get friends list!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def token_mass_dm(self, message):
        try:
            r = self.session.get('https://discord.com/api/v9/users/@me/channels', headers=self.headers)
            if r.status_code == 200:
                channels = r.json()
                for channel in channels:
                    if channel['type'] == 1:
                        self.session.post(f'https://discord.com/api/v9/channels/{channel["id"]}/messages', 
                                        json={'content': message}, headers=self.headers)
                print(f"{Fore.GREEN}Successfully sent mass DM!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Failed to get channels!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def token_delete_dm(self):
        try:
            r = self.session.get('https://discord.com/api/v9/users/@me/channels', headers=self.headers)
            if r.status_code == 200:
                channels = r.json()
                for channel in channels:
                    if channel['type'] == 1:
                        self.session.delete(f'https://discord.com/api/v9/channels/{channel["id"]}', headers=self.headers)
                print(f"{Fore.GREEN}Successfully deleted all DMs!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Failed to get channels!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def token_status_changer(self, status):
        try:
            custom_status = {"custom_status": {"text": status}}
            r = self.session.patch('https://discord.com/api/v9/users/@me/settings', 
                                 json=custom_status, headers=self.headers)
            if r.status_code == 200:
                print(f"{Fore.GREEN}Successfully changed status!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Failed to change status!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def token_language_changer(self, language):
        try:
            payload = {"locale": language}
            r = self.session.patch('https://discord.com/api/v9/users/@me/settings', 
                                 json=payload, headers=self.headers)
            if r.status_code == 200:
                print(f"{Fore.GREEN}Successfully changed language!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Failed to change language!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def token_house_changer(self, house):
        try:
            payload = {"house": house}
            r = self.session.patch('https://discord.com/api/v9/users/@me/hypesquad', 
                                 json=payload, headers=self.headers)
            if r.status_code == 204:
                print(f"{Fore.GREEN}Successfully changed HypeSquad house!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Failed to change HypeSquad house!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def token_theme_changer(self, theme):
        try:
            payload = {"theme": theme}
            r = self.session.patch('https://discord.com/api/v9/users/@me/settings', 
                                 json=payload, headers=self.headers)
            if r.status_code == 200:
                print(f"{Fore.GREEN}Successfully changed theme!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Failed to change theme!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def token_generator(self, amount):
        try:
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            for i in range(int(amount)):
                token = ""
                for x in range(59):
                    token += random.choice(chars)
                print(f"{Fore.GREEN}{token}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def bot_server_nuker(self, server_id):
        try:
            bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
            @bot.event
            async def on_ready():
                guild = bot.get_guild(int(server_id))
                for channel in guild.channels:
                    await channel.delete()
                for role in guild.roles:
                    try:
                        await role.delete()
                    except:
                        pass
                for emoji in guild.emojis:
                    await emoji.delete()
                print(f"{Fore.GREEN}Successfully nuked server!{Style.RESET_ALL}")
                await bot.close()
            bot.run(self.bot_token)
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def bot_invite_to_id(self, invite_code):
        try:
            r = self.session.get(f'https://discord.com/api/v9/invites/{invite_code}')
            if r.status_code == 200:
                data = r.json()
                print(f"\n{Fore.GREEN}Invite Information:{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Server ID: {data['guild']['id']}")
                print(f"Server Name: {data['guild']['name']}")
                print(f"Channel ID: {data['channel']['id']}")
                print(f"Channel Name: {data['channel']['name']}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Invalid Invite Code!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def webhook_info(self):
        try:
            webhook = SyncWebhook.from_url(self.webhook_url)
            info = webhook.fetch()
            print(f"\n{Fore.GREEN}Webhook Information:{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Name: {info.name}")
            print(f"ID: {info.id}")
            print(f"Channel ID: {info.channel_id}")
            print(f"Guild ID: {info.guild_id}")
            print(f"Avatar URL: {info.avatar_url}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def webhook_delete(self):
        try:
            webhook = SyncWebhook.from_url(self.webhook_url)
            webhook.delete()
            print(f"{Fore.GREEN}Successfully deleted webhook!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def webhook_spammer(self, message, amount):
        try:
            webhook = SyncWebhook.from_url(self.webhook_url)
            for i in range(int(amount)):
                webhook.send(message)
            print(f"{Fore.GREEN}Successfully spammed webhook!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def webhook_generator(self, server_id, channel_id, name):
        try:
            url = f"https://discord.com/api/v9/channels/{channel_id}/webhooks"
            payload = {"name": name}
            r = self.session.post(url, json=payload, headers=self.headers)
            if r.status_code == 200:
                data = r.json()
                print(f"\n{Fore.GREEN}Webhook Created:{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Name: {data['name']}")
                print(f"URL: {data['url']}")
                print(f"Token: {data['token']}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Failed to create webhook!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def server_info(self, server_id):
        try:
            r = self.session.get(f'https://discord.com/api/v9/guilds/{server_id}', headers=self.headers)
            if r.status_code == 200:
                server = r.json()
                print(f"\n{Fore.GREEN}Server Information:{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Name: {server['name']}")
                print(f"ID: {server['id']}")
                print(f"Owner ID: {server['owner_id']}")
                print(f"Member Count: {server['member_count']}")
                print(f"Verification Level: {server['verification_level']}")
                print(f"Premium Tier: {server['premium_tier']}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Invalid Server ID!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def nitro_generator(self, amount):
        try:
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            for i in range(int(amount)):
                code = ""
                for x in range(16):
                    code += random.choice(chars)
                print(f"https://discord.gift/{code}")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            
    def menu(self):
        self.banner()
        print(f"{Fore.RED}1. Token Tools")
        print(f"2. Bot Tools")
        print(f"3. Webhook Tools")
        print(f"4. Server Tools")
        print(f"5. Nitro Tools")
        print(f"0. Exit{Style.RESET_ALL}")
        
        choice = input(f"\n{Fore.YELLOW}Select an option: {Style.RESET_ALL}")
        
        if choice == "1":
            self.token_menu()
        elif choice == "2":
            self.bot_menu()
        elif choice == "3":
            self.webhook_menu()
        elif choice == "4":
            self.server_menu()
        elif choice == "5":
            self.nitro_menu()
        elif choice == "0":
            exit()
        else:
            print(f"{Fore.RED}Invalid option!{Style.RESET_ALL}")
            time.sleep(1)
            self.menu()
            
    def token_menu(self):
        self.banner()
        print(f"{Fore.RED}Token Tools:{Style.RESET_ALL}")
        print(f"1. Set Token")
        print(f"2. Token Info")
        print(f"3. Token Nuker")
        print(f"4. Token Joiner")
        print(f"5. Token Leaver")
        print(f"6. Token Login")
        print(f"7. Token To ID")
        print(f"8. Token Server Raid")
        print(f"9. Token Spammer")
        print(f"10. Token Delete Friends")
        print(f"11. Token Block Friends")
        print(f"12. Token Mass DM")
        print(f"13. Token Delete DM")
        print(f"14. Token Status Changer")
        print(f"15. Token Language Changer")
        print(f"16. Token House Changer")
        print(f"17. Token Theme Changer")
        print(f"18. Token Generator")
        print(f"0. Back to Main Menu{Style.RESET_ALL}")
        
        choice = input(f"\n{Fore.YELLOW}Select an option: {Style.RESET_ALL}")
        
        if choice == "1":
            self.set_token()
            self.token_menu()
        elif choice == "2":
            self.token_info()
            input(f"\n{Fore.YELLOW}Press enter to continue...{Style.RESET_ALL}")
            self.token_menu()
        elif choice == "3":
            server_id = input(f"{Fore.RED}Enter Server ID: {Style.RESET_ALL}")
            self.token_nuker(server_id)
            input(f"\n{Fore.YELLOW}Press enter to continue...{Style.RESET_ALL}")
            self.token_menu()
        # ... (similar implementation for other token options)
        elif choice == "0":
            self.menu()
        else:
            print(f"{Fore.RED}Invalid option!{Style.RESET_ALL}")
            time.sleep(1)
            self.token_menu()
            
    def bot_menu(self):
        self.banner()
        print(f"{Fore.RED}Bot Tools:{Style.RESET_ALL}")
        print(f"1. Set Bot Token")
        print(f"2. Bot Server Nuker")
        print(f"3. Bot Invite To ID")
        print(f"0. Back to Main Menu{Style.RESET_ALL}")
        
        choice = input(f"\n{Fore.YELLOW}Select an option: {Style.RESET_ALL}")
        
        if choice == "1":
            self.set_bot_token()
            self.bot_menu()
        elif choice == "2":
            server_id = input(f"{Fore.RED}Enter Server ID: {Style.RESET_ALL}")
            self.bot_server_nuker(server_id)
            input(f"\n{Fore.YELLOW}Press enter to continue...{Style.RESET_ALL}")
            self.bot_menu()
        elif choice == "3":
            invite_code = input(f"{Fore.RED}Enter Invite Code: {Style.RESET_ALL}")
            self.bot_invite_to_id(invite_code)
            input(f"\n{Fore.YELLOW}Press enter to continue...{Style.RESET_ALL}")
            self.bot_menu()
        elif choice == "0":
            self.menu()
        else:
            print(f"{Fore.RED}Invalid option!{Style.RESET_ALL}")
            time.sleep(1)
            self.bot_menu()
            
    def webhook_menu(self):
        self.banner()
        print(f"{Fore.RED}Webhook Tools:{Style.RESET_ALL}")
        print(f"1. Set Webhook URL")
        print(f"2. Webhook Info")
        print(f"3. Webhook Delete")
        print(f"4. Webhook Spammer")
        print(f"5. Webhook Generator")
        print(f"0. Back to Main Menu{Style.RESET_ALL}")
        
        choice = input(f"\n{Fore.YELLOW}Select an option: {Style.RESET_ALL}")
        
        if choice == "1":
            self.set_webhook()
            self.webhook_menu()
        elif choice == "2":
            self.webhook_info()
            input(f"\n{Fore.YELLOW}Press enter to continue...{Style.RESET_ALL}")
            self.webhook_menu()
        elif choice == "3":
            self.webhook_delete()
            input(f"\n{Fore.YELLOW}Press enter to continue...{Style.RESET_ALL}")
            self.webhook_menu()
        elif choice == "4":
            message = input(f"{Fore.RED}Enter Message: {Style.RESET_ALL}")
            amount = input(f"{Fore.RED}Enter Amount: {Style.RESET_ALL}")
            self.webhook_spammer(message, amount)
            input(f"\n{Fore.YELLOW}Press enter to continue...{Style.RESET_ALL}")
            self.webhook_menu()
        elif choice == "5":
            server_id = input(f"{Fore.RED}Enter Server ID: {Style.RESET_ALL}")
            channel_id = input(f"{Fore.RED}Enter Channel ID: {Style.RESET_ALL}")
            name = input(f"{Fore.RED}Enter Webhook Name: {Style.RESET_ALL}")
            self.webhook_generator(server_id, channel_id, name)
            input(f"\n{Fore.YELLOW}Press enter to continue...{Style.RESET_ALL}")
            self.webhook_menu()
        elif choice == "0":
            self.menu()
        else:
            print(f"{Fore.RED}Invalid option!{Style.RESET_ALL}")
            time.sleep(1)
            self.webhook_menu()
            
    def server_menu(self):
        self.banner()
        print(f"{Fore.RED}Server Tools:{Style.RESET_ALL}")
        print(f"1. Server Info")
        print(f"0. Back to Main Menu{Style.RESET_ALL}")
        
        choice = input(f"\n{Fore.YELLOW}Select an option: {Style.RESET_ALL}")
        
        if choice == "1":
            server_id = input(f"{Fore.RED}Enter Server ID: {Style.RESET_ALL}")
            self.server_info(server_id)
            input(f"\n{Fore.YELLOW}Press enter to continue...{Style.RESET_ALL}")
            self.server_menu()
        elif choice == "0":
            self.menu()
        else:
            print(f"{Fore.RED}Invalid option!{Style.RESET_ALL}")
            time.sleep(1)
            self.server_menu()
            
    def nitro_menu(self):
        self.banner()
        print(f"{Fore.RED}Nitro Tools:{Style.RESET_ALL}")
        print(f"1. Nitro Generator")
        print(f"0. Back to Main Menu{Style.RESET_ALL}")
        
        choice = input(f"\n{Fore.YELLOW}Select an option: {Style.RESET_ALL}")
        
        if choice == "1":
            amount = input(f"{Fore.RED}Enter Amount: {Style.RESET_ALL}")
            self.nitro_generator(amount)
            input(f"\n{Fore.YELLOW}Press enter to continue...{Style.RESET_ALL}")
            self.nitro_menu()
        elif choice == "0":
            self.menu()
        else:
            print(f"{Fore.RED}Invalid option!{Style.RESET_ALL}")
            time.sleep(1)
            self.nitro_menu()

if __name__ == "__main__":
    tool = DiscordMultiTool()
    tool.menu()