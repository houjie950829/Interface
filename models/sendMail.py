# coding=utf-8
import smtplib
import time
import os
from PIL import Image  # 图像处理
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from email.mime.multipart import MIMEMultipart
from models.readWritYmal import MyYaml
import platform


class Mail(object):

    def __init__(self, file_new, img_pt, url):
        self.file_new = file_new
        self.img_pt = img_pt
        self.url = url
        self.send_name_from = MyYaml('send_name_from').email
        self.send_tos = MyYaml('send_name_to').email
        self.html_title = MyYaml('title').email
        self.smtp_s = MyYaml('smtp').email
        self.send_pwd_from = MyYaml('send_pwd_from').email

    def reportImg(self):
        """测试图表截图"""
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        system_name = platform.system().lower()
        if system_name == 'windows':
            dir_path = './package/chromedriver.exe'
        else:
            dir_path = './package/chromedriver'
        driver = webdriver.Chrome(dir_path, chrome_options=chrome_options)
        driver.get('file:///' + self.file_new)
        driver.implicitly_wait(10)
        if system_name == 'windows':
            driver.set_window_size(1600,980)
        else:
            js = 'var winW = window.screen.width;var winH = window.screen.height;alert(winW+","+winH)'
            driver.execute_script(js)
            # 获取屏幕分辨率
            line = driver._switch_to.alert.text
            driver._switch_to.alert.accept()
            size = line.split(',')
            driver.set_window_size(int(size[0]), int(size[1]))
        sleep(1)
        driver.get_screenshot_as_file(self.img_pt)
        driver.quit()
        # im = Image.open('./img/reportImg.png')
        # """
        # 裁剪：传入一个元组作为参数
        # 距离图片左边界距离x
        # 距离图片上边界距离
        # 距离图片左边界距离+裁剪框宽度x+w
        # 距离图片上边界距离+裁剪框高度y+h
        # """
        # # 截取图片中一块宽和高都是宽为500，高为370的图像
        # system_version = platform.system()
        # if 'Windows' == system_version:
        #     x = 140
        #     y = 10
        #     w = 530
        #     h = 370
        # else:
        #     x = 140
        #     y = 10
        #     w = 1300
        #     h = 780
        # region = im.crop((x, y, x + w, y + h))
        # region.save("./report/reportImg.png")

    def send_mail(self):
        """发送邮件,携带附件且将内容写入邮件正文"""
        msg_file = MIMEMultipart('related')
        msg_file['from'] = self.send_name_from
        msg_file['to'] = ','.join(self.send_tos)
        msg_file['Subject'] = Header(self.html_title, 'utf-8')

        # t = open(self.file_new, 'rb')
        # html_body = t.read()
        # t.close()
        # msg_html = MIMEText(html_body, 'html', 'utf-8')  # 你所发的文字信息将以html形式呈现
        # msg_file.attach(msg_html)

        f = open(self.img_pt, 'rb')  # 正文插入图片
        mail_body = MIMEImage(f.read())
        f.close()
        mail_body.add_header('Content-ID', '<image1>')
        msg_text = MIMEText(
            '''<b><i><font size="3" color="blue"><a href="{}" target="_blank" class="mnav">点击此处在线查看测试报告</a></font>\
            </i></b><img alt="" src="cid:image1"/>'''.format(self.url), 'html', 'utf-8')  # 你所发的文字信息将以html形式呈现
        msg_file.attach(msg_text)
        msg_file.attach(mail_body)

        att = MIMEText(open(self.file_new, 'rb').read(), 'base64', 'utf-8')  # 添加附件
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="%s_result.html"' % time.strftime('%Y-%m-%d %H_%M_%S')  # 附件名称
        msg_file.attach(att)
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtp_s)  # 连接至邮件服务器
            smtp.login(self.send_name_from, self.send_pwd_from)  # 登录邮件服务器
            smtp.sendmail(self.send_name_from, self.send_tos, msg_file.as_string())  # 发送邮件
            smtp.quit()
            print("给%s发送邮件成功" % ','.join(self.send_tos))
        except Exception as f:
            print("\033[31m","给%s发送邮件失败,失败原因：%s" % (','.join(self.send_tos),f))


if __name__ == '__main__':
    mail = Mail('',os.path.abspath('..') + '\\' + 'img' + '\\' + 'chromedriver.png','http://www.ukuaiqi.com')
    # mail = Mail('/Users/yuzq/workspace/myweb/mysite/templates/1537261821.229674.html','http://127.0.0.1:8000/polls/report/?name=1537102517.02043.html')
    mail.reportImg()
    mail.send_mail()
