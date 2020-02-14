# 导包
import unittest
from tools.HTMLTestRunner import HTMLTestRunner
# 组装测试套件
suite= unittest.defaultTestLoader.discover("./scripts",pattern="test*.py")

# 获取报告存储文件夹 实例化HTMLTestRunner 调用run执 行测试套  件
with open("./report/report.html","wb") as f:
    HTMLTestRunner(stream=f).run(suite)