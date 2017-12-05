import os
import time
from slackclient import SlackClient 
import random
from datetime import datetime

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
	today_y=datetime.today().year
	today_m=datetime.today().month
	today_d=datetime.today().day
	today_h=datetime.today().hour
	today_min=datetime.today().minute

	month_days=[0,31,28,31,30,31,30,31,30,31,30,31,30]
	total=0;

	for year_i in range(1,today_y):
		total=total+365

		if year_i%400==0:
			total=total+1
		elif year_i%100==0:
			pass
		elif year_i%4==0:
			total=total+1 
		else:
			pass

	for month_i in range(1,today_m):
		total=total+month_days[month_i]

	total=total+today_d 
	total_min=today_h*60+today_min

	if total%7==0: #SUN
		if today_h<8: # 00:00-7:59
			response='sleeping...'
		elif total_min>=570 and total_min<=630: # 9:30-10:30
			response='soyeon=watching TV_animal farm. others=taking a rest...'
		elif today_h==12: # 12:00-12:59
			response='yeongseo=part time job. others=lunch time'
		elif today_h==19: # 19:00-19:59
			response='yeongseo=part time job. others=dinner time'
		elif today_h>=11 and today_h<=21:
			response='yeongseo=part time job. others=taking a rest...'
		else:
			response='taking a rest...'
	elif total%7==1: #MON
		if today_h<8: # 00:00-7:59
			response='sleeping...'
		elif total_min>=540 and total_min<630: # 9:00-10:30
			response='security programming class'
		elif total_min>=630 and total_min<=750: # 10:30-12:30
			response='algorithm and practice'
		elif total_min>=751 and total_min<810: # 12:31-13:29
			response='lunch time'
		elif total_min>=810 and total_min<=1110: # 13:30-18:30
			response='Jiho=part time job. others=taking a rest...'
		elif today_h==19: # 19:00-19:59
			response='dinner time'
		elif today_h==22: # 22:00-22:59
			response='yeongseo=watching drama. others=taking a rest...'
		else:
			response='taking a rest...'
	elif total%7==2: #TUE
		if today_h<8: # 00:00-7:59
			response='sleeping...'
		elif total_min>=540 and total_min<630: # 9:00-10:30
			response='introduction to open source SW class'
		elif total_min>=630 and total_min<=720: # 10:30-12:00
			response='assembly language class'
		elif total_min>=721 and total_min<=780: # 12:01-13:00
			response='lunch time'
		elif today_h==14: # 14:00-14:59
			response='English writing class'
		elif today_h==19: # 19:00-19:59
			response='dinner time'
		elif today_h==22: # 22:00-22:59
			response='yeongseo=watching drama. others=taking a rest...'
		elif today_h==23: # 23:00-23:59
			response="yeongseo=watching TV_KANG's restaurent. others=taking a rest..."
		else:
			response='taking a rest...'
	elif total%7==3: #WED
		if today_h<8: # 00:00-7:59
			response='sleeping...'
		elif total_min>=540 and total_min<630: # 9:00-10:30
			response='security programming class'
		elif total_min>=630 and total_min<=750: # 10:30-12:30
			response='algorithm and practice'
		elif total_min>=751 and total_min<810: # 12:31-13:29
			response='lunch time'
		elif total_min>=810 and total_min<=1110: # 13:30-18:30
			response='Jiho=part time job. others=taking a rest...'
		elif today_h==19: # 7:00-7:59
			response='dinner time'
		else:
			response='taking a rest...'
	elif total%7==4: #THU
		if today_h<8: # 00:00-7:59
			response='sleeping...'
		elif total_min>=540 and total_min<630: # 9:00-10:30
			response='introduction to open source SW class'
		elif total_min>=630 and total_min<=720: # 10:30-12:00
			response='assembly language class'
		elif total_min>=721 and total_min<=780: # 12:01-13:00
			response='lunch time'
		elif today_h==14: # 14:00-14:59
			response='English writing class'
		elif total_min>=900 and total_min<=990: # 3:00-4:30
			response='soyeon,yeongseo=world history class. others=taking a rest...'
		elif today_h==19: # 19:00-19:59
			response='dinner time'
		else:
			response='taking a rest...'
	elif total%7==5: #FRI
		if today_h<8: # 00:00-7:59
			response='sleeping...'
		elif today_h==12: # 12:00-12:59
			response='lunch time'
		elif total_min>=810 and total_min<=1110: # 13:30-18:30
			response='Jiho=part time job. others=taking a rest...'
		elif today_h==19: # 19:00-19:59
			response='dinner time'
		elif today_h==23: # 23:00-23:59
			response='yeongseo=watching TV_I live alone. others=taking a rest...'
		else:
			response='taking a rest...'    
	elif total%7==6: #SAT
		if today_h<8: # 00:00-7:59
			response='sleeping...'
		elif today_h==12: # 12:00-12:59
			response='yeongseo=part time job. others=lunch time'
		elif today_h==19: # 19:00-19:59
			response='yeongseo=part time job. others=dinner time'
		elif today_h>=11 and today_h<=21:
			response='yeongseo=part time job. others=taking a rest...'
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
