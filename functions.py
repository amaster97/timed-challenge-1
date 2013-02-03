import requests
import ast

def post_message(from_username, to_username, message):
  r = requests.post('http://amizra.pythonanywhere.com/postmsg', data={'from_username': from_username, 'to_username': to_username, 'message': message})
	if r._content == 'Post msg':
		print 'Message sent.'
	else:
		print 'An error occurred on the message server.'
	
def get_messages(username):
	r = requests.get('http://amizra.pythonanywhere.com/getmsg?username=%s' % username)
	messages = ast.literal_eval(r._content)
	print "You have %d new %s." % (len(messages), "message" if len(messages)==1 else "messages")
	for message in messages:
		from_username = message['from_username']
		content = message['content']
		print '%s says... %s' % (from_username, content)
