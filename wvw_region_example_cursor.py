#  04/24/2021
#
#     [P101-18] How do plugins access file content in Sublime Text?   view_tests.py
#
#
#

import sublime
import sublime_plugin
# import sys


class WvwExampleCursorCommand(sublime_plugin.TextCommand):
    def run(self, edit):   #    , example):

        my_point = 3
        print('my_point:', my_point)
        my_span = sublime.Region(my_point, my_point + 5)
        print('my_span:', my_span)
        self.view.sel().add(my_span)



