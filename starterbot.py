import os
import time
from slackclient import SlackClient 
import random
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import yaml

# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID") 

# constants
AT_BOT = "<@" + "U8ADY32F6" + ">" 
#EXAMPLE_COMMAND = "do" 
WEATHER = "weather" 
SCHEDULE = "schedule" 
HUNGRY = "hungry" 

# instantiate Slack & Twilio clients

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN')) 

def weather(command,channel):
	url="https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&q=%EA%B4%91%EC%A7%84%EA%B5%AC+%EB%82%A0%EC%94%A8"
	res=requests.get(url)
	Soup=BeautifulSoup(res.text,'html.parser')
	nav=Soup.find("strong",{'class':'txt_temp'})
	str=nav.get_text()
	response = "The temperature is now " + str+"\n"
	t=str.split('℃')	
	temp=int(t[0])
	if (temp >= 27):
		response += "Today you should wear a short-sleeve t-shirt, tanktop, sleevless shirt, and shorts. It is a hot day"
	elif temp >= 23 and temp < 27:
		response += "Today you should wear a short-sleeve shirt, t-shirt, shorts, and cotton pants. It's going to be a warm, or maybe even a hot day."
	elif temp >= 20 and temp < 23:
		response += "Recommendations for you clothes are long-sleeved shirt, cardigans, thin hoodies, cotton pants, jeans, or trousers."
	elif temp >= 17 and temp < 20:
		response += "A thin sweater, cardigan, hoodies with jeans, cotton pants, or trousers would do good today! :)"
	elif temp >= 12 and temp < 17:
		response += "Outers such as a jacket, or a cardigan would come in handy ^^"
	elif temp >= 6 and temp < 9:
		response += "Today a thick hoodie, sweater, coat, leather jackets, and jeans would be suitable. Watch out for the coldness *0*"
	elif temp < 6:
		response += "Thick clothings are strongly recommended.. Wear a scarf and gloves as well."
	slack_client.api_call("chat.postMessage", channel=channel,text=response, as_user=True)
          
     

def scheduler(command,channel):

	today_y=datetime.today().year 
	today_m=datetime.today().month 
	today_d=datetime.today().day
	today_h=datetime.today().hour
	today_min=datetime.today().minute   # NOW TIME

	month_days=[0,31,28,31,30,31,30,31,30,31,30,31,30]
	total=0;

	for year_i in range(1,today_y): #leap year
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
		total=total+month_days[month_i] # total day

	total=total+today_d
	total_min=today_h*60+today_min # total time [per minute]

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

	slack_client.api_call("chat.postMessage", channel=channel,text=response, as_user=True)

def lunch(command,channel):
	if command.startswith(HUNGRY):
		lunchlist=['파스타','치킨','초밥','고기','곱창','떡볶이','회','빵','만두','족발','냉면','국밥','돈가스','중식','라면','불고기']
		lunch=lunchlist[random.randint(0,len(lunchlist)-1)]
		a="https://m.store.naver.com/sogum/api/businesses?filterId=s11591591&query=세종대%20"
		b="&searchQuery=세종대%20맛집&x=126.9783880&y=37.5666100&display=1&deviceType=mobile"
		url=a+lunch+b
		q="&start="
		command={}		
		for i in range(1,20):
			query=url+q+str(i)
			
			res=requests.get(query)
			
			info=res.text
			info_rast=yaml.load(info)

			try :
				name=((info_rast['items'][0])['name']).replace("'","\'")
				category=((info_rast['items'][0])['category']).replace("'","\'")

			except :
				#name=((info_rast['items'][0])['name']).replace("'","\'")
				#category=((info_rast['items'][0])['category']).replace("'","\'")
				name=""
				category=""			

			if((info).find('"total":0')>1):
				break

			command[name]=category
		
		response="I recommend"+" "+lunch+"\n"
		for name,category in command.items():
			response+=name+"("+category+")"+"\n"

		slack_client.api_call("chat.postMessage", channel=channel,text=response, as_user=True)

def exception(command,channel):
	response="If you want recommendations on your clothings according to the weather, type in 'weather'."+"\n"+"If you want recommendations on what to eat and where to go to eat that food, type in 'hungry'."+"\n"+"If you are curious about what you're teammates are doing right now, type in 'schedule'."
	slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)

def handle_command(command, channel): 
	if command.startswith(WEATHER): 
		weather(command,channel)
	elif command.startswith(SCHEDULE):
		scheduler(command,channel)
	elif command.startswith(HUNGRY):
		lunch(command,channel)
	else:
		exception(command,channel)
    



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
