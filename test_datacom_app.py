import pytest
import random
from datacom_app import DatacomApplication


@pytest.fixture
def job_application():
    return DatacomApplication("Cloud engineer")

def test_check_role_with_available_position(job_application):
    assert job_application.checkRole() is True

def test_check_role_with_unavailable_position():
    job_application = DatacomApplication("Chief Emoji Officer")
    assert job_application.checkRole() is False

def test_check_hired(job_application, capsys, monkeypatch):

    # Monkeypatching the random function to always return True
    monkeypatch.setattr(random, 'choice', lambda x: True)
    job_application.checkHired()

    captured_output = capsys.readouterr()
    assert "I got hired!" in captured_output.out

def test_apply_to_datacom(job_application, capsys):
    job_application.applyToDatacom()

    captured_output = capsys.readouterr()
    assert "Submitting the application" in captured_output.out
