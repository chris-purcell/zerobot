#!/usr/bin/env python

# Import required modules
import os, requests, time, yaml
from slackclient import SlackClient
from bs4 import BeautifulSoup
from modules import *

# Read configuration variables for Slack login
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
def do_intro():
    channel = '#ring_zero'
    response = "Zerobot connected and running! Type !commands for a list of available commands."
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)
def qwatch():
    channel = '#ring_zero'
    while True:
        data = []
        source = requests.get("http://qwatch.it.rackspace.com").text
        soup = BeautifulSoup(source, 'html.parser')
        table = soup.find('table')
        x = (len(table.find_all('tr')))
        for row in table.find_all('tr')[1:x]:
            col = row.find_all('td')
            name = col[0].getText()
            ticket = 'https://core.rackspace.com/ticket/' + col[1].getText() + "\n"
            if 'windows' in name:
                pass
            else:
                data.append(name.capitalize())
                data.append(ticket)
        response = "Pending SLA Violation tickets:\n" + (' '.join('{}'.format(k) for i,k in enumerate(data)))
        slack_client.api_call("chat.postMessage", channel=channel,
                              text=response, as_user=True)
        time.sleep(300)

def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    possibles = []
    path = os.getcwd()
    filenames = os.listdir(path + "/modules/")
    for filename in filenames:
        if filename.endswith('.py') and not filename.startswith("_"):
            filename = filename.split('.')[0]
            possibles.append(filename)

    response = ''
    if command.startswith(EXAMPLE_COMMAND):
        if command.strip("!") in possibles:
            mypackage = __import__('modules')
            mymodule = getattr(mypackage, command.strip("!"))
            myfunction = getattr(mymodule, command.strip("!"))
            response = myfunction()

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
            if output and 'text' in output and output['text'].startswith("!"):
                return output['text'].lower(), \
                       output['channel']
    return None, None

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 0.1 # 1/10th second delay between reading from firehose
    if slack_client.rtm_connect():
        print("Zerobot connected and running!")
        do_intro()
#        qwatch()
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")

