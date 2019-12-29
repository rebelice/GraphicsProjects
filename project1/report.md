# Project 1 报告

`杨俊逸`
`16307130239`

## 使用说明

```
python main.py
```

### 环境需求

- python 3.8.0
- pygame 1.9.6-3
- numpy 1.17.4-1
- pyaudio 0.2.11-4

## 代码说明

1. 通过wave读入`.wav`音乐文件
2. 通过pyaudio获取音频文件流
3. 并且以Const.CHUNK为单位分隔
4. 初始化pygame
5. 播放时对每个CHUNK的时域数据进行fft后获得频域数据
6. 根据频域数据画出对应高度的矩形

