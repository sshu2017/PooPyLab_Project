import wx
from PooPyLab.unit_procs.streams import pipe


class BasicButton(wx.Button):
    def __init__(self, parent, id, label, pos):
        super().__init__(parent, id, label, pos)
        self.SetSize((70, 50))

    def get_chart_panel(self):
        return self.GetParent().GetParent().GetParent().chart_panel

    def get_guiwwtp(self):
        return self.GetParent().GetParent().GetParent()._guiwwtp


class PipeButton(BasicButton):
    def __init__(self, parent, _id, _label, _pos):
        super().__init__(parent, _id, _label, _pos)
        self.SetLabel("Pipe")
        self.Bind(wx.EVT_BUTTON, self.on_button_click)

    def on_button_click(self, e):
        self.draw_pipe()
        self.add_one_pipe()

    def draw_pipe(self):
        print("Drew a pipe.")
        hline = wx.StaticLine(self.get_chart_panel(),
                              -1,
                              style=wx.LI_HORIZONTAL,
                              pos=(20, 100),
                              size=wx.Size(150, 3))
        hline.SetBackgroundColour('red')

    def add_one_pipe(self):
        print("add_pipe_to_sgraph() is called.")
        print(f"wwtp = {self.get_guiwwtp()}")
        k = 'pipe'
        v = pipe()
        self.get_guiwwtp()[k] = v
        print(f"wwtp = {self.get_guiwwtp()}")


class ReactorButton(BasicButton):
    def __init__(self, parent, id, label, pos):
        super().__init__(parent, id, label, pos)
        self.SetLabel("Reactor")
        self.Bind(wx.EVT_BUTTON, self.on_button_click)

    def on_button_click(self, evt):
        print("ReactorButton on_button_click is called.")
        dc = self.get_chart_panel().dc
        print(f"dc has attr: {dir(dc)}")
        dc.SetPen(wx.Pen("red", style=wx.TRANSPARENT))
        dc.SetBrush(wx.Brush("grey", wx.SOLID))
        dc.DrawRectangle(10, 20, 30, 40)

    # def on_button_click(self, e):
    #     self.draw_reactor()
