#  04/23/21
#   https://gist.github.com/OdatNurd/a70b74e10d0688a915e1859cd4cd4f57


import sublime
import sublime_plugin


class DoFindReplaceCommand(sublime_plugin.TextCommand):
    """
    Find all instances of the search text and replace it with the replacement
    text provided. The arguments allow you to decide if the command should be a
    regular expression (the default) or just plain text, and whether or not
    case should be ignored or not (by default it is not).

    The replacement string may contain the standard regex replacement text,
    should the command be told to do a regex replace.
    """
    def run(self, edit, search, replace, is_regex=True, ignore_case=False):
        flags = 0

        if not is_regex:
            flags |= sublime.LITERAL
        if ignore_case:
            flags |= sublime.IGNORECASE

        replacements = []
        regions = self.view.find_all(search, flags, replace, replacements)

        adjust = 0
        for idx, searched in enumerate(regions):
            replaced = sublime.Region(searched.a - adjust, searched.b - adjust)
            adjust += (replaced.size() - len(replacements[idx]))

            self.view.replace(edit, replaced, replacements[idx])

        if not regions:
            sublime.status_message("Search term was not found")
        else:
            sublime.status_message("Replaced %d matches" % len(regions))
