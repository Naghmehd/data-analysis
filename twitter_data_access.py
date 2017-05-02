from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

consumer_key        = '1nvYyChmmQB3wXTPZ5MJDQ5qG'
consumer_secret     = 'F8QeWpVHVO5k7jWJzZWQrxHY4ZVBqK28lLKnuLCmrX7hOhG1XZ'
access_token      = 	'631410081-Mp1O4sKpkegQUCfElHA51B6i8e8qOG3ih5SgM0vk'
access_token_secret = 	'hKjarfLPJraLTTyDXjhXPkF7sNO90TWnMpuubTvcmLxha'

auth = OAuthHandler(consumer_key,
                    consumer_secret)
auth.set_access_token(access_token,
                      access_token_secret)

class PrintListener(StreamListener):
    def on_status(self, status):
        if not status.text[:3] == 'RT ':
            print(status.text)
            print(status.author.screen_name,
                  status.created_at,
                  status.source,
                  '\n')

    def on_error(self,status_code):
        print("Error code: {}".format(status_code))
        return True # keep stream alive

    def on_timeout(self):
        print('Listener timed out!')
        return True # Keep stream alive

def print_to_terminal():
    listener = PrintListener()
    stream = Stream(auth, listener)
    languages = ('en',)
    stream.sample(languages=languages)

if __name__ == '__main__':
    print_to_terminal()
