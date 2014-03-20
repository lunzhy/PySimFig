__author__ = 'Lunzhy'
import os, re, sys
path = os.path.abspath(os.path.dirname(__file__))
#path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
if not path in sys.path:
    sys.path.append(path)
import common as cm

def getParamValue(param_name, prj_path):
    default_param_path = cm.Default_Parfile_Path
    user_param_path = os.path.join(prj_path, cm.User_Param_File)
    # first search the default parameters
    for file in [user_param_path, user_param_path]:
        if not os.path.exists(file):
            print('This file does not exist. %s' % file)
            continue
        f = open(file)
        lines = f.read()
        pattern = re.compile(param_name + r'\s*:.*')
        match = re.search(pattern, lines)
        if match != None:
            found_line = match.group()
        split_line = re.split(':|#', found_line)
        value = split_line[1].strip()
    return value


def test():
    getParamValue('tc.tunnel.thick', cm.Debug_Folder_Path)


if __name__ == '__main__' : test()
