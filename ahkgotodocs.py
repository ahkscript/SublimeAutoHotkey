import sublime, sublime_plugin
import subprocess
import os
from .utils import find_in_settings

class ahkgotodocs(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			word = self.view.substr(region)

			# If no selection, find word contained by whitespace
			if len(word) == 0:
				word = self.view.substr(self.view.word(region))

			if len(word) != 0:
				
				# Remove non-alpha characters
				wordalphaonly = ''
				for ch in word:
					if(ch.isalpha()):
						wordalphaonly += ch
				word = wordalphaonly

				sublime.status_message("AHKGOTODOCS Loading Documentation For: " + word)
				self.ahkgotodocs_hh(word)
				# self.ahkgotodocs_url(keyword)

	def ahkgotodocs_hh(self, keyword):
		AhkHelpPath = find_in_settings("AhkHelpPath")
		cmd = ["hh.exe", r"mk:@MSITStore:" + AhkHelpPath + r"::/docs/commands/%s.htm" % keyword]
		subprocess.Popen(cmd)

	def ahkgotodocs_url(self, keyword):
		url = "http://www.autohotkey.com/docs/commands/%s.htm" % keyword
		os.startfile(url)
