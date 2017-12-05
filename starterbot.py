import os
import time
from slackclient import SlackClient 
import random
import requests
from bs4 import BeautifulSoup

# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID") 

# constants
AT_BOT = "<@" + BOT_ID + ">" 
EXAMPLE_COMMAND = "do" 
BOKBOT = "weather" 
CHOBOT = "chobot" 
BABOT = "hungry" 
STARTER = "starter" 

# instantiate Slack & Twilio clients

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN')) 

def bokbot(command,channel):
     url="https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&q=%EA%B4%91%EC%A7%84%EA%B5%AC+%EB%82%A0%EC%94%A8"
     res=requests.get(url)
     Soup=BeautifulSoup(res.text,'html.parser')
     nav=Soup.find("strong",{'class':'txt_temp'})
     str=nav.get_text()
     t=str[0]
     temp=int(t)
     if temp >= 27:
	  response = "Today you should wear a short-sleeve t-shirt, tanktop, sleevless shirt, and shorts. It is a hot day *.*"

     elif temp >= 23 and temp < 27:
          response = "Today you should wear a short-sleeve shirt, t-shirt, shorts, and cotton pants. It's going to be a warm, or maybe even a hot day."
     elif temp >= 20 and temp < 23:
          response = "Recommendations for you clothes are long-sleeved shirt, cardigans, thin hoodies, cotton pants, jeans, or trousers."
     elif temp >= 17 and temp < 20:
          response = "A thin sweater, cardigan, hoodies with jeans, cotton pants, or trousers would do good today! :)"
     elif temp >= 12 and temp < 17:
          response = "Outers such as a jacket, or a cardigan would come in handy ^^"
     elif temp >= 6 and temp < 9:
          response = "Today a thick hoodie, sweater, coat, leather jackets, and jeans would be suitable. Watch out for the coldness *0*"
     elif temp < 6:
          response = "Thick clothings are strongly recommended.. Wear a scarf and gloves as well."
     slack_client.api_call("chat.postMessage", channel=channel, 
                          text=response, as_user=True)
          
     

def chobot(command,channel):
     slack_client.api_call("chat.postMessage", channel=channel, 
                          text=response, as_user=True)

def babot(command,channel):
     lunchlist=lunchlist=['pasta','bibimbab','school food','sushi','bulgogi','pizza','hamberger','sandwich','kimchijjigae','haejangguk','doenjangjjigae','ssalguksu','galbitang','tteokbokki','gimbab','ramen','jajangmyeon','jjamppong','kimchi fried rice','naengmyeon','japaness rice served with toppings','pork cutlet','dakgalbi','chicken','convenience store food']               
     response='I recommend %s~!' %lunchlist[random.randint(0,len(lunchlist)-1)]
     slack_client.api_call("chat.postMessage", channel=channel, 
                          text=response, as_user=True)

def starter(command,channel):
     slack_client.api_call("chat.postMessage", channel=channel, 
                          text=response, as_user=True)


def handle_command(command, channel): 
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."

    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!" 
    elif command.startswith(BOKBOT): 
        bokbot(command,channel)
    elif command.startswith(CHOBOT):
        chobot(command,channel)
    elif command.startswith(BABOT):
        babot(command,channel)
    elif command.startswith(STARTER):
        starter(command,channel)




def parse_slack_output(slack_rtm_output): 
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
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
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect(): 
        print("StarterBot connected and running!")
        while True: 
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel: 
                handle_command(command, channel) 
            time.sleep(READ_WEBSOCKET_DELAY) 
    else: 
        print("Connection failed. Invalid Slack token or bot ID?")
