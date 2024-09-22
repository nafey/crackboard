import sublime_plugin
import sublime
import time
from urllib import request, parse
import json
import urllib.error

def call_api(session_key, lang):
    data = { 
        "session_key": session_key, 
        'language_name': lang
    }

    data = json.dumps(data)
    data = str(data)
    data = data.encode('utf-8')


    req =  request.Request("http://crackboard.dev/heartbeat", data=data)

    req.add_header('Content-Type', 'text/plain; charset=utf-8')
    req.add_header("User-agent", "RapidAPI/4.2.5 (Macintosh; OS X/11.7.10) GCDHTTPRequest")

    try:
        resp = request.urlopen(req)
        print("Heartbeat accepted")
    except urllib.error.HTTPError as e:
        print("HTTP error from crackboard: " + str(e.code) + " - " + e.reason)


def get_timestamp():
    return int(time.time())


class CrackboardTextChange(sublime_plugin.TextChangeListener):
    def do_heartbeat(self):
        window = sublime.active_window()
        syntax = (window.active_view().syntax().name)
        lang = (syntax).lower()
        session_key = (sublime.load_settings("crackboard.sublime-settings").get("crackboard_session_key"))
        call_api(session_key, lang)


    def on_text_changed_async(self, changes):
        if (not hasattr(self, "lastime")):
            self.lastime = get_timestamp()
            self.do_heartbeat()


        currtime = get_timestamp()
        if (currtime - self.lastime > 130):
            self.lastime = currtime
            self.do_heartbeat()

class _CrackboardSessionKeyInputHandler(sublime_plugin.TextInputHandler):
    def name(self):
        return "session_key_str"

    def placeholder(self):
        return "Input Crackboard session key"

    def validate(self, text):
        return bool(text)


class CrackboardSetSessionKeyCommand(sublime_plugin.TextCommand):
    def run(self, _edit, session_key_str):
        settings = sublime.load_settings("crackboard.sublime-settings")
        settings.set("crackboard_session_key", session_key_str)
        sublime.save_settings("crackboard.sublime-settings")

    def input(self, _args):
        return _CrackboardSessionKeyInputHandler()

    def input_description(self):
        return "Session Key"


