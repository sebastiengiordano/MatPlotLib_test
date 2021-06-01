import wx

class DisplayGraph(wx.Frame):

    def __init__(self, *args, **kw):
        super(DisplayGraph, self).__init__(*args, **kw)

        self._init_ui()
        self.min_height = 0
        self.max_height = 10000

    def _init_ui(self):

        self.Bind(wx.EVT_PAINT, self._on_paint)
        self.Bind(wx.EVT_SIZING, self._on_size)
        self.Bind(wx.EVT_MAXIMIZE, self._on_size)

        self.SetTitle('Graph by lines')
        self.Size()
        self.Center()

    def _on_paint(self, event):
        w, h = self.GetSize()

        dc = wx.PaintDC(self)
        brush = wx.Brush("white")  
        dc.SetBackground(brush)  
        dc.Clear() 
        dc.SetPen(wx.Pen('RED'))

        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if (row[0]).isnumeric():
                    x, y, z = int(row[0]), int(row[1]), int(row[5])
                    if x > w_max:
                        w_max = x
                    if y > h_max:
                        h_max = y
                    if z > h_max:
                        h_max = z

        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if (row[0]).isnumeric() :                    
                    x, y, z = int(int(row[0])/w_max*w), int(h - int(row[1])/h_max*h), int(h - int(row[5])/h_max*h)
                    if not (x_mem == 0 and y_mem == 0 and z_mem == 0):
                        dc.DrawLine(x_mem, y_mem, x, y)
                        dc.DrawLine(x_mem, z_mem, x, z)
                    x_mem, y_mem, z_mem = x, y, z

    def _on_size(self, event):
        self.reInitBuffer = True
        self.Refresh()

    def received_data(self, *args, **kw):
        pass

    def set_scale(min_height=0, max_height=10000):
        self.min_height = min_height
        self.max_height = max_height


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
