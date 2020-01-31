import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

class PasswordWindow():
    def __init__(self, title='Password Authenticator', msg='Authentification required', first_prompt=True):
        # Load glade layout file
        builder = Gtk.Builder()
        builder.add_from_file('/home/thomas/Git/os-tools/auth/auth.glade')
    
        # Get UI elements
        self.window = builder.get_object('window')
        self.proceed_btn = builder.get_object('proceed_btn')
        self.cancel_btn = builder.get_object('cancel_btn')
        self.pw_label = builder.get_object('pw_label')
        self.pw_entry = builder.get_object('pw_entry')
        self.msg_label = builder.get_object('msg_label')

        # Register events
        self.window.connect("destroy", Gtk.main_quit)
        self.proceed_btn.connect('pressed', self.proceed_btn_pressed)
        self.cancel_btn.connect('pressed', self.cancel_btn_pressed)
        self.pw_entry.connect('activate', self.pw_entry_activate)

        self.window.set_title(title)
        self.msg_label.set_text(msg)
        self.pw_label.set_text('Enter Password:' if first_prompt else 'Re-enter Password:')

        # Load CSS
        self.load_css()

        # Result
        self.result = None

    def load_css(self):
        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        provider.load_from_path('/home/thomas/Git/os-tools/auth/design.css')
        Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def pw_entry_activate(self, widget):
        self.proceed_btn.pressed()

    def proceed_btn_pressed(self, widget):
        self.result = self.pw_entry.get_text()
        self.window.close()

    def cancel_btn_pressed(self, widget):
        self.window.close()

    def ask(self) -> str:
        self.window.show_all()
        Gtk.main()
        return self.result