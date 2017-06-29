#!/usr/bin/env python

import os
import time
import yaml
from slackclient import SlackClient
from modules.weather import weather as weather

with open("credentials", "r") as f:
    cfg = yaml.safe_load(f)

# Zerobot's ID
BOT_ID = cfg["bot_id"]

# Instantiate Slack client
slack_client = SlackClient(cfg["api_token"])

# Constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "!"

# Functions, commands to do stuff with the bot
def commands():
    return """
Available commands:
!commands - This output.
!weather - Get the current weather in the area of the Castle.
"""

"""
def weather():
    result = requests.get("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=0&locCode=78239")
    result.status_code
    c = result.content
    doc = ET.fromstring(c)
    for item in doc.xpath('//item'):
        for elt in item.xpath('descendant::*'):
            if "Currently:" in ET.tostring(elt):
                str = ET.tostring(elt)
                str = str.replace('<title>Currently: ','')
                str = str.replace('</title>','')
                return "The weather is currently " + str
"""

# Bot logic
def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."
    if command.startswith(EXAMPLE_COMMAND):
        if command == '!commands':
            response = commands()
        if command == '!weather':
            response = weather()
    else:
        response = "!foaas RingZeroBot"
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)

def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        This parsing function returns None unless a message is
        directed at the Zerobot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
            # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 0.5 # 1/2 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("Zerobot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")

