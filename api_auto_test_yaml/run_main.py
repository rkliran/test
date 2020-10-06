#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
if __name__ == '__main__':
    os.system(r'pytest --alluredir report')
    os.system(r'COPY config\environment.properties report')
    os.system(r'allure generate report/ -o report/html')
    os.system(r'allure open allure-report')