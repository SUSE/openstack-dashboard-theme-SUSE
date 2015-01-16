import horizon


class Theme(horizon.Dashboard):
    name = "suse_theme"
    slug = "suse_theme"
    panels = ('theme_index', )
    default_panel = 'theme_index'
    nav = False

horizon.register(Theme)
