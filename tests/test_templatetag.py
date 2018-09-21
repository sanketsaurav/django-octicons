#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.template import Template, Context


def test_octicon_rendered():
    tpl = Template(
        """
        {% load octicons %}
        {% octicon 'x' class='disabled' %}
        """
    )
    rendered_tpl = tpl.render(Context({}))

    assert 'class="octicon octicon-x disabled"' in rendered_tpl
    assert 'viewBox="0 0 12 16"' in rendered_tpl
