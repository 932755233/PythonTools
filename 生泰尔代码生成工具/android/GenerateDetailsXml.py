from 生泰尔代码生成工具 import StringTool
from 生泰尔代码生成工具.android.BaseGenerate import BaseGenerate


class GenerateDetailsXml(BaseGenerate):
    xmlHeadMuBan = '''<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/item_bg_normal"
    android:orientation="vertical">

    <include layout="@layout/layout_title_bar" />

    <ScrollView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:scrollbars="none">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:orientation="vertical">

            <TextView
                android:id="@+id/top_tips"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:paddingLeft="@dimen/middlePadding"
                android:paddingTop="@dimen/smallPadding"
                android:paddingBottom="@dimen/smallPadding" />

            <View
                android:layout_width="match_parent"
                android:layout_height="2px"
                android:background="@color/regist_line" />

            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:background="@color/colorWhite"
                android:orientation="vertical">
'''
    # 仅展示
    jinzhanshiItemMuBan = '''
                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:gravity="center_vertical"
                    android:orientation="horizontal"
                    android:paddingTop="@dimen/basicPadding_"
                    android:paddingBottom="@dimen/basicPadding_">

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
    # 可写
    kexieItemMuBan = '''
                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:gravity="center_vertical"
                    android:orientation="horizontal"
                    android:paddingTop="@dimen/basicPadding_"
                    android:paddingBottom="@dimen/basicPadding_">

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
                        android:id="@+id/tv_%s"
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
                    android:paddingTop="@dimen/basicPadding_"
                    android:paddingBottom="@dimen/basicPadding_">
        
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
                     android:paddingTop="@dimen/basicPadding_"
                     android:paddingBottom="@dimen/basicPadding_">
        
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

    topHeadEndMuBan = '''
            </LinearLayout>
    '''

    # 分录承载ListView
    entryContentMuBan = '''
            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:gravity="center_horizontal"
                android:paddingTop="@dimen/middlePadding"
                android:paddingBottom="@dimen/middlePadding"
                android:text="分录名称"
                android:textColor="@color/list_view_item_focus_color"
                android:textSize="@dimen/sticker_text_size_easy_photos" />

            <com.monkeyk.klutils.view.RewriteListView
                android:id="@+id/content_lv"
                android:layout_width="match_parent"
                android:layout_height="50dip"
                android:animateLayoutChanges="true"
                android:cacheColorHint="#00000000"
                android:divider="@color/result_view_transparent"
                android:dividerHeight="@dimen/middlePadding"
                android:padding="@dimen/middlePadding"
                android:scrollbars="none" />
    '''

    # 图片内容
    picContentMuBan = '''
            <LinearLayout
                android:id="@+id/content_ll"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="@dimen/smallMargin"
                android:background="@color/colorWhite"
                android:orientation="vertical">

                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:orientation="horizontal"
                    android:paddingLeft="@dimen/normalPadding"
                    android:paddingTop="@dimen/normalPadding">

                    <TextView
                        android:id="@+id/number_info_tv"
                        style="@style/text_sign_Style"
                        android:visibility="invisible" />

                    <TextView
                        android:id="@+id/number_info_tv1"
                        style="@style/text_Style"
                        android:layout_height="wrap_content"
                        android:layout_toRightOf="@+id/number_info_tv"
                        android:text="图片凭证：" />
                </LinearLayout>

                <com.monkeyk.klutils.view.RewriteGridView
                    android:id="@+id/content_imge"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_gravity="center_horizontal"
                    android:gravity="center"
                    android:listSelector="#00000000"
                    android:numColumns="3"
                    android:padding="@dimen/normalPadding"
                    android:scrollbars="none" />
            </LinearLayout>
    '''

    # 审核内容
    exaContentMuBan = '''
            <com.monkeyk.klutils.view.RewriteListView
                android:id="@+id/approval_pinion_lv"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:background="@color/background"
                android:cacheColorHint="#00000000"
                android:divider="@color/result_view_transparent"
                android:dividerHeight="@dimen/basicPadding_"
                android:paddingTop="@dimen/indicator_corner_radius"
                android:paddingBottom="@dimen/indicator_corner_radius"
                android:scrollbars="none"
                android:visibility="gone"
                tools:visibility="visible" />
    '''
    xmlFootMuBan = '''
            <LinearLayout
                android:id="@+id/ll_bottom"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="@dimen/smallMargin"
                android:orientation="horizontal"
                android:paddingTop="@dimen/normalPadding"
                android:paddingBottom="@dimen/normalPadding">

                <TextView
                    android:id="@+id/tv_save"
                    android:layout_width="0dp"
                    android:layout_height="wrap_content"
                    android:layout_centerInParent="true"
                    android:layout_marginLeft="@dimen/littleMargin"
                    android:layout_marginRight="@dimen/basicMargin"
                    android:layout_weight="1"
                    android:background="@drawable/ripple_button_single"
                    android:gravity="center"
                    android:paddingTop="@dimen/smallPadding"
                    android:paddingBottom="@dimen/smallPadding"
                    android:text="@string/cost_temporary_storage"
                    android:textColor="@color/colorWhite"
                    android:textSize="@dimen/xml_text_size_medium"
                    android:visibility="visible" />

                <TextView
                    android:id="@+id/tv_delete"
                    android:layout_width="0dp"
                    android:layout_height="wrap_content"
                    android:layout_centerInParent="true"
                    android:layout_marginLeft="@dimen/basicMargin"
                    android:layout_marginRight="@dimen/littleMargin"
                    android:layout_weight="1"
                    android:background="@drawable/ripple_button_single"
                    android:gravity="center"
                    android:paddingTop="@dimen/smallPadding"
                    android:paddingBottom="@dimen/smallPadding"
                    android:text="删除"
                    android:textColor="@color/colorWhite"
                    android:textSize="@dimen/xml_text_size_medium"
                    android:visibility="visible" />

                <TextView
                    android:id="@+id/tv_add"
                    android:layout_width="0dp"
                    android:layout_height="wrap_content"
                    android:layout_centerInParent="true"
                    android:layout_marginLeft="@dimen/basicMargin"
                    android:layout_marginRight="@dimen/basicMargin"
                    android:layout_weight="1"
                    android:background="@drawable/ripple_button_single"
                    android:gravity="center"
                    android:paddingTop="@dimen/smallPadding"
                    android:paddingBottom="@dimen/smallPadding"
                    android:text="新增"
                    android:textColor="@color/colorWhite"
                    android:textSize="@dimen/xml_text_size_medium"
                    android:visibility="visible" />

                <TextView
                    android:id="@+id/tv_submit"
                    android:layout_width="0dp"
                    android:layout_height="wrap_content"
                    android:layout_centerInParent="true"
                    android:layout_marginLeft="@dimen/basicMargin"
                    android:layout_marginRight="@dimen/littleMargin"
                    android:layout_weight="1"
                    android:background="@drawable/ripple_button_single"
                    android:gravity="center"
                    android:paddingTop="@dimen/smallPadding"
                    android:paddingBottom="@dimen/smallPadding"
                    android:text="@string/cost_rejection_submit"
                    android:textColor="@color/colorWhite"
                    android:textSize="@dimen/xml_text_size_medium"
                    android:visibility="visible" />
            </LinearLayout>
        </LinearLayout>
    </ScrollView>
</LinearLayout>'''

    def __init__(self, classNamePrefix: str, beanList: [], hasEntry: bool, picture: bool,examine:bool):
        self.fileName = 'layout_details'
        words = StringTool.extract_words_starting_with_capital(classNamePrefix)
        for word in words:
            self.fileName += '_' + word.lower()

        xmlBeanList = sorted(beanList, key=lambda item: item['detialNum'])

        self.contentStr = self.xmlHeadMuBan

        for bean in xmlBeanList:
            if bean['detialNum'] != '':
                if bean['type'] == '可写':
                    self.contentStr += self.kexieItemMuBan % (
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
                    self.contentStr += self.jinzhanshiItemMuBan % (
                        bean['name'].lower(),
                        StringTool.format_xml_show_title(bean['showName']),
                        bean['name'].lower()
                    )

        self.contentStr += self.topHeadEndMuBan

        if hasEntry:
            self.contentStr += self.entryContentMuBan

        if picture:
            self.contentStr += self.picContentMuBan

        if examine:
            self.contentStr += self.exaContentMuBan

        self.contentStr += self.xmlFootMuBan
