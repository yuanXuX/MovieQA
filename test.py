
import sys
import pandas as pd
from pandas import Series, DataFrame
from dataPro import Question
# 创建问题处理对象，这样模型就可以常驻内存
que=Question()
# Restore
def enablePrint():
    sys.stdout = sys.__stdout__
enablePrint()
#example
result=que.question_process("周润发是谁")
print(result)
