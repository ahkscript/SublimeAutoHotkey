import sublime, sublime_plugin
import subprocess
import os

from .utils import find_in_settings


CONTEXT_HELP = os.path.join(
        os.path.dirname(__file__),
        'ContextSensitiveHelp.ahk'
)


class ahkgotodocs(sublime_plugin.TextCommand):
    def run(self, edit):
        AutoHotKeyExePath = find_in_settings("AutoHotKeyExePath")
        region = self.view.sel()[0]
        if region.empty():
            line = self.view.line(region)
            line_contents = self.view.substr(line)
            keyword = line_contents.split(None, 1)[0]
        else:
            keyword = self.view.substr(region)
        # print("Keyword: %s" % keyword)
        cmd = [AutoHotKeyExePath, CONTEXT_HELP, keyword]
        # print("Command: %s" % cmd)
        subprocess.call(cmd)
