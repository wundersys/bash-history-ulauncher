import os
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action import RunScriptAction

class BashHistoryExtension(Extension):
    def __init__(self):
        super(BashHistoryExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        results = []
        with open(f"{os.environ['HOME']}/.bash_history", "r") as f:
            lines = f.readlines()[-50:]  # son 50 komut
            for cmd in reversed(lines):
                cmd = cmd.strip()
                results.append(
                    ExtensionResultItem(
                        icon='images/icon.png',
                        name=cmd,
                        description='Çalıştırmak için Enter',
                        on_enter=RunScriptAction(cmd)
                    )
                )
        return results

if __name__ == '__main__':
    BashHistoryExtension().run()
