#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 无需依赖的接口 在测试函数的参数中不传入"is_login"
import pytest
import allure
from basic.request import req
from common.api_data import testinfo
from basic.checkresult import check_results


@allure.feature("单个API测试")
class TestStandAlone:

    @pytest.mark.parametrize('case', testinfo.stand_alone.values(), ids=testinfo.stand_alone.keys())
    def test_stand_alone_interface(self, case):
        r = req(case['method'], case['route'], case.get('extractresult'), **case['RequestData'])
        check_results(r, case)

if __name__ == "__main__":
    pytest.main(['test_stand_alone.py', '-s', '-v'])
