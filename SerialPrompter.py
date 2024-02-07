def remove_leading_comma(input_string):
    if input_string and input_string[0] == ',':
        return input_string[1:]
    else:
        return input_string


class cr8SerialPrompter:

    def __init__(self):
        pass   
    
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "enabled": ("BOOLEAN", {"default": True, "label_off": "OFF", "label_on": "ON"}),
                "prompt_type": (["positive","negative"], {"default": "positive"}),
                "prompt": ("STRING", {"default": "Prompt", "multiline": True}),
            },
            "optional": {
                "prompt_in": ("SERIAL_PROMPT",),
            }
        }
    
    RETURN_TYPES = ("SERIAL_PROMPT",)
    RETURN_NAMES = ("prompt_out",)
    OUTPUT_NODE = True
    FUNCTION = "execute"
    CATEGORY = "CRE8IT"

    def execute(self, enabled, prompt_type, prompt, prompt_in=None):
        positive = ""
        negative = ""

        if prompt_in:
            positive = prompt_in[0] + positive
            negative = prompt_in[1] + negative
        
        if enabled == True and prompt_type == "positive":
            if prompt[-1] == ",":
                positive = positive + " " + prompt
            else:
                positive = positive + "," + prompt
        
        if enabled == True and prompt_type == "negative":
            if prompt[-1] == ",":
                negative = negative + " " + prompt
            else:
                negative = negative + "," + prompt

        positive = remove_leading_comma(positive)
        negative = remove_leading_comma(negative)
        return((positive, negative),)