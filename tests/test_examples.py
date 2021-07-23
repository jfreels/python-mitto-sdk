"""Test of all scripts at examples directory"""  # noqa: E902
from addict import Dict  # noqa: E402
from examples.create_bulk_job import main as create_bulk_job
from examples.create_cmd_job import main as create_cmd_job
from examples.create_credentials import main as create_credentials
from examples.create_job import main as create_job
from examples.create_job_webhook import main as create_job_webhook
from examples.create_sql_job import main as create_sql_job
from examples.create_tag import main as create_tag
from examples.dbo_update_sql_job import main as dbo_update_sql_job
from examples.delete_job import main as delete_job
from examples.delete_webhook import main as delete_webhook
from examples.get_about_messages import main as get_about_messages
from examples.get_about import main as get_about
from examples.get_conf_info import main as get_conf_info
from examples.get_credentials import main as get_credentials
from examples.get_databases import main as get_databases
from examples.get_job_by_name import main as get_job_by_name
from examples.get_job_schedule import main as get_job_schedule
from examples.get_jobs import main as get_jobs
from examples.get_metrics import main as get_metrics
from examples.get_pkg import main as get_pkg
from examples.get_single_job import main as get_single_job
from examples.get_single_job_status import main as get_single_job_status
from examples.get_single_job_webhook_conf_info import main as get_single_job_webhook_conf_info  # noqa: E501
from examples.get_tags import main as get_tags
from examples.get_webhooks import main as get_webhooks
from examples.start_job import main as start_job
from examples.update_job_credentials import main as update_job_credentials
from examples.update_job import main as update_job
from examples.update_job_schedule import main as update_job_schedule
from examples.update_pkg import main as update_pkg


BULK_JOB_RESPONSE = Dict()
BULK_JOB_RESPONSE.name = "fake_name"  # noqa: E501
BULK_JOB_RESPONSE.title = "fake_title"
BULK_JOB_RESPONSE.type = "fake_type"
BULK_JOB_RESPONSE.tags = "fake_tag"


def test_create_bulk_job(mocker):
    """test create_job.py"""
    def _request_post():
        """return Dict"""
        return Dict({
           "status_code": 200,
           "json": lambda: BULK_JOB_RESPONSE,
           "raise_for_status": lambda: None
        })
    mocker.patch("requests.Session.post", new=_request_post)
    bulk_job = [{
        "name": "fake_name",
        "title": "fake_title",
        "type": "fake_type",
        "tags": [
            "fake_tag"
        ],
        "conf": {
            "dbo": "postgresql://localhost/analytics",
            "sql": "select 1;",
            "parameters": {},
            "kwargs": {},
            "transaction": True,
            "split": False
        }
    }]
    assert create_bulk_job(BULK_JOB=bulk_job) == BULK_JOB_RESPONSE


GET_CMD_JOB_RESPONSE = Dict()
GET_CMD_JOB_RESPONSE.id = 2
GET_CMD_JOB_RESPONSE.name = "cmd_job"
GET_CMD_JOB_RESPONSE.title = "cmd job"
GET_CMD_JOB_RESPONSE.type = "cmd"
GET_CMD_JOB_RESPONSE.tags = "cmd"


def test_create_cmd_job(mocker):
    """testing create_cmd_job.py"""
    def _request_post():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: GET_CMD_JOB_RESPONSE,
            "raise_for_status": None
        })

    mocker.patch("requests.Session.post", new=_request_post)
    cmd_job = {
        "name": "cmd_job",
        "title": "cmd_job",
        "type": "cmd",
        "tags": [
            "cmd"
        ]
    }
    assert create_cmd_job(JOB=cmd_job) == GET_CMD_JOB_RESPONSE


CREDS_RESPONSE = {
    "name": "fake name",
    "type": "fake",
    "data": {}
}


def test_create_credentials(mocker):
    """testing create_credentials.py"""
    def _request_post():
        """returning Dict"""
        return Dict({
            "status code": 200,
            "json": lambda: CREDS_RESPONSE,
            "raise_for_status": lambda: None
        })
    mocker.patch("requests.Session.post", new=_request_post)
    creds = {
        "name": "fake name",
        "type": "fake",
        "data": {}
    }
    assert create_credentials(NEW_CREDS=creds) == CREDS_RESPONSE


GET_JOB_RESPONSE = Dict()
GET_JOB_RESPONSE.id = 1
GET_JOB_RESPONSE.name = "job_name"
GET_JOB_RESPONSE.title = "job name"
CONF_RESPONSE = '{ "hello": "world" }'
GET_JOB_RESPONSE.conf = CONF_RESPONSE


def test_create_job(mocker):
    """testing create_job.py"""
    def _request_post():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: GET_JOB_RESPONSE,
            "raise_for_status": lambda: None
        })

    mocker.patch("requests.Session.post", new=_request_post)
    job = {
        "id": 1,
        "name": "job_name",
        "title": "job name",
        "conf": {
            "hello": "world"
        }
    }
    assert create_job(JOB=job) == GET_JOB_RESPONSE


WEBHOOK_RESPONSE = Dict()
WEBHOOK_RESPONSE.url = (
    'https://webhook.site'
    '/83d6607a-0118-478d-a68c-cf2ab4645314')
WEBHOOK_RESPONSE.method = "POST"
WEBHOOK_RESPONSE.event_type = "JOB_COMPLETE"


def test_create_job_webhook(mocker):
    """testing create_job_webhook.py"""
    def _request_post():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: WEBHOOK_RESPONSE,
            "raise_for_status": lambda: None
        })

    mocker.patch("requests.Session.post", new=_request_post)
    webhook = {
        "url": "https://webhook.site/83d6607a-0118-478d-a68c-cf2ab4645314",
        "method": "POST",
        "event_type": "JOB_COMPLETE"
    }
    assert create_job_webhook(WEBHOOK=webhook) == WEBHOOK_RESPONSE


GET_SQL_JOB_RESPONSE = Dict()
GET_SQL_JOB_RESPONSE.id = 1
GET_SQL_JOB_RESPONSE.name = "sql_job"
GET_SQL_JOB_RESPONSE.title = "sql job"
GET_SQL_JOB_RESPONSE.type = "sql"
GET_SQL_JOB_RESPONSE.tags = "sql"


def test_create_sql_job(mocker):
    """testing create_sql_job.py"""
    def _request_post():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: GET_SQL_JOB_RESPONSE,
            "raise_for_status": None
        })

    mocker.patch("requests.Session.post", new=_request_post)
    sql_job = {
        "name": "sql_job",
        "title": "sql job",
        "type": "sql",
        "tags": [
            "sql"
        ]
    }
    assert create_sql_job(SQL_JOB=sql_job) == GET_CMD_JOB_RESPONSE


TAGS_BODY = {
    "name": "Allow"
}


def test_create_tag(mocker):
    """testing create_tag.py"""
    def _request_post():
        """returning Dict"""
        return Dict({
            "status code": 200,
            "json": lambda: TAGS_BODY,
            "raise_for_status": lambda: None
        })

    mocker.patch("requests.Session.post", new=_request_post)
    tag = {
        "name": "Allow"
    }
    assert create_tag(TAG=tag) == TAGS_BODY


GET_ABOUT_MESSAGES_RESPONSE = Dict()
GET_ABOUT_MESSAGES_RESPONSE.enabled = "false"


def test_get_about_messages(mocker):
    """testing get_about_messages.py"""
    def _request_get():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: GET_ABOUT_MESSAGES_RESPONSE,
            "raise_for_status": lambda: None
        })

    mocker.patch("requests.Session.get", new=_request_get)
    base_url = "https://fake.zuarbase.net"
    api_key = "FAKE_API_KEY"
    about_messages = get_about_messages(BASE_URL=base_url, API_KEY=api_key)
    assert about_messages == GET_ABOUT_MESSAGES_RESPONSE


ABOUT_RESPONSE = Dict()
ABOUT_RESPONSE.version = "2.9.3"
ABOUT_RESPONSE.system.fqdn = "fake.zuarbase.net"


def test_get_about(mocker):
    """testing get_about.py"""
    def _request_get():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: ABOUT_RESPONSE,
            "raise_for_status": lambda: None
        })
    base_url = "https://fake.zuarbase.net"
    api_key = "FAKE_API_KEY"
    mocker.patch("requests.Session.get", new=_request_get)
    assert get_about(BASE_URL=base_url, API_KEY=api_key) == ABOUT_RESPONSE
    assert get_about(BASE_URL=base_url, API_KEY=api_key)["system"]["fqdn"] == "fake.zuarbase.net"  # noqa: E501


GET_JOB_RESPONSE = Dict()
GET_JOB_RESPONSE.id = 1
GET_JOB_RESPONSE.name = "job_name"
GET_JOB_RESPONSE.title = "job name"
CONF_RESPONSE = '{ "hello": "world" }'
GET_JOB_RESPONSE.conf = CONF_RESPONSE


def test_get_conf_info(mocker):
    """testing get_about.py"""
    def _request_get():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: GET_JOB_RESPONSE.conf,
            "raise_for_status": lambda: None
        })
    base_url = "https://fake.zuarbase.net"
    api_key = "FAKE_API_KEY"
    mocker.patch("requests.Session.get", new=_request_get)
    assert get_conf_info(BASE_URL=base_url, API_KEY=api_key) == ABOUT_RESPONSE


GET_CREDENTIALS_RESPONSE = Dict()
GET_CREDENTIALS_RESPONSE.id = 1
GET_CREDENTIALS_RESPONSE.name = "fake name"
GET_CREDENTIALS_RESPONSE.type = "fake"


def test_get_credentials(mocker):
    """testing get_credentials.py"""
    def _request_get():
        """returning Dict"""
        return Dict({
            "status code": 200,
            "json": lambda: GET_CREDENTIALS_RESPONSE,
            "raise_for_status": lambda: None
        })
    mocker.patch("requests.Session.get", new=_request_get)
    base_url = "https://fake.zuarbase.net"
    api_key = "FAKE_API_KEY"
    expected_results = {
        "id": 1,
        "name": "fake name",
        "type": "fake"
    }
    assert get_credentials(BASE_URL=base_url, API_KEY=api_key) == expected_results  # noqa: E501


GET_DATABASES_RESPONSE = Dict()
GET_DATABASES_RESPONSE.name = "fake name"
GET_DATABASES_RESPONSE.size = 10230
GET_DATABASES_RESPONSE.size_hr = "1000 kB"


def test_get_databases(mocker):
    """testing get_databases.py"""
    def _request_get():
        """returning Dict"""
        return Dict({
            "status code": 200,
            "json": lambda: GET_DATABASES_RESPONSE,
            "raise_for_status": lambda: None
        })
    mocker.patch("requests.Session.get", new=_request_get)
    base_url = "https://fake/zuarbase.net"
    api_key = "FAKE_API_KEY"
    expected_results = {
        "name": "fake name",
        "size": 10230,
        "size_hr": "1000 kB"
    }
    assert get_databases(BASE_URL=base_url, API_KEY=api_key) == expected_results  # noqa: E501


GET_BULK_RESPONSE = Dict()
GET_BULK_RESPONSE.name = "fake_name"


def test_get_job_by_name(mocker):
    """testing get_job_by_name.py"""
    def _request_get():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: GET_BULK_RESPONSE,
            "raise_for_status": lambda: None
        })

    mocker.patch("requests.Session.get", new=_request_get)

    base_url = "https://fake.zuarbase.net"
    api_key = "FAKE_API_KEY"

    single_status = get_job_by_name(BASE_URL=base_url, API_KEY=api_key)
    assert single_status == GET_BULK_RESPONSE


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
    """testing get_job_schedule.py"""
    def _request_get():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: GET_JOB_RESPONSE2,
            "raise_for_status": lambda: None
        })

    mocker.patch("requests.Session.get", new=_request_get)

    base_url = "https://fake.zuarbase.net"
    api_key = "FAKE_API_KEY"

    assert get_job_schedule(BASE_URL=base_url, API_KEY=api_key) == GET_JOB_RESPONSE2.schedule  # noqa: E501


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
    """testing get_jobs.py"""
    def _request_post():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: GET_JOBS_RESPONSE,
            "raise_for_status": lambda: None
        })

    mocker.patch("requests.Session.post", new=_request_post)

    base_url = "https://fake.zuarbase.net"
    api_key = "FAKE_API_KEY"

    assert (get_jobs(BASE_URL=base_url, API_KEY=api_key)) == GET_JOBS_RESPONSE["jobs"]  # noqa: E501


GET_METRICS_RESPONSE = Dict()
GET_METRICS_RESPONSE.total_jobs_count = 0
GET_METRICS_RESPONSE.total_runs_count = 0


def test_get_metrics(mocker):
    """testing get_metrics.py"""
    def _request_get():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: GET_METRICS_RESPONSE,
            "raise_for_status": lambda: None
        })

    mocker.patch("requests.Session.get", new=_request_get)
    base_url = "https://fake.zuarbase.net"
    api_key = "FAKE_API_KEY"
    metrics = get_metrics(BASE_URL=base_url, API_KEY=api_key)
    assert metrics == GET_METRICS_RESPONSE


GET_PACKAGE_RESPONSE = Dict()
GET_PACKAGE_RESPONSE.timestamp = "2021-07-05T15:07:26.554979"


def test_get_pkg(mocker):
    """testing get_pkg.py"""
    def _request_get():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: GET_PACKAGE_RESPONSE,
            "raise_for_status": lambda: None
        })

    mocker.patch("requests.Session.get", new=_request_get)
    base_url = "https://fake.zuarbase.net"
    api_key = "FAKE_API_KEY"
    packages = get_pkg(BASE_URL=base_url, API_KEY=api_key)
    assert packages == GET_PACKAGE_RESPONSE


def test_get_single_job(mocker):
    """testing get_single_job.py"""
    def _request_get():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: GET_JOB_RESPONSE,
            "raise_for_status": lambda: None
        })

    mocker.patch("requests.Session.get", new=_request_get)
    base_url = "https://fake.zuarbase.net"
    api_key = "FAKE_API_KEY"

    job = get_single_job(BASE_URL=base_url, API_KEY=api_key)

    expected_results = {
        "id": 1,
        "name": "job_name",
        "title": "job name",
        "conf": {
            "hello": "world"
        }
    }

    assert job == expected_results


GET_STATUS_RESPONSE = Dict()
GET_STATUS_RESPONSE.id = 0


def test_get_single_job_status(mocker):
    """testing get_single_job.py"""
    def _request_get():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: GET_STATUS_RESPONSE,
            "raise_for_status": lambda: None
        })

    mocker.patch("requests.Session.get", new=_request_get)
    base_url = "https://fake.zuarbase.net"
    api_key = "FAKE_API_KEY"
    single_status = get_single_job_status(BASE_URL=base_url, API_KEY=api_key)
    assert single_status == GET_STATUS_RESPONSE


def test_get_single_job_webhook_conf_ifo(mocker):
    """testing get_single_job_webhook_conf_info.py"""
    def _request_get():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: WEBHOOK_RESPONSE,
            "raise_for_status": lambda: None
        })

    mocker.patch("requests.Session.get", new=_request_get)
    base_url = "https://fake.zuarbase.net"
    api_key = "FAKE_API_KEY"
    assert get_single_job_webhook_conf_info(BASE_URL=base_url, API_KEY=api_key) == WEBHOOK_RESPONSE  # noqa: E501


GET_TAGS_RESPONSE = Dict()
GET_TAGS_RESPONSE.id = 1
GET_TAGS_RESPONSE.name = "fake_name"
GET_TAGS_RESPONSE.updated_at = "2021-12-12t12:00:00+00:00"
GET_TAGS_RESPONSE.created_at = "2021-12-12t12:00:00+00:00"


def test_get_tags(mocker):
    """testing get_tags.py"""
    def _request_get():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: GET_TAGS_RESPONSE,
            "raise_for_status": lambda: None
        })
    mocker.patch("requests.Session.get", new=_request_get)
    base_url = "https://fake.zuarbase.net"
    api_key = "FAKE_API_KEY"
    assert get_tags(BASE_URL=base_url, API_KEY=api_key) == GET_TAGS_RESPONSE


def test_get_webhooks(mocker):
    """testing get_webhooks.py"""
    def _request_get():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: WEBHOOK_RESPONSE,
            "raise_for_status": lambda: None
        })

    mocker.patch("requests.Session.get", new=_request_get)
    base_url = "https://fake.zuarbase.net"
    api_key = "FAKE_API_KEY"
    webhooks = get_webhooks(BASE_URL=base_url, API_KEY=api_key)
    assert webhooks == WEBHOOK_RESPONSE


ACTION_RESPONSE = Dict()
ACTION_RESPONSE.id = 345
ACTION_RESPONSE.returncode = None
ACTION_RESPONSE.started_at = "2021-04-19T18:35:10.550109+00:00"


def test_start_job(mocker):
    """testing start_job.py"""
    def _request_post():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: ACTION_RESPONSE,
            "raise_for_status": lambda: None
        })

    mocker.patch("requests.Session.post", new=_request_post)
    base_url = "https://fake.zuarbase.net"
    api_key = "FAKE_API_KEY"
    assert start_job(BASE_URL=base_url, API_KEY=api_key) == ACTION_RESPONSE


def test_update_job_credentials(mocker):
    """testing update_job_credentials.py"""
    def _request_patch():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: GET_JOB_RESPONSE,
            "raise_for_status": lambda: None
        })

    mocker.patch("requests.Session.patch", new=_request_patch)

    base_url = "https://fake.zuarbase.net"
    api_key = "FAKE_API_KEY"

    input_creds = "Fakeforse - fake.fake@zuar.com]"

    assert update_job_credentials(
        BASE_URL=base_url,
        API_KEY=api_key,
        INPUT_CREDS=input_creds
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
    """testing update_job.py"""
    def _request_patch():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: UPDATE_JOB_RESPONSE,
            "raise_for_status": lambda: None
        })

    mocker.patch("requests.Session.patch", new=_request_patch)
    base_url = "https:fake.zuarbase.net"
    api_key = "FAKE_API_KEY"

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
    assert update_job(BASE_URL=base_url, API_KEY=api_key, UPDATE_JOB=UPDATE_JOB_RESPONSE) == UPDATE_JOB_RESPONSE  # noqa: E501


def test_update_job_schedule(mocker):
    """testing update_job_schedule.py"""
    def _request_patch():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: GET_JOB_RESPONSE,
            "raise_for_status": lambda: None
        })

    mocker.patch("requests.Session.patch", new=_request_patch)
    base_url = "https://fake.zuarbase.net"
    api_key = "FAKE_API_KEY"
    schedule = {
        'value': 'never',
        'type': 'never',
        'daily': None,
        'hourly': None,
        'custom': None
    }
    assert update_job_schedule(
        BASE_URL=base_url,
        API_KEY=api_key,
        SCHEDULE=schedule
    ) == GET_JOB_RESPONSE


UPDATE_PKG_RESPONSE = Dict()
UPDATE_PKG_RESPONSE.timestamp = "2021-07-05T15:02:23.012862"


def test_update_pkg(mocker):
    """testing update_pkg.py"""
    def _request_post():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: UPDATE_PKG_RESPONSE,
            "raise_for_status": lambda: None
        })

    mocker.patch("requests.Session.post", new=_request_post)
    base_url = "https://fake.zuarbase.net"
    api_key = "FAKE_API_KEY"
    assert update_pkg(BASE_URL=base_url, API_KEY=api_key) == UPDATE_PKG_RESPONSE  # noqa: E501


CONF_UPDATE_RESPONSE = Dict()
CONF_UPDATE_RESPONSE.dbo = "postrgesql://localhost/fake"


def test_dbo_update_sql_job(mocker):
    """testing dbo_update_sql_job.py"""
    def _request_post():
        """returning Dict"""
        return Dict({
            "status_code": 200,
            "json": lambda: CONF_UPDATE_RESPONSE,
            "raise_for_status": lambda: None
        })

    mocker.patch("requests.Session.post", new=_request_post)
    base_url = "https://fake.zuarbase.net"
    api_key = "FAKE_API_KEY"
    dbo = "postrgesql://localhost/fake"
    assert dbo_update_sql_job(BASE_URL=base_url, API_KEY=api_key, DBO=dbo) == CONF_UPDATE_RESPONSE  # noqa: E501


def test_delete_job(mocker):
    """testing delete_job.py"""
    def _request_delete():
        """returning Dict"""
        return Dict({
            "status_code": 204
        })
    mocker.patch("requests.Session.delete", new=_request_delete)
    base_url = "https://fake.zuarbase.net"
    api_key = "FAKE_API_KEY"
    assert delete_job(BASE_URL=base_url, API_KEY=api_key) == {'status_code': 204}  # noqa: E501


def test_delete_webhook(mocker):
    """testing delete_webhook.py"""
    def _request_delete():
        """returning Dict"""
        return Dict({
            "status_code": 204
        })
    mocker.patch("requests.Session.delete", new=_request_delete)
    base_url = "https://fake.zuarbase.net"
    api_key = "FAKE_API_KEY"
    assert delete_webhook(BASE_URL=base_url, API_KEY=api_key) == {'status_code': 204}  # noqa: E501
