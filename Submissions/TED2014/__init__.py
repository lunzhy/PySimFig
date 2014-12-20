__author__ = 'lunzhy'
import platform, os

if platform.system() == 'Linux':
    Directory_TED2014 = r'/home/lunzhy/SimCTM/projects/TED2014'
    Folder_Save_Figure = r'figures'
elif platform.system() == 'Windows':
    Directory_TED2014 = r'E:\PhD Study\Submissions\TED2014\SctmData'
    Folder_Save_Figure = r'py_figures'

IsSaveFigure = True

def drawFig(fig, name):
    if IsSaveFigure:
        fig_path = os.path.join(Directory_TED2014, Folder_Save_Figure, name)
        fig.savefig(fig_path+'.png', dpi=800, bbox_inches='tight', pad_inches=0.1)
    return
