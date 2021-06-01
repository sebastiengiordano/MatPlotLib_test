from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit import prompt

actions = {"start":"a", "stop": "b"}

class MyCustomCompleter(Completer):
    def get_completions(self, document, complete_event):
        buffer = document.text
        line = document.text.split()
        COMMANDS = actions.keys()
        # show all commands
        if not line:
            for i in [c for c in COMMANDS]:
                yield Completion(i, start_position=-1 * len(document.text), display=i)
        # account for last argument ending in a space
        else:
            if RE_SPACE.match(buffer):
                line.append('')
            # resolve command to the implementation function
            cmd = line[0].strip()
            if cmd in COMMANDS:
                try:
                    impl = getattr(actions[cmd], 'complete')
                except:
                    yield Completion(cmd, start_position=-1 * len(document.text))
                else:
                    args = line[1:]
                    if args:
                        ret = impl(args)
                        if not ret:
                            pass
                        else:
                            for i in ret:
                                ret = cmd + ' ' + ' '.join(args[:-1]) + ' ' + i
                                ret = ' '.join(ret.split())
                                yield Completion(ret, start_position=-1 * (len(document.text)), display=i.split()[-1])
                    else:
                        yield Completion(cmd + ' ', start_position=-1 * len(document.text))
            else:
                results = [c for c in COMMANDS if c.startswith(cmd)]
                for i in results:
                    yield Completion(i, start_position=-1 * len(document.text), display=i)

content = prompt(completer=MyCustomCompleter())
