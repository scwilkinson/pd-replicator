import pandas as pd
import ipywidgets

from threading import Timer

from .constants import DROPDOWN_MAP

class NativeCopyButton(object):
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
        self.dropdown = ipywidgets.Dropdown(
            options=list(DROPDOWN_MAP.keys()),
            value=list(DROPDOWN_MAP.keys())[0],
            disabled=False,
        )

        self.copy_button = ipywidgets.Button(description="Copy")
        self.copy_button.on_click(self._on_copy_button_clicked)

        self.reset_timer = None

        return ipywidgets.HBox([self.copy_button, self.dropdown])

    def _on_copy_button_clicked(self, button):
        if self.reset_timer is not None:
            self.reset_timer.cancel()

        self.reset_timer = Timer(1.0, self._set_button_default)

        if self.input_type == pd.core.frame.DataFrame:
            self._copy_df_to_clipboard(self.input_data)
        else:
            self._copy_df_to_clipboard(pd.DataFrame(self.input_data))

        self._set_button_success()
        self.reset_timer.start()

    def _set_button_success(self):
        self.copy_button.button_style = "success"
        self.copy_button.icon = "check"

    def _set_button_default(self):
        self.copy_button.button_style = ""
        self.copy_button.icon = ""

    def _copy_df_to_clipboard(self, df):
        dropdown_option_dict = DROPDOWN_MAP[self.dropdown.value]
        df.to_clipboard(
            index=dropdown_option_dict["index"], 
            header=dropdown_option_dict["header"]
        )
