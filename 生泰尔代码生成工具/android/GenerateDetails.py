from 生泰尔代码生成工具 import StringTool
from 生泰尔代码生成工具.android.BaseGenerate import BaseGenerate


class GenerateDetails(BaseGenerate):
    fileHeadMuBan = '''package com.centre.workoffice.activity;

import android.app.Activity;
import android.content.Intent;
import android.os.Message;
import android.text.Html;
import android.text.TextUtils;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.AdapterView;
import android.widget.GridView;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.TextView;

import com.monkeyk.base.file.FileBean;
import com.monkeyk.ht.baseexception.BizException;
import com.monkeyk.htjava.bean.BeanHead;
import com.monkeyk.htjava.gson.Gson;
import com.monkeyk.htjava.utils.DateUtil;
import com.monkeyk.htjava.utils.RootConstant;
import com.monkeyk.htjava.utils.StringUtil;
import com.monkeyk.kl_aalibrary.ViewInjector;
import com.monkeyk.kl_annotation.ViewById;
import com.monkeyk.kliselector.EasyPhotos;
import com.monkeyk.kliselector.GlideEngine;
import com.monkeyk.kliselector.glideutil.AddImageAdapter;
import com.monkeyk.kliselector.luban.Luban;
import com.monkeyk.kliselector.luban.OnCompressListener;
import com.monkeyk.klutils.LogUtil;
import com.monkeyk.klutils.dailog.BottemDialog;
import com.monkeyk.klutils.dailog.DateSelelctDialog;
import com.monkeyk.klutils.dailog.ttt.C2089a;
import com.monkeyk.klutils.dailog.ttt.C2091b;
import com.monkeyk.klutils.unified.SharePrefUtil;

import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
'''
    classHeadMuBan = '\npublic class %sDetailsActivity extends %s {\n'

    requestIntMuBan = '''
    private static final int REQUEST_NETWORK_GET_INFO_DATA = 0x2101;
    private static final int REQUEST_NETWORK_SAVE = 0x2102;
    private static final int REQUEST_NETWORK_DELETE = 0x2103;
    private static final int REQUEST_NETWORK_SUBMIT = 0x2104;\n
'''
    selectIntMuBan = '    private static final int SELECTSEARCH_CHOOSE_%s = 0x%d;\n'
    bianliangTopBarMuBan = '''
    @ViewById(onClick = 0)
    TextView txt_left_title;
    @ViewById
    TextView txt_main_title;
    @ViewById
    TextView top_tips;
\n'''

    bianliangKexieMuBan = '''    @ViewById
    TextView tv_%s_red;
    @ViewById
    EditText et_%s;'''

    bianliangKedianMuBan = '''    @ViewById
    TextView tv_%s_red;
    @ViewById(onClick = 0)
    TextView tv_%s;'''

    bianliangDianxieMuBan = '''    @ViewById
    TextView tv_%s_red;
    @ViewById(onClick = 0)
    ImageView iv_%s;
    @ViewById
    TextView et_%s;'''

    bianliangJinzhanshiMuBan = '''    @ViewById
    TextView tv_%s_red;
    @ViewById
    TextView tv_%s;'''

    # 分录需要的控件ID
    entryKongIDMuBan = '''
    @ViewById
    ListView content_lv;%s
    '''
    # 图片需要的控件ID
    picKongIDMuBan = '''
    %s
    @ViewById
    LinearLayout content_ll;
    @ViewById
    GridView content_imge;
    '''

    examineKongIDMuBan = '''
    @ViewById
    ListView approval_pinion_lv;%s
    '''

    # 底部按钮变量
    bianliangBottomButMuBan = '''
    @ViewById
    LinearLayout ll_bottom;
    @ViewById(onClick = 0)
    TextView tv_save;
    @ViewById(onClick = 0)
    TextView tv_delete;
    @ViewById(onClick = 0)
    TextView tv_add;
    @ViewById(onClick = 0)
    TextView tv_submit;
'''

    bianliangTuPianMuBan = '''
    %s
    private Integer flag = -1;
    private List<String> tempList;
    private List<String> tempData;
'''

    bianliangZhuShuJuMuBan = '''
    %s
    private %sBean mBean;
    private String type;
    private String mFid;
    private String datacenter;
'''

    bianliangFenLuMuBan = '''
    %s
    private List<%sEntryBean> entryBeanList;
    private %sEntryAdapter mAdapter;
    private int tempPosition;
'''

    handlerHeadMuBan = '''
    @Override
    public void handler(Message msg) throws BizException {
        super.handler(msg);
        LogUtil.d(this.getClass().getSimpleName() + "---network--" + msg.obj);
        switch (msg.what) {
            case REQUEST_NETWORK_GET_INFO_DATA:
'''

    handlerSetBeanMuBan = '                mBean = %sBean.getBean(String.valueOf(msg.obj));'

    handlerFootMuBan = '''
                formatData();
                break;
            case REQUEST_NETWORK_SAVE:
                showToast("保存成功");
                SharePrefUtil.saveBoolean(this, "常量1", true);// todo 这里需要补齐常量
                mSwipeBackHelper.backward();
                break;
            case REQUEST_NETWORK_SUBMIT:
                showToast("提交成功");
                SharePrefUtil.saveBoolean(this, "常量2", true);// todo 这里需要补齐常量
                mSwipeBackHelper.backward();
                break;
            case REQUEST_NETWORK_DELETE:
                showToast("删除成功");
                SharePrefUtil.saveBoolean(this, "常量3", true);// todo 这里需要补齐常量
                mSwipeBackHelper.backward();
                break;
            default:
                break;
        }
    }
    '''

    picnetworkCorrectFileDataMuBan = '''
    @Override
    protected void networkCorrectFileData(BeanHead bean) {
        if ("1".equals(bean.getState())) {
            if (flag == REQUEST_NETWORK_SUBMIT) {
                showToast("数据提交成功");
                SharePrefUtil.saveBoolean(this, "常量", true);// todo 这里需要补齐常量
                mSwipeBackHelper.backward();
            } else if (flag == REQUEST_NETWORK_SAVE) {
                showToast("数据成功暂存");
                SharePrefUtil.saveBoolean(this, "常量", true);// todo 这里需要补齐常量
                mSwipeBackHelper.backward();
            }
        } else if ("0".equals(bean.getState())) {
            if (StringUtil.isNotEmpty(bean.getMsg())) {
                showToast(bean.getMsg());
            } else {
                showToast(getString(R.string.get_failed_submit));
            }
        }
    }
'''

    formatDataHeadMuBan = '''
    private void formatData() {
'''
    formatDataSetItemMuBan = '        %s.setText(mBean.get%s());\n'

    formatDataZhuangtaiMuBan = '''
        // todo 这里需要替换状态值
        if (TextUtils.equals("processed", type)) {
'''
    formatDataChaKJItemMuBan = '''
            tv_%s_red.setVisibility(View.INVISIBLE);
            %s.setBackgroundResource(R.drawable.rounded_text);
            %s.setFocusable(false);
            %s.setClickable(false);
            %s.setFocusableInTouchMode(false); 
'''

    formatDataEntry1MuBan = '''
            if (entryBeanList == null || entryBeanList.size() == 0) {
                content_lv.setVisibility(View.GONE);
            } else {
                mAdapter.notifyDataSetChanged(entryBeanList);
            }
    '''

    formatDataEntry2MuBan = '''
            if (entryBeanList == null || entryBeanList.size() == 0) {
                entryBeanList = new ArrayList<>();
                entryBeanList.add(new %sEntryBean());
            }
            mAdapter.notifyDataSetChanged(entryBeanList);
    '''
    formatDataShowEndMuBan = '''
            ll_bottom.setVisibility(View.VISIBLE);
            tv_delete.setVisibility(View.VISIBLE);
        } else {
            ll_bottom.setVisibility(View.VISIBLE);
            tv_delete.setVisibility(View.GONE);
        }
'''
    formatDataShowPicMuBan = '''
        %s
        data.clear();
        if (mBean.getAttachInfos() != null && mBean.getAttachInfos().size() > 0) {
            //拆出来是否图片和非图片的情况
            tempData.clear();
            for (AttachInfoBean bean : mBean.getAttachInfos()) {
                if (bean.getFPathAll().endsWith("bmp") ||
                        bean.getFPathAll().endsWith("jpg") || bean.getFPathAll().endsWith("gif") ||
                        bean.getFPathAll().endsWith("png") || bean.getFPathAll().endsWith("tif") || bean.getFPathAll().endsWith("jpeg")) {
                    tempData.add(bean.getFPathAll());
                }
            }
            if (tempData.size() != 0) {
                data.clear();
                content_ll.setVisibility(View.VISIBLE);
                data.addAll(tempData);
                adapter.notifyDataSetChanged();
            }
        }
'''
    formatDataShowExaMuBan = '''
        %s
        if (mBean.getApproveOpinionInfos() != null && mBean.getApproveOpinionInfos().size() > 0) {
            approval_pinion_lv.setVisibility(View.VISIBLE);
            ApproveOpinionAdapter opinionAdapter = new ApproveOpinionAdapter(this, mBean.getApproveOpinionInfos());
            View footView = LayoutInflater.from(this).inflate(R.layout.activity_billcommon_head, null);
            TextView titleNumber = footView.findViewById(R.id.base_billcommon_tv);
            titleNumber.setText("审核意见");
            approval_pinion_lv.addHeaderView(footView);
            approval_pinion_lv.setAdapter(opinionAdapter);
            opinionAdapter.notifyDataSetChanged();
        } else {
            approval_pinion_lv.setVisibility(View.GONE);
        }
'''
    picOnItemClickMuBan = '''
    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
        tempList.clear();
        onClickCamera(position, 0x2716, true);
    }
'''

    initDataHeadMuBan = '''
    @Override
    protected void initData() throws BizException {
        super.initData();

        txt_left_title.setVisibility(View.VISIBLE);
        top_tips.setText(Html.fromHtml("<font color='#888888'>带有</font><font color='#ff3030'>*</font><font color='#888888'>符号为必填项</font>"));
        Intent intent = getIntent();
        type = intent.getStringExtra("TYPE");
        mFid = intent.getStringExtra("FID");
        datacenter = intent.getStringExtra("DATACENTRE");
        String type_name = intent.getStringExtra("type_name");
        if (TextUtils.isEmpty(type_name)) {
            txt_main_title.setText("%s");
        } else {
            txt_main_title.setText(type_name);
        }
        mBean = new %sBean();
'''

    initDataPicMuBan = '''
        flag = -1;
        tempList = new ArrayList<>();
        tempData = new ArrayList<>();
        tempData.clear();
        initInfo();
        content_imge.setOnItemClickListener(this);
        content_imge.setAdapter(adapter);
        adapter.setmInterface(new AddImageAdapter.AddImageInterface() {
            @Override
            public void delAction(int position) {
                if (data.size() > 0) {
                    deletePicture(data.get(position));
                    data.remove(position);
                    adapter.notifyDataSetChanged();
                }
            }
        });
'''

    entryInitDataHeadMuBan = '''
        entryBeanList = new ArrayList<>();
        entryBeanList.add(new %sEntryBean());
        mAdapter = new %sEntryAdapter(this, entryBeanList, type);
        content_lv.setAdapter(mAdapter);
        mAdapter.setDataInterfaceCallBack(new %sEntryAdapter.DataInterfaceCallBack() {
            @Override
            public void delBean(int position) {
                if (entryBeanList.size() > 1) {
                    entryBeanList.remove(position);
                    mAdapter.notifyDataSetChanged();
                } else {
                    showToast("删除失败！至少保留一条明细条目");
                }
            }
'''

    initDataEndMuBan = '''
        formatData();
        if (!TextUtils.isEmpty(mFid)) {
            getData(mFid);
        }
    }
'''
    getDataMuBan = '''
    private void getData(String fid) {
        Map hashMap = new HashMap();
        hashMap.put("fID", fid);
        Map mapRoot = new HashMap();
        mapRoot.put(RootConstant.APP_REQUST_KEY, REQUEST_NETWORK_GET_INFO_DATA);
        mapRoot.put(RootConstant.APP_REQUST_URL, AppConstants.getUrl() + AppConstants.补齐链接);// todo 此处需要补齐链接
        mapRoot.put(RootConstant.APP_REQUST_CONTENT, hashMap);
        ViewInjector.networkRequest(this, this, mapRoot);
    }
'''
    getLayoutIdMuBan = '''
    @Override
    protected int getLayoutId() throws BizException {
        return R.layout.%s;
    }
    '''

    widgetOnClickHeadMuBan = '''
    @Override
    public void widgetOnClick(View v) throws BizException {
        super.widgetOnClick(v);
        switch (v.getId()) {
            case R.id.txt_left_title:
                mSwipeBackHelper.backward();
                break;
'''
    widgetOnClickXiajiMuBan = '''
            case R.id.%s:%s
                Intent %sIntent = new Intent();
                %sIntent.putExtra("PRIV_URL", AppConstants.替换链接);// todo 这里需要替换链接
                %sIntent.putExtra("PRIV_TITLE", "%s");
                %sIntent.setClass(this, SelectSearchInfoActivity.class);
                startActivityForResult(%sIntent, SELECTSEARCH_CHOOSE_%s);
                break;
'''
    widgetOnClickShowDateDialog = '''
            // todo 这里需要更改时间格式
            case R.id.%s:%s
                DateSelelctDialog %sDateDialog = new DateSelelctDialog();
                %sDateDialog.initCustomTimePicker(this, new boolean[]{true, true, true, false, false, false})
                %sDateDialog.setTimeSelectListener(new DateSelelctDialog.TimeSelectListener() {
                    @Override
                    public void onSelect(Date date, View v) {
                        try {
                            %s.setText(DateUtil.getDateYmd(date));
                            mBean.set%s(DateUtil.getDateYmd(date));
                        } catch (Exception e) {
                            LogUtil.sendException(e);
                        }
                    }
                });
                %sDateDialog.timeShowInfo();
                break;
'''
    widgetOnClickShowBottomDialog = '''
            // todo 这里需要补充枚举类型
            case R.id.%s:%s
                List<C2089a> %sEnumList = EasStateEnumUtils.getInstance().补充枚举类型();
                BottemDialog %scVar = new BottemDialog(this, %sEnumList, (View) null);
                %scVar.isTitleShow(false).show();
                %scVar.setOnOperItemClickL((adapterView, view, i, j) -> {
                    %s.setText(%sEnumList.get(i).f5192a);
                    mBean.set%s(%sEnumList.get(i).f5192a);
                    // todo 这里需要设置ID
                    mBean.set((String)%sEnumList.get(i).object);
                    %scVar.dismiss();
                });
                break;
'''
    widgetOnClickAddEntryMuBan = '''
            case R.id.tv_add:%s
                entryBeanList.add(new %sEntryBean());
                mAdapter.setData(entryBeanList);
                mAdapter.notifyDataSetChanged();
                break;
'''

    widgetOnClickDeleteMuBan = '''
            case R.id.tv_delete:
                HashMap deleteMap = new HashMap();
                if (TextUtils.isEmpty(mFid)) {
                    return;
                }
                deleteMap.put("fID", mFid);
                deleteMap.put("fDataCenter", datacenter);
                Map deleteRoot = new HashMap();
                deleteRoot.put(RootConstant.APP_REQUST_KEY, REQUEST_NETWORK_DELETE);
                deleteRoot.put(RootConstant.APP_REQUST_URL, AppConstants.getUrl() + AppConstants.替换链接);// todo 这里需要替换链接
                deleteRoot.put(RootConstant.APP_REQUST_CONTENT, deleteMap);
                ViewInjector.networkRequest(this, this, deleteRoot);
                break;    
'''
    widgetOnClickSavePicMuBan = '''
            case R.id.tv_save:
                HashMap saveMap = new HashMap();
                String saveTempData = getSubmitData();
                if (TextUtils.isEmpty(saveTempData)) {
                    return;
                }
                saveMap.put("jsonData", saveTempData);
                saveMap.put("fDataCenter", datacenter);
                saveMap.put(RootConstant.APP_JSON_APPID, getString(R.string.app_appid_));
                saveMap.put(RootConstant.APP_JSON_UKEY, SharePrefUtil.getString(this, AppConstants.CONFIG_SCAN_UKEY, ""));
//                if (data.size() == 0) {
//                    showToast("请上传图片");
//                }
                List<FileBean> saveFiles = new ArrayList<FileBean>();
                saveFiles.clear();
                for (String file : data) {
                    FileBean fileBean = new FileBean();
                    fileBean.setFUrlName(file);
                    saveFiles.add(fileBean);
                }
                flag = REQUEST_NETWORK_SAVE;// todo 这里需要替换链接
                universalRequestFile(AppConstants.getUrl() + AppConstants.替换链接, saveMap, saveFiles, RootConstant.BASE_NETWORK_UPLOAD, RootConstant.BASE_NETWORK_UPLOAD_POST);
                break;
'''
    widgetOnClickSaveMuBan = '''
            case R.id.tv_save:
                HashMap saveMap = new HashMap();
                String saveTempData = getSubmitData();
                if (TextUtils.isEmpty(saveTempData)) {
                    return;
                }
                saveMap.put("fDataCenter", fDataCenter);
                saveMap.put("jsonData", jsonData);
                saveMap.put(RootConstant.APP_JSON_APPID, getString(R.string.app_appid_));
                saveMap.put(RootConstant.APP_JSON_UKEY, SharePrefUtil.getString(this, AppConstants.CONFIG_SCAN_UKEY, ""));
                Map saveRoot = new HashMap();
                saveRoot.put(RootConstant.APP_REQUST_KEY, REQUEST_NETWORK_SAVE);
                saveRoot.put(RootConstant.APP_REQUST_URL, AppConstants.getUrl() + AppConstants.补齐链接);// todo 这里需要补齐链接
                saveRoot.put(RootConstant.APP_REQUST_CONTENT, saveMap);
                ViewInjector.networkRequest(this, this, saveRoot);
'''
    widgetOnClickSubmitPicMuBan = '''
            case R.id.tv_submit:
                HashMap submitMap = new HashMap();
                String submitTempData = getSubmitData();
                if (TextUtils.isEmpty(submitTempData)) {
                    return;
                }
                submitMap.put("jsonData", submitTempData);
                submitMap.put("fDataCenter", datacenter);
                submitMap.put(RootConstant.APP_JSON_APPID, getString(R.string.app_appid_));
                submitMap.put(RootConstant.APP_JSON_UKEY, SharePrefUtil.getString(this, AppConstants.CONFIG_SCAN_UKEY, ""));

//                if (data.size() == 0) {
//                    showToast("请上传图片");
//                }
                List<FileBean> submitFiles = new ArrayList<FileBean>();
                submitFiles.clear();
                for (String file : data) {
                    FileBean fileBean = new FileBean();
                    fileBean.setFUrlName(file);
                    submitFiles.add(fileBean);
                }
                flag = REQUEST_NETWORK_SUBMIT;// todo 这里需要替换链接
                universalRequestFile(AppConstants.getUrl() + AppConstants.替换链接, submitMap, submitFiles, RootConstant.BASE_NETWORK_UPLOAD, RootConstant.BASE_NETWORK_UPLOAD_POST);
                break;
'''
    widgetOnClickSubmitMuBan = '''
            case R.id.tv_submit:
                HashMap submitMap = new HashMap();
                String saveTempData = getSubmitData();
                if (TextUtils.isEmpty(saveTempData)) {
                    return;
                }
                submitMap.put("fDataCenter", fDataCenter);
                submitMap.put("jsonData", jsonData);
                submitMap.put(RootConstant.APP_JSON_APPID, getString(R.string.app_appid_));
                submitMap.put(RootConstant.APP_JSON_UKEY, SharePrefUtil.getString(this, AppConstants.CONFIG_SCAN_UKEY, ""));
                Map submitRoot = new HashMap();
                submitRoot.put(RootConstant.APP_REQUST_KEY, REQUEST_NETWORK_SUBMIT);
                submitRoot.put(RootConstant.APP_REQUST_URL, AppConstants.getUrl() + AppConstants.补齐链接);// todo 这里需要补齐链接
                submitRoot.put(RootConstant.APP_REQUST_CONTENT, submitMap);
                ViewInjector.networkRequest(this, this, submitRoot);
'''
    widgetOnClickEndMuBan = '''
            default:
                break;
        }
    }
'''
    getSubmitDataCheckXieData = '''
        if (TextUtils.isEmpty(%s.getText().toString().trim())) {
            showToast("请检查%s！");
            return "";
        }
        mBean.set%s(%s.getText().toString().trim());
'''
    getSubmitDataCheckDianData = '''
        if (TextUtils.isEmpty(mBean.get%s())) {
            showToast("请检查%s！");
            return "";
        }
'''

    getSubmitDataEndMuBan = '''
        return new Gson().toJson(mBean);
    }
'''
    onActivityResultHeadMuBan = '''
    @Override
    public void onActivityResult(int reqCode, int resultCode, Intent data1) {
        super.onActivityResult(reqCode, resultCode, data1);
        if (resultCode == Activity.RESULT_OK) {
'''
    onActivityResultItemMuBan = '''if (reqCode == SELECTSEARCH_CHOOSE_%s && data1 != null && data1.hasExtra("PRIV_FNAME")) {
                String fName2 = data1.getStringExtra("PRIV_FNAME");
                String fID2 = data1.getStringExtra("PRIV_FID");
                if (StringUtil.isNotEmpty(fName2) && StringUtil.isNotEmpty(fID2)) {
                    %s.setText(fName2);
                    mBean.set%s(fName2);
                    mBean.set(fID2);// todo 这里需要补齐ID
                }
            } 
'''

    # 分录点击事件
    entryXiajiMuBan = '''
            @Override
            public void choose%s(int position) {
                tempPosition = position;
                Map map = new HashMap();
                map.put("fDataCenter", datacenter);
                Intent intent = new Intent();
                intent.putExtra("PRIV_URL", AppConstants.补齐链接);//todo 这里需要补齐链接
                intent.putExtra("PRIV_TITLE", "%s");
                intent.putExtra("PRIV_FILTER", new Gson().toJson(map));
                intent.setClass(%sDetailsActivity.this, SelectSearchInfoActivity.class);
                startActivityForResult(intent, SELECTSEARCH_CHOOSE_%s);
            }
'''
    entryDialogMuBan = '''
            @Override
            public void choose%s(int position) {
                List<C2089a> listTemp = EasStateEnumUtils.getInstance().补充枚举类型();
                BottemDialog cVar = new BottemDialog(%sDetailsActivity.this, listTemp, (View) null);
                cVar.isTitleShow(false).show();
                cVar.setOnOperItemClickL(new C2091b() {
                    @Override
                    public void onOperItemClick(AdapterView<?> adapterView, View view, int i, long j) {
                        C2089a c2089abean = listTemp.get(i);
                        %sEntryBean entryBean = entryBeanList.get(position);
                        entryBean.set%s(String.valueOf(c2089abean.f5192a));
                        entryBean.set(String.valueOf(c2089abean.object));// todo 需要补齐ID
                        updateItem(position);
                        cVar.dismiss();
                    }
                });
            }
'''
    entryDateDialogMuBan = '''
            @Override
            public void choose%s(int position) {
                DateSelelctDialog dateDialog = new DateSelelctDialog();
                dateDialog.initCustomTimePicker(%sDetailsActivity.this, new boolean[]{true, true, true, false, false, false})
                dateDialog.setTimeSelectListener(new DateSelelctDialog.TimeSelectListener() {
                    @Override
                    public void onSelect(Date date, View v) {
                        try {
                            %sEntryBean entryBean = entryBeanList.get(position);
                            entryBean.set%s(DateUtil.getDateYmd(date));
                            updateItem(position);
                        } catch (Exception e) {
                            LogUtil.sendException(e);
                        }
                    }
                });
                dateDialog.timeShowInfo();
            }
'''

    entryCheckBeanContentMuBan = '''
            if (TextUtils.isEmpty(bean.get%s())) {
                showToast("请检查%s！");
                return "";
            }
'''

    entryOnActivityResultItemMuBan = '''if (reqCode == SELECTSEARCH_CHOOSE_%s && data1 != null && data1.hasExtra("PRIV_FNAME")) {
                String fName2 = data1.getStringExtra("PRIV_FNAME");
                String fID2 = data1.getStringExtra("PRIV_FID");
                if (StringUtil.isNotEmpty(fName2) && StringUtil.isNotEmpty(fID2)) {

                    %sEntryBean entryBean = entryBeanList.get(tempPosition);
                    entryBean.set%s(fName2);
                    entryBean.set(fID2);// todo 这里需要补齐id

                    updateItem(tempPosition);
                }
            }
'''
    updateItemMuBan = '''
    public void updateItem(int position) {
        /**第一个可见的位置**/
        int firstVisiblePosition = content_lv.getFirstVisiblePosition();
        /**最后一个可见的位置**/
        int lastVisiblePosition = content_lv.getLastVisiblePosition();

        /**在看见范围内才更新，不可见的滑动后自动会调用getView方法更新**/
        if (position >= firstVisiblePosition && position <= lastVisiblePosition) {
            /**获取指定位置view对象**/
            View view = content_lv.getChildAt(position - firstVisiblePosition);
            mAdapter.getView(position, view, content_lv);
        }
    }
'''
    picEndMuBan = '''
    @Override
    public void switchSourceMethod(int str) {
        C2089a c2089abean = list.get(str);
        if (String.valueOf(c2089abean.object).equals("1")) {
            EasyPhotos.createAlbum(this, false, GlideEngine.getInstance(), 9).start(0x2716);
        } else if (String.valueOf(c2089abean.object).equals("0")) {
            EasyPhotos.createCamera(this).start(0x2716);
        }
    }

    @Override
    protected void compressWithLs(List<String> photos) {
        tempList.clear();
        Luban.with(this)
                .load(photos)
                .ignoreBy(100)
                .setTargetDir(getPath(photos))
                .setCompressListener(new OnCompressListener() {
                    @Override
                    public void onSuccess(ArrayList<String> file) {
                        tempList.add(String.valueOf(file.get(0)));
                        data.addAll(file);
                        adapter.setImages(data);
                        adapter.notifyDataSetChanged();
                    }
                }).launch(this);
    }

    @Override
    protected void deletePicture(String str) {
        deleteAttachBeanInfo(str);
    }

    private void deleteAttachBeanInfo(String pathAll) {
        String tempFID = "";
        if (mBean != null && mBean.getAttachInfos() != null && mBean.getAttachInfos().size() > 0) {
            for (AttachInfoBean bean : mBean.getAttachInfos()) {
                if (bean.getFPathAll().equals(pathAll)) {
                    tempFID = bean.getFID();
                    break;
                }
            }
        }
        if (StringUtil.isNotEmpty(tempFID)) {
            Map<String, Object> map = new HashMap<>();
            Map mapRoot = new HashMap();
            map.put(RootConstant.APP_JSON_APPID, getString(R.string.app_appid_));
            map.put(RootConstant.APP_JSON_UKEY, SharePrefUtil.getString(this, AppConstants.CONFIG_SCAN_UKEY, ""));
            map.put("fAttachmentID", tempFID);
            mapRoot.put(RootConstant.APP_REQUST_KEY, 0x1001);
            mapRoot.put(RootConstant.APP_REQUST_ALERT, 2);
            mapRoot.put(RootConstant.APP_REQUST_URL, AppConstants.getUrl() + AppConstants.URL + AppConstants.COST_EASATTACHMENT_DELETE);
            mapRoot.put(RootConstant.APP_REQUST_CONTENT, map);
            ViewInjector.networkRequest(this, this, mapRoot);
        }
    }
'''

    def __init__(self, classNamePrefix: str, danName: str, beanList: [], entryBeanList: [], picture: bool,
                 examine: bool, ann: bool):
        global entryCheckBeanContentStrList, entryChooseItemStrList
        self.ann = ann
        self.fileName = '%sDetailsActivity' % classNamePrefix

        xmlBeanList = sorted(beanList, key=lambda item: item['detialNum'])

        selectChooseIntStrList = []

        bianliangKongjianStrList = []

        formatDataSetItemStrList = []

        formatDataChaKJStrList = []

        widgetOnClickItemStrList = []

        seletIntStart: int = 3000

        getSubmitDataGetStrList = []

        onActivityResultItemStrList = []

        for index, bean in enumerate(xmlBeanList):
            if bean['detialNum'] != '':
                beanNameTemp = bean['name'][0].upper() + bean['name'][1:]
                if bean['type'] == '可写':
                    idTemp = 'et_%s' % bean['name'].lower()
                    strTemp = self.bianliangKexieMuBan % (bean['name'].lower(), bean['name'].lower())
                    getSubmitDataGetStrList.append(
                        self.getSubmitDataCheckXieData % (idTemp, bean['showName'], beanNameTemp, idTemp)
                    )

                elif '可点' in bean['type']:
                    idTemp = 'tv_%s' % bean['name'].lower()
                    strTemp = self.bianliangKedianMuBan % (bean['name'].lower(), bean['name'].lower())
                    widgetOnClickItemStrList.append(self.returnWidgetOnClick(bean['type'], bean))
                    getSubmitDataGetStrList.append(
                        self.getSubmitDataCheckDianData % (beanNameTemp, bean['showName'])
                    )
                    if '下级选择' in bean['type']:
                        seletIntStart = seletIntStart + 1
                        selectChooseIntStrList.append(
                            self.selectIntMuBan % (bean['name'].upper(), seletIntStart))
                        onActivityResultItemStrList.append(
                            self.onActivityResultItemMuBan % (bean['name'].upper(), idTemp, beanNameTemp)
                        )

                elif '点写' in bean['type']:
                    idTemp = 'et_%s' % bean['name'].lower()
                    strTemp = self.bianliangDianxieMuBan % (
                        bean['name'].lower(), bean['name'].lower(), bean['name'].lower())
                    widgetOnClickItemStrList.append(self.returnWidgetOnClick(bean['type'], bean))
                    getSubmitDataGetStrList.append(
                        self.getSubmitDataCheckXieData % (idTemp, bean['showName'], beanNameTemp, idTemp)
                    )
                    if '下级选择' in bean['type']:
                        seletIntStart = seletIntStart + 1
                        selectChooseIntStrList.append(
                            self.selectIntMuBan % (bean['name'].upper(), seletIntStart))
                        onActivityResultItemStrList.append(
                            self.onActivityResultItemMuBan % (bean['name'].upper(), idTemp, beanNameTemp)
                        )

                else:
                    idTemp = 'tv_%s' % bean['name'].lower()
                    strTemp = self.bianliangJinzhanshiMuBan % (bean['name'].lower(), bean['name'].lower())

                if ann:
                    bianliangKongjianStrList.append('%s // %s\n' % (strTemp, bean['showName']))
                else:
                    bianliangKongjianStrList.append('%s\n' % strTemp)

                formatDataSetItemStrList.append(self.formatDataSetItemMuBan % (idTemp, beanNameTemp))

                formatDataChaKJStrList.append(
                    self.formatDataChaKJItemMuBan % (bean['name'].lower(), idTemp, idTemp, idTemp, idTemp)
                )

        entryBeanSortedList = sorted(entryBeanList, key=lambda item: item['listNum'])

        hasEntry = len(entryBeanSortedList) > 0

        if hasEntry:

            entryChooseItemStrList = []

            entryCheckBeanContentStrList = []

            seletIntStart2 = 4000

            for index, bean in enumerate(entryBeanSortedList):
                if bean['listNum'] != '':
                    beanNameTemp = bean['name'][0].upper() + bean['name'][1:]
                    if '可点' in bean['type'] or '点写' in bean['type']:
                        entryChooseItemStrList.append(self.returnEntryOnClick(classNamePrefix, bean))
                        if '下级选择' in bean['type']:
                            seletIntStart2 = seletIntStart2 + 1
                            selectChooseIntStrList.append(
                                self.selectIntMuBan % (bean['name'].upper(), seletIntStart2))
                            onActivityResultItemStrList.append(self.entryOnActivityResultItemMuBan % (
                                bean['name'].upper(),
                                classNamePrefix,
                                beanNameTemp
                            ))
                    entryCheckBeanContentStrList.append(
                        self.entryCheckBeanContentMuBan % (beanNameTemp, bean['showName'])
                    )

        # 开始组装数据
        # import数据
        self.contentStr = self.fileHeadMuBan
        # 文件名和继承
        if picture:
            self.contentStr += self.classHeadMuBan % (classNamePrefix, 'BaseDailyActivity')
        else:
            self.contentStr += self.classHeadMuBan % (classNamePrefix, 'CentreBaseActivity')
        # 接口返回需要的标识
        self.contentStr += self.requestIntMuBan

        for strTemp in selectChooseIntStrList:
            self.contentStr += strTemp
        # 获取topbar的id
        self.contentStr += self.bianliangTopBarMuBan

        # 获取组件id
        for strTemp in bianliangKongjianStrList:
            self.contentStr += strTemp

        if hasEntry:
            # 分录需要的控件id
            self.contentStr += self.entryKongIDMuBan % (' // 分录控件ID' if ann else '')

        if picture:
            # 附件需要的控件ID
            self.contentStr += self.picKongIDMuBan % (' // 附件需要的控件ID' if ann else '')

        if examine:
            # 审核审批需要的控件ID
            self.contentStr += self.examineKongIDMuBan % (' // 审核审批需要的控件ID' if ann else '')

        # 底部按钮的控件id
        self.contentStr += self.bianliangBottomButMuBan

        if picture:
            self.contentStr += self.bianliangTuPianMuBan % (' // 图片上传用的' if ann else '')
        self.contentStr += self.bianliangZhuShuJuMuBan % ((' // 详情主数据' if ann else ''), classNamePrefix)

        if hasEntry:
            self.contentStr += self.bianliangFenLuMuBan % (
                (' // 分录' if ann else ''), classNamePrefix, classNamePrefix
            )

        self.contentStr += self.handlerHeadMuBan
        self.contentStr += self.handlerSetBeanMuBan % classNamePrefix
        self.contentStr += self.handlerFootMuBan

        if picture:
            self.contentStr += self.picnetworkCorrectFileDataMuBan

        self.contentStr += self.formatDataHeadMuBan

        for strTemp in formatDataSetItemStrList:
            self.contentStr += strTemp

        if hasEntry:
            self.contentStr += '\n        entryBeanList = mBean.getEntryInfos();\n'

        self.contentStr += self.formatDataZhuangtaiMuBan

        for strTemp in formatDataChaKJStrList:
            self.contentStr += strTemp

        self.contentStr += '\n            ll_bottom.setVisibility(View.GONE);\n'

        if hasEntry:
            self.contentStr += self.formatDataEntry1MuBan
        self.contentStr += '\n        } else if (TextUtils.equals("approval", type)) { // todo 这里需要替换状态值\n'
        if hasEntry:
            self.contentStr += self.formatDataEntry2MuBan % classNamePrefix
        self.contentStr += self.formatDataShowEndMuBan

        if picture:
            self.contentStr += self.formatDataShowPicMuBan % (' // 图片上传用的' if ann else '')

        if examine:
            self.contentStr += self.formatDataShowExaMuBan % (' // 审核用的' if ann else '')

        self.contentStr += '\n    }'

        # 图片控件的点击事件
        if picture:
            self.contentStr += self.picOnItemClickMuBan

        # initData 方法
        self.contentStr += self.initDataHeadMuBan % (danName, classNamePrefix)

        if picture:
            self.contentStr += self.initDataPicMuBan

        if hasEntry:
            self.contentStr += self.entryInitDataHeadMuBan % (classNamePrefix, classNamePrefix, classNamePrefix)
            for strTemp in entryChooseItemStrList:
                self.contentStr += strTemp
            self.contentStr += '\n        });\n'
        self.contentStr += self.initDataEndMuBan

        # 获取数据getData方法
        self.contentStr += self.getDataMuBan

        # getLayoutId 方法
        detailsFileName = 'layout_details'
        words = StringTool.extract_words_starting_with_capital(classNamePrefix)
        for word in words:
            detailsFileName += '_' + word.lower()
        self.contentStr += self.getLayoutIdMuBan % detailsFileName

        # widgetOnClick 方法
        self.contentStr += self.widgetOnClickHeadMuBan
        for strTemp in widgetOnClickItemStrList:
            self.contentStr += strTemp

        self.contentStr += self.widgetOnClickAddEntryMuBan % ((' // 分录添加条目' if ann else ''), classNamePrefix)

        # 保存和提交按钮根据是否有图片附件上传而变动
        if picture:
            self.contentStr += self.widgetOnClickSavePicMuBan
        else:
            self.contentStr += self.widgetOnClickSaveMuBan
        if picture:
            self.contentStr += self.widgetOnClickSubmitPicMuBan
        else:
            self.contentStr += self.widgetOnClickSubmitMuBan
        self.contentStr += self.widgetOnClickEndMuBan

        self.contentStr += '\n    public String getSubmitData() {\n'
        for strTemp in getSubmitDataGetStrList:
            self.contentStr += strTemp

        if hasEntry:
            self.contentStr += '\n        for (EntertainEntryBean bean : entryBeanList) {\n'
            for strTemp in entryCheckBeanContentStrList:
                self.contentStr += strTemp
            self.contentStr += '\n        }\n        mBean.setEntertainRequestBillEntryInfos(entryBeanList);\n'

        self.contentStr += self.getSubmitDataEndMuBan

        # onActivityResult 方法
        self.contentStr += self.onActivityResultHeadMuBan
        for index, strTemp in enumerate(onActivityResultItemStrList):
            if index != 0:
                self.contentStr += '            else '
            else:
                self.contentStr += '            '
            self.contentStr += strTemp
        self.contentStr += '        }\n    }\n'

        if hasEntry:
            self.contentStr += self.updateItemMuBan

        if picture:
            self.contentStr += self.picEndMuBan
        self.contentStr += '\n}'

    def returnEntryOnClick(self, classNamePrefix: str, bean):
        beanNameTemp = bean['name'][0].upper() + bean['name'][1:]
        if '下级选择' in bean['type']:
            return self.entryXiajiMuBan % (
                bean['name'],
                bean['showName'],
                classNamePrefix,
                bean['name'].upper()
            )
        elif '弹窗选择' in bean['type']:
            return self.entryDialogMuBan % (
                bean['name'],
                classNamePrefix,
                classNamePrefix,
                beanNameTemp
            )
        else:
            return self.entryDateDialogMuBan % (
                bean['name'],
                classNamePrefix,
                classNamePrefix,
                beanNameTemp
            )

    def returnWidgetOnClick(self, flag, bean):
        idTemp = 'tv_%s' % bean['name'].lower()
        if '点写' in flag:
            idTemp = 'et_%s' % bean['name'].lower()
        if '下级选择' in flag:
            return self.widgetOnClickXiajiMuBan % (
                (idTemp if '可点' in flag else 'iv_%s' % bean['name'].lower()),
                ('// %s' % bean['showName'] if self.ann else ''),
                bean['name'].lower(),
                bean['name'].lower(),
                bean['name'].lower(),
                bean['showName'],
                bean['name'].lower(),
                bean['name'].lower(),
                bean['name'].upper()
            )
        elif '弹窗选择' in flag:
            return self.widgetOnClickShowBottomDialog % (
                (idTemp if '可点' in flag else 'iv_%s' % bean['name'].lower()),
                ('// %s' % bean['showName'] if self.ann else ''),
                bean['name'],
                bean['name'],
                bean['name'],
                bean['name'],
                bean['name'],
                idTemp,
                bean['name'],
                bean['name'][0].upper() + bean['name'][1:],
                bean['name'],
                bean['name'],
                bean['name']
            )
        else:
            return self.widgetOnClickShowDateDialog % (
                (idTemp if '可点' in flag else 'iv_%s' % bean['name'].lower()),
                ('// %s' % bean['showName'] if self.ann else ''),
                bean['name'].lower(),
                bean['name'].lower(),
                bean['name'].lower(),
                idTemp,
                bean['name'][0].upper() + bean['name'][1:],
                bean['name'].lower(),
            )
