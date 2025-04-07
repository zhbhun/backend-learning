输入音频 =》音频分析（librosa/essentia 提取频谱、响度、频段能量） =》EQ 推荐算法（根据分析自动生成 EQ 配置）=》润色处理（ffmpeg / sox / pydub 应用 EQ、压缩、de-esser 等）=》输出音频

## 分析

- [librosa](https://github.com/librosa/librosa) - Python library for audio and music analysis
- [essentia](https://github.com/MTG/essentia) - C++ library for audio and music analysis, description and synthesis, including Python bindings

## 处理

- ffmpeg
- sox
- pydub

### 自动 EQ 处理

- [AutoEq](https://github.com/jaakkopasanen/AutoEq)

```bash
ffmpeg -i input.wav -af \
"equalizer=f=80:t=q:w=1:g=-6,\
equalizer=f=1500:t=q:w=1.2:g=4,\
equalizer=f=8000:t=q:w=2:g=-4" \
output_eq.wav
```

### 响度归一 / loudnorm / LUFS

- [ffmpeg-normalize](https://github.com/slhck/ffmpeg-normalize) - 

```bash
ffmpeg -i input.wav -af loudnorm=I=-16:TP=-1.5:LRA=11 output_loud.wav
```

### 降噪

- [rnnoise](https://github.com/xiph/rnnoise): 高效降噪模型
- [afftdn](https://ffmpeg.org/ffmpeg-filters.html#afftdn): 频域去噪

### 压缩器

- ...

## 参考

- [让声音更好听——EQ均衡器](https://www.bilibili.com/opus/377302225442210596)
- [如何对人声进行均衡：新手入门指南](https://emastered.com/zh/blog/how-to-eq-vocals)
- [新手如何通过均衡器完美处理人声](https://m.midifan.com/article_body.php?id=7268)
