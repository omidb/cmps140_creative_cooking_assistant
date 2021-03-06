"""
Data structures used for communication between modules.
"""


class Message(object):
    """
    Base class for messages exchanged between the NLU and DM and DM
    and NLG.  It implements frame-and-slot semantics through its
    frame attribute, which is a dictionary.  It also stores metadata
    using its other attributes.
    """

    def __init__(self):
        """
        Create a new Message.
        """
        # Mike: Not sure if this is necessary
        # The variable name 'type' conflicts with the Python's built-in type()
        # function.
        # self.msg_type = msg_type
        # Frame implements frame-and-slot semantics.
        self.frame = {}
        # Additional metadata attributes could be added.
