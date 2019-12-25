from AppKit import NSWorkspace
import time

active_window_name = ""

while True:
    new_window_name = (NSWorkspace.sharedWorkspace()
    .activeApplication()['NSApplicationName'])

    if active_window_name != new_window_name:
        active_window_name = new_window_name.encode(encoding="utf-8", errors="strict")
        print (active_window_name)

# If needed for performance reasons time.sleep (10)
