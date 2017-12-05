import os
import time
from slackclient import SlackClient 
import random

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
     
     #temp=input("오늘의 기온을 입력해주세요(섭씨온도(℃): ")
     temp=10
     if temp >= 27:
          response = "오늘은 나시티, 반팔 티셔츠, 반바지, 민소매 옷을 입기에 적절한 날이네요! :)"
     elif temp >= 23 and temp < 27:
          response = "오늘은 반팔, 얇은 셔츠, 얇은 긴팔, 반바지, 면바지를 입기에 적절한 날이네요~ :)"
     elif temp >= 20 and temp < 23:
          response = "오늘은 긴팔티, 가디건, 얇은 후드티, 면바지, 슬랙스, 스키니 등을 입기에 적절한 날이네요!"
     elif temp >= 17 and temp < 20:
          response = "얇은 니트, 가디건, 후드티나 맨투맨과 청바지, 면바지, 슬랙스 등을 매치해서 입으면 좋을 날이에요 ^ㅠ^"
     elif temp >= 12 and temp < 17:
          response = "자켓, 셔츠 가디건이나 야상 같은 겉옷을 챙기시면 좋을 날이에요!"
     elif temp >= 6 and temp < 9:
          response = "코트나 가죽자켓 같은 겉옷에 맨투맨, 니트, 후드티 등을 속에 입으면 적당할 날이에요!"
     elif temp < 6:
          response = "패딩 같은 두꺼운 겉옷에 장갑, 목도리도 착용해야 될 날이에요! 읏추읏추~"
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
