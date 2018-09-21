#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from octicons.templatetags.octicons import Octicon


def test_failure_when_octicon_not_exist():
    with pytest.raises(ValueError) as exc:
        Octicon('some-dummy-icon')

    assert str(exc.value) == "Couldn't find octicon symbol for some-dummy-icon"


def test_initialization():
    icon = Octicon('x')
    assert icon


def test_keywords_for_icon():
    icon = Octicon('x')
    assert icon.keywords == ['remove', 'close', 'delete']


def test_attributes_are_readable():
    icon = Octicon('x')
    assert icon.path
    assert icon.options
    assert icon.symbol == 'x'
    assert icon.width == 12
    assert icon.height == 16


def test_viewbox():
    icon = Octicon('x')
    assert 'viewBox="0 0 12 16"' in icon.to_svg


def test_includes_other_html_attributes():
    icon = Octicon('x', foo='bar', disabled='true')
    assert 'disabled="true"' in icon.to_svg
    assert 'foo="bar"' in icon.to_svg


def test_includes_classess_passed_in():
    icon = Octicon('x', **{'class': 'text-closed'})
    assert 'class="octicon octicon-x text-closed"' in icon.to_svg


def test_size_always_has_width_and_height():
    icon = Octicon('x')
    assert 'height="16"' in icon.to_svg
    assert 'width="12"' in icon.to_svg


def test_size_converts_number_height_to_integer():
    icon = Octicon('x', height=60)
    assert 'height="60"' in icon.to_svg
    assert 'width="45"' in icon.to_svg


def test_size_converts_number_width_to_integer():
    icon = Octicon('x', width=45)
    assert 'height="60"' in icon.to_svg
    assert 'width="45"' in icon.to_svg


def test_size_custom_height_width_passed():
    icon = Octicon('x', height="60", width="60")
    assert 'height="60"' in icon.to_svg
    assert 'width="60"' in icon.to_svg


def test_a11y_include_attributes():
    icon = Octicon('x', **{'aria-label': 'Close'})
    assert 'role="img"' in icon.to_svg
    assert 'aria-label="Close"' in icon.to_svg


def test_a11y_has_aria_hidden_when_no_label_passed():
    icon = Octicon('x')
    assert 'aria-hidden="true"' in icon.to_svg
