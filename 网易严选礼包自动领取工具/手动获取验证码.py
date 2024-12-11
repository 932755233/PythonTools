import csv
import time

from PySide2.QtCore import QThread, Signal
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtUiTools import QUiLoader
from AuthCodeUtils import AuthCodeUtils


class MainWindow:
    # 生成exe可执行文件
    # D:\develop\Python\Python38\Scripts\pyinstaller 手动获取验证码.py - Fw

    def __init__(self):
        self.config = './config.csv'
        self.beans = []
        self.workThread = None
        self.authCodeUtils = AuthCodeUtils()
        self.ui = QUiLoader().load('shoudonghuoqu.ui')
        self.ui.pbStartGetCode.clicked.connect(self.startGetAuthCode)
        self.ui.te_url.setFont(QFont("宋体", 12))
        self.ui.pteTokenList.setFont(QFont("宋体", 12))
        self.ui.ptePhoneList.setFont(QFont("宋体", 12))
        self.ui.teResult.setFont(QFont("宋体", 12))
        self.ui.teOther.setFont(QFont("宋体", 12))
        self.ui.teResult.setReadOnly(True)
        self.ui.teOther.setReadOnly(True)
        with open(self.config, 'r') as csvfile:
            reader = csv.reader(csvfile)
            print('这里走了1111')
            tempRea = list(reader)
            if len(tempRea) > 0:
                self.authCodeUtils.tokens = tempRea[0]
                self.authCodeUtils.urlStr = tempRea[1][0]
            # for i in reader:
            #     self.authCodeUtils.tokens = i
            #
            #     print('这里走了')
            #     print(i, '这里也走了')
            # if (len(reader) > 0):

        for token in self.authCodeUtils.tokens:
            self.ui.pteTokenList.insertPlainText(f'{token}\n')
        self.ui.te_url.setPlainText(self.authCodeUtils.urlStr)

    def close_event(self):
        print('保存tokens')
        with open(self.config, 'w',newline='') as csvfile:
            writer = csv.writer(csvfile)
            tokens = self.ui.pteTokenList.toPlainText().strip().split('\n')
            urlStr = self.ui.te_url.toPlainText().strip().split('\n')
            print(tokens)
            writer.writerow(tokens)
            writer.writerow(urlStr)

    def startGetAuthCode(self):
        # sss = QPushButton()
        # sss.
        self.ui.pbStartGetCode.text()
        if self.ui.pbStartGetCode.text() == '开始':
            self.workThread = GetAuthCodeThread(self.ui.ptePhoneList, self.ui.pteTokenList, self.ui.te_url)
            self.workThread.start()
            self.workThread.signal.connect(self.showAuthCode)
            self.ui.pbStartGetCode.setText('结束')
        else:
            self.workThread.terminate()
            self.ui.pbStartGetCode.setText('开始')

    def showAuthCode(self, beans):
        if self.beans == beans:
            print('无变动')
            return
        else:
            self.beans = beans
        print(beans)
        self.ui.teResult.clear()
        self.ui.teOther.clear()
        # 是否显示手机
        withPhoneChecked = self.ui.cbWithPhone.isChecked()
        print(f'显示手机：{withPhoneChecked}')

        if len(beans) == 0:
            self.ui.teResult.setPlainText('未找到\n')
            return

        # 验证码部分
        for bean in beans:
            if withPhoneChecked:
                self.ui.teResult.insertPlainText(f'{bean["phone"]}----{bean["code"]}\n')
            else:
                self.ui.teResult.insertPlainText(f'{bean["code"]}\n')

        # 其他部分
        for bean in beans:
            # if withPhoneChecked:
            #     self.ui.teOther.insertPlainText(f'{bean["time"]}----{bean["token"]}\n')
            # else:
            self.ui.teOther.insertPlainText(f'{bean["phone"]}----{bean["time"]}----{bean["token"]}\n')

    def getAuthCode(self):
        self.ui.teResult.clear()
        self.ui.teOther.clear()

        tokens = self.ui.pteTokenList.toPlainText().split('\n')
        self.authCodeUtils.tokens = tokens

        withPhoneChecked = self.ui.cbWithPhone.isChecked()
        print(f'显示手机：{withPhoneChecked}')

        phoneStrs = self.ui.ptePhoneList.toPlainText().split('\n')
        print(phoneStrs)

        if phoneStrs[0] == '':
            self.ui.teResult.setPlainText('请输入手机号\n')
            return

        beans = []
        for phoneStr in phoneStrs:
            if phoneStr != '':
                QApplication.processEvents()
                bean = self.authCodeUtils.getAuthCode(phoneStr.strip())
                beans.append(bean)

        if len(beans) == 0:
            self.ui.teResult.setPlainText('未找到\n')
            return
        # 验证码部分
        for bean in beans:
            if withPhoneChecked:
                self.ui.teResult.insertPlainText(f'{bean["phone"]}----{bean["code"]}\n')
            else:
                self.ui.teResult.insertPlainText(f'{bean["code"]}\n')

        # 其他部分
        for bean in beans:
            if withPhoneChecked:
                self.ui.teOther.insertPlainText(f'{bean["time"]}----{bean["token"]}\n')
            else:
                self.ui.teOther.insertPlainText(f'{bean["phone"]}----{bean["time"]}----{bean["token"]}\n')

        # for phoneStr in phoneStrs:
        #     self.ui.teOther.insertPlainText(f'{phoneStr}\n')

        # qqq = QPlainTextEdit()
        # qqq.toPlainText().split('\n')
        #
        # cb = QCheckBox()
        # cb.isChecked()
        # self.ui.pteResult


class GetAuthCodeThread(QThread):
    signal = Signal(object)

    def __init__(self, ptePhoneList, pteTokenList, te_url):
        super(GetAuthCodeThread, self).__init__()
        self.te_url = te_url
        self.ptePhoneList = ptePhoneList
        self.pteTokenList = pteTokenList
        self.authCodeUtils = AuthCodeUtils()

    def __int__(self):
        super(GetAuthCodeThread, self).__int__()

    def setPhoneList(self):
        pass

    def run(self) -> None:
        while True:
            time.sleep(1)
            urlStr = self.te_url.toPlainText().strip()
            self.authCodeUtils.urlStr = urlStr

            tokens = self.pteTokenList.toPlainText().split('\n')
            self.authCodeUtils.tokens = tokens

            phoneStrs = self.ptePhoneList.toPlainText().split('\n')

            print('开始', phoneStrs)
            beans = []
            print(self.authCodeUtils.tokens)
            for phoneStr in phoneStrs:
                if phoneStr != '':
                    bean = self.authCodeUtils.getAuthCode(phoneStr.strip())
                    beans.append(bean)
            self.signal.emit(beans)


if __name__ == '__main__':
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.ui.show()
    # 退出时关闭所有 Timer
    app.aboutToQuit.connect(mainWindow.close_event)
    app.exec_()
