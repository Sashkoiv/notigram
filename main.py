# import glib
from gi.repository import GLib as glib
import dbus
from dbus.mainloop.glib import DBusGMainLoop
from pprint import pprint as print


def notifications(bus, message):
    print([arg for arg in message.get_args_list()])

DBusGMainLoop(set_as_default=True)

bus = dbus.SessionBus()
bus.add_match_string_non_blocking("""eavesdrop=true,
    interface='org.freedesktop.Notifications',
    member='Notify'""")
bus.add_message_filter(notifications)

mainloop = glib.MainLoop()
mainloop.run()
