"""testing client.py functions"""  # noqa: E902
import requests

from addict import Dict
from src.mitto_sdk import Mitto


def mock_response(response):
    def _request(*args, params=None, **kwargs):
        """return Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: response,
            "raise_for_status": lambda: None
        })
    return _request


def test_init(mocker):
    mocker.patch.object(requests, 'Session', autospec=True)
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    assert mitto.session.params["API_KEY"] == "FAKE_API_KEY"


def test_base_url_ends_with_slash(mocker):
    mocker.patch.object(requests, 'Session', autospec=True)
    mitto = Mitto(
        base_url="https://fake.zuarbase.net/",
        api_key="FAKE_API_KEY"
    )
    assert mitto.base_url == "https://fake.zuarbase.net"


ABOUT_RESPONSE = Dict()
ABOUT_RESPONSE.version = "2.9.3"
ABOUT_RESPONSE.system.fqdn = "fake.zuarbase.net"


def test_get_about(mocker):
    mocker.patch("requests.Session.get", new=mock_response(ABOUT_RESPONSE))
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    assert mitto.get_about() == ABOUT_RESPONSE
    assert mitto.get_about()["system"]["fqdn"] == "fake.zuarbase.net"


GET_JOB_RESPONSE = Dict()
GET_JOB_RESPONSE.id = 1
GET_JOB_RESPONSE.name = "job_name"
GET_JOB_RESPONSE.title = "job name"
CONF_RESPONSE = '{ "hello": "world" }'
GET_JOB_RESPONSE.conf = CONF_RESPONSE


def test_get_job(mocker):
    mocker.patch("requests.Session.get", new=mock_response(GET_JOB_RESPONSE))
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    job = mitto.get_job(49)

    expected_results = {
        "id": 1,
        "name": "job_name",
        "title": "job name",
        "conf": {
            "hello": "world"
        }
    }

    assert job == expected_results


GET_JOB_RESPONSE2 = Dict()
GET_JOB_RESPONSE2.id = 1
GET_JOB_RESPONSE2.name = "job_name"
GET_JOB_RESPONSE2.title = "job name"
CONF_RESPONSE2 = '{ "hello": "world" }'
GET_JOB_RESPONSE2.conf = CONF_RESPONSE2
GET_JOB_RESPONSE2.schedule = Dict()
GET_JOB_RESPONSE2.schedule.type = "daily"
GET_JOB_RESPONSE2.schedule.daily = {
    "minute": 0,
    "hour": 12,
    "ampm": "AM"
}


def test_get_job_schedule(mocker):
    mocker.patch("requests.Session.get", new=mock_response(GET_JOB_RESPONSE2))
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )

    assert mitto.get_job_schedule(job_id=47) == GET_JOB_RESPONSE2.schedule


def test_update_schedule(mocker):
    mocker.patch("requests.Session.patch", new=mock_response(GET_JOB_RESPONSE))
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    assert mitto.update_job_schedule(
        job_id=1,
        job_schedule={
            'value': 'never',
            'type': 'never',
            'daily': None,
            'hourly': None,
            'custom': None
        }
    ) == GET_JOB_RESPONSE


UPDATE_JOB_RESPONSE = {
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


def test_update_job(mocker):
    mocker.patch("requests.Session.patch", new=mock_response(UPDATE_JOB_RESPONSE))  # noqa: E501
    mitto = Mitto(
        base_url="https:fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    assert mitto.update_job(job_id=52, update_job_body=UPDATE_JOB_RESPONSE)


def test_update_job_conf(mocker):
    mocker.patch("requests.Session.patch", new=mock_response(GET_JOB_RESPONSE))
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    new_conf = Dict()
    new_conf.id = 1
    new_conf.name = "fake_job"
    new_conf.title = "fake job"
    assert mitto.update_job_conf(
        job_id=1,
        job_conf=new_conf
    ) == GET_JOB_RESPONSE


def test_create_job(mocker):
    mocker.patch("requests.Session.post", new=mock_response(GET_JOB_RESPONSE))
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    job = {
        "id": 1,
        "name": "job_name",
        "title": "job name",
        "conf": {
            "hello": "world"
        }
    }
    assert mitto.create_job(job=job) == GET_JOB_RESPONSE


GET_CMD_JOB_RESPONSE = Dict()
GET_CMD_JOB_RESPONSE.id = 2
GET_CMD_JOB_RESPONSE.name = "cmd_job"
GET_CMD_JOB_RESPONSE.title = "cmd job"
GET_CMD_JOB_RESPONSE.type = "cmd"
GET_CMD_JOB_RESPONSE.tags = "cmd"


def test_create_cmd_job(mocker):
    mocker.patch("requests.Session.post", new=mock_response(GET_CMD_JOB_RESPONSE))  # noqa: E501
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    cmd_job = {
        "name": "cmd_job",
        "title": "cmd job",
        "type": "cmd",
        "tags": [
            "cmd"
        ]
    }
    assert (mitto.create_job(job=cmd_job)) == GET_CMD_JOB_RESPONSE


ACTION_RESPONSE = Dict()
ACTION_RESPONSE.id = 68848
ACTION_RESPONSE.returncode = None
ACTION_RESPONSE.started_at = "2021-04-19T18:35:10.550109+00:00"


def test_job_action(mocker):
    mocker.patch("requests.Session.post", new=mock_response(ACTION_RESPONSE))
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    action = "start"
    job_id = 65
    assert mitto.job_action(job_id, action) == ACTION_RESPONSE
    assert mitto.start_job(65) == ACTION_RESPONSE


WEBHOOK_RESPONSE = Dict()
WEBHOOK_RESPONSE.url = (
    'https://webhook.site'
    '/83d6607a-0118-478d-a68c-cf2ab4645314')
WEBHOOK_RESPONSE.method = "POST"
WEBHOOK_RESPONSE.event_type = "JOB_COMPLETE"


def test_create_job_webhook(mocker):
    mocker.patch("requests.Session.post", new=mock_response(WEBHOOK_RESPONSE))
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    webhook = {
        "url": "https://webhook.site/83d6607a-0118-478d-a68c-cf2ab4645314",
        "method": "POST",
        "event_type": "JOB_COMPLETE",
        "content_type": "application/json",
        "body": '{ "text": "hello world" }',
        "enabled": True
    }
    assert mitto.create_job_webhook(
        job_id=1,
        job_hook=webhook
    ) == WEBHOOK_RESPONSE


def test_get_job_webhooks(mocker):
    mocker.patch("requests.Session.get", new=mock_response(WEBHOOK_RESPONSE))
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    assert mitto.get_job_webhooks(
        job_id=1
    ) == WEBHOOK_RESPONSE


GET_JOBS_RESPONSE = Dict()
GET_JOBS_RESPONSE.jobs = []
GET_JOBS_RESPONSE.jobs.append(GET_JOB_RESPONSE)
GET_JOBS_RESPONSE.pagination = {
    'count': 82,
    'limit': 50,
    'more_pages': False,
    'offset': 50
}


def test_get_jobs(mocker):
    mocker.patch("requests.Session.post", new=mock_response(GET_JOBS_RESPONSE))
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    assert list(mitto.get_jobs()) == GET_JOBS_RESPONSE["jobs"]


def test_start_job(mocker):
    mocker.patch("requests.Session.post", new=mock_response(ACTION_RESPONSE))
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    assert mitto.start_job(3) == ACTION_RESPONSE


def test_migrate_to_new_db(mocker):
    mocker.patch("requests.Session.patch", new=mock_response(GET_JOB_RESPONSE.conf))  # noqa: E501
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    new_conf = Dict()
    new_conf.id = 1
    new_conf.name = "fake_job"
    new_conf.title = "fake job"
    new_conf.dbo = "fakesql"
    assert mitto.update_job_conf(
        job_id=49,
        job_conf=new_conf
    ) == GET_JOB_RESPONSE.conf


GET_TAGS_RESPONSE = Dict()
GET_TAGS_RESPONSE.id = 1
GET_TAGS_RESPONSE.name = "fake_name"
GET_TAGS_RESPONSE.updated_at = "2021-12-12t12:00:00+00:00"
GET_TAGS_RESPONSE.created_at = "2021-12-12t12:00:00+00:00"


def test_get_tags(mocker):
    mocker.patch("requests.Session.get", new=mock_response(GET_TAGS_RESPONSE))
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    assert mitto.get_tags(tags_id=1) == GET_TAGS_RESPONSE


def test_delete_job(mocker):
    def _request_delete(*args, params=None, **kwargs):
        return Dict({
            "status_code": 204
        })
    mocker.patch("requests.Session.delete", new=_request_delete)
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    assert mitto.delete_job(job_id=1) == {'status_code': 204}


def test_delete_webhook(mocker):
    def _request_delete(*args, params=None, **kwargs):
        return Dict({
            "status_code": 204
        })
    mocker.patch("requests.Session.delete", new=_request_delete)
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    assert mitto.delete_webhook(webhook_id=1) == {'status_code': 204}


GET_ABOUT_MESSAGES_RESPONSE = Dict()
GET_ABOUT_MESSAGES_RESPONSE.enabled = "false"


def test_get_about_messages(mocker):
    mocker.patch("requests.Session.get", new=mock_response(GET_ABOUT_MESSAGES_RESPONSE))  # noqa: E501
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    about_messages = mitto.get_about_messages()
    assert about_messages == GET_ABOUT_MESSAGES_RESPONSE


def test_get_webhooks(mocker):
    mocker.patch("requests.Session.get", new=mock_response(WEBHOOK_RESPONSE))
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    webhooks = mitto.get_webhooks()
    assert webhooks == WEBHOOK_RESPONSE


GET_METRICS_RESPONSE = Dict()
GET_METRICS_RESPONSE.total_jobs_count = 0
GET_METRICS_RESPONSE.total_runs_count = 0


def test_get_metrics(mocker):
    mocker.patch("requests.Session.get", new=mock_response(GET_METRICS_RESPONSE))  # noqa: E501
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    metrics = mitto.get_metrics()
    assert metrics == GET_METRICS_RESPONSE


GET_PACKAGE_RESPONSE = Dict()
GET_PACKAGE_RESPONSE.timestamp = "2021-07-05T15:07:26.554979"


def test_get_pkg(mocker):
    mocker.patch("requests.Session.get", new=mock_response(GET_PACKAGE_RESPONSE))  # noqa: E501
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    packages = mitto.get_pkg()
    assert packages == GET_PACKAGE_RESPONSE


GET_STATUS_RESPONSE = Dict()
GET_STATUS_RESPONSE.id = 0


def test_get_single_job_status(mocker):
    mocker.patch("requests.Session.get", new=mock_response(GET_STATUS_RESPONSE))  # noqa: E501
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    single_status = mitto.get_single_job_status(1)
    assert single_status == GET_STATUS_RESPONSE


GET_BULK_RESPONSE = Dict()
GET_BULK_RESPONSE.name = "fake_name"


def test_get_bulk_jobs(mocker):
    mocker.patch("requests.Session.get", new=mock_response(GET_BULK_RESPONSE))
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    single_status = mitto.get_bulk_jobs()
    assert single_status == GET_BULK_RESPONSE


BULK_JOB_RESPONSE = Dict()
BULK_JOB_RESPONSE.name = "fake_name"  # noqa: E501
BULK_JOB_RESPONSE.title = "fake_title"
BULK_JOB_RESPONSE.type = "fake_type"
BULK_JOB_RESPONSE.tags = "fake_tag"


def test_create_bulk_jobs(mocker):
    mocker.patch("requests.Session.post", new=mock_response(BULK_JOB_RESPONSE))
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    bulk_job = [{
        "name": "fake_name",
        "title": "fake_title",
        "type": "fake_type",
        "tags": [
            "fake_tag"
        ]
    }]
    assert mitto.create_bulk_jobs(
        bulk_job=bulk_job
    ) == BULK_JOB_RESPONSE


UPDATE_PKG_RESPONSE = Dict()
UPDATE_PKG_RESPONSE.timestamp = "2021-07-05T15:02:23.012862"


def test_update_pkg(mocker):
    mocker.patch("requests.Session.post", new=mock_response(UPDATE_PKG_RESPONSE))  # noqa: E501
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    assert mitto.update_pkg() == UPDATE_PKG_RESPONSE


TAGS_BODY = {
    "name": "Allow"
}


def test_create_tags(mocker):
    mocker.patch("requests.Session.post", new=mock_response(TAGS_BODY))
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    tags = {
        "name": "Allow"
    }
    assert mitto.create_tags(tags=tags) == TAGS_BODY


CREDS_RESPONSE = {
    "name": "fake name",
    "type": "fake",
    "data": {}
}


def test_create_credentials(mocker):
    mocker.patch("requests.Session.post", new=mock_response(CREDS_RESPONSE))  # noqa: E501
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    creds = {
        "name": "fake name",
        "type": "fake",
        "data": {}
    }
    assert mitto.create_credentials(creds=creds) == CREDS_RESPONSE


GET_CREDENTIALS_RESPONSE = Dict()
GET_CREDENTIALS_RESPONSE.id = 1
GET_CREDENTIALS_RESPONSE.name = "fake name"
GET_CREDENTIALS_RESPONSE.type = "fake"


def test_get_credentials(mocker):
    mocker.patch("requests.Session.get", new=mock_response(GET_CREDENTIALS_RESPONSE))  # noqa: E501
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    expected_results = {
        "id": 1,
        "name": "fake name",
        "type": "fake"
    }
    assert mitto.get_credentials() == expected_results


GET_DATABASES_RESPONSE = Dict()
GET_DATABASES_RESPONSE.name = "fake name"
GET_DATABASES_RESPONSE.size = 10230
GET_DATABASES_RESPONSE.size_hr = "1000 kB"


def test_get_databases(mocker):
    mocker.patch("requests.Session.get", new=mock_response(GET_DATABASES_RESPONSE))  # noqa: E501
    mitto = Mitto(
        base_url="https://fake/zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    expected_results = {
        "name": "fake name",
        "size": 10230,
        "size_hr": "1000 kB"
    }
    assert mitto.get_databases() == expected_results


UPDATE_WEBHOOK_RESPONSE = {
    "url": "https://webhook.site/83d6607a-0118-478d-a68c-cf2ab4645314"
}


def test_update_a_webhook(mocker):
    mocker.patch("requests.Session.put", new=mock_response(UPDATE_WEBHOOK_RESPONSE))  # noqa: E501
    mitto = Mitto(
        base_url="https://fake.zuarbase.net",
        api_key="FAKE_API_KEY"
    )
    webhook = {
        "url": "https://webhook.site/83d6607a-0118-478d-a68c-cf2ab4645314"
    }
    assert mitto.update_a_webhook(webhook_id=1, webhook=webhook) == UPDATE_WEBHOOK_RESPONSE  # noqa: E501
