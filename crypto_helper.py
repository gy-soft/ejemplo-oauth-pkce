from Crypto.Random.random import StrongRandom
from Crypto.Hash.SHA256 import SHA256Hash
import base64
import webbrowser

OAUTH_HOST = "https://www.dropbox.com/oauth2/authorize"
CLIENT_ID = "tpr1swzr3p44n26"
BASE_URL = "{0}?client_id={1}&response_type=code&code_challenge_method=S256&code_challenge={2}"

def get_url(challenge):
  return BASE_URL.format(OAUTH_HOST, CLIENT_ID, challenge)

class CryptoHelper():
  def __init__(self):
    self.rnd = StrongRandom()

  def get_code(self):
    mapped = map(lambda x: self.rnd.getrandbits(8), range(32))
    encoded = base64.urlsafe_b64encode(bytes(mapped))
    verifier = encoded.decode().replace("=", "")
    hash = SHA256Hash.new(self)
    hash.update(verifier.encode("utf-8"))
    digest = base64.urlsafe_b64encode(hash.digest())
    challenge = digest.decode().replace("=", "")
    return {
      "verifier": verifier,
      "challenge": challenge
    }
