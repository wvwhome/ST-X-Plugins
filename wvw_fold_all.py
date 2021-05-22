#
#    04/23/2021
#
#   wvw_fold_all.py
#
#   Author:  Warren Van Wyck     wvanwyck@outlook.com
#
#   Description:
#     Partial emulation of XEDIT All macro that I used since 1987 in IBM CMS XEDIT
#     And then  uniXEDIT and The Hessling Editor.
#     Select the line(s) with the word under the cursor/caret and fold/hide the rest of them.
#     Set a bookmark for each line with a hit.
#     Maybe - Position to the top of the file.
#
#    Credits:
#    Copy some code from https://github.com/davidpeckham/sublime-filterlines   filter.py
#
#    ---  Change History --
#   04/03/21: Set bookmark for each line with a hit/match.
#
#    Example key settings:
#
#    { "keys": ["f7"], "command": "fold_all" },
#    { "keys": ["f8"], "command": "unfold_all" },
#    { "keys": ["shift+f8"], "command": "unfold" },           #  just one folded section/region
#
#  https://cnpagency.com/blog/creating-sublime-text-3-plugins-part-1/
#
#
# This will execute your class and do the requested action. You’ll notice that ST3 automatically
# parses the class name “ExampleCommand” as a command to execute since it has the text “Command” appended to the end.
# Once ST3 recognizes this, it strips the “command” string off of the end
# and takes the beginning as the actual name in lower case (ex: ExampleCommand = example).
# Multiple capitals will result in underscore separators between words.
#
#
import sublime
import sublime_plugin
import itertools

class WvwFoldAllCommand(sublime_plugin.TextCommand):
    #      self, edit, text, pos, event
    def run(self, edit):

        sel_ctr = 0
        for sel_region in self.view.sel():
            sel_ctr += 1
            # print('sel   :',  sel_region)
            sel_word_loc = self.view.word(sel_region)
            # print('sel_word_loc :', sel_word_loc)


            sel_word = self.view.substr(sel_word_loc)
            # print('sel_word:', sel_word)
            # Only use the first selection for folding.   A 'word' could be a string of blanks.
            if sel_ctr == 1:
                needle = sel_word
                # print('needle:', needle, 'length:', len(needle))
                break

        lines_group = itertools.groupby(
                    self.view.find_all(needle, sublime.IGNORECASE), self.view.line)

        lines_list = [line_item for (line_item, _ )  in lines_group]
        # print('number of lines:', len(lines_list), lines_list)
        source_lines_list = self.view.lines(sublime.Region(0, self.view.size()))
        # print('len source_lines_list:', len(source_lines_list))

        filtered_line_numbers_list = {
                                self.view.rowcol(line.begin())[0] for line in lines_list  }
        regions_list = []
        region = None

        for line in source_lines_list:
            matched = (
                        self.view.rowcol(line.begin() )[0] in filtered_line_numbers_list)
            if matched:
                if region:
                    regions_list.append(region)
                    region = None
            else:
                if region:
                    region = region.cover(line)
                else:
                    region = sublime.Region(line.begin(), line.end())

        if region:
            regions_list.append(region)
        if regions_list:
            self.view.fold(regions_list)

        self.view.add_regions("bookmarks", lines_list, "bookmarks", "bookmark", sublime.HIDDEN | sublime.PERSISTENT)


        # self.view.run_command("move_to", {"extend": "false", "to": "bof"})   #  Display  Beginning of the file ... maybe not where we started.
