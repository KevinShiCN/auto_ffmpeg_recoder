import os
import pyautogui
input_file = (pyautogui.prompt(text='请输入文件路径：',
                               title='确认文件路径', default=''))[1:-1]
output_file_full = "{}1{}".format(input_file[0:-4], input_file[-4:])
print("input_file是{}".format(input_file))
print("output_file_full是{}".format(output_file_full))
process = "ffmpeg.exe -hwaccel cuvid -c:v h264_cuvid -i {} -c:v h264_nvenc -y {}".format(
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
