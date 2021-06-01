import wx
import math 
from math import pi
from matplotlib.patches import Ellipse
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import \
     FigureCanvasWxAgg as FigureCanvas

# TIMER_ID = wx.NewId()


class _MonitorPlot(wx.Frame):
    def __init__(self, data, scale=1):
        self.scale = scale
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          title="FlowVB Progress Monitor", size=(800, 600))
        self.fig = Figure((8, 6), 100)
        self.canvas = FigureCanvas(self, wx.ID_ANY, self.fig)
        self.ax = self.fig.add_subplot(111)

        x_lims = [data[:, 0].min(), data[:, 0].max()]
        y_lims = [data[:, 1].min(), data[:, 1].max()]

        self.ax.set_xlim(x_lims)
        self.ax.set_ylim(y_lims)
        self.ax.set_autoscale_on(False)

        self.l_data = self.ax.plot(data[:, 0], data[:, 1], color='blue',
                               linestyle='', marker='o')

        self.canvas.draw()
        self.bg = self.canvas.copy_from_bbox(self.ax.bbox)

        self.Bind(wx.EVT_IDLE, self._onIdle)

    def update_plot(self, pos, cov):
        self.canvas.restore_region(self.bg)

        for k in range(pos.shape[0]):
            l_center, = self.ax.plot(pos[k, 0], pos[k, 1],
                                     color='red', marker='+')

            U, s, Vh = np.linalg.svd(cov[k, :, :])
            orient = math.atan2(U[1, 0], U[0, 0]) * 180 / pi
            ellipsePlot = Ellipse(xy=pos[k, :], width=2.0 * math.sqrt(s[0]),
                                  height=2.0 * math.sqrt(s[1]),
                                  angle=orient, facecolor='none',
                                  edgecolor='red')
            self.ax.add_patch(ellipsePlot)

        self.canvas.draw()
        self.canvas.blit(self.ax.bbox)