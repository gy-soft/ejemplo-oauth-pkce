import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from webbrowser import open as open_browser
import requests
from crypto_helper import CryptoHelper

OAUTH_HOST = "https://www.dropbox.com/oauth2/authorize"
TOKEN_HOST = "https://api.dropbox.com/oauth2/token"
API_HOST = "https://api.dropboxapi.com/2/files/list_folder"
CLIENT_ID = "tpr1swzr3p44n26"
OAUTH_URL = "{0}?client_id={1}&response_type=code&code_challenge_method=S256&code_challenge={2}"
TOKEN_URL = "{0}?client_id={1}&grant_type=authorization_code&code={2}&code_verifier={3}"

class OauthWindow(Gtk.Window):
  def __init__(self):
    Gtk.Window.__init__(self, title="OAuth authenticator")

    self.code_verifier = ""
    self.token = ""
    self.crypto_helper = CryptoHelper()

    builder = Gtk.Builder()
    builder.add_from_file("./main.glade")
    container = builder.get_object("container")
    btn_grantapp = builder.get_object("btn_grantapp")
    btn_grantapp.connect("clicked", self.grant_app)
    btn_gettoken = builder.get_object("btn_gettoken")
    btn_gettoken.connect("clicked", self.generate_token)
    btn_callapi = builder.get_object("btn_callapi")
    btn_callapi.connect("clicked", self.call_api)
    self.txt_authcode = builder.get_object("txt_auth_code")
    self.txt_response = builder.get_object("txt_response")
    self.add(container)

  def grant_app(self, widget):
    code = self.crypto_helper.generate_verifier_code()
    self.code_verifier = code["verifier"]
    auth_url = OAUTH_URL.format(OAUTH_HOST, CLIENT_ID, code["challenge"])
    open_browser(auth_url)

  def generate_token(self, widget):
    oauth_code = self.txt_authcode.get_text()
    params = {
      "client_id": CLIENT_ID,
      "grant_type": "authorization_code",
      "code": oauth_code,
      "code_verifier": self.code_verifier
    }
    response = requests.post(TOKEN_HOST, params)
    json = response.json()
    self.token = json["access_token"]

  def call_api(self, widget):
    json = {
      "path": ""
    }
    headers = {
      "Authorization": "Bearer {0}".format(self.token)
    }
    response = requests.post(API_HOST,headers=headers,json=json)
    json = response.text
    buffer = self.txt_response.get_buffer()
    buffer.set_text(json.replace("{", "{\n").replace("}", "}\n").replace(",", ",\n"))
