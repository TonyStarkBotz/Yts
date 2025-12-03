import feedparser
import telebot
import time

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHANNEL = "@yourchannelusername"

bot = telebot.TeleBot(BOT_TOKEN)

RSS_FEEDS = [
    "https://yts.ag/rss/0/720p/all/0/en",
    "https://yts.ag/rss/0/1080p/all/0/en",
    "https://yts.ag/rss/0/720p/all/0/hi",
    "https://yts.ag/rss/0/1080p/all/0/hi",
]

posted = set()

def check():
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)

        for entry in feed.entries:
            link = entry.link

            if link not in posted:
                # Create your custom message
                msg = f"/qbl {link}\nTag: @PeTeRIsMaaLiK 838364275"

                # Send to channel
                bot.send_message(CHANNEL, msg)

                # Mark as posted to avoid duplicate uploads
                posted.add(link)


# Real-time loop: checks feed every 1 second
while True:
    check()
    time.sleep(1)
