from IPython.display import display

from .widgets.html_copy_button import HtmlCopyButton
from .widgets.native_copy_button import NativeCopyButton

__version__ = '0.0.1'
__author__ = 'Sam Wilkinson'


def replicator(input_data, native=True):
    if native:
        copy_widget = NativeCopyButton(input_data).get_widget()
    else:
        copy_widget = HtmlCopyButton(input_data).get_widget()

    display(copy_widget)
    display(input_data)