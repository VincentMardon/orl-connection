from rest_framework.renderers import BrowsableAPIRenderer

class BrowsableAPIRendererWithoutForms(BrowsableAPIRenderer):
    """
    Renders the browsable api, but excludes the forms.
    """
    def get_context(self, *args, **kwargs):
        context = super().get_context(*args, **kwargs)
        context['display_edit_forms'] = False
        
        return context