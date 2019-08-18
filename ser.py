#!/usr/bin/env python4
# vim:fileencoding=UTF-8
# -*- coding: UTF-8 -*-

"""
Created on 5 april 2019 y.

@author: nww

@doc: https://free-astro.org/index.php/File:SER_Doc_V3b.pdf
"""


import os
from config import *
import struct
import numpy as np
from matplotlib import pyplot as plt
import datetime
from progress import Progress
import configparser


class ser():
    """
    Набор методов для работы с набором изображений в формате SER
    """
    def __init__(self, fname=None):
        # luids 
        self.MONO       = 0
        self.BAYER_RGGB = 8
        self.BAYER_GRBG = 9
        self.BAYER_GBRG = 10
        self.BAYER_BGGR = 11
        self.BAYER_CYYM = 16
        self.BAYER_YCMY = 17
        self.BAYER_YMCY = 18
        self.BAYER_MYYC = 19
        self.RGB        = 100
        self.BGR        = 101

        if fname != None:
            self.read(fname)

        self.Auto_Exp_Max_Exp           = None
        self.Auto_Exp_Max_Gain          = None
        self.Auto_Exp_Target_Brightness = None
        self.Bin                        = None
        self.Brightness                 = None
        self.Capture_Area_Size          = None
        self.Capture_Limit              = None
        self.Colour_Format              = None
        self.Debayer_Preview            = None
        self.Exposure                   = None
        self.Flip                       = None
        self.Gain                       = None
        self.Hardware_Bin               = None
        self.High_Speed_Mode            = None
        self.Mono_Bin                   = None
        self.Output_Format              = None
        self.OverClock                  = None
        self.Raw_Foramt                 = None
        self.StartX                     = None
        self.StartY                     = None
        self.Temperature                = None
        self.Timestamp_Frames           = None
        self.Turbo_USB                  = None
        self.White_Balance_B            = None
        self.White_Balance_R            = None

        if os.path.isfile(fname + '.txt'):
            config = configparser.ConfigParser()
            config.read(fname + '.txt')

            self.Auto_Exp_Max_Exp           = config['ZWO ASI120MC']['Auto Exp Max Exp']
            self.Auto_Exp_Max_Gain          = config['ZWO ASI120MC']['Auto Exp Max Gain']
            self.Auto_Exp_Target_Brightness = config['ZWO ASI120MC']['Auto Exp Target Brightness']
            self.Bin                        = config['ZWO ASI120MC']['Bin']
            self.Brightness                 = config['ZWO ASI120MC']['Brightness']
            self.Capture_Area_Size          = config['ZWO ASI120MC']['Capture Area Size']
            self.Capture_Limit              = config['ZWO ASI120MC']['Capture Limit']
            self.Colour_Format              = config['ZWO ASI120MC']['Colour Format']
            self.Debayer_Preview            = config['ZWO ASI120MC']['Debayer Preview']
            self.Exposure                   = config['ZWO ASI120MC']['Exposure']
            self.Flip                       = config['ZWO ASI120MC']['Flip']
            self.Gain                       = config['ZWO ASI120MC']['Gain']
            self.Hardware_Bin               = config['ZWO ASI120MC']['Hardware Bin']
            self.High_Speed_Mode            = config['ZWO ASI120MC']['High Speed Mode']
            self.Mono_Bin                   = config['ZWO ASI120MC']['Mono Bin']
            self.Output_Format              = config['ZWO ASI120MC']['Output Format']
#             self.OverClock                  = config['ZWO ASI120MC']['OverClock']
            self.Raw_Foramt                 = config['ZWO ASI120MC']['Raw Foramt']
            self.StartX                     = config['ZWO ASI120MC']['StartX']
            self.StartY                     = config['ZWO ASI120MC']['StartY']
            self.Temperature                = config['ZWO ASI120MC']['Temperature']
            self.Timestamp_Frames           = config['ZWO ASI120MC']['Timestamp Frames']
            self.Turbo_USB                  = config['ZWO ASI120MC']['Turbo USB']
            self.White_Balance_B            = config['ZWO ASI120MC']['White Balance (B)']
            self.White_Balance_R            = config['ZWO ASI120MC']['White Balance (R)']


    def __exit__(self, type, value, tb):
        """
        """
        pass


    def __enter__(self):
        """
        """
        return self


    def read(self, fname):
        """
        Загружаем информацию из файла
        """
        self.fname = fname

        # Зпгружаем информацию из заголовка
        with open(self.fname, 'rb') as fd:
            self.header = fd.read(178)
            self.parse_header()

#             self.framecount = 2 # ?????????????????
            self.frames = np.zeros((self.framecount, self.imageheight, self.imagewidth))
            tmp_array = np.zeros(self.imagewidth)
            dt = np.dtype(np.int16)
            dt = dt.newbyteorder('<')
            for frame in range(self.framecount):
                Progress(frame, self.framecount)

                t_frame = fd.read(self.imageheight * self.imagewidth * self.pixeldepthperplane//8)
#                 for line in range(self.imageheight):
#                     for pixel in range(self.imagewidth):
#                         index = (line * self.imagewidth + pixel) * 2
#                         self.frames[frame][line][pixel] = struct.unpack('<H', t_frame[index:index+2])[0]
#                 logging.debug(self.frames[frame][0])

                for line in range(self.imageheight):
#                     t_line = fd.read(self.imagewidth * self.pixeldepthperplane//8)
                    t_line = t_frame[line * self.imagewidth * 2 : (line * self.imagewidth + self.imagewidth) * 2]
                    t_a    = np.frombuffer(t_line, dtype=dt)
                    self.frames[frame][line] = t_a
#                 logging.debug(t_line[:7])
#                 logging.debug(self.frames[frame][0])
#                 logging.debug('')

            self.trailer = fd.read(self.framecount * 8)
            self.parse_trailer()

#         plt.imshow(self.frames[0], interpolation='nearest')
#         plt.show()
#         logging.debug(self.frames[0].max(), self.frames[0].min())


    def parse_header(self):
        """
        """
        self.fileid             = self.header[0:14]
        self.luid               = struct.unpack('<i', self.header[14:18])[0]
        self.colorid            = struct.unpack('<i', self.header[18:22])[0]
        self.littleendian_FALSE = 0
        self.littleendian_TRUE  = 1
        self.littleendian       = struct.unpack('<i', self.header[22:26])[0]
        self.imagewidth         = struct.unpack('<i', self.header[26:30])[0]
        self.imageheight        = struct.unpack('<i', self.header[30:34])[0]
        self.pixeldepthperplane = struct.unpack('<i', self.header[34:38])[0]
        self.framecount         = struct.unpack('<i', self.header[38:42])[0]
        self.observer           = self.header[42:82]
        self.telescope          = self.header[82:122]
        self.datetime           = struct.unpack('<q', self.header[122:130])[0]
        self.datetime_utc       = struct.unpack('<q', self.header[130:138])[0]
#         logging.info('{0}x{1}'.format(self.imagewidth, self.imageheight))


    def parse_trailer(self):
        """
        """
        for i in range(0, self.framecount*8, 8):
#             logging.debug(struct.unpack('<Q', self.trailer[i:i+8])[0])
#             tuli = (struct.unpack('<Q', self.trailer[i:i+8])[0] - 116444736000000000) / 10000000
#             tuli = (struct.unpack('<Q', self.trailer[i:i+8])[0] - 481184899200000000) / 10000000
#             tuli = (struct.unpack('<Q', self.trailer[i:i+8])[0] - 4811848992000000000) / 10000000
            tuli = (struct.unpack('<Q', self.trailer[i:i+8])[0])
#             tuli += 226332006210048.0
#             logging.debug('tuli=%f' % (tuli))
#             t, ms = divmod(tuli, 10000000)
#             logging.debug('t=%f, ms=%f %f' % (t, ms, 10000000))
#             t, s = divmod(t, 60)
#             logging.debug('t=%f, s=%f %f' % (t, s, 60))
#             t, m = divmod(t, 60)
#             logging.debug('t=%f, m=%f %f' % (t, m, 60))
#             t, h = divmod(t, 24)
#             logging.debug('t=%f, h=%f %f' % (t, h, 24))
#             y, d = divmod(t, 365.25)
#             logging.debug('t=%f, d=%f %f' % (y, d, 365.25))
#             logging.debug('y=%f, d=%f, h=%f, m=%f, s=%f, ms=%f' % (y, d, h, m, s, ms))
#             tuli = (struct.unpack('<Q', self.trailer[i:i+8])[0] - 481184899200000000) / 10
#             logging.debug(datetime.datetime.fromtimestamp(datetime.timedelta(microseconds=tuli) + datetime.datetime(1970, 1, 1)))
#             logging.debug(datetime.timedelta(microseconds=tuli) + datetime.datetime(1970, 1, 1))
#             logging.debug(datetime.timedelta(microseconds=tuli))


    def show_header(self):
        """
        """
        print('fileid = %s'             % (self.fileid))
        print('luid = %s'               % (self.luid))
        print('colorid = %s'            % (self.colorid))
        print('littleendian_FALSE = %s' % (self.littleendian_FALSE))
        print('littleendian_TRUE = %s'  % (self.littleendian_TRUE))
        print('littleendian = %s'       % (self.littleendian))
        print('imagewidth = %s'         % (self.imagewidth))
        print('imageheight = %s'        % (self.imageheight))
        print('pixeldepthperplane = %s' % (self.pixeldepthperplane))
        print('framecount = %s'         % (self.framecount))
        print('observer = %s'           % (self.observer))
        print('telescope = %s'          % (self.telescope))
        print('datetime = %s'           % (self.datetime))
        print('datetime_utc = %s'       % (self.datetime_utc))


    def set_header(self, header):
        """
        """
        self.header = header
        self.parse_header()


    def write(self, fname):
        """
        """
        self.fname = fname

        with open(self.fname, 'wb') as fd:
            fd.write(self.header)
            for frame in range(self.framecount):
                logging.debug('frame = %d' % frame)
                for line in range(self.imageheight):
                    for pixel in range(self.imagewidth):
                        fd.write(struct.pack('<H', int(round(self.frames[frame][line][pixel]))))
            fd.write(self.trailer)
