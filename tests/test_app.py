"""Test Template."""

import pytest

from kpi_app import app


@pytest.mark.unit
def test_hello():
    """Validate package is importable"""
    assert app.hello_world() == "Hello World!"
