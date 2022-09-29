import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

export_width = 240
export_height = 160
preserveAspectRatio = "none"

export_dirName = "{}x{}".format(export_width, export_height)

current_path = os.getcwd()
dir_1x1 = os.path.join(current_path, "flags", "1x1")
dir_4x3 = os.path.join("flags", "4x3")

files = []
for (dirpath, dirnames, filenames) in os.walk(dir_1x1):
    files.extend(filenames)
    break


def modify_size(directory, files):
    path = os.path.join(directory, export_dirName)
    for f in files:
        filename = os.path.join(directory, f)
        update = False
        with open(filename, "r") as flag:
            lines = flag.readlines()
            if lines[0].find("width") == -1 and lines[0].find("height") == -1 and lines[0].find("viewBox") > 0:
                line = lines[0]
                line_moded = line[:-2]
                line_moded = line_moded + ' width="{}" height="{}" preserveAspectRatio="{}">{}'.format(export_width, export_height, preserveAspectRatio, "\n")
                lines[0] = line_moded
                print(line_moded)
                update = True
                
        if update:
            filename = os.path.join(path, f)
            if os.path.isdir(path):
                with open(filename, "w") as flag:
                    flag.writelines(lines)
            else:
                os.mkdir(path)
                with open(filename, "w") as flag:
                    flag.writelines(lines)
                    
    for file in os.listdir(path):
        print(file)
        filename = os.path.join(path, file)
        print(os.path.isfile(filename))
        if os.path.isfile(filename) and filename.endswith(".svg"):
            drawing = svg2rlg(filename)
            renderPM.drawToFile(drawing, "{}.png".format(filename[:-4]), fmt="PNG")

modify_size(dir_1x1, files)
# add_ids(dir_4x3)



