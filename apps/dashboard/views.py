# Create your views here.
from django.utils.translation import ugettext_lazy as _
from suit_dashboard.layout import Grid, Row, Column
from suit_dashboard.views import DashboardView

from dashboard.boxes import BoxMachineBasicInfo, BoxMachineBasicInfoChart, BoxMinionStatusChart


class HomeView(DashboardView):
    template_name = 'main.html'
    crumbs = (
        {'url': 'admin:index', 'name': _('Home')},
    )
    grid = Grid(
        Row(
            Column(BoxMachineBasicInfo(), width=6),
            Column(BoxMinionStatusChart(), width=6),
            Column(BoxMachineBasicInfoChart(), width=12),
        )
    )