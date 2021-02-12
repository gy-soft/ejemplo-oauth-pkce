from Crypto.Random.random import StrongRandom
import base64
import webbrowser

OAUTH_HOST = "https://www.dropbox.com/oauth2/authorize"
CLIENT_ID = "tpr1swzr3p44n26"

def get_url():
  "{}?"
  return OAUTH_HOST + 

class CryptoHelper():
  def __init__(self):
    self.rnd = StrongRandom()

  def get_random(self):
    mapped = map(lambda x: self.rnd.getrandbits(8), range(32))
    encoded = base64.b64encode(bytes(mapped))
    webbrowser.open()
    print(str(encoded))
