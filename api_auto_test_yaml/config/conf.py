#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

# 获取项目根目录
# cur_path = os.path.abspath(os.path.dirname(os.getcwd()))
# cur_path = os.path.abspath('..')
cur_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = cur_path + r'\logs'
DATA_DIR = cur_path + r'\apiData'