# -*- coding: utf-8 -*-
import os
from PIL import Image
import numpy as np
 
def print_photo(photo_file, width=120, k=1.0, reverse=False, outfile=None):
  """打印照片，默认120个字符宽度"""
   
  im = Image.open(photo_file).convert('L') # 打开图片文件，转为灰度格式
 
 
 

  height = int(k*width*im.size[1]/im.size[0]) # 打印图像高度，k为矫正系数，用于矫正不同终端环境像素宽高比
  arr = np.array(im.resize((width, height ))) # 转为NumPy数组
  if reverse: # 反色处理
    arr = 255 - arr
   
  chs = np.array([
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','X','Y','Z','1','2','3','4','5','6','7','8','9','0']) #灰度-字符映射表
  arr= chs[(arr/32).astype(np.uint8)] # 灰度转为对应字符
   
  
  
  
  if outfile:
    with open(outfile, 'w') as fp:
      for row in arr.tolist():
        fp.write(''.join(row))
        fp.write('\n')
  else:
    for i in range(arr.shape[0]): # 逐像素打印
      for j in range(arr.shape[1]):
        print(arr[i,j], end=' ')
      

 
#if __name__ == '__main__':
print_photo('5.jpg', width=160, k=0.5, outfile='a.txt')
#os.system('notepad a.txt')
os.system('notepad a.txt')



import calendar
 
cal = calendar.month(2016, 1)

print (cal)


  
  
  


  



























































































































































































