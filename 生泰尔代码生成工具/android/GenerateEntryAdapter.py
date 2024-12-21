from 生泰尔代码生成工具 import StringTool
from 生泰尔代码生成工具.android.BaseGenerate import BaseGenerate


class GenerateEntryAdapter(BaseGenerate):
    importMuban = '''package com.centre.workoffice.adapter;

import android.content.Context;
import android.text.Editable;
import android.text.TextUtils;
import android.text.TextWatcher;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;

import com.monkeyk.klutils.adapter.BasisBaseAdapter;
import com.monkeyk.klutils.adapter.BasisBaseViewHolder;

import java.util.List;

'''
    classHeadMuban = '''
public class %sDetailsEntryAdapter extends BasisBaseAdapter<%sEntryBean, %sDetailsEntryAdapter.ViewHolder> {

    private String type;

    public %sDetailsEntryAdapter(Context context, List<%sEntryBean> list, String type) {
        super(context, list);
        this.type = type;
    }

    @Override
    protected ViewHolder ViewHolder(int t) {
        return new ViewHolder();
    }'''

    initItemDataHeadMuban = '''
    @Override
    protected void initItemData(int position, ViewHolder holder, View root) {
        %sEntryBean bean = mList.get(position);
        if (bean != null) {
            hideView(holder);
    '''
    initItemDataFootMuban = '''
            holder.iv_delete.setOnClickListener(v -> {
                if (this.mDataCallBack != null) {
                    mDataCallBack.delBean(position);
                }
            });
        }
    }'''

    # 写模板
    xieRemoveTextWatcherMuBan = '''
            if (holder.%s.getTag() instanceof TextWatcher) {
                holder.%s.removeTextChangedListener((TextWatcher) holder.%s.getTag());
            }
'''

    # 设置内容模板需要根据类型传入是否textview还是edittext
    setTextMuban = '            holder.%s.setText(bean.get%s());'

    # 可写
    xieTextWatcherMuBan = '''
            TextWatcher %sTextWatcher = new TextWatcher() {
                @Override
                public void beforeTextChanged(CharSequence s, int start, int count, int after) {
                }
            
                @Override
                public void onTextChanged(CharSequence s, int start, int before, int count) {
                }
            
                @Override
                public void afterTextChanged(Editable s) {
                    if (TextUtils.isEmpty(s)) {
                        bean.set%s("");
                    } else {
                        bean.set%s(s.toString());
                    }
                }
            };
    '''
    # 点写
    dianxieTextWatcherMuBan = '''
            TextWatcher %sTextWatcher = new TextWatcher() {
               @Override
               public void beforeTextChanged(CharSequence s, int start, int count, int after) {
               }
            
               @Override
               public void onTextChanged(CharSequence s, int start, int before, int count) {
               }
            
               @Override
               public void afterTextChanged(Editable s) {
                   if (TextUtils.isEmpty(s)) {
                       bean.set%s("");
                   } else {
                       if (!TextUtils.equals(bean.get%s(), s.toString().trim())) {
                        bean.set%s(s.toString().trim());
                        // todo 这里需要补齐ID
                        bean.setID("");
                    }
                   }
               }
            };
'''

    addTextChangedListenerMuBan = '            holder.%s.addTextChangedListener(%sTextWatcher);'
    setTagMuBan = '\n            holder.%s.setTag(%sTextWatcher);'

    # 点击的模板
    setOnClickListenerMuBan = '''
            holder.%s.setOnClickListener(v -> {
                if (this.mDataCallBack != null) {
                    mDataCallBack.choose%s(position);
                }
            });
'''

    # 查看详情全部只需要展示
    hideViewHeadMuBan = '''
    private void hideView(ViewHolder holder) {
        // TODO: 这里需要补齐页面类型：%s
        if (TextUtils.equals("", type)) {

    '''
    hideViewItemMuBan = '''
            holder.tv_%s_red.setVisibility(View.INVISIBLE);
            holder.%s.setBackgroundResource(R.drawable.rounded_text);
            holder.%s.setFocusable(false);
            holder.%s.setClickable(false);
            holder.%s.setFocusableInTouchMode(false);
'''
    hideViewFootMuBan = '''
            holder.rl_bottom.setVisibility(View.GONE);
        }
    }
    '''

    callBackHeadMuBan = '''
    private DataInterfaceCallBack mDataCallBack;

    public void setDataInterfaceCallBack(DataInterfaceCallBack dataCallBack) {
        this.mDataCallBack = dataCallBack;
    }

    public interface DataInterfaceCallBack {
        void delBean(int position);
    '''

    callBackItemMuBan = '        void choose%s(int position);\n\n'

    callBackFootMuBan = '''
    }

    public void notifyDataSetChanged(List<EntertainEntryBean> list) {
        this.mList = list;
        notifyDataSetChanged();
    }
    '''
    viewHolderHeadMuBan = '\n    static class ViewHolder extends BasisBaseViewHolder {\n'

    viewHolderBianLiantMuBan = '''
        TextView tv_%s_red;
        %s %s;
'''
    viewHolderLayoutMuBan = '''
        RelativeLayout rl_bottom;
        ImageView iv_delete;

        @Override
        public int getItemLayout() {
            return R.layout.%s;
        }
    '''
    viewHolderFindViewHeadMuBan = '''
        @Override
        public void initItemView() {
    '''
    viewHolderFindViewItemMuBan = '''
            tv_%s_red = findViewById(R.id.tv_%s_red);
            %s = findViewById(R.id.%s);
'''
    classEndMuban = '''
        }
    }
}'''

    def __init__(self, classNamePrefix: str, entryBeanList: [], annotation=False):
        self.fileName = '%sEntryAdapter' % classNamePrefix
        xmlFileName = 'item_entry'
        words = StringTool.extract_words_starting_with_capital(classNamePrefix)
        for word in words:
            xmlFileName += '_' + word.lower()

        classHeadStr = self.classHeadMuban % (
            classNamePrefix,
            classNamePrefix,
            classNamePrefix,
            classNamePrefix,
            classNamePrefix)

        initItemDataHeadStr = self.initItemDataHeadMuban % classNamePrefix

        beanList = sorted(entryBeanList, key=lambda item: item['listNum'])

        removeTextChangeStrList = []
        setTextStrList = []
        newTextWatcherStrList = []
        addTextWatcherStrList = []
        setTagStrList = []

        clickStrList = []
        hideViewItemStrList = []
        callbackItemStrList = []
        viewHolderBianLiangStrList = []
        viewHolderFindViewStrList = []
        for bean in beanList:
            if bean['listNum'] != '':
                compName = 'TextView'
                idTemp = 'tv_%s' % bean['name'].lower()
                beanName = bean['name'][0].upper() + bean['name'][1:]
                if bean['type'] == '可写':
                    idTemp = 'et_%s' % bean['name'].lower()
                    removeTextChangeStrList.append(self.xieRemoveTextWatcherMuBan % (
                        idTemp,
                        idTemp,
                        idTemp
                    ))

                    newTextWatcherStrList.append(self.xieTextWatcherMuBan % (bean['name'], beanName, beanName))

                    addTextWatcherStrList.append(
                        self.addTextChangedListenerMuBan % (idTemp, bean['name']))

                    setTagStrList.append(self.setTagMuBan % (idTemp, bean['name']))

                    hideViewItemStrList.append(
                        self.hideViewItemMuBan % (bean['name'].lower(), idTemp, idTemp, idTemp, idTemp)
                    )

                    compName = 'EditText'

                elif '可点' in bean['type']:
                    idTemp = 'tv_%s' % bean['name'].lower()

                    clickStrList.append(self.setOnClickListenerMuBan % (idTemp, bean['name']))

                    hideViewItemStrList.append(
                        self.hideViewItemMuBan % (bean['name'].lower(), idTemp, idTemp, idTemp, idTemp)
                    )

                    callbackItemStrList.append(self.callBackItemMuBan % bean['name'])

                    compName = 'TextView'

                elif '点写' in bean['type']:
                    idTemp = 'et_%s' % bean['name'].lower()
                    removeTextChangeStrList.append(self.xieRemoveTextWatcherMuBan % (
                        idTemp,
                        idTemp,
                        idTemp
                    ))

                    newTextWatcherStrList.append(
                        self.dianxieTextWatcherMuBan % (bean['name'], beanName, beanName, beanName))

                    addTextWatcherStrList.append(
                        self.addTextChangedListenerMuBan % (idTemp, bean['name']))

                    setTagStrList.append(self.setTagMuBan % (idTemp, bean['name']))

                    ivIdTemp = 'iv_%s' % bean['name'].lower()
                    clickStrList.append(self.setOnClickListenerMuBan % (ivIdTemp, bean['name']))

                    hideViewItemStrList.append(
                        self.hideViewItemMuBan % (bean['name'].lower(), idTemp, idTemp, idTemp, idTemp)
                    )

                    hideViewItemStrList.append(
                        '            holder.iv_%s.setVisibility(View.GONE);\n' % bean['name'].lower())

                    callbackItemStrList.append(self.callBackItemMuBan % bean['name'])

                    viewHolderBianLiangStrList.append('        ImageView %s;\n' % ivIdTemp)

                    viewHolderFindViewStrList.append(
                        '            %s = findViewById(R.id.%s);\n' % (ivIdTemp, ivIdTemp)
                    )

                    compName = 'EditText'

                else:
                    idTemp = 'tv_%s' % bean['name'].lower()

                setTextStr = self.setTextMuban % (idTemp, beanName)
                if annotation:
                    setTextStr += '// %s\n' % bean['showName']
                else:
                    setTextStr += '\n'
                setTextStrList.append(setTextStr)

                viewHolderBianLiangStrList.append(
                    self.viewHolderBianLiantMuBan % (bean['name'].lower(), compName, idTemp))

                viewHolderFindViewStrList.append(
                    self.viewHolderFindViewItemMuBan % (bean['name'].lower(), bean['name'].lower(), idTemp, idTemp)
                )

        self.contentStr = self.importMuban
        self.contentStr += classHeadStr
        self.contentStr += initItemDataHeadStr
        for strTemp in removeTextChangeStrList: self.contentStr += strTemp
        for strTemp in setTextStrList: self.contentStr += strTemp
        for strTemp in newTextWatcherStrList: self.contentStr += strTemp
        for strTemp in setTagStrList: self.contentStr += strTemp
        for strTemp in clickStrList: self.contentStr += strTemp
        self.contentStr += self.initItemDataFootMuban
        self.contentStr += self.hideViewHeadMuBan
        for strTemp in hideViewItemStrList: self.contentStr += strTemp
        self.contentStr += self.hideViewFootMuBan
        self.contentStr += self.callBackHeadMuBan
        for strTemp in callbackItemStrList: self.contentStr += strTemp
        self.contentStr += self.callBackFootMuBan
        self.contentStr += self.viewHolderHeadMuBan
        for strTemp in viewHolderBianLiangStrList: self.contentStr += strTemp
        self.contentStr += self.viewHolderLayoutMuBan % xmlFileName
        self.contentStr += self.viewHolderFindViewHeadMuBan
        for strTemp in viewHolderFindViewStrList: self.contentStr += strTemp
        self.contentStr += self.classEndMuban
