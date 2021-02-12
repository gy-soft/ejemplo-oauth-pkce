import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from oauth_window import OauthWindow

window = OauthWindow()
window.show()
window.connect("destroy", Gtk.main_quit)
Gtk.main()
