import platform
from suit_dashboard.box import Item, Box

from cmdb.models import SHost
from cmdb.models import Host

# upMinionCount = Host.objects.filter(minion_status=1).count()
# downMinionCount = Host.objects.filter(minion_status=0).count()

def machine_usage_chart():

    # idc_109 = IDC.objects.filter(name='109').values('id')[0]['id']  # 109机房
    # idc_111 = IDC.objects.filter(name='111').values('id')[0]['id']  # 111机房
    SHost_109 = SHost.objects.filter(idc__name=109).count()
    SHost_111 = SHost.objects.filter(idc__name=111).count()
    vHost_109 = Host.objects.filter(idc__name=109, virtual='VMware').count()
    vHost_111 = Host.objects.filter(idc__name=111, virtual='VMware').count()
    pHost_109 = Host.objects.filter(idc__name=109, virtual='physical').count()
    pHost_111 = Host.objects.filter(idc__name=111, virtual='physical').count()
    pHost_210 = Host.objects.filter(idc__name=210, virtual='physical').count()

    chart_options = {
        'chart': {
            'type': 'column',
            'height': 350,
        },
        'title': {
            'text': '主机分布'
        },
        'xAxis': {
            'categories': ['109机房', '111机房', '210机房']
        },
        'plotOptions': {
            'column': {
                'pointPadding': 0.2,
                'borderWidth': 0,
            }
        },
        'series': [
            {
                'name': '宿主机',
                'data': [SHost_109, SHost_111]

            },
            {
                'name': '虚拟机',
                'data': [vHost_109, vHost_111],
            },
            {
                'name': '物理机',
                'data': [pHost_109, pHost_111, pHost_210]
            }
        ],
    }
    return chart_options


def minion_status_chart():

    upMinionCount = Host.objects.filter(minion_status=1).count()
    downMinionCount = Host.objects.filter(minion_status=0).count()

    chart_options = {
        'chart': {
            'type': 'pie',
            'height': 243,
        },
        'title': {
            'text': '客户端运行状态'
        },
        'tooltip': {
            'percentageDecimals': 1
        },
        'legend': {
            'enabled': False
        },
        'plotOptions': {
            'pie': {
                'colors': ['red', 'green'],
                'allowPointSelect': True,
                'cursor': 'pointer',
                'dataLabels': {
                    'enabled': True,
                    'format': '<b>{point.name}%</b>: {point.percentage:.1f} %',
                },
                'showInLegend': True
            }
        },
        'series': [{
            'name': 'minion_status',
            'data': [
                ['DOWN',    downMinionCount],
                ['UP',  upMinionCount],
            ]
        }]
    }
    return chart_options


class BoxMachineBasicInfo(Box):
    def get_items(self):
        upMinionCount = Host.objects.filter(minion_status=1).count()
        downMinionCount = Host.objects.filter(minion_status=0).count()

        # 系统基础信息
        item_info = Item(
            html_id='SysInfo', name='主机系统信息',
            display=Item.AS_TABLE,
            value=(
                ('主机名', platform.node()),
                ('系统', '%s, %s, %s' % (
                   platform.system(),
                   ' '.join(platform.linux_distribution()),
                   platform.release())),
                ('架构', ' '.join(platform.architecture())),
                ('处理器', platform.processor()),
                ('Python版本', platform.python_version()),
                ('接入宿主机数量', SHost.objects.count()),
                ('接入主机数量', Host.objects.count()),
                ('客户端运行情况', '运行中 %s,未运行 %s' % (upMinionCount, downMinionCount)),
            ),
            classes='table-bordered table-condensed '
                    'table-hover table-striped'
        )

        return [item_info]


class BoxMachineBasicInfoChart(Box):
    def get_items(self):
        item_chart = Item(
            html_id='machine-usage',
            name='主机分布情况',
            value=machine_usage_chart(),
            display=Item.AS_HIGHCHARTS)

        return [item_chart]


class BoxMinionStatusChart(Box):
    def get_items(self):
        item_chart = Item(
            html_id='minion-usage',
            name='客户端运行情况',
            value=minion_status_chart(),
            display=Item.AS_HIGHCHARTS)

        return [item_chart]
