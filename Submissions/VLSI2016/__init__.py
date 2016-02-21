__author__ = 'lunzhy'
import platform, os

if platform.system() == 'Linux':
    Directory_VLSI2016 = r'/home/lunzhy/SimCTM/projects/VLSI2016'
    Folder_Save_Figure = r'figures'
elif platform.system() == 'Windows':
    Directory_VLSI2016 = r'E:\PhD Study\Submissions\VLSI2016\SctmData'
    Folder_Save_Figure = r'py_figures'

IsSaveFigure = True


def drawFig(fig, name):
    if IsSaveFigure:
        fig_path = os.path.join(Directory_VLSI2016, Folder_Save_Figure, name)
        fig.savefig(fig_path+'.png', dpi=800, bbox_inches='tight', pad_inches=0.1)
    return
