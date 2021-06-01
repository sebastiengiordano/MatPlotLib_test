from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
sub_completer = WordCompleter(u"Bar", u"Baz")
completer = WordCompleter([u"Hello", u"World"])
session = PromptSession(u"> ", completer=completer)
session.prompt(pre_run=session.default_buffer.start_completion)