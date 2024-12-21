import fileinput
import os.path



class GenerateBean:
    # 模板
    bianLiangMuBan = '    private String %s;\n'
    bianLiangMuBan2 = '    private String %s;// %s\n'

    picImportMuBan = 'import com.centre.workoffice.centre.c_eastask.bean.AttachInfoBean;\n'
    exaImportMuBan = 'import com.centre.workoffice.centre.c_eastask.bean.ApproveOpinionBean;\n'
    entryBianLiangMuBan = '    private List<%sEntryBean> entryInfos;\n'
    picBianLiangMuBan = '    private List<AttachInfoBean> attachInfos;\n'
    exaBianLiangMuBan = '    private List<ApproveOpinionBean> approveOpinionInfos;\n'

    entryGetSetMuBan = '''
    public List<%sEntryBean> getEntryInfos() {
        return entryInfos;
    }

    public void setEntryInfos(List<%sEntryBean> entryInfos) {
        this.entryInfos = entryInfos;
    }'''
    picGetSetMuBan = '''
    public List<AttachInfoBean> getAttachInfos() {
        return attachInfos;
    }

    public void setAttachInfos(List<AttachInfoBean> attachInfos) {
        this.attachInfos = attachInfos;
    }'''
    exaGetSetMuBan = '''
    public List<ApproveOpinionBean> getApproveOpinionInfos() {
        return approveOpinionInfos;
    }

    public void setApproveOpinionInfos(List<ApproveOpinionBean> approveOpinionInfos) {
        this.approveOpinionInfos = approveOpinionInfos;
    }'''

    getMuBan = '''
    public String get%s() {
        return %s;
    }'''
    setMuBan = '''
    public void set%s(String %s) {
        this.%s = %s;
    }'''

    classCreateMuBan = 'public class %s extends SuperBean {\n'
    endClassMuBan = '\n}\n'

    getListBeanMuBan = '''
    public static List<%s> getListBean(String result) throws BizException {
        try {
            List<%s> list = new ArrayList<>();
            if (StringUtil.isNotEmpty(result) && !"[]".equals(result.trim())) {
                list.addAll((List<%s>) getDataBean(%s.class, result));
            }
            return list;
        } catch (Exception e) {
            throw new BizException(e);
        }
    }'''
    getBeanMuBan1 = '''
    public static EntertainBean getBean(String result) throws BizException {
        try {
            JsonObject jsonObject = JsonParser.parseString(result).getAsJsonObject();
            EntertainBean bean = (EntertainBean) getDataBean(EntertainBean.class, result);
    '''
    getBeanMuBan2 = '''
            return bean;
        } catch (Exception e) {
            throw new BizException(e);
        }
    }
    '''
    # 可用
    # annotation = False
    # fileName = ''
    # importStrList = []
    # bianLiangStrList = []
    annotation = False
    picture = False
    examine = False
    isEntry = False

    def __init__(self, classNamePrefix: str, beanList: [], isEntry: bool):

        self.beanList = beanList
        self.isEntry = isEntry
        self.classNamePrefix = classNamePrefix

        self.importStrList = [
            'package com.centre.workoffice.bean;\n\n',
            'import com.monkeyk.ht.baseexception.BizException;\n',
            'import com.monkeyk.htjava.bean.SuperBean;\n',
            'import com.monkeyk.htjava.utils.StringUtil;\n'
        ]
        self.bianLiangStrList = []
        self.getAndSetStrList = []

    def generate(self):
        if self.isEntry:
            self.fileName = '%sEntryBean' % self.classNamePrefix
        else:
            self.fileName = '%sBean' % self.classNamePrefix
            self.importStrList.extend(['import com.monkeyk.htjava.gson.JsonObject;\n',
                                       'import com.monkeyk.htjava.gson.JsonParser;\n', ])
        self.classCreateStr = self.classCreateMuBan % self.fileName
        # 组合变量
        for bean in self.beanList:
            if self.annotation:
                self.bianLiangStrList.append(self.bianLiangMuBan2 % (bean['name'], bean['showName']))
            else:
                self.bianLiangStrList.append(self.bianLiangMuBan % bean['name'])

        # 分录变量
        if not self.isEntry:
            self.bianLiangStrList.append(self.entryBianLiangMuBan % self.classNamePrefix)
            self.getAndSetStrList.append(self.entryGetSetMuBan % (self.classNamePrefix, self.classNamePrefix))

        # 图片附件变量
        if self.picture & (not self.isEntry):
            self.importStrList.insert(1, self.picImportMuBan)
            self.bianLiangStrList.append(self.picBianLiangMuBan)
            self.getAndSetStrList.append(self.picGetSetMuBan)

        # 审核变量
        if self.picture & (not self.isEntry):
            self.importStrList.insert(2, self.exaImportMuBan)
            self.bianLiangStrList.append(self.exaBianLiangMuBan)
            self.getAndSetStrList.append(self.exaGetSetMuBan)

        # 组合get和set
        for bean in self.beanList:
            name = bean['name'][0].upper() + bean['name'][1:]
            getStrTemp = self.getMuBan % (name, bean['name'])
            setStrTemp = self.setMuBan % (name, bean['name'], bean['name'], bean['name'])
            self.getAndSetStrList.append(getStrTemp)
            self.getAndSetStrList.append(setStrTemp)

        self.getListBeanStr = self.getListBeanMuBan % (self.fileName, self.fileName, self.fileName, self.fileName)
        if not self.isEntry:

            strTemp = self.getBeanMuBan1
            strTemp = strTemp + '''
            if (jsonObject.has("entryInfos")) {
                bean.setEntryInfos(%sEntryBean.getListBean(jsonObject.get("entryInfos").toString()));
            }''' % self.classNamePrefix
            if self.picture:
                strTemp = strTemp + '''
            if (jsonObject.has("attachInfos")) {
                bean.setAttachInfos(AttachInfoBean.getListBean(jsonObject.get("attachInfos").toString()));
            }'''

            if self.examine:
                strTemp = strTemp + '''
            if (jsonObject.has("approveOpinionInfos")) {
                bean.setApproveOpinionInfos(ApproveOpinionBean.getListBean(jsonObject.get("approveOpinionInfos").toString()));
            }'''

            self.getBeanStr = strTemp + self.getBeanMuBan2
        else:
            self.getBeanStr = ''

        self.importStrList.extend(['\nimport java.util.ArrayList;\n',
                                   'import java.util.List;\n\n'])

    def getResultStr(self):
        strTemp = ''
        for str in self.importStrList:
            strTemp += str
        strTemp += self.classCreateStr
        for str in self.bianLiangStrList:
            strTemp += str
        for str in self.getAndSetStrList:
            strTemp += str
        strTemp += self.getListBeanStr
        strTemp += self.getBeanStr
        strTemp += self.endClassMuBan
        # return {'filename': self.fileName, 'content': strTemp}
        return [self.fileName, strTemp]

    def generateFile(self, path):

        if not os.path.exists(path):
            os.makedirs(path)
        resultPath = path + r'\%s.java' % self.fileName

        with open(resultPath, 'w') as file:
            for str in self.importStrList:
                file.write(str)
            file.write(self.classCreateStr)
            for str in self.bianLiangStrList:
                file.write(str)
            for str in self.getAndSetStrList:
                file.write(str)
            file.write(self.getListBeanStr)
            file.write(self.getBeanStr)
            file.write(self.endClassMuBan)
