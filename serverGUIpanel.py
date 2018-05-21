# -*- coding: utf-8 -*-
try:
    from tkinter import *
except Exception as e:
    logging.info("Error: \"{}\"\n".format(e))
    input(".: END :.")
    exit()

okno = Tk()
okno.title("SERVER GUI PANEL")
okno.geometry("300x200+200+200")

tlacitka = []

tlacitko1 = Button(okno, text="START")
tlacitko1.grid(row=0, column=1)
tlacitka.append(tlacitko1)

tlacitko2 = Button(okno, text="STOP", bg="red")
tlacitko2.grid(row=0, column=2)
tlacitka.append(tlacitko2)

tlacitko3 = Button(okno, text="RESTART")
tlacitko3.grid(row=0, column=3)
tlacitka.append(tlacitko3)

okno.mainloop()

import gi
#gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ButtonWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Button Demo")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button = Gtk.Button.new_with_label("Click Me")
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Open")
        button.connect("clicked", self.on_open_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Close")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

    def on_click_me_clicked(self, button):
        print("\"Click me\" button was clicked")

    def on_open_clicked(self, button):
        print("\"Open\" button was clicked")

    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()

win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()