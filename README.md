# Utils
前言 : 很早之前就想整理一份这样的文档,但是我太懒了所以此前就一直没整理,乱是乱一点,起码自己还能看的过去,毕竟主要作为参考,哈哈.....
#
此模块仅以我个人代码风格编写,大部分方法只做了简单封装,利于后期扩展

目录说明 : 

**Enca_selenium :** selenium封装文件夹
	
    Driver_Funcation.py		# webdriver模块封装,包含浏览器事件及键盘事件,其实还可以将部分方法return出去以便于链式调用,后面有时间的话再更新吧
    
    ActionChains_Funcation.py		# actionchains模块封装,包含鼠标事件,此模块需要接收driver对象
    
    Expected_Conditions_Funcation.py		# Expected_Conditions 通常叫做EC模块,可以用于web自动化时对页面断言,
    										也可以在web自动化任务中为元素添加等待,此文件只作为后续使用时的参考文件,
                                			常用的两种等待方式已封装至Driver_Funcation.py/Enca_intelligent_wait
    
    chromedriver_init_parameter.py		# 此文件只作为使用google Chrome时修改浏览器默认参数的参考文件
    
**cookie**
            
   	Cookie_Fncation.py		# 发送requests请求时将cookie保存在本地文件
    
**file**
	
    CSV_File_Funcation.py		# .csv文件常用方法
    
   	EXCEL_File_Funcation.py		# excel文件常用方法
    
    Initialization_File_Funcation.py		#.ini文件常用方法
    
    JSON_File_Funcation.py		#.json文件常用方法
    
    Logging_File_Funcation.py	# 封装的logger类,按需使用
    
    Logging_File_Funcation2.py
    
    Yaml_File_Funcation.py		#.yaml文件常用方法
    
    关于将csv文件写入到mysql数据库的脚本.py		#	如果爬虫脚本有入库需求则以此文件作为参考
    
 **ocr** 参考于DDDDOCR开源库,其他验证码识别库后面作总结
 	
    OCR_图片识别.py		#ddddocr库识别图片验证码的例子,具体案例可以参考https://github.com/1803664082/chictr.org.cn此项目
    OCR_文字点选.py		#ddddocr库文字点选的例子
 
 **proxy**
 	
    ProxyIp_Funcation.py		# 从各大网站上爬取可用代理IP保存在本地,业务逻辑可以作为参考使用,爬取的IP质量不稳定不推荐使用,还是花钱买稳定一点的吧    
    stealth文件夹		# 从node.js 里面下载下来的一个文件,主要作用就是绕过selenium指纹反爬虫,原理暂不清楚
    
    ua文件夹		# 读取useragent.db文件并返回ua; 主要作用就是防ua反爬,和from fake_useragent import UserAgent 模块作用一致
    
 
---
 # 后记
 **关于文档更新**
 	
    后期如果有时间或有变动时再更新,此文档只作为代码编写时的参考文档
 **关于反爬虫(如何判断自己已被反爬)**
 		
 	 
    现象1:打开后页面白屏
      原因:selenium指纹被识别到了
      解决方式:
        1.CDP 命令，在网页加载前运行一段代码，进而改变浏览器的指纹特征
        1+2.stealth.min.js
        1+2+3.修改浏览器默认参数
        4.操作已开启的浏览器
        5.undetected_chromedriver 这是一个防止浏览器指纹特征被识别的依赖库
        6.http://www.360doc.com/content/23/0131/12/77509131_1065600038.shtml
        7.如果指纹识别不严格的话,其实可以尝试将浏览器版本回退到老一点的版本在试试
     查看当前浏览器指纹:https://bot.sannysoft.com/
     
    现象2:requests请求到的html有字体混乱或乱入
    	原因:字体反爬
   		解决方式:
        网上找教程,关键词:字体反爬虫
        
    现象3:爬着爬着IP被封了
    	原因: ip反爬虫/ua反爬虫/cookie反爬虫
    	解决方式:
        代理请求参数,使用random.chose()随机使用
        
    现象4:碰到各种类型的验证码
    	原因: 一直用同一个ip/ua/cookie导致被识别;或固定此操作需要识别
    	解决方式:
        1.花钱接入打码平台
        2.ai深度学习(成本太高)
        3.第三方识别库:pytesseract(辣鸡),PaddleOCR,easyocr,muggle_ocr,dddd_ocr
        4.https://blog.csdn.net/qq_38017966/article/details/118724459
        
    反爬现象过多,不11举栗
    .
    .
    .
    .
    
 **关于JS反爬**
 	
    正在学习,研究这东西得有人带着入门啊,TMD
 **关于str处理**
 	
    原则上来讲是不建议修改元数据的,如果需要进行数据格式化,尽量在处理前保存数据副本或者将格式化代码封装成后置执行
    一般格式化数据流程: 获取到数据文件中需要格式化的列或行, 根据需求处理为list/dict,进行格式化,将格式化的数据覆盖到元数据位置
    如果数据较整齐,推荐使用正则表达式进行匹配
 **关于文本解析方式**
    
    仅基于我个人使用习惯
    	xpath 推荐使用,其有一百多个内置函数,不会出现定位不到的情况
    	css 个人不推荐
    	beautifulsoup(bs)  一般出现表格数据的时候使用
        
  **关于框架**
  	
    推荐使用Scrspy(用的人多),当然一些大佬的框架也可以参考使用
 
 
    
 
