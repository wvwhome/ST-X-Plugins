#  04/21//2021
#   https://www.sublimetext.com/docs/1/plugin-examples
#  <binding key="ctrl+alt+d" command="duplicate"/>
#  doesn't work
#  Error in console:  TypeError: run() missing 1 required positional argument: 'args'
#    remove args
#
#     for region in view.sel():
# AttributeError: 'Edit' object has no attribute 'sel'


#
import sublime_plugin

# Extends TextCommand so that run() receives a View to modify.
class DuplicateCommand(sublime_plugin.TextCommand):
    def run(self, view):
        # Walk through each region in the selection
        print('view:', view)
        for region in view.sel():
            # Only interested in empty regions, otherwise they may span multiple
            # lines, which doesn't make sense for this command.
            if region.empty():
                # Expand the region to the full line it resides on, excluding the newline
                line = view.line(region)
                # Extract the string for the line, and add a newline
                lineContents = view.substr(line) + '\n'
                # Add the text at the beginning of the line
                view.insert(line.begin(), lineContents)
