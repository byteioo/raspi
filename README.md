# raspi
### 一个在线管理树莓派的web网页
------

纯属按照个人需求定制的，所需模块如下：

> * DHT11  (使用GPIO 18)
> * 一个云台（二自由度）两个舵机都是sg90 (使用GPIO 20 21)
> * 电源模块 (驱动上面的云台)
> * picamera


该项目对GPIO的控制使用Python，且使用了flask框架，所以使用之前你需要
```
sudo pip install flask
```
倘若下载速度极慢，请换阿里的源

clone项目之后，在raspi目录下
```
nano cam/pkg/config.py
```
填写WS_URL和WS_TOKEN！！！，然后授与sh文件执行权限
```
sudo chmod +x *.sh
./start.sh
```
项目便启动了,
配合frp食用味道更佳
