
import os
import sys

# sys.path.insert(0, os.path.abspath("../"))
sys.path.insert(0, os.path.dirname(__file__))


class {{cookiecutter.module_name}}(object):

    def __init__(self, feed={}):
        '''

        :param feed:
        '''
        self.checkpoint_dir = os.path.dirname(__file__)+"/checkpoint"

    def run(self, feed={}):
        '''

        :param feed:
        :return:
        '''
