import os

from PySide6.QtGui import QTextCursor
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox, QFileDialog, \
    QMessageBox

from 生泰尔代码生成工具 import FileCreateTool, StringTool
from 生泰尔代码生成工具.android.GenerateBean import GenerateBean
from 生泰尔代码生成工具.android.GenerateDetails import GenerateDetails
from 生泰尔代码生成工具.android.GenerateDetailsXml import GenerateDetailsXml
from 生泰尔代码生成工具.android.GenerateEntryAdapter import GenerateEntryAdapter
from 生泰尔代码生成工具.android.GenerateEntryAdapterXml import GenerateEntryAdapterXml
from 生泰尔代码生成工具.android.GenerateFragment import GenerateFragment
from 生泰尔代码生成工具.android.GenerateFragmentAdapter import GenerateFragmentAdapter
from 生泰尔代码生成工具.android.GenerateFragmentAdapterXml import GenerateFragmentAdapterXml
from 生泰尔代码生成工具.android.GenerateListActivity import GenerateListActivity
from 生泰尔代码生成工具.ui_main import Ui_Form

uiLoader = QUiLoader()


class MainWindow(QMainWindow):
    classNamePrefix = ''
    fragmentNameList = []
    beanList = []
    entryBeanList = []
    picture = False  # 是否需要图片附件
    examine = False  # 是否需要审核
    annotation = False  # 是否需要注释
    lieBiaoType = ['隐藏',
                   '仅展示',
                   '可写',
                   '可点-下级选择',
                   '可点-弹窗选择',
                   '可点-时间选择',
                   '点写-下级选择',
                   '点写-弹窗选择',
                   '点写-时间选择',
                   '单据状态']

    outputPath = r'\output'
    # 安卓路径
    androidPath = r'\Android'
    harmonyPath = r'\Harmony'

    def __init__(self):
        super().__init__()
        self.typeName = ''
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # self.ui = uiLoader.load('ui_main.ui')

        self.ui.pbut_listAndMainBean_add.clicked.connect(self.addListAndMainBean)
        self.ui.pbut_listAndMainBean_remove.clicked.connect(self.removeListAndMainBean)
        self.ui.tw_listAndMainBean.cellActivated.connect(self.addListAndMainBean)  # 回车键被按下的回调

        self.ui.tw_listAndMainBean.insertRow(0)
        cbox = QComboBox()
        cbox.addItems(self.lieBiaoType)
        self.ui.tw_listAndMainBean.setCellWidget(0, 2, cbox)

        self.ui.but_entryBean_add.clicked.connect(self.addEntryItem)
        self.ui.but_entryBean_remove.clicked.connect(self.removeEntryItem)
        self.ui.tw_entryBean.cellActivated.connect(self.addEntryItem)

        # self.ui.tw_entryBean.insertRow(0)
        # cbox = QComboBox()
        # cbox.addItems(self.lieBiaoType)
        # self.ui.tw_entryBean.setCellWidget(0, 2, cbox)

        self.ui.pbut_listLineName_add.clicked.connect(self.addFragmentItem)
        self.ui.pbut_listLineName_remove.clicked.connect(self.removeFragmentItem)
        self.ui.tw_listLineName.cellActivated.connect(self.addFragmentItem)

        self.ui.but_selectOutPath.clicked.connect(self.chooseSavePathListener)

        self.ui.edit_outPath.setText(os.getcwd())

        self.ui.but_start.clicked.connect(self.startTask)

        self.ui.cb_picture.toggled.connect(self.picToggledChangeListener)
        self.ui.cb_examine.toggled.connect(self.examineToggledChangeListener)
        self.ui.cb_annotation.toggled.connect(self.annotationToggledChangeListener)

    def picToggledChangeListener(self, checked):
        self.picture = checked

    def examineToggledChangeListener(self, checked):
        self.examine = checked

    def annotationToggledChangeListener(self, checked):
        self.annotation = checked

    def chooseSavePathListener(self):
        filePath = QFileDialog.getExistingDirectory(self, "选择路径")
        if filePath:
            self.ui.edit_outPath.setText(filePath)

    def addFragmentItem(self):
        self.ui.tw_listLineName.insertRow(self.ui.tw_listLineName.rowCount())
        cbox = QComboBox()
        cbox.addItems(self.lieBiaoType)
        self.ui.tw_listLineName.setCellWidget(self.ui.tw_listLineName.rowCount() - 1, 2, cbox)

    def removeFragmentItem(self):
        self.ui.tw_listLineName.removeRow(self.ui.tw_listLineName.rowCount() - 1)

    def addEntryItem(self):
        self.ui.tw_entryBean.insertRow(self.ui.tw_entryBean.rowCount())
        cbox = QComboBox()
        cbox.addItems(self.lieBiaoType)
        self.ui.tw_entryBean.setCellWidget(self.ui.tw_entryBean.rowCount() - 1, 2, cbox)

    def removeEntryItem(self):
        self.ui.tw_entryBean.removeRow(self.ui.tw_entryBean.rowCount() - 1)

    def addListAndMainBean(self):
        self.ui.tw_listAndMainBean.insertRow(self.ui.tw_listAndMainBean.rowCount())
        cbox = QComboBox()
        cbox.addItems(self.lieBiaoType)
        self.ui.tw_listAndMainBean.setCellWidget(self.ui.tw_listAndMainBean.rowCount() - 1, 2, cbox)

    def removeListAndMainBean(self):
        self.ui.tw_listAndMainBean.removeRow(self.ui.tw_listAndMainBean.rowCount() - 1)

    def panDuanNoneType(self, widget):
        if widget:
            return widget.text()
        else:
            return ""

    def showCriticalQMessageBox(self, errorMessage):
        QMessageBox.critical(self.ui.but_start, '错误', errorMessage)

    def startTask(self):
        # 生成安卓保存路径
        androidSavePath = self.ui.edit_outPath.text() + self.outputPath + self.androidPath

        self.beanList.clear()
        self.entryBeanList.clear()
        self.fragmentNameList.clear()
        if self.ui.edit_className.text() != '':
            self.classNamePrefix = self.ui.edit_className.text()
        else:
            self.showCriticalQMessageBox('类名前缀需要输入')
            return

        if self.ui.edit_className_2.text() != '':
            self.typeName = self.ui.edit_className_2.text()
        else:
            self.showCriticalQMessageBox('单据名称需要输入')
            return

        try:
            for i in range(self.ui.tw_listAndMainBean.rowCount()):
                bean = {}
                bean['showName'] = self.ui.tw_listAndMainBean.item(i, 0).text()
                bean['name'] = self.ui.tw_listAndMainBean.item(i, 1).text()
                bean['type'] = self.ui.tw_listAndMainBean.cellWidget(i, 2).currentText()
                bean['listNum'] = self.panDuanNoneType(self.ui.tw_listAndMainBean.item(i, 3))
                bean['detialNum'] = self.panDuanNoneType(self.ui.tw_listAndMainBean.item(i, 4))
                self.beanList.append(bean)

            # 最后一条添加为fDataCenter
            bean = {}
            bean['showName'] = "fDataCenter"
            bean['name'] = "fDataCenter"
            bean['type'] = self.lieBiaoType[0]
            bean['listNum'] = ""
            bean['detialNum'] = ""
            self.beanList.append(bean)
        except AttributeError:
            self.showCriticalQMessageBox('详情数据的显示名称和变量名称不得为空')
            raise AttributeError

        try:
            for i in range(self.ui.tw_entryBean.rowCount()):
                bean = {}
                bean['showName'] = self.ui.tw_entryBean.item(i, 0).text()
                bean['name'] = self.ui.tw_entryBean.item(i, 1).text()
                bean['type'] = self.ui.tw_entryBean.cellWidget(i, 2).currentText()
                bean['listNum'] = self.panDuanNoneType(self.ui.tw_entryBean.item(i, 3))
                self.entryBeanList.append(bean)
        except AttributeError:
            self.showCriticalQMessageBox('分录数据的显示名称和变量名称不得为空')
            raise AttributeError

        for i in range(self.ui.tw_listLineName.rowCount()):
            bean = {}
            bean['showName'] = self.ui.tw_listLineName.item(i, 0).text()
            bean['name'] = self.ui.tw_listLineName.item(i, 1).text()
            self.fragmentNameList.append(bean)

        lowerFileName = ''
        words = StringTool.extract_words_starting_with_capital(self.classNamePrefix)
        for word in words:
            lowerFileName += '_' + word.lower()
        self.showLog('安卓保存路径：%s' % androidSavePath)
        self.showLog('类名前缀：%s' % self.classNamePrefix)
        self.showLog('文件名：')
        self.showLog('%sListActivity.java' % self.classNamePrefix)
        self.showLog('layout_list%s.xml' % lowerFileName)
        for bean in self.fragmentNameList:
            self.showLog('%s%sFragment.java' % (self.classNamePrefix, bean['name']))
        fragmentXmlFileName = 'layout_fragment' + lowerFileName
        self.showLog('%s.xml' % fragmentXmlFileName)
        self.showLog('%sAdapter.java' % self.classNamePrefix)
        self.showLog('item_fragment%s.xml' % lowerFileName)
        self.showLog('%sDetailActivity.java' % self.classNamePrefix)
        self.showLog('layout_detial%s.xml' % lowerFileName)
        self.showLog('%sEntryAdapter.java' % self.classNamePrefix)
        self.showLog('item_entry%s.xml' % lowerFileName)
        self.showLog('↓↓↓↓↓↓')
        self.showLog('列表Fragment个数：%d' % len(self.fragmentNameList))
        self.showLog('详情Bean变量个数：%d' % len(self.beanList))
        self.showLog('详情分录Bean变量个数：%d' % len(self.entryBeanList))
        self.showLog('需要图片：%s' % (self.picture and '是' or '否'))
        self.showLog('需要审核：%s' % (self.examine and '是' or '否'))
        self.showLog('需要注释：%s' % (self.annotation and '是' or '否'))
        self.showLog('↓↓↓开始↓↓↓')
        # 数据获取完毕

        # Bean
        # 获取详情bean
        generateMainBean = GenerateBean(self.classNamePrefix, self.beanList, False)
        # 获取图片check
        generateMainBean.annotation = self.annotation
        generateMainBean.picture = self.picture
        generateMainBean.examine = self.examine
        generateMainBean.generate()
        mainBeanFilename, mainBeanContent = generateMainBean.getResultStr()
        # 主数据bean文件
        FileCreateTool.generateFile(
            r'%s\bean\%s.java' % (androidSavePath, mainBeanFilename),
            mainBeanContent)
        self.showLog('生成详情bean文件')

        # 获取分录bean
        if len(self.entryBeanList) > 0:
            generateEntryBean = GenerateBean(self.classNamePrefix, self.entryBeanList, True)
            generateEntryBean.annotation = self.annotation
            generateEntryBean.generate()
            entryBeanFilename, entryBeanContent = generateEntryBean.getResultStr()
            # 分录bean文件
            FileCreateTool.generateFile(
                r'%s\bean\%s.java' % (androidSavePath, entryBeanFilename),
                entryBeanContent)
            self.showLog('生成分录bean文件')

        # Fragment的Adapter的xml
        generateFragmentAdapterXml = GenerateFragmentAdapterXml(self.classNamePrefix, self.beanList)
        fragmentAdapterXmlFileName, fragmentAdapterXmlContent = generateFragmentAdapterXml.getResult()
        # 列表adapter的xml文件
        FileCreateTool.generateFile(
            r'%s\xml\%s.xml' % (androidSavePath, fragmentAdapterXmlFileName),
            fragmentAdapterXmlContent)
        self.showLog('生成列表adapter的xml文件')

        # Fragment的adapter
        gg = GenerateFragmentAdapter(self.classNamePrefix, self.beanList, fragmentAdapterXmlFileName, self.annotation)
        fragmentAdapterFilename, fragmentAdapterContent = gg.getResult()
        FileCreateTool.generateFile(
            r'%s\adapter\%s.java' % (androidSavePath, fragmentAdapterFilename),
            fragmentAdapterContent)
        self.showLog('生成列表adapter文件')

        # Fragment
        for bean in self.fragmentNameList:
            generateFragment = GenerateFragment(self.classNamePrefix, bean['name'], self.typeName)
            fragmentFileName, fragmentContent = generateFragment.getResult()
            FileCreateTool.generateFile(
                r'%s\fragment\%s.java' % (androidSavePath, fragmentFileName),
                fragmentContent)
            self.showLog('生成Fragment的%s文件' % bean['name'])

        # xml
        oldPath = os.getcwd() + '/template/fragment_xml.xml'

        newPath = r'%s\xml\%s.xml' % (androidSavePath, fragmentXmlFileName)
        FileCreateTool.copyFile(oldPath, newPath)
        self.showLog('生成Fragment的xml文件')

        # ListActivity
        generateListActivity = GenerateListActivity(self.classNamePrefix, self.fragmentNameList)
        listActivityFilename, listActivityContent, listActivityXmlFilename, listActivityXmlContent = generateListActivity.getResult()
        FileCreateTool.generateFile(
            r'%s\activity\%s.java' % (androidSavePath, listActivityFilename),
            listActivityContent)
        FileCreateTool.generateFile(
            r'%s\xml\%s.xml' % (androidSavePath, listActivityXmlFilename),
            listActivityXmlContent)
        self.showLog('生成列表的java和xml文件')

        # adapter xml
        gg = GenerateEntryAdapterXml(self.classNamePrefix, self.entryBeanList)
        fileName, contentStr = gg.getResult()
        FileCreateTool.generateFile(
            r'%s\xml\%s.xml' % (androidSavePath, fileName),
            contentStr)
        self.showLog('生成详情分录Adapter的xml文件')

        # adapter
        gg = GenerateEntryAdapter(self.classNamePrefix, self.entryBeanList, self.annotation)
        fileName, contentStr = gg.getResult()
        FileCreateTool.generateFile(
            r'%s\adapter\%s.java' % (androidSavePath, fileName),
            contentStr)
        self.showLog('生成详情分录Adapter文件')
        # details xml
        gg = GenerateDetailsXml(self.classNamePrefix,
                                self.beanList,
                                len(self.entryBeanList) > 0,
                                self.picture,
                                self.examine)
        fileName, contentStr = gg.getResult()
        FileCreateTool.generateFile(
            r'%s\xml\%s.xml' % (androidSavePath, fileName),
            contentStr)
        self.showLog('生成详情的xml文件')
        # details
        gg = GenerateDetails(self.classNamePrefix,
                             self.typeName,
                             self.beanList,
                             self.entryBeanList,
                             self.picture,
                             self.examine,
                             self.annotation)
        fileName, contentStr = gg.getResult()
        FileCreateTool.generateFile(
            r'%s\activity\%s.java' % (androidSavePath, fileName),
            contentStr)
        self.showLog('生成详情文件')

        self.showLog('↑↑↑结束↑↑↑')
        self.showLog('--------------------------------------')

    def showLog(self, text):
        print('showLog')
        cursor = self.ui.plainT_output.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.ui.plainT_output.setTextCursor(cursor)
        self.ui.plainT_output.insertPlainText(f'{text}\n')


app = QApplication()
main = MainWindow()
main.show()
app.exec()
