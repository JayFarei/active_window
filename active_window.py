from AppKit import NSWorkspace
import time

active_window_name = ""
new_window_name = (NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'])
active_window_name = new_window_name.encode(encoding="utf-8", errors="strict")
print (active_window_name)

# to be used in ubersicht - the output has to be unique and triggered by the command vs a stream of data.

## only works with python 2.7
