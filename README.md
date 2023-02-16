# Utils
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
