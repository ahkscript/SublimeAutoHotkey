import sublime, sublime_plugin
import subprocess
import os
from .utils import find_in_settings

class ahkgotodocs(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			word = self.view.word(region)
			if not word.empty():
				keyword = self.view.substr(word)
				sublime.status_message("AutoHotkey Help: " + keyword)

				self.ahkgotodocs_hh(keyword)
				# self.ahkgotodocs_url(keyword)

	def ahkgotodocs_hh(self, keyword):
		AhkHelpPath = find_in_settings("AhkHelpPath")
		cmd = ["hh.exe", r"mk:@MSITStore:" + AhkHelpPath + r"::/docs/commands/%s.htm" % keyword]
		subprocess.Popen(cmd)

	def ahkgotodocs_url(self, keyword):
		url = "http://www.autohotkey.com/docs/commands/%s.htm" % keyword
		os.startfile(url)
