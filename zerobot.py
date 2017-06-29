#!/usr/bin/env python

import os
import time
import yaml
from slackclient import SlackClient
from modules import *

with open("credentials", "r") as f:
    cfg = yaml.safe_load(f)

# Zerobot's ID
BOT_ID = cfg["bot_id"]

# Instantiate Slack client
slack_client = SlackClient(cfg["api_token"])

# Constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "!"

# Bot logic
def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Type @zerobot !commands for a list of available commands."
    if command.startswith(EXAMPLE_COMMAND):
        if command == '!commands':
            response = commands.commands()
        if command == '!weather':
            response = weather.weather()
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
    READ_WEBSOCKET_DELAY = 0.1 # 1/2 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("Zerobot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")

