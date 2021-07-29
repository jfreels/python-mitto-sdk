"""Test of all scripts at examples directory"""  # noqa: E902
from addict import Dict  # noqa: E402
from collections import OrderedDict

import examples


def mock_response(response):
    def _request(*args, params=None, **kwargs):
        """return Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: response,
            "raise_for_status": lambda: None
        })
    return _request


def _request_delete(*args, params=None, **kwargs):
    return Dict({
        "status_code": 204
    })


BASE_URL = "https://fake.zuarbase.net"
API_KEY = "FAKE_API_KEY"


def test_create_bulk_job(mocker, test_create_bulk_job):
    """test create_job.py"""
    mocker.patch("requests.Session.post", new=[test_create_bulk_job])
    assert examples.create_bulk_job.main(BULK_JOB=[test_create_bulk_job]) == [test_create_bulk_job]  # noqa: E501


def test_create_credentials(mocker):
    """testing create_credentials.py"""
    mocker.patch("requests.Session.post", new=[test_create_credentials])  # noqa: E501
    creds = {
        "name": "fake name",
        "type": "fake",
        "data": {}
    }
    assert examples.create_credentials.main(NEW_CREDS=creds) == [test_create_credentials]  # noqa: E501


def test_create_job(mocker):
    """testing create_job.py"""
    mocker.patch("requests.Session.post", new=[test_create_job])
    job = {
        "id": 1,
        "name": "job_name",
        "title": "job name",
        "conf": {
            "hello": "world"
        }
    }
    assert examples.create_job.main(JOB=job) == [test_create_job]


def test_create_job_webhook(mocker):
    """testing create_job_webhook.py"""
    mocker.patch("requests.Session.post", new=[test_create_job_webhook])
    webhook = {
        "id": 1,
        "url": "https://webhook.site/83d6607a-0118-478d-a68c-cf2ab4645314",
        "method": "POST",
        "event_type": "JOB_COMPLETE"
    }
    assert examples.create_job_webhook.main(WEBHOOK=webhook) == [test_create_job_webhook]  # noqa: E501


def test_create_sql_job(mocker):
    """testing create_sql_job.py"""
    mocker.patch("requests.Session.post", new=[test_create_sql_job])  # noqa: E501
    assert examples.create_sql_job.main() == [test_create_sql_job]  # noqa: E501


def test_create_tag(mocker):
    """testing create_tag.py"""
    mocker.patch("requests.Session.post", new=[test_create_tag])
    tag = {
        "name": "Allow"
    }
    assert examples.create_tag.main(TAG=tag) == [test_create_tag]


def test_get_about_messages(mocker):
    """testing get_about_messages.py"""
    mocker.patch("requests.Session.get", new=[test_get_about_messages])  # noqa: E501
    about_messages = examples.get_about_messages.main(BASE_URL, API_KEY)  # noqa: E501
    assert about_messages == [test_get_about_messages]


def test_get_about(mocker):
    """testing get_about.py"""
    mocker.patch("requests.Session.get", new=[test_get_about])
    assert examples.get_about.main(BASE_URL, API_KEY) == [test_get_about]  # noqa: E501
    assert examples.get_about.main(BASE_URL, API_KEY)["system"]["fqdn"] == "fake.zuarbase.net"  # noqa: E501


def test_get_single_job(mocker):
    """testing get_single_job.py"""
    mocker.patch("requests.Session.get", new=[test_get_single_job])
    job = examples.get_single_job.main(BASE_URL, API_KEY)

    expected_results = {
        "id": 1,
        "name": "job_name",
        "title": "job name",
        "conf": {
            "hello": "world"
        }
    }

    assert job == expected_results


def test_get_conf_info(mocker):
    """testing get_about.py"""
    mocker.patch("requests.Session.get", new=[test_get_conf_info])  # noqa: E501
    expected_results = OrderedDict([('hello', 'world')])
    assert examples.get_conf_info.main() == expected_results  # noqa: E501


def test_get_credentials(mocker):
    """testing get_credentials.py"""
    mocker.patch("requests.Session.get", new=[test_get_credentials])  # noqa: E501
    expected_results = {
        "id": 1,
        "name": "fake name",
        "type": "fake"
    }
    assert examples.get_credentials.main(BASE_URL, API_KEY) == expected_results  # noqa: E501


def test_get_databases(mocker):
    """testing get_databases.py"""
    mocker.patch("requests.Session.get", new=[test_get_databases])  # noqa: E501
    expected_results = {
        "name": "fake name",
        "size": 10230,
        "size_hr": "1000 kB"
    }
    assert examples.get_databases.main(BASE_URL, API_KEY) == expected_results


def test_get_job_by_name(mocker):
    """testing get_job_by_name.py"""
    mocker.patch("requests.Session.post", new=mock_response(BULK_JOB_RESPONSE))
    mocker.patch("requests.Session.get", new=mock_response(GET_BULK_RESPONSE))
    single_status = examples.get_job_by_name.main(BASE_URL, API_KEY)
    assert single_status == GET_BULK_RESPONSE


def test_get_job_schedule(mocker):
    """testing get_job_schedule.py"""
    mocker.patch("requests.Session.post", new=mock_response(GET_JOB_RESPONSE2.schedule))  # noqa: E501
    mocker.patch("requests.Session.get", new=mock_response(GET_JOB_RESPONSE2.schedule))  # noqa: E501
    assert examples.get_job_schedule.main(BASE_URL, API_KEY) == GET_JOB_RESPONSE2.schedule  # noqa: E501


def test_search_jobs(mocker):
    """testing get_jobs.py"""
    mocker.patch("requests.Session.post", new=mock_response(GET_JOB_RESPONSE))
    mocker.patch("requests.Session.post", new=mock_response(GET_JOBS_RESPONSE))
    assert list(examples.get_jobs.main(BASE_URL, API_KEY)) == GET_JOBS_RESPONSE["jobs"]  # noqa: E501


def test_get_metrics(mocker):
    """testing get_metrics.py"""
    mocker.patch("requests.Session.get", new=mock_response(GET_METRICS_RESPONSE))  # noqa: E501
    metrics = examples.get_metrics.main(BASE_URL, API_KEY)
    assert metrics == GET_METRICS_RESPONSE


def test_get_pkg(mocker):
    """testing get_pkg.py"""
    mocker.patch("requests.Session.get", new=mock_response(GET_PACKAGE_RESPONSE))  # noqa; E501
    packages = examples.get_pkg.main(BASE_URL, API_KEY)
    assert packages == GET_PACKAGE_RESPONSE


def test_get_single_job_webhook_conf_info(mocker):
    """testing get_single_job_webhook_conf_info.py"""
    mocker.patch("requests.Session.post", new=mock_response(GET_JOB_RESPONSE))
    mocker.patch("requests.Session.get", new=mock_response(WEBHOOK_RESPONSE))
    assert examples.get_single_job_webhook_conf_info.main(BASE_URL, API_KEY) == WEBHOOK_RESPONSE  # noqa: E501


def test_get_tags(mocker):
    """testing get_tags.py"""
    mocker.patch("requests.Session.post", new=mock_response(TAGS_BODY))
    mocker.patch("requests.Session.get", new=mock_response(GET_TAGS_RESPONSE))
    assert examples.get_tags.main(BASE_URL, API_KEY) == GET_TAGS_RESPONSE  # noqa: E501


def test_get_webhooks(mocker):
    """testing get_webhooks.py"""
    mocker.patch("requests.Session.post", new=mock_response(WEBHOOK_RESPONSE))
    mocker.patch("requests.Session.get", new=mock_response(WEBHOOK_RESPONSE))
    webhooks = examples.get_webhooks.main(BASE_URL, API_KEY)
    assert webhooks == WEBHOOK_RESPONSE


def test_start_job(mocker):
    """testing start_job.py"""
    mocker.patch("requests.Session.post", new=mock_response(GET_JOB_RESPONSE))
    mocker.patch("requests.Session.post", new=mock_response(ACTION_RESPONSE))
    assert examples.start_job.main(BASE_URL, API_KEY) == ACTION_RESPONSE  # noqa: E501


def test_get_single_job_status(mocker):
    """testing get_single_job.py"""
    mocker.patch("requests.Session.post", new=mock_response(GET_JOB_RESPONSE))
    mocker.patch("requests.Session.post", new=mock_response(ACTION_RESPONSE))
    mocker.patch("requests.Session.get", new=mock_response(GET_STATUS_RESPONSE))  # noqa: E501
    single_status = examples.get_single_job_status.main(BASE_URL, API_KEY)  # noqa: E501
    assert single_status == GET_STATUS_RESPONSE


def test_update_job_credentials(mocker):
    """testing update_job_credentials.py"""
    mocker.patch("requests.Session.post", new=mock_response(GET_JOB_RESPONSE))  # noqa: E501
    mocker.patch("requests.Session.patch", new=mock_response(UPDATE_JOB_CREDS_RESPONSE))  # noqa: E501
    input_creds = "Fakeforse - fake.fake@zuar.com]"
    assert examples.update_job_credentials.main(
        BASE_URL,
        API_KEY,
        INPUT_CREDS=input_creds
    ) == UPDATE_JOB_CREDS_RESPONSE


def test_update_job(mocker):
    """testing update_job.py"""
    mocker.patch("requests.Session.post", new=mock_response(GET_JOB_RESPONSE))
    mocker.patch("requests.Session.patch", new=mock_response(UPDATE_JOB_RESPONSE))  # noqa: E501
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
    assert examples.update_job.main(BASE_URL, API_KEY, UPDATE_JOB=update_job) == UPDATE_JOB_RESPONSE  # noqa: E501


def test_update_job_schedule(mocker):
    """testing update_job_schedule.py"""
    mocker.patch("requests.Session.get", new=mock_response(GET_JOB_RESPONSE2))  # noqa: E501
    mocker.patch("requests.Session.patch", new=mock_response(UPDATE_JOB_RESPONSE))  # noqa: E501

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
        BASE_URL,
        API_KEY,
        SCHEDULE=schedule
    ) == UPDATE_JOB_RESPONSE


def test_update_pkg(mocker):
    """testing update_pkg.py"""
    mocker.patch("requests.Session.post", new=mock_response(UPDATE_PKG_RESPONSE))  # noqa: E501
    assert examples.update_pkg.main(BASE_URL, API_KEY) == UPDATE_PKG_RESPONSE  # noqa: E501


def test_dbo_update_sql_job(mocker):
    """testing dbo_update_sql_job.py"""
    mocker.patch("requests.Session.post", new=mock_response(GET_JOB_RESPONSE2))
    mocker.patch("requests.Session.patch", new=mock_response(CONF_UPDATE_RESPONSE))  # noqa: E501
    dbo = "postrgesql://localhost/fake"
    assert examples.dbo_update_sql_job.main(BASE_URL, API_KEY, DBO=dbo) == CONF_UPDATE_RESPONSE  # noqa: E501


def test_delete_job(mocker):
    """testing delete_job.py"""
    mocker.patch("requests.Session.post", new=mock_response(GET_JOB_RESPONSE))
    mocker.patch("requests.Session.delete", new=_request_delete)
    assert examples.delete_job.main(BASE_URL, API_KEY) == {'status_code': 204}  # noqa: E501


def test_delete_webhook(mocker):
    """testing delete_webhook.py"""
    mocker.patch("requests.Session.post", new=mock_response(GET_JOB_RESPONSE))
    mocker.patch("requests.Session.post", new=mock_response(WEBHOOK_RESPONSE))
    mocker.patch("requests.Session.delete", new=_request_delete)
    assert examples.delete_webhook.main(BASE_URL, API_KEY) == {'status_code': 204}  # noqa: E501
