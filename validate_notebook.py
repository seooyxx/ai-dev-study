import nbformat

with open('week-1/answer.ipynb') as f:
    nb = nbformat.read(f, as_version=4)
    for cell in nb.cells:
        if cell.cell_type == 'code' and cell.execution_count is None:
            print(f'Cell {cell.source[:30]}... not executed.')
            exit(1)
    print('All cells executed successfully.')