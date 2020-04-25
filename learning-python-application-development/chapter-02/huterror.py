"""
Hut Error
"""


class HutError(Exception):
    def __init__(self, code):
        self.error_message = ""
        self.error_dict = {
            000: "E000: Unspecified Error code",
            101: "E001: Out of range: Number > 5",
            102: "E102: Out of range: Negative number",
            103: "E103: not a number!",
        }
        try:
            self.error_message = self.error_dict[code]
        except KeyError:
            self.error_message = self.error_dict[000]
        # print(f"\n Error message:{self.error_message}")
