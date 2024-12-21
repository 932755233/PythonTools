from 生泰尔代码生成工具 import StringTool


# 生成列表的Adapter的xml
class GenerateFragmentAdapterXml:
    xmlStartMuBan = '''<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:descendantFocusability="beforeDescendants"
    android:padding="@dimen/middlePadding">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:background="@drawable/item_card_background_selector"
        android:descendantFocusability="afterDescendants"
        android:orientation="vertical"
        android:padding="@dimen/basicPadding_">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical">
'''

    xmlEndMuBan = '''
            </LinearLayout>
    </LinearLayout>
</FrameLayout>'''

    xmlItemMuBan = '''
            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:gravity="center_vertical"
                android:orientation="horizontal">

                <TextView
                    style="@style/text_Style"
                    android:text="%s:" />

                <TextView
                    android:id="@+id/%s"
                    style="@style/edit_style"
                    android:layout_width="0dp"
                    android:layout_weight="1"
                    android:background="@null" />
            </LinearLayout>
    '''

    xmlItemStateMuBan = '''
            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:gravity="center_vertical"
                android:orientation="horizontal">

                <TextView
                    android:id="@+id/tv_tips"
                    style="@style/text_Style"
                    android:text="%s:" />

                <TextView
                    android:id="@+id/%s"
                    style="@style/edit_style"
                    android:layout_width="0dp"
                    android:layout_weight="1"
                    android:background="@null" />
            </LinearLayout>
    '''

    def __init__(self, classNamePrefix: str, beanList: [{str, str}]):

        self.fileName = 'item_fragment'
        words = StringTool.extract_words_starting_with_capital(classNamePrefix)
        for word in words:
            self.fileName += '_' + word.lower()

        xmlBeanList = sorted(beanList, key=lambda item: item['listNum'])
        self.contentStr = self.xmlStartMuBan
        for xmlBean in xmlBeanList:
            if xmlBean['listNum'] != '':
                strTemp = 'tv_' + xmlBean['name'].lower()
                if xmlBean['type'] == '单据状态':
                    self.contentStr += self.xmlItemStateMuBan % (xmlBean['showName'], strTemp)
                else:
                    self.contentStr += self.xmlItemMuBan % (xmlBean['showName'], strTemp)

        self.contentStr += self.xmlEndMuBan

    def getResult(self):
        # return {'filename': self.fileName, 'content': strTemp}
        return [self.fileName, self.contentStr]
