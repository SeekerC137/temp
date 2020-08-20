import os
import nbformat
from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor

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

converter('temp0001.ipynb')
converter('temp0002.ipynb')
converter('temp0003.ipynb')
converter('temp0004.ipynb')
converter('temp0005.ipynb')
converter('temp0006.ipynb')
converter('temp0007.ipynb')
converter('temp0008.ipynb')
converter('temp0009.ipynb')
converter('temp0010.ipynb')
converter('temp0011.ipynb')
converter('temp0012.ipynb')
converter('temp0013.ipynb')
converter('temp0014.ipynb')
converter('temp0015.ipynb')
converter('temp0016.ipynb')
converter('temp0017.ipynb')
converter('temp0018.ipynb')
converter('temp0019.ipynb')
converter('temp0020.ipynb')
converter('temp0021.ipynb')
converter('temp0022.ipynb')
converter('temp0023.ipynb')
converter('temp0024.ipynb')
converter('temp0025.ipynb')
converter('temp0026.ipynb')
converter('temp0027.ipynb')
converter('temp0028.ipynb')
converter('temp0029.ipynb')
converter('temp0030.ipynb')
converter('temp0031.ipynb')
converter('temp0032.ipynb')
converter('temp0033.ipynb')