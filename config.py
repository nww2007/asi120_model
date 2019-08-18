#!/usr/bin/env python
# vim:fileencoding=UTF-8
# -*- coding: UTF-8 -*-

'''
Created on 5 april 2019 y.

@author: nww
'''
import logging
import sys

# logging.basicConfig(format = u'%(filename)s:%(lineno)d# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.DEBUG, filename = u'mv2log.log')
logging.basicConfig(format = u'%(filename)s:%(lineno)d: %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.DEBUG, stream=sys.stdout)
# logging.basicConfig(format = u'%(filename)s:%(lineno)d: %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.DEBUG, filename = sys.stdout)
