import os
import nbformat
from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor

import sys # bugfix after 26.01.2021
import asyncio # bugfix after 26.01.2021

if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'): # bugfix after 26.01.2021
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # bugfix after 26.01.2021


def converter(input_file):
    f = open(input_file, 'r', encoding='utf-8').read()
    jake_notebook = nbformat.reads(f, as_version=4)
    jake_notebook.cells[0]
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(jake_notebook, {'metadata': {'path': 'C:\\Scripts\\temp'}})
    html_exporter = HTMLExporter()
    (body, resources) = html_exporter.from_notebook_node(jake_notebook)
    with open(input_file.split('.ipynb')[0] + '.html', 'w', encoding='utf-8') as out:
        out.write(body)


path = 'C:\\Scripts\\temp\\'

converter(f'{path}temp0001.ipynb')
converter(f'{path}temp0002.ipynb')
converter(f'{path}temp0003.ipynb')
converter(f'{path}temp0004.ipynb')
converter(f'{path}temp0005.ipynb')
converter(f'{path}temp0006.ipynb')
converter(f'{path}temp0007.ipynb')
converter(f'{path}temp0008.ipynb')
converter(f'{path}temp0009.ipynb')
converter(f'{path}temp0010.ipynb')
converter(f'{path}temp0011.ipynb')
converter(f'{path}temp0012.ipynb')
converter(f'{path}temp0013.ipynb')
converter(f'{path}temp0014.ipynb')
converter(f'{path}temp0015.ipynb')
converter(f'{path}temp0016.ipynb')
converter(f'{path}temp0017.ipynb')
converter(f'{path}temp0018.ipynb')
converter(f'{path}temp0019.ipynb')
converter(f'{path}temp0020.ipynb')
converter(f'{path}temp0021.ipynb')
converter(f'{path}temp0022.ipynb')
converter(f'{path}temp0023.ipynb')
converter(f'{path}temp0024.ipynb')
converter(f'{path}temp0025.ipynb')
converter(f'{path}temp0026.ipynb')
converter(f'{path}temp0027.ipynb')
converter(f'{path}temp0028.ipynb')
converter(f'{path}temp0029.ipynb')
converter(f'{path}temp0030.ipynb')
converter(f'{path}temp0031.ipynb')
converter(f'{path}temp0032.ipynb')
converter(f'{path}temp0033.ipynb')