#  05/05/2021
#  from https://stackoverflow.com/questions/37595322/show-total-line-count-status-bar-sublime-text-3
#  A few mods:   two seconds.

import time
import sublime
import sublime_plugin

last_change = time.time()
update_interval = 2.0  #  two seconds

class LineCountUpdateListener(sublime_plugin.EventListener):
    def update_line_count(self, view):
        line_count = view.rowcol(view.size())[0] + 1
        view.set_status("line_count", "Lines: {0}".format(line_count))

    def on_modified(self, view):
        global last_change
        current_change = time.time()
        # check if we haven't embedded the change in the last update
        if current_change > last_change + update_interval:
            last_change = current_change
            sublime.set_timeout(lambda: self.update_line_count(view),
                                int(update_interval * 1000))  #  milliseconds

    on_new = update_line_count
    on_load = update_line_count
