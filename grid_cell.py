class GridCell():
    def __init__(self, can, start_x, start_y, size, state):
        color = "black" if state else "white"

        self._state = state
        self._can = can
        self._id = self._can.create_rectangle((
            start_x,
            start_y,
            start_x + size,
            start_y + size
        ), fill = color)

        self._can.tag_bind(self._id, "<ButtonPress-1>", self.switch_state)

    def switch_state(self, event = None):
        if(self._state):
            self._state = False
            self._can.itemconfigure(self._id, fill = "white")
        else:
            self._state = True
            self._can.itemconfigure(self._id, fill = "black")

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        if(value):
            self._can.itemconfigure(self._id, fill = "black")
        else:
            self._can.itemconfigure(self._id, fill = "white")