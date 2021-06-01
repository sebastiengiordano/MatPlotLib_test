from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

def bottom_toolbar():
    return [('class:bottom-toolbar', ' This is a toolbar. ')]

style = Style.from_dict({
    'bottom-toolbar': '#ffffff bg:#333333',
})

text = prompt('> ', bottom_toolbar=bottom_toolbar, style=style)
print('You said: %s' % text)
