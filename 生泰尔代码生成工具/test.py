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

if __name__ == '__main__':
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
    for strTemp in lieBiaoType:
        print(strTemp)

    classNamePrefix = 'Entertain'
    beanList = []

    beanList.append(
        {'showName': '单据编码', 'name': 'fNumber', 'type': '仅展示', 'listNum': '1', 'detialNum': '1'})
    beanList.append(
        {'showName': '业务日期', 'name': 'fBizDate', 'type': '仅展示', 'listNum': '2', 'detialNum': '2'})
    beanList.append(
        {'showName': '付款单位', 'name': 'payer', 'type': '可写', 'listNum': '', 'detialNum': ''})
    beanList.append(
        {'showName': '技术经理', 'name': 'JiShuJingLi', 'type': '可点-下级选择', 'listNum': '3', 'detialNum': '3'})
    beanList.append(
        {'showName': '申请人', 'name': 'ShenQingRen', 'type': '可点-弹窗选择', 'listNum': '4', 'detialNum': '4'})
    beanList.append(
        {'showName': '申请人电话', 'name': 'ShenQingRenDianHua', 'type': '可写', 'listNum': '6', 'detialNum': '6'})
    beanList.append(
        {'showName': '申请人部门', 'name': 'ShenQingBuMen', 'type': '仅展示', 'listNum': '7', 'detialNum': '7'})
    beanList.append(
        {'showName': '支持详情说明', 'name': 'ZhiChiXiangShuoMing', 'type': '可写', 'listNum': '5', 'detialNum': '5'})
    beanList.append(
        {'showName': '单据状态', 'name': 'DanJuZhuangTai', 'type': '点写-弹窗选择', 'listNum': '8', 'detialNum': '8'})
    beanList.append(
        {'showName': '客户名称', 'name': 'KeHuMingCheng', 'type': '点写-下级选择', 'listNum': '9', 'detialNum': '9'})
    print()
    for bean in beanList:
        print(bean)

    gg = GenerateDetails(classNamePrefix, '招待费', beanList, beanList, True, True, True)
    fileName, contentStr = gg.getResult()
    FileCreateTool.generateFile(
        r'G:\CodeGitHub\PythonTools\生泰尔代码生成工具\output\android\activity\%s.java' % fileName,
        contentStr)

    # gg = GenerateDetailsXml(classNamePrefix, beanList, False, False, False)
    # fileName, contentStr = gg.getResult()
    # FileCreateTool.generateFile(
    #     r'G:\CodeGitHub\PythonTools\生泰尔代码生成工具\output\android\xml\%s.xml' % fileName,
    #     contentStr)

    # gg = GenerateEntryAdapter(classNamePrefix, beanList, True)
    # filename, content = gg.getResult()
    # FileCreateTool.generateFile(
    #     r'G:\CodeGitHub\PythonTools\生泰尔代码生成工具\output\android\adapter\%s.java' % filename,
    #     content)
    # gg = GenerateEntryAdapterXml(classNamePrefix, beanList)
    # filename, content = gg.getResult()
    # FileCreateTool.generateFile(
    #     r'G:\CodeGitHub\PythonTools\生泰尔代码生成工具\output\android\xml\%s.xml' % filename,
    #     content)

    # print(StringTool.format_xml_show_title('周'))
    # print(StringTool.format_xml_show_title('忠煜'))
    # print(StringTool.format_xml_show_title('仅展示'))
    # print(StringTool.format_xml_show_title('周忠煜好'))
    # print(StringTool.format_xml_show_title('周忠煜好好'))

    # gg = GenerateListActivity(classNamePrefix, beanList)
    # filename, content, filename1, content1 = gg.getResult()
    #
    # FileCreateTool.generateFile(
    #     r'G:\CodeGitHub\PythonTools\生泰尔代码生成工具\output\android\activity\%s.java' % filename,
    #     content)
    # FileCreateTool.generateFile(
    #     r'G:\CodeGitHub\PythonTools\生泰尔代码生成工具\output\android\xml\%s.xml' % filename1,
    #     content1)

    # gg = GenerateFragment(classNamePrefix,'Approval','招待费申请单')
    # filename, content = gg.getResult()
    # FileCreateTool.generateFile(
    #     r'G:\CodeGitHub\PythonTools\生泰尔代码生成工具\output\android\fragment\%s.java' % filename,
    #     content)

    # gg = GenerateFragmentAdapter(classNamePrefix, beanList, 'item_fragment_zhou_zhongyu', True)
    # filename, content = gg.getResult()
    # FileCreateTool.generateFile(
    #     r'G:\CodeGitHub\PythonTools\生泰尔代码生成工具\output\android\xml\%s.java' % filename,
    #     content)

    # gg = GenerateFragmentAdapterXml(classNamePrefix, beanList)

    # strtemp = 'MettePurRequestBillAdapter'
    # words = StringTool.extract_words_starting_with_capital(strtemp)
    # print(words)

    # generateMainBeanFile = GenerateBean('Entertain', beanList, False)
    # generateMainBeanFile.annotation = True
    # generateMainBeanFile.picture = True
    # generateMainBeanFile.examine = True
    # generateMainBeanFile.generate()
    # # result = generateMainBeanFile.getResultStr()
    # # print(result['content'])
    # # print(result['filename'])
    # filename, content = generateMainBeanFile.getResultStr()
    #
    # FileCreateTool.generateFile(
    #     r'G:\CodeGitHub\PythonTools\生泰尔代码生成工具\output\android\bean\%s.java' % filename,
    #     content)
    # # generateMainBeanFile.generateFile(r'G:\CodeGitHub\PythonTools\生泰尔代码生成工具\output\android\bean')
    #
    # generateEntryBeanFile = GenerateBean('Entertain', beanList, True)
    # generateEntryBeanFile.generate()
    # # generateEntryBeanFile.generateFile(r'G:\CodeGitHub\PythonTools\生泰尔代码生成工具\output\android\bean')
