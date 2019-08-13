# 0807对MVC模式下的一些理解
  
  今天在接触自定义模板的时候出现了诸多问题，主要是对MVC工作流程不熟悉，个人理解的
  MVC工作流如下:
  1. C：app目录下的url通过re或者字符匹配相应参数传递给views视图页中的指定函数，eg:
 >re_path(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})', views.archives, name='archive')

此url匹配式匹配url中的year(4位整数)和month(2位整数)，传给views中的archives函数做参数

  2. V：views中的函数，将所需要传递给模板的数据保存在context中，传给模板，key在模板中调用，
  item为实际传入的参数值
  
  3. M： model在自定义模板工作模式下由前端html模板文件获取，自身调用，一般工作模式下由V中的
  函数声明调用，并传递给模板
  
  
 C：幕后的调度器，负责收取url或者模板获得的参数并传递到V中的相应位置  
 V：功能的具体实现的地方，并将数据映射到模板  
 M：数据库或者数据