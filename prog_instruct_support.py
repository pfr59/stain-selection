#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    Sep 09, 2019 12:50:27 PM CDT  platform: Windows NT
#    Sep 09, 2019 12:53:24 PM CDT  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def btn_close_prog_instruct(p1):
    print('prog_instruct_support.btn_close_prog_instruct')
    sys.stdout.flush()
    destroy_window()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import prog_instruct
    prog_instruct.vp_start_gui()




