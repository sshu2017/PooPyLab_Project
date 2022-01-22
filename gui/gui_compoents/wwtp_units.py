from PooPyLab.unit_procs.streams import pipe


class PipeUnit(object):
    """
    A pipe_unit object is a dictionary that presents a pipe and contains the information about how it is connected.
    """
    def __init__(self, _id):
        self.pipe = pipe()
        self._id = _id
        self._upstream = None
        self._downstream_main = None
        self._downstream_side = None
