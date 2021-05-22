#  Hello, World! for 3.3.6 (default, Mar 29 2018, 23:30:25) [MSC v.1600 64 bit (AMD64)]  of internal Python  04/23/21.#
#
#  Must be named 'example.py'
#  https://cnpagency.com/blog/creating-sublime-text-3-plugins-part-1/
#
# Its function is simple: the line “Hello, World!” is prepended to the beginning of the document you are viewing. To see it in action, you will need to open the console and type:

# view.run_command('example')

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

class wvwExampleCommand(sublime_plugin.TextCommand):
    #      self, edit, text, pos, event
    def run(self, edit):
        self.view.insert(   edit,
                            0,                #  character position in the file to insert after
                            "#  Hello, World! for "  + sys.version  +  '  of internal Python  04/23/21.')
        # print(__file__)

    def input_description(self):
        return 'Example by WVW'
