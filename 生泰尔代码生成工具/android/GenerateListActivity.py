from 生泰尔代码生成工具 import StringTool
from 生泰尔代码生成工具.android.BaseGenerate import BaseGenerate


class GenerateListActivity(BaseGenerate):
    importMuban = '''package com.centre.workoffice.activity;

import android.content.Intent;
import android.view.View;
import android.widget.RelativeLayout;
import android.widget.TextView;

import androidx.fragment.app.Fragment;
import androidx.viewpager.widget.ViewPager;

import com.monkeyk.ht.baseexception.BizException;
import com.monkeyk.kl_annotation.ViewById;
import com.monkeyk.klutils.adapter.ViewPagerAdapter;

import java.util.ArrayList;
import java.util.List;

'''
    classHeadMuban = '''public class %sListActivity extends CentreBaseActivity implements ViewPager.OnPageChangeListener {
    @ViewById(onClick = 0)
    TextView txt_left_title;  // 回退按钮
    @ViewById
    TextView txt_main_title;// 标题

'''

    bianliangItemMuban = '''
    @ViewById(onClick = 0)
    RelativeLayout rl_%s;
    @ViewById
    View view_%s;
    @ViewById
    TextView tv_%s;
    '''
    bianliangEndMuban = '''
    @ViewById
    ViewPager viewpager_coll;
    private List<Fragment> fragments;
    private List<View> viewList;
    private List<TextView> textViewList;
    '''

    getLayoutIdMuban = '''
    @Override
    protected int getLayoutId() throws BizException {
        return R.layout.layout_list%s;
    }
    '''

    initDataHeadMuban = '''
    @Override
    protected void initData() throws Exception {
        super.initData();
        txt_left_title.setVisibility(View.VISIBLE);
        Intent intent = getIntent();
        String fName = intent.getStringExtra("type_name");
        txt_main_title.setText(fName);
        fragments = new ArrayList<>();
        viewList = new ArrayList<>();
        textViewList = new ArrayList<>();
    '''
    initDataItemMuban = '''
        fragments.add(new %s%sFragment());
        viewList.add(view_%s);
        textViewList.add(tv_%s);
    '''
    initDataEndMuban = '''
        viewpager_coll.setOnPageChangeListener(this);
        viewpager_coll.setAdapter(new ViewPagerAdapter(getSupportFragmentManager(), fragments));
        setSelectedBackground(0);
    }
    '''

    viewPagerMuban = '''
    @Override
    public void onPageScrolled(int position, float positionOffset, int positionOffsetPixels) {
    }

    @Override
    public void onPageSelected(int position) {
        setSelectedBackground(position);
    }

    @Override
    public void onPageScrollStateChanged(int state) {
    }

    private void setSelectedBackground(int position) {
        viewpager_coll.setCurrentItem(position);
        for (View view : viewList) {
            view.setBackgroundDrawable(null);
        }
        for (int i = 0; i < viewList.size(); i++) {
            if (i == position) {
                viewList.get(i).setBackgroundResource(R.color.color_login_background);
            }
        }
        for (int i = 0; i < textViewList.size(); i++) {
            if (i == position) {
                textViewList.get(i).setTextColor(getResources().getColor(R.color.color_login_background));
            } else {
                textViewList.get(i).setTextColor(getResources().getColor(R.color.text_front_style_scannd));
            }
        }
    }
    '''

    widgetOnClickHeadMuban = '''
    @Override
    public void widgetOnClick(View v) throws BizException {
        switch (v.getId()) {
            case R.id.txt_left_title:
                mSwipeBackHelper.backward();
                break;
    '''
    widgetOnClickItemMuban = '''
            case R.id.rl_%s:
                setSelectedBackground(%d);
                break;
    '''
    widgetOnClickFootMuban = '''
            default:
                break;
        }
    }
}'''

    xmlHeadMuban = '''<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/background"
    android:orientation="vertical">

    <include layout="@layout/layout_title_bar" />

    <RelativeLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:visibility="visible">

        <LinearLayout
            android:id="@+id/need_process_ll"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="horizontal">

'''
    xmlItemMuban = '''
            <RelativeLayout
                android:id="@+id/rl_%s"
                android:layout_width="0dip"
                android:layout_height="wrap_content"
                android:layout_weight="1">

                <View
                    android:id="@+id/view_%s"
                    android:layout_width="match_parent"
                    android:layout_height="2dip"
                    android:layout_below="@+id/tv_%s"
                    android:layout_marginLeft="12dip"
                    android:layout_marginRight="12dip"
                    android:background="@null" />

                <TextView
                    android:id="@+id/tv_%s"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_centerInParent="true"
                    android:layout_marginTop="17dip"
                    android:background="@null"
                    android:clickable="false"
                    android:text="%s"
                    android:textColor="@color/text_front_style_scannd"
                    android:textSize="@dimen/xml_text_size_medium" />
            </RelativeLayout>
'''
    xmlFootMuban = '''
        </LinearLayout>

        <ImageView
            android:id="@+id/iv1"
            android:layout_width="match_parent"
            android:layout_height="1.5px"
            android:layout_below="@+id/need_process_ll"
            android:background="@color/collaborative_view_background" />

        <com.monkeyk.klutils.view.ScrollViewPager
            android:id="@+id/viewpager_coll"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            android:layout_below="@+id/iv1"
            android:layout_gravity="center" />
    </RelativeLayout>
</LinearLayout>
'''

    def __init__(self, classNamePrefix: str, fragmentNameList: []):
        self.fileName = '%sListActivity' % classNamePrefix

        classHeadStr = self.classHeadMuban % classNamePrefix

        bianliangStrList = []
        for bean in fragmentNameList:
            bianliangStrList.append(
                self.bianliangItemMuban % (bean['name'].lower(), bean['name'].lower(), bean['name'].lower()))

        lowerFileName = ''
        words = StringTool.extract_words_starting_with_capital(classNamePrefix)
        for word in words:
            lowerFileName += '_' + word.lower()
        getLayoutIdStr = self.getLayoutIdMuban % lowerFileName

        initDataItemStrList = []
        for bean in fragmentNameList:
            strTemp = self.initDataItemMuban % (
                classNamePrefix, bean['name'], bean['name'].lower(), bean['name'].lower())
            initDataItemStrList.append(strTemp)

        clickItemStrList = []
        for i, bean in enumerate(fragmentNameList):
            clickItemStrList.append(self.widgetOnClickItemMuban % (bean['name'].lower(), i))

        self.contentStr = self.importMuban

        self.contentStr += classHeadStr

        for strTemp in bianliangStrList:
            self.contentStr += strTemp

        self.contentStr += self.bianliangEndMuban

        self.contentStr += getLayoutIdStr

        self.contentStr += self.initDataHeadMuban

        for strTemp in initDataItemStrList:
            self.contentStr += strTemp

        self.contentStr += self.initDataEndMuban

        self.contentStr += self.viewPagerMuban

        self.contentStr += self.widgetOnClickHeadMuban

        for strTemp in clickItemStrList:
            self.contentStr += strTemp

        self.contentStr += self.widgetOnClickFootMuban

        # xml文件
        self.xmlFileName = 'layout_list%s' % lowerFileName

        self.xmlContentStr = self.xmlHeadMuban

        for bean in fragmentNameList:
            strTemp = self.xmlItemMuban % (
                bean['name'].lower(),
                bean['name'].lower(),
                bean['name'].lower(),
                bean['name'].lower(),
                bean['showName'])
            self.xmlContentStr += strTemp
        self.xmlContentStr += self.xmlFootMuban

    def getResult(self):
        return [self.fileName, self.contentStr, self.xmlFileName, self.xmlContentStr]
