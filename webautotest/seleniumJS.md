### document.title

- 获取页面标题

### window.alert("Hello selenium")

- 进行alert窗口

### JSON.stringify(performance.timing)

- 获取当前浏览器页面的性能数据

execute_script 执行JS

return 返回js的返回结果

document.documentElement.scrollTop=123

大部分时间控件都是readonly属性，自动化中对该类控件操作可以使用JS操作

处理思路： 要取消日期的readonly属性 给value赋值 用js实现上述两点，然后在用webdriver对js进行处理

