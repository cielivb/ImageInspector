""" Test App for ImageInspector widget """

import wx
import image_inspector



class TestPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)

        buttons = []
        btn1 = wx.Button(self, label='small.png', id=1)
        btn2 = wx.Button(self, label='medium.jpg', id=2)
        btn3 = wx.Button(self, label='medium_vertical.jpg', id=3)
        btn4 = wx.Button(self, label='nebula.webp', id=4)
        buttons.append(btn1)
        buttons.append(btn2)
        buttons.append(btn3)
        buttons.append(btn4)

        sizer = wx.GridSizer(cols=2)
        for button in buttons:
            self.Bind(wx.EVT_BUTTON, self.open_viewer, button)
            sizer.Add(button, 0, wx.ALIGN_CENTRE, 5)
        self.SetSizer(sizer)

    def open_viewer(self, event):
        if event.GetId() == 1:
            image_inspector.view(self, 'images/small.png')
        elif event.GetId() == 2:
            image_inspector.view(self, 'images/medium.jpg')
        elif event.GetId() == 3:
            image_inspector.view(self, 'images/medium_vertical.jpg')
        elif event.GetId() == 4:
            image_inspector.view(self, 'images/nebula.webp')


class TestFrame(wx.Frame):
    def __init__(self, parent, size, pos):
        wx.Frame.__init__(self, parent, size=size, pos=pos)
        self.panel = TestPanel(self)
        self.SetAutoLayout(False)
        self.Show()

if __name__ == '__main__':
    test_app = wx.App(False)
    frame = TestFrame(None, size=(300,100), pos=(500,200))
    test_app.MainLoop()