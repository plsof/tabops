from .BaseArchitecture import BaseArchitecture


class wtv(BaseArchitecture):

    class Meta:
        verbose_name = "电视看点"
        verbose_name_plural = verbose_name


class bimsboot(BaseArchitecture):

    class Meta:
        verbose_name = "终端管理"
        verbose_name_plural = verbose_name


class bimspanel(BaseArchitecture):

    class Meta:
        verbose_name = "桌面管理"
        verbose_name_plural = verbose_name


class epg(BaseArchitecture):

    class Meta:
        verbose_name = "播控点播"
        verbose_name_plural = verbose_name


class tms(BaseArchitecture):

    class Meta:
        verbose_name = "播控认证"
        verbose_name_plural = verbose_name


class tptopic(BaseArchitecture):

    class Meta:
        verbose_name = "播控专题"
        verbose_name_plural = verbose_name


class pic(BaseArchitecture):

    class Meta:
        verbose_name = "图片"
        verbose_name_plural = verbose_name


class ppl(BaseArchitecture):

    class Meta:
        verbose_name = "看单"
        verbose_name_plural = verbose_name


class mscreen(BaseArchitecture):

    class Meta:
        verbose_name = "多屏"
        verbose_name_plural = verbose_name


class xmpp(BaseArchitecture):

    class Meta:
        verbose_name = "消息系统"
        verbose_name_plural = verbose_name


class uic(BaseArchitecture):

    class Meta:
        verbose_name = "用户中心"
        verbose_name_plural = verbose_name


class cossearch(BaseArchitecture):

    class Meta:
        verbose_name = "融合搜索"
        verbose_name_plural = verbose_name


class dms2(BaseArchitecture):

    class Meta:
        verbose_name = "DMS2.0"
        verbose_name_plural = verbose_name


class cosepg(BaseArchitecture):

    class Meta:
        verbose_name = "融合EPG"
        verbose_name_plural = verbose_name


class nginx(BaseArchitecture):

    class Meta:
        verbose_name = "Nginx"
        verbose_name_plural = verbose_name


class bigdata(BaseArchitecture):

    class Meta:
        verbose_name = '大数据'
        verbose_name_plural = '大数据'


class product(BaseArchitecture):

    class Meta:
        verbose_name = '产品管理'
        verbose_name_plural = '产品管理'


class unionpay(BaseArchitecture):

    class Meta:
        verbose_name = '统一支付'
        verbose_name_plural = '统一支付'


class lbss(BaseArchitecture):

    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = '用户管理'


class exchange(BaseArchitecture):

    class Meta:
        verbose_name = '自动兑换'
        verbose_name_plural = '自动兑换'


class mppl(BaseArchitecture):

    class Meta:
        verbose_name = '手机看单'
        verbose_name_plural = '手机看单'


class mcossearch(BaseArchitecture):

    class Meta:
        verbose_name = '手机融合搜索'
        verbose_name_plural = '手机融合搜索'


class mcosepg(BaseArchitecture):

    class Meta:
        verbose_name = '手机融合EPG'
        verbose_name_plural = '手机融合EPG'


class sms(BaseArchitecture):

    class Meta:
        verbose_name = 'SMS'
        verbose_name_plural = 'SMS'


class dangj(BaseArchitecture):

    class Meta:
        verbose_name = '党建平台'
        verbose_name_plural = '党建平台'


class ub(BaseArchitecture):

    class Meta:
        verbose_name = '行为系统'
        verbose_name_plural = '行为系统'


class injection(BaseArchitecture):

    class Meta:
        verbose_name = '注入系统'
        verbose_name_plural = '注入系统'


class ad(BaseArchitecture):

    class Meta:
        verbose_name = '广告系统'
        verbose_name_plural = '广告系统'


class ndms(BaseArchitecture):

    class Meta:
        verbose_name = 'NDMS'
        verbose_name_plural = 'NDMS'
