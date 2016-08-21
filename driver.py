import tweepy, time, sys, yaml


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

	def test(self):
		# print('++++++++++')
		# print(self.api)
		# print('++++++++++')
		# for k, v in self.creds.items():
		# 	print(k, v)

		self.tweet()


def main():
	bot = Bot()
	bot.test()

if __name__ == '__main__':
	main()