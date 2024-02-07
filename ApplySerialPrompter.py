class cr8ApplySerialPrompter:

    def __init__(self):
        pass   
    
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Subject": ("SERIAL_PROMPT",),
            },
            "optional": {
                "Situation": ("SERIAL_PROMPT",),
                "Quality": ("SERIAL_PROMPT",),
            }
        }
    
    RETURN_TYPES = ("STRING","STRING")
    RETURN_NAMES = ("positive","negative")
    OUTPUT_NODE = True
    FUNCTION = "execute"
    CATEGORY = "CRE8IT"

    def execute(self, Subject, Situation=None, Quality=None):
        pos = Subject[0]
        neg = Subject[1]

        if Situation != None:
            pos = pos + ", " + Situation[0]
            neg = neg + ", " + Situation[1]
        if Quality != None:
            pos = pos + ", " + Quality[0]
            neg = neg + ", " + Quality[1]

        return(pos,neg)

    