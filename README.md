## 这是一个网络小说的爬取工具，使用方法如下：
1. git clone到本地
2. 下载python库依赖（bs4，requests，docx等）
3. downloader目录下为下载工具，其中实现了简单的多线程下载功能；对于不同的页面，需要根据不同的页面结构对原脚本进行修改，以获取正确的文字内容
4. downloader下载工具下载完成后会在本地download文件夹下生成page-id的文件（拉取时没有该文件夹，需要自行创建）
5. 下载完成后将download文件夹拷贝至其他相应的formater目录下，这里formater目录为魔女之旅，formater目录下的formater.py是对步骤4中下载的html进行格式化解析，以生成方便阅读的格式，一般可以按章节生成对应的txt文件，这里还提供了生成docx的代码
