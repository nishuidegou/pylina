import wx
import time
import wx.gizmos as gizmos
import datetime


class MACE(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, None, -1, "MACE PQ MONITORING SYSTEM", wx.DefaultPosition, wx.Size(600, 500),
                          style=wx.MINIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU |
                                wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)

        menubar = wx.MenuBar()
        self.statusbar = self.CreateStatusBar()
        file = wx.Menu()
        help = wx.Menu()

        menubar.Append(file, "File")
        menubar.Append(help, "Help")
        self.SetMenuBar(menubar)

        # FOR REAL TIME MONITOR#

        array = ['12', '40', '20', '221', '222', '223', '3.1', '3.2',
                 '3.3']  # values should be dynamic, basing on string sent via the serial port

        self.panelA = wx.Window(self, -1, style=wx.SIMPLE_BORDER)
        self.panelA.SetBackgroundColour(wx.WHITE)

        self.SetAutoLayout(True)

        style = gizmos.LED_ALIGN_CENTER
        self.led = gizmos.LEDNumberCtrl(self, -1, (100, 40), (150, 35), style)
        self.OnTimer(None)
        self.timer = wx.Timer(self, -1)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.OnTimer)

        powlabel = wx.StaticText(self.panelA, -1, "Real Power (Watts)", pos=(60, 102))
        self.powdisp = gizmos.LEDNumberCtrl(self.panelA, -1, (180, 90), (125, 35), style)
        self.powdisp.SetValue(array[1])

        imlabel = wx.StaticText(self.panelA, -1, "Imaginary Power (VAR)", pos=(60, 154))
        self.imdisp = gizmos.LEDNumberCtrl(self.panelA, -1, (180, 142), (125, 35), style)
        self.imdisp.SetValue(array[2])

        volabel = wx.StaticText(self.panelA, -1, "Voltages (Volts)", pos=(40, 200))
        curlabel = wx.StaticText(self.panelA, -1, "Currents (Amps)", pos=(220, 200))

        p1 = wx.StaticText(self.panelA, -1, "Phase 1", pos=(155, 232))
        p2 = wx.StaticText(self.panelA, -1, "Phase 2", pos=(155, 282))
        p3 = wx.StaticText(self.panelA, -1, "Phase 3", pos=(155, 332))

        self.p1vdisp = gizmos.LEDNumberCtrl(self.panelA, -1, (20, 220), (125, 35), style)
        self.p1vdisp.SetValue(array[3])
        self.p1cdisp = gizmos.LEDNumberCtrl(self.panelA, -1, (200, 220), (125, 35), style)
        self.p1cdisp.SetValue(array[6])

        self.p2vdisp = gizmos.LEDNumberCtrl(self.panelA, -1, (20, 270), (125, 35), style)
        self.p2vdisp.SetValue(array[4])
        self.p2cdisp = gizmos.LEDNumberCtrl(self.panelA, -1, (200, 270), (125, 35), style)
        self.p2cdisp.SetValue(array[7])

        self.p3vdisp = gizmos.LEDNumberCtrl(self.panelA, -1, (20, 320), (125, 35), style)
        self.p3vdisp.SetValue(array[5])
        self.p3cdisp = gizmos.LEDNumberCtrl(self.panelA, -1, (200, 320), (125, 35), style)
        self.p3cdisp.SetValue(array[8])

        lc = wx.LayoutConstraints()
        lc.top.SameAs(self, wx.Top, 5)
        lc.left.SameAs(self, wx.Left, 5)
        lc.bottom.SameAs(self, wx.Bottom, 5)
        lc.right.PercentOf(self, wx.Right, 60)
        self.panelA.SetConstraints(lc)

        # FOR DUMPED DATA DISPLAY#
        self.panelB = wx.Window(self, -1, style=wx.SIMPLE_BORDER)
        self.panelB.SetBackgroundColour(wx.WHITE)

        PanelLabel = wx.StaticText(self.panelB, -1, "Dummped Data", (5, 5))
        PanelLabel.SetForegroundColour(wx.BLACK)

        lc = wx.LayoutConstraints()
        lc.top.SameAs(self, wx.Top, 5)
        lc.right.SameAs(self, wx.Right, 5)
        lc.bottom.SameAs(self, wx.Bottom, 5)
        lc.left.RightOf(self.panelA, 5)
        self.panelB.SetConstraints(lc)

    def OnTimer(self, event):
        current = time.localtime(time.time())
        ts = time.strftime("%H %M %S", current)
        self.led.SetValue(ts)


class MyApp(wx.App):
    def OnInit(self):
        frame = MACE(None, -1, 'MACE Power Quality Monitor')
        frame.Show()
        self.SetTopWindow(frame)
        return 1


app = MyApp(0)
app.MainLoop()