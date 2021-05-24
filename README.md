## Sublime Text Plugins 

The names of the plugins and commands have a prefix of 'wvw_'/'Wvw' in order to differentiate/blame.  Of course, anyone may change these for their preferences.

- Create bookmarks for the text/word under the cursor.   `wvw_fold_all.py`  Example key bindings: ` { "keys": ["f7"], "command": "wvw_fold_all" },`   `{ "keys": ["f8"], "command": "unfold_all" },`   Only the first cursor in the view determines the selection.
- Create bookmarks for text.  `wvw_mark_lines_containing.py`  This is similar to `wvw_fold_all.py` except the text can be modified and an informational message is displayed.  Example key binding:  ` { "keys": ["alt+m"], "command": "wvw_mark_lines_containing", "args": {"my_option": "D" } },`

- Create multiple additional cursors in a range. `wvw_extend_range_cursors.py`  Example mouse binding:  

  ```
  {
          "button": "button2", "modifiers": ["alt"],
          "press_command": "wvw_extend_range_cursors",
       },
  ```

  Cursors are added from the first cursor to the line where the mouse is clicked (Alt + Right-Click).  Two modes:  if the first cursor is not at the end of the line, then a column position is preserved for those line s that have that column.  If the first cursor is at the end of the line, then cursors are added to the end of each line.



By a 30 year professed IBM CMS XEDIT/Rexx editor junkie -- uni-XEDIT and The Hessling Editor (THE). Yes, ST far surpasses these.

Beta version  05/24/2021

