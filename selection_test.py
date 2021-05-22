#  04/23/2021
#
#   https://gist.github.com/OdatNurd/94db30476f1560e49d5d7bf2f09ff119
#


import sublime
import sublime_plugin


class ReverseSelectAllCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        span = sublime.Region(len(self.view), 0)
        self.view.sel().add(span)


class RemoveSomeSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        span = sublime.Region(7, 14) # "sublime" on line one
        self.view.sel().subtract(span)


class FlipCaretCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        new_sel = []
        for sel in self.view.sel():
            new_sel.append(sublime.Region(sel.b, sel.a))

        self.view.sel().clear()
        self.view.sel().add_all(new_sel)


class BrokenSelectCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        view.sel().clear()
        view.sel().add(sublime.Region(14, 14))
