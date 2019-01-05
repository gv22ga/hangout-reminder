# script to send automated remainder every week at a specific time on an already existing hangout group

# script taken from https://gist.github.com/tdryer/0cf6903eeb3dc948bae0
# changed it a bit to work with multiline messages and add scheduling

import time
import schedule
import asyncio
import hangups

# oauth token
# try 'hangups --token-path=refresh_token.txt --manual-login' and follow the instructions
REFRESH_TOKEN_PATH = 'refresh_token.txt'

# hangout conversation id
# try hangups with debug mode, you can find the conversation id in log file
# 'hangups --token-path=refresh_token.txt --log log --debug'
CONVERSATION_ID = '<HANGOUT_CONVERSATION_ID>'

# message to send
MESSAGE = 'automated remainder \U0001f60e \n <b>#FridayLunch</b> \n say no to cook'


@asyncio.coroutine
def send_message(client):
	request = hangups.hangouts_pb2.SendChatMessageRequest(
		request_header=client.get_request_header(),
		event_request_header=hangups.hangouts_pb2.EventRequestHeader(
			conversation_id=hangups.hangouts_pb2.ConversationId(
				id=CONVERSATION_ID
			),
			client_generated_id=client.get_client_generated_id(),
		),
		message_content=hangups.hangouts_pb2.MessageContent(
			segment=[obj.serialize() for obj in hangups.ChatMessageSegment.from_str(MESSAGE)],
		),
	)
	yield from client.send_chat_message(request)
	yield from client.disconnect()


def remind():
	cookies = hangups.auth.get_auth_stdin(REFRESH_TOKEN_PATH)
	client = hangups.Client(cookies)
	client.on_connect.add_observer(lambda: asyncio.async(send_message(client)))
	loop = asyncio.get_event_loop()
	loop.run_until_complete(client.connect())


if __name__ == '__main__':
	schedule.every().thursday.at("12:30").do(remind) # time in UTC
	print('started')
	while True:
		schedule.run_pending()
		time.sleep(60) # wait one minute
