# 导包
import unittest
from tools.HTMLTestRunner import HTMLTestRunner
# 组装测试套件
suite= unittest.defaultTestLoader.discover("./scripts",pattern="test*.py")

# 获取报告存储文件夹 实例化HTMLTestRunner 调用run执行测试套件
with open("./report/ihrm_report.html","wb") as f:
    HTMLTestRunner(stream=f).run(suite)