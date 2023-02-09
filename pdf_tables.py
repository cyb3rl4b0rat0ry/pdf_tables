import tabula
import sys
import os

dir = sys.argv[1]

dfs = tabula.convert_into_by_batch(dir, output_format='csv', pages='all')
