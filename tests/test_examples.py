"""Test of all scripts at examples directory"""  # noqa: E901
from addict import Dict  # noqa: E402
from collections import OrderedDict  # noqa: F401# pylint: disable=W0611, C0411

import examples
import json  # noqa: F401# pylint: disable=W0611, C0411

BASE_URL = "https://fake.zuarbase.net"
API_KEY = "FAKE_API_KEY"


def mock_response(response):
    def _request(*args, params=None, **kwargs):
        """return Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: response,
            "raise_for_status": lambda: None
        })
    return _request


def _request_delete():
    def _request(*args, params=None, **kwargs):
        """return Dict"""
        return Dict({
            "status_code": 204
        })
    return _request


def test_create_bulk_job(mocker, test_bulk_job_fixture):
    """test create_job.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_bulk_job_fixture))  # noqa: E501
    assert examples.create_bulk_job.main(BULK_JOB=test_bulk_job_fixture) == test_bulk_job_fixture  # noqa: E501


def test_create_credentials(mocker, test_credentials_fixture):
    """testing create_credentials.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_credentials_fixture))  # noqa: E501
    assert examples.create_credentials.main(NEW_CREDS=test_credentials_fixture) == test_credentials_fixture  # noqa: E501


def test_create_job(mocker, test_io_job_fixture):
    """testing create_job.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_io_job_fixture))  # noqa: E501
    assert examples.create_job.main(JOB=test_io_job_fixture) == test_io_job_fixture  # noqa: E501


def test_create_job_webhook(mocker, test_create_job_webhook_fixture):
    """testing create_job_webhook.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_create_job_webhook_fixture))  # noqa: E501
    assert examples.create_job_webhook.main(WEBHOOK=test_create_job_webhook_fixture) == test_create_job_webhook_fixture  # noqa: E501


def test_create_sql_job(mocker, test_sql_job_fixture):
    """testing create_sql_job.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_sql_job_fixture))  # noqa: E501
    assert examples.create_sql_job.main(SQL_JOB=test_sql_job_fixture) == test_sql_job_fixture  # noqa: E501


def test_create_tag(mocker, test_tag_fixture):
    """testing create_tag.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_tag_fixture))
    assert examples.create_tag.main(TAG=test_tag_fixture) == test_tag_fixture  # noqa: E501


def test_get_about_messages(mocker, test_get_about_messages_fixture):
    """testing get_about_messages.py"""
    mocker.patch("requests.Session.get", new=mock_response(test_get_about_messages_fixture))  # noqa: E501
    about_messages = examples.get_about_messages.main(BASE_URL=BASE_URL, API_KEY=API_KEY)  # noqa: E501
    assert about_messages == test_get_about_messages_fixture


def test_get_about(mocker, test_get_about_fixture):
    """testing get_about.py"""
    mocker.patch("requests.Session.get", new=mock_response(test_get_about_fixture))  # noqa: E501
    assert examples.get_about.main(BASE_URL=BASE_URL, API_KEY=API_KEY) == test_get_about_fixture  # noqa: E501
    assert examples.get_about.main(BASE_URL=BASE_URL, API_KEY=API_KEY)["system"]["fqdn"] == "aziz-mitto.zuarbase.net"  # noqa: E501


def test_get_single_job(mocker, test_get_job_fixture):
    """testing get_single_job.py"""
    mocker.patch("requests.Session.get", new=mock_response(test_get_job_fixture))  # noqa: E501
    job = examples.get_single_job.main(BASE_URL=BASE_URL, API_KEY=API_KEY)
    assert job == test_get_job_fixture


def test_get_conf_info(mocker, test_get_conf_info_fixture):
    """testing get_about.py"""
    mocker.patch("requests.Session.get", new=mock_response(test_get_conf_info_fixture))  # noqa: E501
    assert examples.get_conf_info.main(BASE_URL=BASE_URL, API_KEY=API_KEY) == test_get_conf_info_fixture["conf"]  # noqa: E501


def test_get_credentials(mocker, test_get_credentials_fixture):
    """testing get_credentials.py"""
    mocker.patch("requests.Session.get", new=mock_response(test_get_credentials_fixture))  # noqa: E501
    assert examples.get_credentials.main(BASE_URL=BASE_URL, API_KEY=API_KEY) == test_get_credentials_fixture  # noqa: E501


def test_get_databases(mocker, test_get_databases_fixture):
    """testing get_databases.py"""
    mocker.patch("requests.Session.get", new=mock_response(test_get_databases_fixture))  # noqa: E501
    assert examples.get_databases.main(BASE_URL=BASE_URL, API_KEY=API_KEY) == test_get_databases_fixture  # noqa: E501


def test_get_job_by_name(mocker, test_get_job_by_name_fixture):
    """testing get_job_by_name.py"""
    mocker.patch("requests.Session.get", new=mock_response(test_get_job_by_name_fixture))  # noqa: E501
    single_status = examples.get_job_by_name.main(BASE_URL=BASE_URL, API_KEY=API_KEY)  # noqa: E501
    assert single_status == test_get_job_by_name_fixture


def test_get_job_schedule(mocker, test_get_job_schedule_fixture):
    """testing get_job_schedule.py"""
    mocker.patch("requests.Session.get", new=mock_response(test_get_job_schedule_fixture))  # noqa: E501
    assert examples.get_job_schedule.main(BASE_URL=BASE_URL, API_KEY=API_KEY) == test_get_job_schedule_fixture  # noqa: E501


def test_search_jobs(mocker, test_get_jobs_fixture):
    """testing get_jobs.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_get_jobs_fixture))  # noqa: E501
    assert list(examples.get_jobs.main(BASE_URL=BASE_URL, API_KEY=API_KEY)) == test_get_jobs_fixture["jobs"]  # noqa: E501


def test_get_metrics(mocker, test_get_metrics_fixture):
    """testing get_metrics.py"""
    mocker.patch("requests.Session.get", new=mock_response(test_get_metrics_fixture))  # noqa: E501
    metrics = examples.get_metrics.main(BASE_URL=BASE_URL, API_KEY=API_KEY)
    assert metrics == test_get_metrics_fixture


def test_get_pkg(mocker, test_get_pkg_fixture):
    """testing get_pkg.py"""
    mocker.patch("requests.Session.get", new=mock_response(test_get_pkg_fixture))  # noqa; E501
    packages = examples.get_pkg.main(BASE_URL=BASE_URL, API_KEY=API_KEY)
    assert packages == test_get_pkg_fixture


def test_get_single_job_webhook_conf_info(mocker, test_get_single_job_webhook_conf_info_fixture):  # noqa: E501
    """testing get_single_job_webhook_conf_info.py"""
    mocker.patch("requests.Session.get", new=mock_response(test_get_single_job_webhook_conf_info_fixture))  # noqa:
    assert examples.get_single_job_webhook_conf_info.main(BASE_URL=BASE_URL, API_KEY=API_KEY) == test_get_single_job_webhook_conf_info_fixture  # noqa: E501


def test_get_tags(mocker, test_get_tags_fixture):
    """testing get_tags.py"""
    mocker.patch("requests.Session.get", new=mock_response(test_get_tags_fixture))  # noqa: E501
    assert examples.get_tags.main(BASE_URL=BASE_URL, API_KEY=API_KEY) == test_get_tags_fixture  # noqa: E501


def test_get_webhooks(mocker, test_get_webhooks_fixture, test_io_job_fixture):
    """testing get_webhooks.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_io_job_fixture))  # noqa: E501
    mocker.patch("requests.Session.get", new=mock_response(test_get_webhooks_fixture))  # noqa: E501
    webhooks = examples.get_webhooks.main(BASE_URL=BASE_URL, API_KEY=API_KEY)
    assert webhooks == test_get_webhooks_fixture


def test_start_job(mocker, test_start_job_fixture):
    """testing start_job.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_start_job_fixture))  # noqa: E501
    assert examples.start_job.main(BASE_URL=BASE_URL, API_KEY=API_KEY) == test_start_job_fixture  # noqa: E501


def test_get_single_job_status(mocker, test_get_single_job_status_fixture, test_io_job_fixture):  # noqa: E501
    """testing get_single_job.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_io_job_fixture))  # noqa: E501
    mocker.patch("requests.Session.get", new=mock_response(test_get_single_job_status_fixture))  # noqa: E501
    single_status = examples.get_single_job_status.main(BASE_URL=BASE_URL, API_KEY=API_KEY)  # noqa: E501
    assert single_status == test_get_single_job_status_fixture


def test_update_job_credentials(mocker, test_update_job_credentials_fixture, test_io_job_fixture, test_get_jobs_fixture):  # noqa: E501
    """testing update_job_credentials.py"""
    mocker.patch("requests.Session.get", new=mock_response(test_io_job_fixture))  # noqa: E501
    mocker.patch("requests.Session.post", new=mock_response(test_get_jobs_fixture))  # noqa: E501
    mocker.patch("requests.Session.patch", new=mock_response(test_update_job_credentials_fixture))  # noqa: E501
    input_creds = "Fakeforse - fake.fake@zuar.com"
    assert examples.update_job_credentials.main(
        BASE_URL=BASE_URL,
        API_KEY=API_KEY,
        INPUT_CREDS=input_creds
    ) == test_update_job_credentials_fixture


def test_update_job(mocker, test_update_job_fixture):
    """testing update_job.py"""
    mocker.patch("requests.Session.patch", new=mock_response(test_update_job_fixture))  # noqa: E501
    update_job = {
        "title": "sql",
        "type": "sql",
        "markdown": "string",
        "schedule": {
          "type": "daily",
          "daily": {
            "minute": 0,
            "hour": 6,
            "ampm": "AM"
          },
        },
        "timeout": 0,
        "notify": 0,
        "delay": 0,
        "continue_on_error": True,
        "concurrency": 0,
        "conf": "string",
        "tags": [
            "string"
        ],
        "input": {},
        "output": {},
        "sdl": {},
        "steps": [
            "string"
        ]
    }
    assert examples.update_job.main(BASE_URL=BASE_URL, API_KEY=API_KEY, UPDATE_JOB=update_job) == test_update_job_fixture  # noqa: E501


def test_update_job_schedule(mocker, test_update_job_schedule_fixture):
    """testing update_job_schedule.py"""
    mocker.patch("requests.Session.patch", new=mock_response(test_update_job_schedule_fixture))  # noqa: E501

    schedule = {
        "value": "daily",
        "type": "daily",
        "daily": {
          "minute": 0,
          "hour": 6,
          "ampm": "AM"
        },
        "hourly": None,
        "custom": None
    }

    assert examples.update_job_schedule.main(
        BASE_URL=BASE_URL,
        API_KEY=BASE_URL,
        SCHEDULE=schedule
    ) == test_update_job_schedule_fixture


def test_update_pkg(mocker, test_update_pkg_fixture):
    """testing update_pkg.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_update_pkg_fixture))  # noqa: E501
    assert examples.update_pkg.main(BASE_URL=BASE_URL, API_KEY=API_KEY) == test_update_pkg_fixture  # noqa: E501


def test_dbo_update_sql_job(mocker, test_dbo_update_sql_job_fixture, test_sql_job_fixture):  # noqa: E501
    """testing dbo_update_sql_job.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_sql_job_fixture))  # noqa: E501
    mocker.patch("requests.Session.patch", new=mock_response(test_dbo_update_sql_job_fixture))  # noqa: E501
    dbo = "postrgesql://localhost/fake"
    assert examples.dbo_update_sql_job.main(BASE_URL=BASE_URL, API_KEY=API_KEY, DBO=dbo) == test_dbo_update_sql_job_fixture  # noqa: E501


def test_delete_job(mocker, test_delete_job_fixture):
    """testing delete_job.py"""
    mocker.patch("requests.Session.delete", new=_request_delete())
    assert examples.delete_job.main(BASE_URL=BASE_URL, API_KEY=API_KEY) == test_delete_job_fixture  # noqa: E501


def test_delete_webhook(mocker, test_delete_job_webhook_fixture, test_io_job_fixture, test_create_job_webhook_fixture):  # noqa: E501
    """testing delete_webhook.py"""
    mocker.patch("requests.Session.post", new=mock_response(test_io_job_fixture))  # noqa: E501
    mocker.patch("requests.Session.post", new=mock_response(test_create_job_webhook_fixture))  # noqa: E501
    mocker.patch("requests.Session.delete", new=_request_delete())  # noqa: E501
    assert examples.delete_webhook.main(BASE_URL=BASE_URL, API_KEY=API_KEY) == test_delete_job_webhook_fixture  # noqa: E501


def test_update_a_webhook(mocker, test_get_webhooks_fixture, test_update_a_webhook_fixture):  # noqa: E501
    """testing update_a_webhook.py"""
    mocker.patch("requests.Session.get", new=mock_response(test_get_webhooks_fixture))  # noqa: E501
    mocker.patch("requests.Session.put", new=mock_response(test_update_a_webhook_fixture))  # noqa: E501
    WEBHOOK = "https://fakehook.com"
    assert examples.update_a_webhook.main(BASE_URL=BASE_URL, API_KEY=API_KEY, WEBHOOK=WEBHOOK) == [test_update_a_webhook_fixture]  # noqa: E501
