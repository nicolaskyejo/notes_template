"""
A script for generating a 'tex' output file that contains image(s) in the
current directory.
"""

import os
import glob


images = glob.glob('*.png')
images.sort(key=os.path.getmtime)  # sort by modification date/time

with open('images.tex', 'w') as f:
    for image in images:
        name = image.split('.')[0]
        f.write(f"""\\begin{{figure}}[h]
    \\centering
    \\includegraphics[width=7.1cm]{{{image}}}
    \\caption{{\\textit{{{name.replace('_', ' ')}}}}}
    \\label{{fig:{name}}}
\\end{{figure}}\n\n""")
