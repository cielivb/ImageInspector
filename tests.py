""" Test App for ImageInspector widget """

import wx
import image_inspector



class TestPanel(wx.Panel):
    """ Hosts buttons to instantiate ImageInspectors with various images """

    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)

        self.id_url = {
            1:'images/small.png',
            2:'images/medium.jpg',
            3:'images/medium_vertical.jpg',
            4:'images/nebula.webp',
            5:'images/my_gif.gif',
            6:'https://scitechdaily.com/images/image-of-the-planetary-nebula-NGC-5189.jpg',
            7:'https://i.kym-cdn.com/entries/icons/mobile/000/015/559/It_Was_Me__Dio!.jpg'
        }

        btn1 = wx.Button(self, label='small.png', id=1)
        btn2 = wx.Button(self, label='medium.jpg', id=2)
        btn3 = wx.Button(self, label='medium_vertical.jpg', id=3)
        btn4 = wx.Button(self, label='nebula.webp', id=4)
        btn5 = wx.Button(self, label='my_gif.gif', id=5)
        btn6 = wx.Button(self, label='nebula from web', id=6)
        btn7 = wx.Button(self, label='(from web) who is it?', id=7)

        sizer = wx.GridSizer(cols=2)

        # Add each button to sizer and bind each button to self.open_viewer
        for child in self.GetChildren():
            if type(child) is wx.Button:
                self.Bind(wx.EVT_BUTTON, self.open_inspector, child)
                sizer.Add(child, 0, wx.ALIGN_CENTRE, 5)                

        self.SetSizer(sizer)


    def open_inspector(self, event):
        """ Opens an instance of ImageInspector 

        The syntax for doing so is
        image_inspector.view(parent=self, image_file='image/path') 
        where 'image/path' is the path to your image file, and can be either a
        local file or a web address
        
        """
        image_inspector.view(parent=self, 
                             image_file=self.id_url[event.GetId()])



class TestFrame(wx.Frame):
    def __init__(self, parent, size, pos):
        wx.Frame.__init__(self, parent, size=size, pos=pos)
        self.Bind(wx.EVT_CLOSE, self.on_close) # Important!!
        self.panel = TestPanel(self)        
        self.SetAutoLayout(False)
        self.Show()

    def on_close(self, event):
        """ Inform ImageInspector frames the main app is closing. 
        This ensures temp image files are tidied up. Not including
        this section could lead to data bloat.
        """
        test_panel = self.GetChildren()[0]
        for child in test_panel.GetChildren():
            if type(child) is image_inspector.ImageInspector:
                child.Close()
        self.Destroy()


if __name__ == '__main__':
    test_app = wx.App(False)
    frame = TestFrame(None, size=(300,200), pos=(500,200))
    test_app.MainLoop()