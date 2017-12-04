import os
import time
from slackclient import SlackClient 
import random

# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID") 

# constants
AT_BOT = "<@" + BOT_ID + ">" 
EXAMPLE_COMMAND = "do" 
BOKBOT = "bokbot" 
CHOBOT = "schedule" 
BABOT = "hungry" 
STARTER = "starter" 

# instantiate Slack & Twilio clients

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN')) 

def bokbot(command,channel):
     slack_client.api_call("chat.postMessage", channel=channel, 
                          text=response, as_user=True)


def chobot(command,channel):
    year=int(input("Input year:"))
	month=int(input("Input month:"))
	day=int(input("Input day:"))
	hour=int(input("Input hour:"))
	minute=int(input("Input minute:"))

	month_days=[0,31,28,31,30,31,30,31,30,31,30,31,30]
	total=0;

	for year_i in range(1,year):
		total=total+365

		if year_i%400==0:
	        total=total+1 #윤년=366일
	    elif year_i%100==0:
	        pass
	    elif year_i%4==0:
	        total=total+1 #윤년
	    else:
	        pass

	for month_i in range(1,month):
    	total=total+month_days[month_i]

	total=total+day #00년도 00월 00일을 일(day)로 표현

	if total%7==0: #SUN
		if hour<=8:
			response='sleeping...'
		else:
			response='taking a rest...'
    elif total%7==1: #MON
		if hour<=8:
			response='sleeping...'
		else:
			response='taking a rest...'
	elif total%7==2: #TUE
		if hour<=8:
			response='sleeping...'
		else:
			response='taking a rest...'
	elif total%7==3: #WED
		if hour<=8:
			response='sleeping...'
		else:
			response='taking a rest...'
	elif total%7==4: #THU
		if hour<=8:
			response='sleeping...'
		else:
			response='taking a rest...'
	elif total%7==5: #FRI
		if hour<=8:
			response='sleeping...'
		else:
			response='taking a rest...'    
	elif total%7==6: #SAT
		if hour<=8:
			response='sleeping...'
		else:
			response='taking a rest...'

	slack_client.api_call("chat.postMessage", channel=channel, 
                          text=response, as_user=True)

def babot(command,channel):
     lunchlist=['pasta','bibimbab','school food','sushi','bulgogi','pizza','hamberger','sandwich','kimchijjigae','haejangguk','doenjangjjigae','ssalguksu','galbitang','tteokbokki','gimbab','ramen','jajangmyeon','jjamppong','kimchi fried rice','naengmyeon','japaness rice served with toppings','pork cutlet','dakgalbi','chicken','convenience store food']               
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
