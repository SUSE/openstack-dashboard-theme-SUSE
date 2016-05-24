from django.core.urlresolvers import reverse_lazy

# The name of the dashboard to be added to HORIZON['dashboards']. Required.
DASHBOARD = 'help'
# If set to True, this dashboard will be set as the default dashboard.
DEFAULT = False
# A dictionary of exception classes to be added to HORIZON['exceptions'].
ADD_EXCEPTIONS = {}
# A list of applications to be added to INSTALLED_APPS.
ADD_INSTALLED_APPS = ['openstack_dashboard.dashboards.help']

UPDATE_HORIZON_CONFIG = {
    'help_url': reverse_lazy('horizon:help:guides:index'),
}
