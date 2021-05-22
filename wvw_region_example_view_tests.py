#  04/24/2021
#
#     [P101-18] How do plugins access file content in Sublime Text?   view_tests.py
#
#    https://gist.github.com/OdatNurd/db26854a4ddb82078877198c8d9c694c#file-view_tests-py
#
#  Example:
#    { "keys": ["f1"], "command": "wvw_region_example" , "args": {"example": "1"}},
#
#     or on the Console
#
#    view.run_command('wvw_region_example', {'example': '1'})
#
#

import sublime
import sublime_plugin
import datetime
# import sys


class WvwRegionExampleCommand(sublime_plugin.TextCommand):
    def run(self, edit, example):
        start_time = datetime.datetime.now()

        # example = '1'
        # example = '10'
        # example = '11'

        # example = '12'



        def printx(*argv):
            print(example, *argv)


        printx()
        printx('example       :', example, 'at', start_time)  #  'with', sys.version)   #   04/28/21:  3.8.8 (default, Mar 10 2021, 13:30:47) [MSC v.1915 64 bit (AMD64)]
        printx('plugin file   :', __file__)
        printx('buffer id     :', self.view.buffer_id())
        printx('buffer name   :', self.view.name())


        printx('view id       :', self.view.id())
        printx('type of view  :', type(self.view))
        printx('length of view:',  len(self.view))

        printx('primary view? :', self.view.is_primary() )
        printx('file name     :', self.view.file_name() )
        printx('buffer size   :', self.view.size() )
        printx('syntax        :', self.view.settings().get('syntax') )


        printx('visible region:', self.view.visible_region())
        #  dip: a float that represents a device-independent pixel.
        printx('viewport pos. :', self.view.viewport_position())   #  vector: a tuple of (dip, dip) representing x and y coordinates.
        printx('viewport exten:', self.view.viewport_extent())
        printx('layout extent :', self.view.layout_extent())
        printx('em width      :', self.view.em_width())

        printx('buffer name   :', self.view.name() )
        printx('dirty view?   :', self.view.is_dirty() )
        printx('read only?    :', self.view.is_read_only() )
        printx('classify 0    :', hex(self.view.classify(0) ))
        printx('find word     :', self.view.rowcol(self.view.find_by_class(0, True, sublime.CLASS_WORD_START)))
        printx('empty line    :', self.view.rowcol(self.view.find_by_class(0, True, sublime.CLASS_EMPTY_LINE)))


        #  If two arguments, use as two parameters for Region
        example = example.strip()
        if ' ' in example:
            ex_list = example.split()
            example = ex_list[0]
            ex_1 = ex_list[1]
            try:
                ex_2 = ex_list[2]
                region = sublime.Region(int(ex_1), int(ex_2))     #  zero based
            except:
                pass


        if  example == "1":
            region = sublime.Region(0, 40)     #  zero based
        elif example == "2":
            region = sublime.Region(50, 120)
        elif example == "3":
            region = sublime.Region(5)
        elif example == "4":
            region = self.view.word(5)
        elif example == "5":
            region = self.view.line(5)
        elif example == "6":
            region = self.view.full_line(5)
        elif example == "7":
            region = self.view.lines(sublime.Region(10, 200))
        elif example == "8":
            region = sublime.Region(self.view.text_point(1, 7))    #  row and column are zero based
        elif example == "9":
            region = self.view.find_all("example")

        elif example == "10":
            region = self.view.find_by_selector("comment")    #  Yes works
            # region = self.view.find_by_selector("end")   #  nothing
            # region = self.view.find_by_selector("function")    #  nothing
            # region = self.view.find_by_selector("meta.string.python")     #  Yes, works
            # region = self.view.find_by_selector("test")     #  nothing, unless sublime.PERSISTENT flagg is used for add_regions


            printx('10 type and region:', type(region), region)  #  <class 'list'> [Region(0, 132), Region(204, 246), Region(247, 277), Region(2
            try:
                printx('10 type  region[0]:', type(region[0]))
            except IndexError:
                pass

        elif example == "11":
            #   Display icons for lines with a cursor
            printx('type self.view.sel():', type(self.view.sel()))   #   <class 'sublime.Selection'>
            for s in self.view.sel():
                printx('type s:', type(s), s)   #   <class 'sublime.Region'>
            region_set = [s for s in self.view.sel()]   # with Cursors
            printx('type region_set:', type(region_set))
            try:
                printx('type region_set[0]:', type(region_set[0]))    #   <class 'sublime.Region'>
            except IndexError:
                pass

            printx('region_set:', region_set)

            region = region_set

        elif example == '12':
            # region_key = 'bookmarks'
            region_key = 'test'
            # region_key = 'comment.line.number-sign.python'   #  nothing

            region_set = self.view.get_regions(region_key )
            printx('12:', region_key, 'Region type and set/list:', type(region_set),  region_set)
            try:
                printx('type region_set[0]:', type(region_set[0]))    #   <class 'sublime.Region'>
            except IndexError:
                pass
            region = region_set


        elif example == '13':
            #    Must be run with a key binding
            #    If run from the console, the cursor is NOT set.   04/30/2021
            #  Use row and column to set another Selection
            my_point = self.view.text_point(int(ex_1) + 1, int(ex_2) + 1)
            # self.view.selection.add((my_point, my_point))
            printx('my_point:', my_point)
            my_span = sublime.Region(my_point, my_point + 5)
            print('my_span:', my_span)
            self.view.sel().add(my_span)



        # The API method we use below expects a list of regions, but not all of
        # the examples above provide one.
        printx('type region:', type(region))
        if not isinstance(region, list):
            region_list = [region]
        else:
            region_list = region

        # printx('type region:', type(region))
        # printx('type region[0]:', type(region[0]))
        printx('number of regions:', len(region_list))

        printx('region_list:', region_list)
        for region_item in region_list:
            # printx(type(region_item))
            point_1, point_2 = region_item
            printx()
            printx(region_item, 'row-col 1 offset:', self.view.rowcol(point_1), 'row-col 2:', self.view.rowcol(point_2))
            printx(region_item, 'point 1 scope   :', self.view.scope_name(point_1))
            printx(region_item, 'point 2 scope   :', self.view.scope_name(point_2))

        if example != '13':
            region_key = 'test'
            printx('add region_key:', region_key, 'for region_list')
            self.view.add_regions(region_key, region_list, "region.orangish", "bookmark",
                flags=sublime.DRAW_EMPTY | sublime.DRAW_NO_FILL  | sublime.PERSISTENT )

        printx()
        printx('finish example:', example )

        # old = view.get_regions("bookmarks")
        # new = [sublime.Region(self.view.line(sel.b).begin()) for sel in region]

        # printx('new:', new)

        # for sel in new:
        #     if sel not in old:
        #         old.append(sel)
        #     else:
        #         del old[old.index(sel)]

        # self.view.add_regions("bookmarks", new, "comment.black", "bookmark",
        # self.view.add_regions("bookmarks", region, "comment.black", "bookmark",
        #     flags=sublime.DRAW_EMPTY | sublime.DRAW_NO_FILL)

        # content = [self.view.substr(r) for r in region]
        # sublime.message_dialog("\n".join(content))
