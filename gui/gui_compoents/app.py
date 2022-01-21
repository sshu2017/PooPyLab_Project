import wx

from gui_compoents.frame import MainFrame


class MainApp(wx.App):
    def OnInit(self):
        frame = MainFrame(None, -1, 'PoopyLab')
        frame.Show()
        return True
