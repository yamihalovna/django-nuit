from django.shortcuts import render
from django.views.generic import ListView

class PaginatedListView(ListView):
    object_link = True

    def get_context_data(self, **kwargs):
        context = super(PaginatedListView, self).get_context_data(**kwargs)
        context['object_link'] = self.object_link
        return context











#===================================================

def home(request):

    template_name = request.GET.get('template', 'bothmenu-topbar')

    return render(request, 'nuit/mytemplate.html', {'template_name': 'nuit/%s.html' % template_name, 'template_short_name': template_name})

def app_menu(request):
    return (
        {
            'id': 'empty',
            'name': 'Empty',
            'link': '?template=empty',
        },
        {
            'id': 'topbar',
            'name': 'Top Bar',
            'link': '?template=topbar',
        },
        {
            'id': 'leftmenu',
            'name': 'Left Menu',
            'link': '?template=leftmenu',
        },
        {
            'id': 'rightmenu',
            'name': 'Right Menu',
            'link': '?template=rightmenu',
        },
        {
            'id': 'bothmenu',
            'name': 'Both Menus',
            'link': '?template=bothmenu',
        },
        {
            'id': 'leftmenu-topbar',
            'name': 'Left Menu & Top Bar',
            'link': '?template=leftmenu-topbar',
        },
        {
            'id': 'rightmenu-topbar',
            'name': 'Right Menu & Top Bar',
            'link': '?template=rightmenu-topbar',
        },
        {
            'id': 'bothmenu-topbar',
            'name': 'Both Menus & Top Bar',
            'link': '?template=bothmenu-topbar',
        },
    )
