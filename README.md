# zwjss_blog
>note：7月30日开始的django BLOG,
>参考zmrenwu教程进行的第一次尝试

## step1:
### 搭建BLOG文章的数据库结构， 具体结构为:
  文章id | 标题 | 正文 | 发表时间 | 最后修改时间 | 分类 | 标签 |
### 配置后台admin：
  1. 注册models中的类
  2. 自定义admin界面
### shell环境下进行测试，符合预期，models基本完成

## step2:
>MVC:M即为models，V即为Views，C即为Control
>在django环境中，个人理解的工作流程为：发出请求->URL捕获->Views视图层调用HTML页面->读取models数据
>此为一套基础的相应流程
### 1.zwjss_blog下url配置，定义app的namespace
### 2.blog（app）下的urls配置，定义各功能的name及对应的view
### 3.HTML模板学习及修改，了解具体标签对应的功能以及调用模式
### 4.整体页面布局
### TODO:views视图层代码重构，去除冗余部分

## step3:
>对整个架构进行审查规划修改
### 基础页面搭建完毕后，对页面各功能栏进行规划，代码重构等
  
