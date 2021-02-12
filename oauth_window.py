import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from crypto_helper import CryptoHelper

class OauthWindow(Gtk.Window):
  def __init__(self):
    Gtk.Window.__init__(self, title="OAuth authenticator")

    self.crypto_helper = CryptoHelper()

    builder = Gtk.Builder()
    builder.add_from_file("./main.glade")
    container = builder.get_object("container")
    button = builder.get_object("btn_auth")
    button.connect("clicked", self.print_random)
    self.add(container)

  def print_random(self, widget):
    self.crypto_helper.get_random()
