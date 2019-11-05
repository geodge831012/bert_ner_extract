# -*- coding:utf-8 -*-
from distutils.core import setup
from Cython.Build import cythonize
import numpy as np
setup(ext_modules=cythonize(['ner_extract.py', 'news_provider.py', 'label_processor.py']), include_dirs = [np.get_include()])
