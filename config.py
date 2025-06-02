import random

# Configure multiple Reddit accounts
class Config:
    accounts = [
        {
            "client_id": "vp6qhCl2yzg8z7AcqD8esg",
            "client_secret": "1xbb9e2uiifYu8wagtzz9X8T9qsMGQ",
            "username": "codej4ckal",
            "password": "jackalbot4148",
        },
        # Add more accounts as needed
        {
            "client_id": "AnotherClientID",
            "client_secret": "AnotherClientSecret",
            "username": "AnotherUsername",
            "password": "AnotherPassword",
        },
    ]

class Botconfig:
    proxies = [
        # Add more proxies as needed
    ]
    
    new_posts = True
    
    # Interval between posts or comments in minutes
    cooldown = 10 
    
    # Set to True if you need to setup webhook for logs
    webhook = ""
    
    discord_webhook = False
     
    # Select purpose of bot: 'ai', 'ad', or 'post'
    type = "ai"
    
    all_subreddits = True
    
    ads = [
        '''
        Advertisement 1: in providing paid hacking services @codej4ckal on tg!
        ''',
        '''
        Advertisement 2: i can teach you hacking and cybersecurity @codej4ckal on tg!
        ''',
        '''
        Advertisement 3: hacking services and teaching available @codej4ckal on tg!
        ''',
    ]
    
    # If set to False, will only post in the specific subreddits
    subreddits = [
        "test",
        "gachagaming",
        "TowerofGod",
    ]

    posts = [
        {"title": "Hey there, upvote for an upvote!", "body": "UPVOTE PLEASE"},
        {"title": "Upvote for upvote, part 2!", "body": "UPVOTE PLEASE"}
    ]
    
    log_file = "commented_posts.txt"

    @staticmethod
    def get_random_proxy():
        if Botconfig.proxies:
            return random.choice(Botconfig.proxies)
        return None
