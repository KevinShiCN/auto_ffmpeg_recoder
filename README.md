# auto_ffmpeg_recoder

## 注意事项

此项目为个人项目，未对外部进行足够的兼容，请根据需要使用

## 使用方法

### 确保 FFmpeg 已经被下载到本地并添加至了环境变量

Github不支持超过100MB的文件！
<https://www.ffmpeg.org/>

### 安装依赖

```Bash
pip install -r requirements.txt
```

### 弹窗输入视频地址运行

main.py 运行之后一次输入一个文件地址可自动将视频转码，解决无法快进问题

### 通过拖拽文件至.bat 文件自动输出文件路径运行

可以直接将视频文件拖拽至`无法快进视频转码\_拖拽至 bat 运行.bat`文件以自动运行`main_dragged.py`脚本
