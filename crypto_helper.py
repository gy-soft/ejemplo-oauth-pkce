from Crypto.Random.random import StrongRandom
from Crypto.Hash.SHA256 import SHA256Hash
from base64 import urlsafe_b64encode as b64encode
import webbrowser

class CryptoHelper():
  def __init__(self):
    self.rnd = StrongRandom()

  def get_code(self):
    mapped = map(lambda x: self.rnd.getrandbits(8), range(32))
    encoded = b64encode(bytes(mapped))
    verifier = encoded.decode().replace("=", "")
    hash = SHA256Hash.new(self)
    hash.update(verifier.encode("utf-8"))
    digest = b64encode(hash.digest())
    challenge = digest.decode().replace("=", "")
    return {
      "verifier": verifier,
      "challenge": challenge
    }
