from 生泰尔代码生成工具.android.BaseGenerate import BaseGenerate


class GenerateFragmentAdapter(BaseGenerate):
    # 模板
    createClassStartMuBan = '''public class %sAdapter extends BasisBaseAdapter<%sBean, %sAdapter.ViewHolder> {

    public %sAdapter(Context context, List<%sBean> list) {
        super(context, list);
    }

    @Override
    protected ViewHolder ViewHolder(int t) {
        return new ViewHolder();
    }

    @Override
    protected void initItemData(int position, ViewHolder holder, View root) {
        %sBean bean = mList.get(position);
        if (bean != null) {\n'''

    initItemDataMuBan = '            holder.tv_%s.setText(bean.get%s());\n'
    initItemDataAnnotationMuBan = '            holder.tv_%s.setText(bean.get%s());// %s\n'
    initItemDataStateMuBan = '            EasStateEnumUtils.getInstance().controlDetectionManageStateTextView(mContext, holder.tv_tips, holder.tv_%s, bean.get%s());\n'

    initDataEndMuBan = '''       }
    }

    class ViewHodler extends BasisBaseViewHolder {
'''
    viewHolderBianMuBan = '        TextView tv_%s;\n'
    viewHolderBianAnnotationMuBan = '        TextView tv_%s;// %s\n'

    layoutImportMuBan = '''
        @Override
        public int getItemLayout() {
            return R.layout.%s;
        }
        '''
    initItemViewHeadMuBan = '''
        @Override
        public void initItemView() {\n'''
    initItemViewItemMuBan = '            tv_%s = findViewById(R.id.tv_%s);\n'
    initItemViewFootMuBan = '''        }
    }
}'''

    def __init__(self, classNamePrefix: str, beanList: [], xmlFileName: str, annotation: bool = False):
        self.fileName = '%sAdapter' % classNamePrefix
        self.importStrList = [
            'package com.centre.workoffice.adapter;\n\n',
            'import android.content.Context;\n',
            'import android.view.View;\n',
            'import android.widget.TextView;\n\n'
            'import com.centre.workoffice.base.EasStateEnumUtils;\n'
            'import com.monkeyk.klutils.adapter.BasisBaseAdapter;\n'
            'import com.monkeyk.klutils.adapter.BasisBaseViewHolder;\n\n'
            'import java.util.List;\n\n'
        ]

        fileHeadStr = self.createClassStartMuBan % (
            classNamePrefix,
            classNamePrefix,
            classNamePrefix,
            classNamePrefix,
            classNamePrefix,
            classNamePrefix)

        adapterBeanList = sorted(beanList, key=lambda item: item['listNum'])

        hasState = False
        initDataStrList = []
        for bean in adapterBeanList:
            if bean['listNum'] != '':
                leftId = bean['name'].lower()
                getName = bean['name'][0].upper() + bean['name'][1:]
                if bean['type'] == '单据状态':
                    hasState = True
                    initDataStrList.append(self.initItemDataStateMuBan % (leftId, getName))
                else:
                    if annotation:
                        initDataStrList.append(self.initItemDataAnnotationMuBan % (leftId, getName, bean['showName']))
                    else:
                        initDataStrList.append(self.initItemDataMuBan % (leftId, getName))

        viewHolderBianStrList = []
        for bean in adapterBeanList:
            if bean['listNum'] != '':
                leftId = bean['name'].lower()
                if annotation:
                    viewHolderBianStrList.append(self.viewHolderBianAnnotationMuBan % (leftId, bean['showName']))
                else:
                    viewHolderBianStrList.append(self.viewHolderBianMuBan % leftId)

        if hasState:
            viewHolderBianStrList.append('        TextView tv_tips;\n')  # 需要多一个状态颜色改变的

        layoutImportStr = self.layoutImportMuBan % xmlFileName

        initItemViewStrList = []
        initItemViewStrList.append(self.initItemViewHeadMuBan)
        for bean in adapterBeanList:
            if bean['listNum'] != '':
                leftId = bean['name'].lower()
                initItemViewStrList.append(self.initItemViewItemMuBan % (leftId, leftId))

        if hasState:
            initItemViewStrList.append('            tv_tips = findViewById(R.id.tv_tips);\n')

        initItemViewStrList.append(self.initItemViewFootMuBan)

        # 组合字符串
        self.contentStr = ''
        for strTemp in self.importStrList:
            self.contentStr += strTemp

        self.contentStr += fileHeadStr

        for strTemp in initDataStrList:
            self.contentStr += strTemp

        self.contentStr += self.initDataEndMuBan

        for strTemp in viewHolderBianStrList:
            self.contentStr += strTemp

        self.contentStr += layoutImportStr

        for strTemp in initItemViewStrList:
            self.contentStr += strTemp
