# jellyfin

```shell
# 根据系统选择下载包
# 需要指定字体 解决中文出现异常问题
# 判断cpu支持解码 https://www.cpu-monkey.com/en/ 从此网站查询
docker run -d \
           --name jellyfin \
           --restart=always \
           -e TZ=Asia/Shanghai \
           -p 8096:8096 \
           -p 8920:8920 \
           -v /data/docker/jellyfin/config:/config \
           -v /data/docker/jellyfin/cache:/cache \
           -v /data/Media:/media \
           # 使用特殊网络连接 或者 修改hosts文件 来访问插件仓库 二选一即可
           -e HTTP_PROXY=http://ip:port \
           -e HTTPS_PROXY=http://ip:port \
           -v /volume1/docker/jellyfin/hosts:/etc/hosts \
           # 修改系统自带的字体
           -v /data/docker/jellyfin/dejavu:/usr/share/fonts/truetype/dejavu \
           # 增加备用字体
           -v /data/docker/jellyfin/Fonts:/Fonts \
           # 增加https证书配置
           -v /volume2/docker/jellyfin/certs:/certs \
           # intel/amd gpu解码映射
           --device /dev/dri/renderD128:/dev/dri/renderD128 \
           # nvidia gpu解码映射
           --runtime=nvidia --gpus all \
           jellyfin/jellyfin:latest

# 添加其他源
# MetaShark
https://github.com/cxfksword/jellyfin-plugin-metashark/releases/download/manifest/manifest.json
# MeiamSubtitles
https://github.com/91270/MeiamSubtitles.Release/raw/main/Plugin/manifest-stable.json

# 添加主题 在 控制台 - 常规 - 自定义CSS代码 加入以下代码 保存即可
@import url("https://cdn.jsdelivr.net/npm/jellyskin@latest/dist/main.css");
@import url("https://cdn.jsdelivr.net/npm/jellyskin@latest/dist/logo.css");
@import url("https://cdn.jsdelivr.net/npm/jellyskin@latest/dist/addons/gradients/sea.css");

# 设置硬件转码 以e3-1246 v3为例
# 转码 选择 QSV
# 硬件解码 选择 H264 VC1 取消选择 首选系统原生的DXVA或VA-API硬件解码器
# 硬件编码选项 启用硬件编码
# 选择 启用VPP色调映射
# 添加备用字体路径 /Fonts 勾选启用备用字体

# 设置字幕
# 个人设置 - 字幕
# 语言偏好 中文
# 字幕模式 智能模式
# 烧录字幕 全部
```

