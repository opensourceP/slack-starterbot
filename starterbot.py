import os
import time
from slackclient import SlackClient #슬랙클라이언트 패키지 


# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID") #봇 아이디

# constants
AT_BOT = "<@" + BOT_ID + ">" 
EXAMPLE_COMMAND = "do" #기본 명령어 do

# instantiate Slack & Twilio clients
#slack_client = "xoxb-279681170305-OHdDBMEgHsrvGkyjmtrVNBEi"
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN')) #봇 토큰으로 슬랙클라이언트 설정

def handle_command(command, channel): #입력한 command 
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    #기본 대답설정
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."

    #압력받은 커멘드가 "do"이면 실행
    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!" #대답 설정
    slack_client.api_call("chat.postMessage", channel=channel, #슬랙 채널에 대답 쓰기
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output): #입력 받은 것으로 채널과 커멘드로 나눠서 반환
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output #입력
    if output_list and len(output_list) > 0: #입력내용이 0보다 커야함
        for output in output_list: 
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel'] ##채널고 텍스트 리턴
    return None, None #없으면 none 


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect(): #연결 성공했을 시에
        print("StarterBot connected and running!") #봇이 연결되었고 러닝중
        while True: 
            command, channel = parse_slack_output(slack_client.rtm_read()) #리턴받은 텍스트와 채널 저장
            if command and channel: 
                handle_command(command, channel) #함수로 보내기
            time.sleep(READ_WEBSOCKET_DELAY) 
    else: #연결 실패
        print("Connection failed. Invalid Slack token or bot ID?")
