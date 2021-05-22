#  05/06/2021
#   wvw_extend_select_cursors.py
#
#   Author: Warren Van Wyck   wvanwyck@outlook.com
#
#    Mode:
#
#   1) First the nearest cursor above.  If not at the end of line, then add cursors from that row and for that column down to and including the target line selected.
#      skip lines that do not have that column.
#   2) First the nearest cursor above.  If that cursor is at the end of the line, then add cursors to the end of each line from that row and down to and including the target line selected.
#
#   region.b is where the cursor is.
#
#    Mouse binding:
#
#   Folder: C:\Users\wvw\AppData\Roaming\Sublime Text\Packages\Default
#   File:   Default (Windows).sublime-mousemap
#
#      or
#
# window.run_command("edit_settings", {"base_file": "${packages}/Default/Default ($platform).sublime-mousemap", "default": "[\n\t$0\n]\n"})
#
#
#     //  05/05/21 WVW Add this stanza -- or whatever you prefer
#     {
#        "button": "button1", "modifiers": ["alt"],
#        "press_command": "wvw_extend_select",
#     },


import sublime
import sublime_plugin

class WvwExtendSelectCursorsCommand(sublime_plugin.TextCommand):
    def run(self, edit, event=None):

        end_of_line_mode_ind = False

        if not event:
            new_point = 0
        else:
            new_point = self.view.window_to_text((event["x"], event["y"]))

        new_row_zero, new_col_zero =  self.view.rowcol(new_point)
        # print('cursor point:', new_point, 'R/C:', new_row_zero, new_col_zero)

        selection_obj = self.view.sel()
        # print('type sel:', type(sel))

        new_sel = []
        sel_row_zero_list = []
        sel_col_zero_list = []
        start_row_zero = -1

        for j, sel_region in enumerate(selection_obj):
            # print(type(sel_region), sel_region)
            # print(j, 'line for region:', self.view.line(sel_region))
            point_b = sel_region.b   #  where the cursor is

            sel_row_zero, sel_col_zero = self.view.rowcol(point_b)
            sel_row_zero_list.append(sel_row_zero)
            sel_col_zero_list.append(sel_col_zero)

            # print(j, 'existing:', str(sel_row_zero + 1), str(sel_col_zero + 1))
            new_sel.append(sel_region)

            if new_row_zero < sel_row_zero:
                pass
            else:
                start_row_zero = sel_row_zero
                start_col_zero = sel_col_zero
                start_cursor_point  = point_b

        if start_row_zero >= 0:
            start_line_region = self.view.line(start_cursor_point)
            # print('start_line_region:', start_line_region)
            # start_line_first_point_ = start_line_region.a
            start_line_last_point = start_line_region.b

            start_line_row_zero, start_line_last_col_zero = self.view.rowcol(start_line_last_point)
            # print('sss:', start_line_last_col_zero, start_col_zero)
            if start_line_last_point ==  start_cursor_point:
                end_of_line_mode_ind = True
                # print('end of line mode:', end_of_line_mode_ind)


            for n in range(0, new_row_zero - start_row_zero):
                # print('start_row_zero:', start_row_zero)
                add_row_zero = start_row_zero + n + 1
                add_col_zero = start_col_zero
                if end_of_line_mode_ind:
                    # Find end of line column
                    begin_of_line_point = self.view.text_point(add_row_zero, 0)
                    add_line_region = self.view.line(begin_of_line_point)
                    add_cursor_point = add_line_region.b
                    new_sel.append(sublime.Region(add_cursor_point, add_cursor_point))
                else:
                    add_cursor_point = self.view.text_point(add_row_zero, add_col_zero)
                    # print('add_cursor_point:', add_cursor_point)
                    #  Check if the column is actually in this row
                    check_row_zero, check_col_zero = self.view.rowcol(add_cursor_point)
                    if check_col_zero >= start_col_zero:
                        # print(n, 'add R/C:', check_row_zero, check_col_zero)
                        new_sel.append(sublime.Region(add_cursor_point, add_cursor_point))


        self.view.sel().clear()
        self.view.sel().add_all(new_sel)

    def want_event(self):
        return True
