#!/usr/bin/env python3
# vim:fileencoding=UTF-8
# -*- coding: UTF-8 -*-

"""
Created on 19 may 2019 y.
"""

import sys
from numpy import interp


class Progress:
    """
    Progress bar class
    """
    def __init__(self, value, end, title='Downloading', buffer=20):
        self.title = title
        #when calling in a for loop it doesn't include the last number
        self.end = end -1
        self.buffer = buffer
        self.value = value
        self.progress()


    def progress(self):
        """
        Progress bar method
        """
        maped = int(interp(self.value, [0, self.end], [0, self.buffer]))
        if self.end != 0:
            print(f'{self.title}: [{"#"*maped}{"-"*(self.buffer - maped)}]\
                    {self.value}/{self.end} {((self.value/self.end)*100):.2f}%',
                  end='\r', flush=True, file=sys.stderr)

    def stupid(self):
        """
        Stupid
        """
        pass
