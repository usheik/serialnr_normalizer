###########################################################
# NOON Internship BTL Tracking Tools                      #
# Dev - Umayr Sheik                                       #
# November 24 2018                                        #
# Module: SERIALNR_NORMALIZER                             #
# Script: normalizer                                      #
# Purpose: Generate a list of stores/serial_nrs           #
#          for the initial shj/abu distro                 #
###########################################################

import os
import time
import shutil
import xlrd
from collections import defaultdict

def parse_distro_sheet(file_path):
    distro_info = dict()

    book = xlrd.open_workbook(file_path, formatting_info=True)
    distro = book.sheet_by_index(0)
    codes = book.sheet_by_index(1)

    no_of_cols_distro = distro.ncols
    no_of_rows_distro = distro.nrows

    no_of_cols_codes = codes.ncols
    no_of_rows_codes = codes.nrows

    for row_index in range(0, no_of_rows_distro):
        distro_info[sheet.cell(row_index,0).value] = sheet.cell(row_index,3).value
        print ('Distro: %s - %s') % (sheet.cell(row_index,0).value, sheet.cell(row_index,3).value)
        