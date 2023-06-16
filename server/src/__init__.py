import os

try:
    from .api import application
except Exception as ex:
    os.environ['OPENBLAS_NUM_THREADS'] = '1'
    from .api import application
    print(ex)
