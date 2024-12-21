from 生泰尔代码生成工具 import StringTool
from 生泰尔代码生成工具.android.BaseGenerate import BaseGenerate


class GenerateEntryAdapterXml(BaseGenerate):
    # 可点可写安卓 代码  TechnicalSupportApplicationEntryAdapter.java

    # lieBiaoType = ['隐藏',
    #                '仅展示',
    #                '可写',
    #                '可点-下级选择',
    #                '可点-弹窗选择',
    #                '可点-时间选择',
    #                '点写-下级选择',
    #                '点写-弹窗选择',
    #                '点写-时间选择',
    #                '单据状态']

    xmlHeadMuban = '''<?xml version="1.0" encoding="utf-8"?>
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
        android:paddingTop="@dimen/basicPadding_"
        android:paddingBottom="@dimen/basicPadding_">
'''

    # 仅展示模板
    jinzhanshiMuban = '''
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:gravity="center_vertical"
            android:orientation="horizontal"
            android:paddingTop="@dimen/stroke_width"
            android:paddingBottom="@dimen/stroke_width">

            <TextView
                android:id="@+id/tv_%s_red"
                style="@style/text_sign_Style"
                android:layout_height="match_parent"
                android:text="*"
                android:visibility="invisible" />

            <TextView
                style="@style/text_Style"
                android:layout_gravity="top"
                android:text="%s:" />

            <TextView
                android:id="@+id/tv_%s"
                style="@style/edit_style"
                android:layout_width="0dp"
                android:layout_weight="1"
                android:background="@drawable/rounded_text" />
        </LinearLayout>
        '''
    # 可写模板
    kexieMuban = '''
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:gravity="center_vertical"
            android:orientation="horizontal"
            android:paddingTop="@dimen/stroke_width"
            android:paddingBottom="@dimen/stroke_width">

            <TextView
                android:id="@+id/tv_%s_red"
                style="@style/text_sign_Style"
                android:layout_height="match_parent"
                android:text="*"
                android:visibility="visible" />

            <TextView
                style="@style/text_Style"
                android:layout_gravity="top"
                android:text="%s:" />

            <EditText
                android:id="@+id/et_%s"
                style="@style/edit_style"
                android:layout_width="0dp"
                android:layout_weight="1"
                android:hint="请输入%s" />
        </LinearLayout>
        '''
    # 可点
    kedianMuban = '''
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:gravity="center_vertical"
            android:orientation="horizontal"
            android:paddingTop="@dimen/stroke_width"
            android:paddingBottom="@dimen/stroke_width">

            <TextView
                android:id="@+id/tv_%s_red"
                style="@style/text_sign_Style"
                android:layout_height="match_parent"
                android:text="*"
                android:visibility="visible" />

            <TextView
                style="@style/text_Style"
                android:layout_gravity="top"
                android:text="%s:" />

            <TextView
                android:id="@+id/tv_%s"
                style="@style/edit_style"
                android:layout_width="0dp"
                android:layout_weight="1"
                android:hint="请选择%s" />
        </LinearLayout>
    '''
    # 点写
    dianxieMuban = '''
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:gravity="center_vertical"
            android:orientation="horizontal"
            android:paddingTop="@dimen/stroke_width"
            android:paddingBottom="@dimen/stroke_width">

            <TextView
                android:id="@+id/tv_%s_red"
                style="@style/text_sign_Style"
                android:layout_height="match_parent"
                android:text="*"
                android:visibility="visible" />

            <TextView
                style="@style/text_Style"
                android:layout_gravity="top"
                android:text="%s:" />

            <RelativeLayout
                android:layout_width="0dp"
                android:layout_weight="1"
                android:padding="0dp"
                style="@style/edit_style"
                android:layout_height="wrap_content">

                <EditText
                    android:id="@+id/et_%s"
                    style="@style/edit_style"
                    android:layout_marginRight="0dp"
                    android:layout_width="match_parent"
                    android:hint="请输入或选择%s" />

                <ImageView
                    android:id="@+id/iv_%s"
                    android:layout_centerVertical="true"
                    android:layout_alignParentRight="true"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:background="@mipmap/add_user_info"/>
            </RelativeLayout>
        </LinearLayout>
    '''

    xmlFootMuban = '''
        <RelativeLayout
            android:id="@+id/rl_bottom"
            android:layout_width="match_parent"
            android:layout_height="wrap_content">

            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:layout_centerInParent="true"
                android:text="金额计量单位:元"
                android:textColor="@color/red"
                android:textSize="@dimen/big_text_size"
                android:visibility="invisible" />

            <ImageView
                android:id="@+id/iv_delete"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:layout_alignParentRight="true"
                android:background="@drawable/ripple_item_single"
                android:padding="@dimen/normalPadding"
                android:src="@mipmap/store_img_del" />
        </RelativeLayout>
    </LinearLayout>
</FrameLayout>
'''

    def __init__(self, classNamePrefix: str, entryBeanList: []):
        self.fileName = 'item_entry'
        words = StringTool.extract_words_starting_with_capital(classNamePrefix)
        for word in words:
            self.fileName += '_' + word.lower()

        xmlBeanList = sorted(entryBeanList, key=lambda item: item['listNum'])

        self.contentStr = self.xmlHeadMuban

        for bean in xmlBeanList:
            if bean['listNum'] != '':
                if bean['type'] == '可写':
                    self.contentStr += self.kexieMuban % (
                        bean['name'].lower(),
                        StringTool.format_xml_show_title(bean['showName']),
                        bean['name'].lower(),
                        bean['showName']
                    )
                elif '可点' in bean['type']:
                    self.contentStr += self.kedianMuban % (
                        bean['name'].lower(),
                        StringTool.format_xml_show_title(bean['showName']),
                        bean['name'].lower(),
                        bean['showName']
                    )
                elif '点写' in bean['type']:
                    self.contentStr += self.dianxieMuban % (
                        bean['name'].lower(),
                        StringTool.format_xml_show_title(bean['showName']),
                        bean['name'].lower(),
                        bean['showName'],
                        bean['name'].lower()
                    )
                else:
                    self.contentStr += self.jinzhanshiMuban % (
                        bean['name'].lower(),
                        StringTool.format_xml_show_title(bean['showName']),
                        bean['name'].lower()
                    )

        self.contentStr += self.xmlFootMuban
