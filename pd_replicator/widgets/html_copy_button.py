import ipywidgets
import pandas as pd

from threading import Timer
from IPython.display import display, HTML, clear_output

from .constants import DROPDOWN_MAP
from .html import SCRIPT_HTML, BUTTON_HTML


class HtmlCopyButton(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.input_type = type(self.input_data)

        if self.input_type not in [pd.core.frame.DataFrame, pd.core.series.Series]:
            raise TypeError(
                "Expected DataFrame or Series, got a {}".format(
                    self.input_type.__name__
                )
            )

    def get_widget(self):
        self.dropdown=ipywidgets.Dropdown(
            options=list(DROPDOWN_MAP.keys()),
            value=list(DROPDOWN_MAP.keys())[0],
            disabled=False,
        )
        self.dropdown.observe(self._on_dropdown_change, 'value')

        display(HTML(SCRIPT_HTML))

        self.copy_buttons={key: self._get_html_button(value["index"], value["header"]) for key, value in DROPDOWN_MAP.items()}
        self.current_copy_button=ipywidgets.HBox(children=[self.copy_buttons[self.dropdown.value]])

        return ipywidgets.HBox([self.current_copy_button, self.dropdown])

    def _on_dropdown_change(self, dropdown_key):
        self.current_copy_button.children=[self.copy_buttons[dropdown_key.new]]

    def _get_html_button(self, index, header):
        if self.input_type == pd.core.frame.DataFrame:
            return ipywidgets.HTML(BUTTON_HTML.format(self.input_data.to_csv(index=index, header=header, sep='\t')))
        else:
            return ipywidgets.HTML(BUTTON_HTML.format(pd.DataFrame(self.input_data).to_csv(index=index, header=header, sep='\t')))
