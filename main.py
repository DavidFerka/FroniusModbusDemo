from utils import demo
import sys
from gui_local import guimain as gui
import threading
import time


if __name__ == '__main__':
    user_interface = gui.MainGui()
    user_interface.start_gui()


