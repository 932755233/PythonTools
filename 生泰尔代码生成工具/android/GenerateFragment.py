from 生泰尔代码生成工具 import StringTool
from 生泰尔代码生成工具.android.BaseGenerate import BaseGenerate


class GenerateFragment(BaseGenerate):
    importMuBan = '''package com.centre.workoffice.fragment;

import android.content.Intent;
import android.graphics.drawable.ColorDrawable;
import android.os.Message;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.monkeyk.base.ui.BaseFragment;
import com.monkeyk.centre.utils.DensityUtil;
import com.monkeyk.centre.view.searchview.ICallBack;
import com.monkeyk.centre.view.searchview.SearchView;
import com.monkeyk.ht.baseexception.BizException;
import com.monkeyk.ht.pulltorefreshView.PullToRefreshLayout;
import com.monkeyk.ht.pulltorefreshView.PullableListView;
import com.monkeyk.htjava.utils.RootConstant;
import com.monkeyk.htjava.utils.StringUtil;
import com.monkeyk.kl_aalibrary.ViewInjector;
import com.monkeyk.kl_annotation.ViewById;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
'''

    classHeadMuBan = '''
public class %s extends BaseFragment implements PullToRefreshLayout.OnRefreshListener, AdapterView.OnItemClickListener {
    @ViewById
    TextView base_relevant_tv;
    @ViewById
    LinearLayout ll_content;
    @ViewById
    PullToRefreshLayout pull_freshlayout_view;
    @ViewById
    PullableListView pull_freshlayout_list;
    @ViewById
    SearchView search_view;
    private int currentPage = 0;
    private int totalPage = 0;
    private String filter;
'''
    bianliangMuBan = '''
    private List<%sBean> mList;
    private %sAdapter mAdapter;
    '''
    handlerMuBan = '''
    @Override
    public void handler(Message msg) throws BizException {
        super.handler(msg);
        List<%sBean> mSBean = loadData(String.valueOf(msg.obj));
        switch (msg.what) {
            case RootConstant.APP_LOAD_FIRST_PAGE:
                pull_freshlayout_view.refreshFinish(PullToRefreshLayout.SUCCEED);
                if (mSBean.size() == 0) {
                    ll_content.setVisibility(View.GONE);
                    base_relevant_tv.setVisibility(View.VISIBLE);
                } else {
                    ll_content.setVisibility(View.VISIBLE);
                    base_relevant_tv.setVisibility(View.GONE);
                    mList.clear();
                    mList.addAll(mSBean);
                    mAdapter.setData(mList);
                }
                break;
            case RootConstant.APP_LOAD_MORE_PAGE:
                pull_freshlayout_view.loadmoreFinish(PullToRefreshLayout.SUCCEED);
                mList.addAll(mSBean);
                mAdapter.setData(mList);
                break;
            default:
                break;
        }
    }
    '''
    onItemClickMuBan = '''
    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
        Intent intent = new Intent();
        // todo 这里需要更改ID
        intent.putExtra("FID", mList.get(position).getFID());
        intent.putExtra("DATACENTRE", mList.get(position).getFDataCenter());
        intent.putExtra("type_name", "%s");
        intent.putExtra("TYPE", "%s");
        startIntent(mContext, intent, %sDetailsActivity.class);
    }
    '''
    bindLayoutMuBan = '''
    @Override
    protected View bindLayout(LayoutInflater inflater, ViewGroup container) {
        return inflater.inflate(R.layout.%s, container, false);
    }
    '''
    initDataMuBan = '''
    @Override
    protected void initData() throws BizException {
        pull_freshlayout_view.setOnRefreshListener(this);
        pull_freshlayout_list.setOnItemClickListener(this);
        pull_freshlayout_list.setDivider(new ColorDrawable(0x00000000));
        pull_freshlayout_list.setDividerHeight(DensityUtil.dip2px(mContext, 8));
        search_view.setOnClickSearch(new ICallBack() {
            @Override
            public void SearchAciton(String string) {
                filter = string;
                getData(0, RootConstant.APP_LOAD_FIRST_PAGE);
            }

            @Override
            public void clearAciton() {
            }
        });
        mList = new ArrayList<>();
        mAdapter = new %sAdapter(getContext(), mList);
        pull_freshlayout_list.setAdapter(mAdapter);

    }
    '''
    onResumeOnGetDataMuBan = '''
    @Override
    public void onResume() {
        super.onResume();
        if (ifRefresh) {
            getData(0, RootConstant.APP_LOAD_FIRST_PAGE);
        }
    }

    @Override
    public void networkErrorData(int type, boolean isOnCallback) {
        super.networkErrorData(type, isOnCallback);
        pull_freshlayout_view.loadmoreFinish(PullToRefreshLayout.FAIL);
        pull_freshlayout_view.refreshFinish(PullToRefreshLayout.FAIL);
    }

    @Override
    public void onRefresh(PullToRefreshLayout pullToRefreshLayout) {
        getData(0, RootConstant.APP_LOAD_FIRST_PAGE);

    }

    @Override
    public void onLoadMore(PullToRefreshLayout pullToRefreshLayout) {
        int size = currentPage + 1;
        if (size < totalPage) {
            getData(size, RootConstant.APP_LOAD_MORE_PAGE);
        } else {
            pullToRefreshLayout.loadmoreFinish(PullToRefreshLayout.NOMORE);
        }
    }

    private void getData(int number, int key) {
        HashMap hashMap = new HashMap();
        hashMap.put(RootConstant.APP_JSON_PAGENO, number);
        hashMap.put(RootConstant.APP_JSON_PAGESIZE, RootConstant.APP_PAGESIZE_NUMBER);
        hashMap.put("jsonStr", filter);
        Map mapRoot = new HashMap();
        mapRoot.put(RootConstant.APP_REQUST_KEY, key);
        // todo 这里需要补充地址
        mapRoot.put(RootConstant.APP_REQUST_URL, AppConstants.getUrl() + AppConstants.这里需要补充地址);
        mapRoot.put(RootConstant.APP_REQUST_CONTENT, hashMap);
        ViewInjector.networkRequest(_mActivity, this, mapRoot);
    }
    '''
    loadDataMuBan = '''
    private List<%sBean> loadData(String loginHead) throws BizException {
        NeedCollBean needCollBean = NeedCollBean.getBean(loginHead);
        List<%sBean> mList = new ArrayList<>();
        currentPage = Integer.parseInt(needCollBean.getCurrentPage());
        totalPage = Integer.parseInt(needCollBean.getTotalPage());
        String needLoad = needCollBean.getList();
        if (StringUtil.isNotEmpty(needLoad)) {
            mList.addAll(%sBean.getListBean(needLoad));
        }
        return mList;
    }
}
'''

    def __init__(self, classNamePrefix: str,
                 infix: str,
                 typeName: str):
        self.fileName = '%s%sFragment' % (classNamePrefix, infix)
        classHeadStr = self.classHeadMuBan % self.fileName
        bianliangStr = self.bianliangMuBan % (classNamePrefix, classNamePrefix)
        handlerStr = self.handlerMuBan % classNamePrefix
        # todo 这里需要其他文件配合
        onItemClickStr = self.onItemClickMuBan % (typeName, infix.lower(), classNamePrefix)

        xmlFileName = 'layout_fragment'
        words = StringTool.extract_words_starting_with_capital(classNamePrefix)
        for word in words:
            xmlFileName += '_' + word.lower()
        bindLayoutStr = self.bindLayoutMuBan % xmlFileName
        initDataStr = self.initDataMuBan % classNamePrefix
        onResumeOnGetDataStr = self.onResumeOnGetDataMuBan
        loadDataStr = self.loadDataMuBan % (classNamePrefix, classNamePrefix, classNamePrefix)

        self.contentStr += self.importMuBan
        self.contentStr += classHeadStr
        self.contentStr += bianliangStr
        self.contentStr += handlerStr
        self.contentStr += onItemClickStr
        self.contentStr += bindLayoutStr
        self.contentStr += initDataStr
        self.contentStr += onResumeOnGetDataStr
        self.contentStr += loadDataStr
