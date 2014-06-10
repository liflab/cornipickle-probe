from django.core.urlresolvers import reverse
from menu import Menu, MenuItem
from django.utils.translation import gettext as _

# Add two items to our main menu
Menu.add_item(
    "main", MenuItem(
        _("Probes"),
        reverse("probe_project.apps.probe_dispatcher.views.probes"),
        weight=10
    )
)

Menu.add_item(
    "main", MenuItem(
        _("Sensors"),
        reverse("probe_project.apps.probe_dispatcher.views.sensors"),
        weight=20
    )
)