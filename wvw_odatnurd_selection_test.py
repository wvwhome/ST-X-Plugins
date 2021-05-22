#  04/30/2021
#  https://www.youtube.com/watch?v=-gh3oEDkh_4


import sublime
import sublime_plugin

#  Must bind to key, else the Cursor is not set
class WvwReverseSelectAllCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        span = sublime.Region(len(self.view) - 1, 20)
        self.view.sel().add(span)


class WvwRemoveSomeSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        span = sublime.Region(7, 14) # "sublime" on line one
        self.view.sel().subtract(span)


class WvwFlipCaretCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        new_sel = []
        for sel in self.view.sel():
            new_sel.append(sublime.Region(sel.b, sel.a))

        self.view.sel().clear()
        self.view.sel().add_all(new_sel)


class WvwBrokenSelectCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        view.sel().clear()
        view.sel().add(sublime.Region(14, 14))
