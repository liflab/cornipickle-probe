from django.core.urlresolvers import reverse
from menu import Menu, MenuItem
from django.utils.translation import gettext as _

# Adding items to our main menu

Menu.add_item(
    "main",MenuItem(
        _("Dashboard"),
    reverse("probe_project.apps.dashboards.views.datum"),
    weight=10)
)

Menu.add_item(
    "main", MenuItem(
        _("Probes"),
        reverse("probe_project.apps.probe_dispatcher.views.probes"),
        weight=20
    )
)

Menu.add_item(
    "main", MenuItem(
        _("Sensors"),
        reverse("probe_project.apps.probe_dispatcher.views.sensors"),
        weight=30
    )
)


Menu.add_item(
    "main", MenuItem(
        _("Administration"),
        reverse("admin:index"),
        weight=80,
        separator=True,
        check=lambda request: request.user.is_superuser
    )
)