import os
import cv2 as cv
import fitz

from PIL import Image
from tqdm import tqdm

class PdfHandler:

    def pdf_to_img(self,pdf_path,img_path,zoom_x,zoom_y,rotation_angle):
        '''
        pdf文件每页内容都转换成图片

        :param pdf_path:
        :param img_path:
        :param zoom_x:
        :param zoom_y:
        :param rotation_angle:
        :return:
        '''
        # 如果没有存储文件的目录，则创建
        if not os.path.exists(img_path):
            os.mkdir(img_path)
        # 打开PDF文件
        with fitz.open(pdf_path) as pdf:
            # 逐页读取PDF
            for page_index in tqdm(range(0, pdf.pageCount)):
                page = pdf[page_index]
                # 设置缩放和旋转系数,zoom_x, zoom_y取相同值，表示等比例缩放
                trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotation_angle)
                pm = page.getPixmap(matrix=trans, alpha=False)
                # 开始写图像
                page_num = page_index + 1 # 页码从1开始
                pm.writePNG(f'{img_path}/{page_num}.png') # 第1张图片名：1.png，以此类推

    def img_to_pdf(self,imgPath, new_pdf_name):
        '''
        将图片转为pdf

        :param imgPath: 图片路径
        :param new_pdf_name: 多张图片合并成的pdf文件名
        :return:
        '''
        with fitz.open() as doc:  # 新建一个空文档
            for path in os.listdir(imgPath):
                img = fitz.open(f'{imgPath}/{path}')  # 打开图片
                pdfbytes = img.convertToPDF()  # 使用图片创建单页的 PDF
                with fitz.open("pdf", pdfbytes) as imgpdf:
                    doc.insertPDF(imgpdf)
                img.close()
            doc.insert_pdf()
            doc.save(new_pdf_name)

    def split_pdf(self,old_pdf_name, new_pdf_name, from_page, to_page):
        '''
        从pdf文件中拆分出部分，拆出部分成为新的pdf文件

        :param old_pdf_name: 原pdf文件名
        :param new_pdf_name: 拆分后合并出的新pdf文件名
        :param from_page: 原pdf文件起始页码索引（0开始，默认0）
        :param to_page: 原pdf文件结尾页码索引（0开始，默认最后一页）
        :return:
        '''
        with fitz.open(old_pdf_name) as old_pdf, fitz.open() as new_pdf:
            new_pdf.insert_pdf(old_pdf, from_page, to_page)
            new_pdf.save(new_pdf_name)

    def get_pdf_text(self,pdf_path):
        '''
        获取每页pdf文件文本

        :param pdf_path: pdf文件路径
        :return:
        '''
        # 打开pdf文件，并新建html文件
        with fitz.open(pdf_path) as pdf:

            # 遍历每一页pdf，并显示进度条
            for page in tqdm(pdf):
                text = page.get_text() #提取文本，传入参数'html'即：page.get_text('html') 则提取每页内容为html
            print(f'第{page+1}页解析内容:\n{text}')


    def parse_img(self,img_name):
        '''
        利用opencv+pytesseract解析图片中的文字
        :param img_name: 具体图片名
        :return:
        '''
        img = cv.imread(img_name)
        text = pytesseract.image_to_string(Image.fromarray(img), lang='eng') # lang可以根据文本内容来定，简体中文：chi_sim
        print(text)
