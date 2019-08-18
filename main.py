#!/usr/bin/env python3
# vim:fileencoding=UTF-8
# -*- coding: UTF-8 -*-
# Created: 15.06.2019
# Copyright (c) 2019 Vladimir Nekrasov
# License: The MIT License

"""
ZWO ASI120MC modeling main module
"""

import os
import sys
from config import *
# import logging
import ser

# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import numpy as np


# LOGGING_FORMAT = u'%(filename)s:%(lineno)d: %(levelname)-8s [%(asctime)s] %(message)s'
# logging.basicConfig(format=LOGGING_FORMAT, level=logging.DEBUG, stream=sys.stdout)


# def save(name='', fmt='png'):
#     """
#     Save graph as picture
#     """
#     pwd = os.getcwd()
#     i_path = './pictures/{}'.format(fmt)
#     if not os.path.exists(i_path):
#         os.mkdir(i_path)
#     os.chdir(i_path)
#     plt.savefig('{}.{}'.format(name, fmt), fmt='png')
#     os.chdir(pwd)
#     #plt.close()


def main(argv):
    """
    The main function
    """
    logging.info('%s started.\n', argv[0])

    dir_frames_files = '/media/nww/My Book/Astro/Калибровка ZWO ASI120MC/'
    bad_frames_files = {
        'ASICAP_2019-05-26_14_57_16_519.SER': [0, 24, ],
        'ASICAP_2019-05-27_20_28_20_715.SER': [i for i in range(2, 50)],
        'ASICAP_2019-05-30_19_25_35_038.SER': [31, 55],
        'ASICAP_2019-06-01_12_13_38_230.SER': [5, 7, 48, ],
        'ASICAP_2019-06-03_21_18_12_392.SER': [2, 5],
        'ASICAP_2019-06-06_07_26_52_321.SER': [11, 12, 13, 14, 15, 36, 37, 38, 39, 42, 45, 46, ],
        'ASICAP_2019-06-08_11_59_50_148.SER': [],
        'ASICAP_2019-06-09_09_08_45_326.SER': [],
        'ASICAP_2019-06-10_17_40_44_257.SER': [49],
        'ASICAP_2019-06-14_20_16_14_624.SER': [11, 16, 27, 38, 39, ],
        'ASICAP_2019-06-15_22_33_02_393.SER': [],
        'ASICAP_2019-06-16_08_34_15_481.SER': [49],
        'ASICAP_2019-06-16_14_53_10_561.SER': [],
        'ASICAP_2019-06-16_21_53_09_221.SER': [],
        'ASICAP_2019-06-17_18_36_01_199.SER': [],
        'ASICAP_2019-06-18_17_22_38_943.SER': [],
        'ASICAP_2019-06-18_21_57_52_911.SER': [],
        'ASICAP_2019-06-19_05_53_39_991.SER': [0],
        'ASICAP_2019-06-19_16_36_57_102.SER': [],
        'ASICAP_2019-06-19_21_24_34_737.SER': [],
        'ASICAP_2019-06-20_18_29_58_066.SER': [],
        'ASICAP_2019-06-21_18_15_15_795.SER': [0],
        'ASICAP_2019-06-21_21_24_42_580.SER': [],
        'ASICAP_2019-06-22_08_23_19_649.SER': [],
        'ASICAP_2019-06-22_11_40_54_969.SER': [],
        'ASICAP_2019-06-22_13_58_11_457.SER': [],
        'ASICAP_2019-06-22_16_58_59_288.SER': [],
        'ASICAP_2019-06-22_18_19_57_156.SER': [],
        'ASICAP_2019-06-22_21_51_38_009.SER': [],
        'ASICAP_2019-06-22_22_53_26_805.SER': [],
        'ASICAP_2019-06-23_08_29_18_533.SER': [],
        'ASICAP_2019-06-23_10_17_48_617.SER': [],
        'ASICAP_2019-06-23_11_34_16_273.SER': [],
        'ASICAP_2019-06-23_12_58_53_167.SER': [],
        'ASICAP_2019-06-23_13_36_42_723.SER': [],
        'ASICAP_2019-06-23_14_18_48_951.SER': [],
        'ASICAP_2019-06-23_14_56_53_993.SER': [],
        'ASICAP_2019-06-23_15_26_52_431.SER': [],
        'ASICAP_2019-06-23_15_50_29_035.SER': [],
        'ASICAP_2019-06-23_16_12_28_450.SER': [],
        'ASICAP_2019-06-23_16_33_23_726.SER': [],
        'ASICAP_2019-06-23_16_57_48_160.SER': [],
        'ASICAP_2019-06-23_17_05_00_410.SER': [],
        'ASICAP_2019-06-23_17_21_40_270.SER': [],
        'ASICAP_2019-06-23_17_28_19_714.SER': [],
        'ASICAP_2019-06-23_17_35_10_812.SER': [],
        'ASICAP_2019-06-23_17_41_33_046.SER': [],
        'ASICAP_2019-06-23_17_45_10_580.SER': [],
        'ASICAP_2019-06-23_17_48_40_563.SER': [],
        'ASICAP_2019-06-23_17_52_17_049.SER': [],
        'ASICAP_2019-06-23_17_55_40_074.SER': [],
        'ASICAP_2019-06-23_17_59_13_141.SER': [],
        'ASICAP_2019-06-23_18_01_05_417.SER': [],
        'ASICAP_2019-06-23_18_02_52_603.SER': [],
        'ASICAP_2019-06-23_18_04_45_294.SER': [],
        'ASICAP_2019-06-23_18_06_26_654.SER': [],
        'ASICAP_2019-06-23_18_08_30_316.SER': [],
        'ASICAP_2019-06-23_18_09_35_935.SER': [],
        'ASICAP_2019-06-23_18_10_51_459.SER': [],
        'ASICAP_2019-06-23_18_11_57_810.SER': [1],
        'ASICAP_2019-06-23_18_13_08_344.SER': [],
        'ASICAP_2019-06-23_18_14_29_504.SER': [],
        'ASICAP_2019-06-23_18_15_00_300.SER': [],
        'ASICAP_2019-06-23_18_15_29_684.SER': [],
        'ASICAP_2019-06-23_18_15_57_939.SER': [],
        'ASICAP_2019-06-23_18_16_23_762.SER': [],
        'ASICAP_2019-06-23_18_17_00_508.SER': [],
        'ASICAP_2019-06-23_18_17_17_403.SER': [],
        'ASICAP_2019-06-23_18_17_35_859.SER': [],
        'ASICAP_2019-06-23_18_17_55_570.SER': [],
        'ASICAP_2019-06-23_18_18_13_183.SER': [],
        'ASICAP_2019-06-23_18_18_42_632.SER': [],
        'ASICAP_2019-06-23_18_19_03_872.SER': [],
        'ASICAP_2019-06-23_18_19_31_141.SER': [],
        'ASICAP_2019-06-23_18_19_50_198.SER': [],
        'ASICAP_2019-06-23_18_20_06_316.SER': [],
        'ASICAP_2019-06-23_18_20_53_375.SER': [],
        'ASICAP_2019-06-23_18_21_23_375.SER': [],
        'ASICAP_2019-06-23_18_21_54_691.SER': [],
        'ASICAP_2019-06-23_18_22_25_288.SER': [],
        'ASICAP_2019-06-23_18_22_53_060.SER': [],
        'ASICAP_2019-06-23_18_23_37_684.SER': [],
        'ASICAP_2019-06-23_18_23_52_529.SER': [],
        'ASICAP_2019-06-23_18_24_08_613.SER': [],
        'ASICAP_2019-06-23_18_24_23_881.SER': [],
        'ASICAP_2019-06-23_18_24_36_250.SER': [],
        'ASICAP_2019-06-23_18_25_01_317.SER': [],
        'ASICAP_2019-06-23_18_25_18_499.SER': [],
        'ASICAP_2019-06-23_18_25_35_460.SER': [],
        'ASICAP_2019-06-23_18_25_52_414.SER': [],
        'ASICAP_2019-06-23_18_26_08_114.SER': [],
        'ASICAP_2019-06-23_18_26_31_111.SER': [],
        'ASICAP_2019-06-23_18_26_47_709.SER': [],
        'ASICAP_2019-06-23_18_27_03_604.SER': [],
        'ASICAP_2019-06-23_18_27_23_398.SER': [],
        'ASICAP_2019-06-23_18_27_41_168.SER': [],
        'ASICAP_2019-06-23_18_28_03_650.SER': [],
        'ASICAP_2019-06-23_18_28_18_490.SER': [],
        'ASICAP_2019-06-23_18_28_33_549.SER': [0],
        'ASICAP_2019-06-23_18_28_50_060.SER': [],
        'ASICAP_2019-06-23_18_29_02_480.SER': [],
        'ASICAP_2019-06-23_18_29_25_724.SER': [],
        'ASICAP_2019-06-23_18_29_39_713.SER': [],
        'ASICAP_2019-06-23_18_29_55_308.SER': [],
        'ASICAP_2019-06-23_18_30_13_547.SER': [],
        'ASICAP_2019-06-23_18_30_28_768.SER': [],
        'ASICAP_2019-06-23_18_30_50_667.SER': [],
        'ASICAP_2019-06-23_18_31_07_454.SER': [],
        'ASICAP_2019-06-23_18_31_25_754.SER': [],
        'ASICAP_2019-06-23_18_31_41_524.SER': [],
        'ASICAP_2019-06-23_18_31_55_915.SER': [],
        'ASICAP_2019-06-23_18_32_23_242.SER': [],
        'ASICAP_2019-06-23_18_32_40_596.SER': [],
        'ASICAP_2019-06-23_18_32_56_869.SER': [],
        'ASICAP_2019-06-23_18_33_14_292.SER': [],
        'ASICAP_2019-06-23_18_33_29_413.SER': [],
        'ASICAP_2019-06-23_18_33_52_619.SER': [],
        'ASICAP_2019-06-23_18_34_08_159.SER': [],
        'ASICAP_2019-06-23_18_34_22_607.SER': [],
        'ASICAP_2019-06-23_18_34_45_934.SER': [],
        'ASICAP_2019-06-23_18_35_00_887.SER': [],
        'ASICAP_2019-06-23_18_35_22_978.SER': [],
        'ASICAP_2019-06-23_18_35_39_644.SER': [],
        'ASICAP_2019-06-23_18_35_56_873.SER': [],
        'ASICAP_2019-06-23_18_36_12_730.SER': [],
        'ASICAP_2019-06-23_18_36_32_391.SER': [],
        'ASICAP_2019-06-23_18_36_54_866.SER': [],
        'ASICAP_2019-06-23_18_37_19_665.SER': [],
        'ASICAP_2019-06-23_18_37_36_374.SER': [],
        'ASICAP_2019-06-23_18_37_50_814.SER': [],
        'ASICAP_2019-06-23_18_38_04_870.SER': [],
        'ASICAP_2019-06-23_18_38_42_962.SER': [],
        'ASICAP_2019-06-23_18_39_08_425.SER': [],
        'ASICAP_2019-06-23_18_39_26_095.SER': [],
        'ASICAP_2019-06-23_18_39_43_608.SER': [],
        'ASICAP_2019-06-23_18_39_56_276.SER': [],
        'ASICAP_2019-06-23_18_40_14_838.SER': [],
        'ASICAP_2019-06-23_18_40_34_086.SER': [],
        'ASICAP_2019-06-23_18_40_51_158.SER': [],
        'ASICAP_2019-06-23_18_41_09_997.SER': [],
        'ASICAP_2019-06-23_18_41_22_185.SER': [],
    }

    files = bad_frames_files.keys()
    files = sorted(files)

    # Для всех файлов из списка
    for file_name in files:
        pathname = os.path.join(dir_frames_files, file_name)
        with ser.ser(pathname) as tser:
            framecount      = tser.framecount
            Brightness      = tser.Brightness
            Exposure        = tser.Exposure
            Gain            = tser.Gain
            Temperature     = tser.Temperature
            White_Balance_B = tser.White_Balance_B
            White_Balance_R = tser.White_Balance_R
            # Для всех изображений из файла
            for n_frame in range(tser.framecount):
                logging.debug(n_frame)

#             plt.imshow(tser.frames[0])
#             plt.show()
#             for i in range(16):
#                 logging.debug(tser.frames[i][:3])

#     logging.debug(os.getcwd())
#     logging.debug('Current version on matplotlib library is %s', mpl.__version__)
# 
#     fig = plt.figure()    # Создание объекта Figure
#     ax = fig.gca(projection='3d')
# #     print(fig.axes)       # Список текущих областей рисования пуст
# #     print(type(fig))      # тип объекта Figure
# #     plt.scatter(1.0, 1.0) # scatter - метод для нанесения маркера в точке (1.0, 1.0)
# #     plt.plot_wireframe([x for x in range(10)], [x for x in range(10)], [x for x in range(10)])
# 
#     # Make data.
# #     X = np.arange(-5, 5, 0.25)
# #     Y = np.arange(-5, 5, 0.25)
# #     X, Y = np.meshgrid(X, Y)
# #     R = np.sqrt(X**2 + Y**2)
# #     Z = np.sin(R)
#     X = [-1, 0, 1, 1, 0, -1]
#     Y = [-1, -1, -1, 1, 1, 1]
#     Z = [1, -1, 1, -1, 1, -1]
# 
#     # Plot the surface.
# #     surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
# #                            linewidth=0, antialiased=False)
#     surf = ax.plot_surface(X, Y, Z)
# 
#     # После нанесения графического элемента в виде маркера
#     # список текущих областей состоит из одной области
# #     print(fig.axes)
# 
# #     # смотри преамбулу
# #     save(name='pic_1_4_1', fmt='pdf')
# #     save(name='pic_1_4_1', fmt='png')
# 
#     plt.show()

    logging.info('%s finished.\n', argv[0])
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
