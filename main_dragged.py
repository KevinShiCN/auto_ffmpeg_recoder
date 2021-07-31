import os
import pyautogui
import sys
# 通过拖拽至bat直接将文件路径作为输出至droppedFile
droppedFile = sys.argv[1]
print(droppedFile)
# input_file = (pyautogui.prompt(text='请输入文件路径：',
#                                title='确认文件路径', default=''))[1:-1]
# 这里input改为了拖拽来的文件名
input_file = droppedFile
output_file_full = "{}1{}".format(input_file[0:-4], input_file[-4:])
print("input_file是{}".format(input_file))
print("output_file_full是{}".format(output_file_full))
process = "ffmpeg -hwaccel cuvid -c:v h264_cuvid -i {} -c:v h264_nvenc -y {}".format(
    input_file, output_file_full)
print(process)
os.system(process)
print("文件{}转换成功！".format(output_file_full))
os.system("pause")
delete_confirmation = pyautogui.confirm(
    text="请确认是否删除文件", title='最终确认', buttons=['确定！', '否'])
if delete_confirmation == "确定！":
    os.remove(input_file)
else:
    pass
