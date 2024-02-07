from .SerialPrompter import cr8SerialPrompter
from .ApplySerialPrompter import cr8ApplySerialPrompter
from .ImageSizer import cr8ImageSizer


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "SerialPrompter": cr8SerialPrompter,
    "ApplySerialPrompter": cr8ApplySerialPrompter,
    "ImageSizer": cr8ImageSizer
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "SerialPrompter": "CRE8IT Serial Prompter",
    "ApplySerialPrompter": "CRE8IT Apply Serial Prompter",
    "ImageSizer": "CRE8IT Image Sizer"
}