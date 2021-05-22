#  Hello, World! for 3.3.6 (default, Mar 29 2018, 23:30:25) [MSC v.1600 64 bit (AMD64)]  of internal Python.#
#
#  Must be named 'example.py'
#  https://cnpagency.com/blog/creating-sublime-text-3-plugins-part-1/
#

# view.run_command('wvwb_example')

# This will execute your class and do the requested action. You’ll notice that ST3 automatically
# parses the class name “ExampleCommand” as a command to execute since it has the text “Command” appended to the end.
# Once ST3 recognizes this, it strips the “command” string off of the end
# and takes the beginning as the actual name in lower case (ex: ExampleCommand = example).
# Multiple capitals will result in underscore separators between words.
#
#
# import sublime
import sublime_plugin
import sys

class wvwBexampleCommand(sublime_plugin.TextCommand):
    #      self, edit, text, pos, event
    def run(self, edit):
        for s in self.view.sel():
            print('sel   :',  s)
            s_loc = self.view.word(s)
            print('s_loc :', s_loc)
            s_text = self.view.substr(s_loc)
            print('s_text:', s_text)
