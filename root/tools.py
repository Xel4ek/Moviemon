from django.shortcuts import render
from django.template.loader import render_to_string

from .models import Supplier

'''
actions = {up?:<url>, down?:<url>, left?:<url>, right?:<url>, 
            start?:<url>, select?: <url>,
            a?: <url>, b?: <url>}
url = {url:route_name, par?: <any>, title?: <string>, query? <dict>}
'''


class Render:
    def __init__(self, request, route='index', context=None, actions=None,):
        self.request = request
        self.route = route
        self.actions = actions if actions else {}
        self.context = context if context else {}

    def add_context(self, context: dict):
        self.context = {*self.context, *context}

    def add_actions(self, added: dict):
        self.actions = {*self.actions, *added}

    def render(self):
        Supplier.dump()
        return render(self.request, 'root/' + self.route + '.html',
                      {'controls': render_to_string('root/controls.html', self.actions), **self.context})
