#!/usr/bin/env python

import wx
import wx.html as html

#----------------------------------------------------------------------
ID_New  = wx.NewId()
ID_Exit = wx.NewId()
#----------------------------------------------------------------------

class MyParentFrame(wx.MDIParentFrame):
    def __init__(self):
        wx.MDIParentFrame.__init__(self, None, -1, "pollng", size=(600,400))

        self.winCount = 0
        menu = wx.Menu()
        menu.Append(ID_New, "&New Window")
        menu.AppendSeparator()
        menu.Append(ID_Exit, "E&xit")

        menubar = wx.MenuBar()
        menubar.Append(menu, "&File")
        self.SetMenuBar(menubar)

        self.CreateStatusBar()

        self.Bind(wx.EVT_MENU, self.OnNewWindow, id=ID_New)
        self.Bind(wx.EVT_MENU, self.OnExit, id=ID_Exit)

    def OnExit(self, evt):
        self.Close(True)

    def OnNewWindow(self, evt):
        self.winCount = self.winCount + 1
        win = wx.MDIChildFrame(self, -1, "Child Window: %d" % self.winCount)
        self.html = html.HtmlWindow(win, -1)
        self.html.LoadPage('http://wikipedia.org')

#----------------------------------------------------------------------

if __name__ == '__main__':
    class MyApp(wx.App):
        def OnInit(self):
            frame = MyParentFrame()
            frame.Show(True)
            self.SetTopWindow(frame)
            return True

    app = MyApp(False)
    app.MainLoop()
