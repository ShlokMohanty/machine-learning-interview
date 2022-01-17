"""Thin wrapper to call TensorFlow's API generation script.
this file exists to provide a main function for the py_binary in the API generation
genrule. It just calls the main function for the actual API generation script in TensorFlow.
"""

from __future__ import absolute_import 
from __future__ import division 
from __future__ import print_function 

import keras # pylint: disable=unused-import 
from tensorflow.python.tools.api.generator import python_api 

if __name__ == '__main__':
python_api.main()
