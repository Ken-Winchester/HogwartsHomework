## chrome浏览器复用

- 退出当前的所有Chrome浏览器
  - 浏览器设置-->网站设置-->后台同步-->关闭 禁止最近关闭的网站完成数据收发操作 （不添加任何网站就是全部网站）
- 找到Chrome的启动路径
- 配置环境变量
- 启动命令(Windows)：chrome --remote-debugging-port=9898
- 启动命令(Mac):Google \ Chrome --remote-debugging-port=9898
