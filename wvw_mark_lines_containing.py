#  04/24/2021
#  https://forum.sublimetext.com/t/add-bookmark-not-toggle-based-upon-find-results/9061/4
#
#  04/30/21 WVW: Add information dialog.  'D' option displays the information dialog.    'N' does not.
#            By default use the text/word/substr under the first cursor.
#
#   For example:
#     { "keys": ["alt+m"], "command": "wvw_mark_lines_containing", "args": {"my_option": "D" } },
#     { "keys": ["alt+shift+m"], "command": "wvw_mark_lines_containing", "args": {"my_option": "N" } },
#
#   Multiple bookmarks can be on one line
#   The first bookmark might not be in the viewport.

import sublime
import sublime_plugin

class WvwMarkLinesContainingCommand(sublime_plugin.WindowCommand):

    global_option = 'g1'

    def run(self, my_option):
        global global_option
        global_option = my_option
        selections_list = self.window.active_view().sel()
        select_first_region     = selections_list[0]
        select_first_point_a, _ = select_first_region
        select_first_word_region  = self.window.active_view().word(select_first_point_a)
        select_first_word         = self.window.active_view().substr(select_first_word_region)

        self.window.show_input_panel("Mark Lines Containing:", select_first_word, self.on_done, None, None)
        pass

    def on_done(self, text):
        # print('global_option:', global_option)

        ExistingBookmarks = self.window.active_view().get_regions("bookmarks")

        RegionsResult = self.window.active_view().find_all(text, sublime.IGNORECASE)
        new_RegionsResult = RegionsResult.copy()

        for ThisExistingBookmark in ExistingBookmarks:
            RegionsResult.append(ThisExistingBookmark)

        self.window.active_view().add_regions("bookmarks", RegionsResult, "bookmarks", "bookmark", sublime.HIDDEN | sublime.PERSISTENT)

        number_regions = len(new_RegionsResult)
        if number_regions > 0:
            region_one = new_RegionsResult[0]
            point_a, point_b = region_one
            one_row_col_zero_based = self.window.active_view().rowcol(point_a)
            one_row_zero_based, _ = one_row_col_zero_based

            region_last = new_RegionsResult[number_regions - 1]
            point_a, point_b = region_last
            last_row_col_zero_based = self.window.active_view().rowcol(point_a)
            last_row_zero_based, _ = last_row_col_zero_based

            if global_option == 'D':
                sublime.message_dialog( "\n"  +  str(number_regions)  +  ' hits found for "'  +  text  +  '"'  \
                                        "\nFirst on line: "  +  str(one_row_zero_based + 1)  +  \
                                        "\nLast on line: "   +  str(last_row_zero_based + 1))

            self.window.active_view().run_command("move_to",  {"extend": "false",
                                                                "to": "bof"
                                                                })
            self.window.active_view().run_command("next_bookmark")

        else:
            sublime.message_dialog( '\nNo hits found for "'  +  text  +  '"')

