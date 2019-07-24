#encoding=utf-8

from django.http import JsonResponse
from django.shortcuts import render
import time


num_progress = 0 # 当前的后台进度值（不喜欢全局变量也可以很轻易地换成别的方法代替）




'''
展示界面 UI
'''
def show_progress1(request):
    # return JsonResponse(num_progress, safe=False)
    return render(request, 'datahexun.html')



'''
后台实际处理程序
'''
def process_data(request):
    # ...
    global num_progress

    for i in range(12345666):
        # ... 数据处理业务
        num_progress = i * 100 / 12345666; # 更新后台进度值，因为想返回百分数所以乘100
        # print 'num_progress=' + str(num_progress)
        # time.sleep(1)
        res = num_progress
        # print 'i='+str(i)
        # print 'res----='+str(res)
    return JsonResponse(res, safe=False)

'''
前端JS需要访问此程序来更新数据
'''
def show_progress(request):
    print 'show_progress----------'+str(num_progress)
    return JsonResponse(num_progress, safe=False)
