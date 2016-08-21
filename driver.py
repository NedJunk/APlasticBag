import tweepy, time, sys, yaml, json


class Bot(object):
	"""docstring for Bot"""
	def __init__(self):
		super(Bot, self).__init__()
		self.creds = None
		self.api = self.load_api()
		
	def load_api(self):
		with open('credentials.yaml', 'r') as f:
			self.creds = yaml.load(f)
			auth = tweepy.OAuthHandler(self.creds['CONSUMER_KEY'], self.creds['CONSUMER_SECRET'])
			auth.set_access_token(self.creds['ACCESS_TOKEN'], self.creds['ACCESS_TOKEN_SECRET'])
			return tweepy.API(auth)

	def tweet(self):
		question = self.pop_question()
		self.api.update_status(question)

	def pop_question(self):
		with open('questions.txt', 'r+') as f:
			questions = f.readlines()
			q = questions[0]
			f.seek(0)
			f.truncate()
			f.writelines(questions[1:])
			return q.strip()

	def get_my_tweets(self):
		return [status._json for status in tweepy.Cursor(self.api.user_timeline).items()]

	def get_my_tweet(self, status_id):
		for s in self.get_my_tweets():
			if s['id'] == status_id:
				print(s['id'])
				# return s

	def get_response_to(self, status_id):
		for m in self.get_my_mentions():
			if m['in_reply_to_status_id'] == status_id:
				print(m['text'])

	def get_my_mentions(self):
		return [mention._json for mention in tweepy.Cursor(self.api.mentions_timeline).items()]


	def test(self):
		# print('++++++++++')
		# print(self.api)
		# print('++++++++++')
		# for k, v in self.creds.items():
		# 	print(k, v)

		# self.tweet()
		# print([tweet['id'] for tweet in self.get_my_tweets()])
		# print(self.get_my_tweet(767443708417486848)['text'])
		self.get_response_to(767442132546170881)


def main():
	bot = Bot()
	bot.test()

if __name__ == '__main__':
	main()