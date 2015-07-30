import sublime

import os

def find_in_settings(key):
    settings = sublime.load_settings("AutoHotkey.sublime-settings")
    path_list = settings.get(key)
    for path in path_list:
        if os.path.isfile(path):
            # print ("Found %s=%s" % (key, path))
            break
        else:
            # print ("Not Found %s=%s" % (key, path))
            continue
    # Also try old settings format where path is stored as a named-key in a dictionary.
    else:
        path = settings.get(key)["default"]

    return path
