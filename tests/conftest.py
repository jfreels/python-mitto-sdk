import os
import shutil

from pathlib import Path
import pytest


@pytest.fixture(scope="session")
def test_bulk_job():
    path = os.path.join(os.path.dirname(__file__), "data", "create_bulk_job.json")  # noqa: E501
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_create_cmd_job():
    path = os.path.join(os.path.dirname(__file__), "data", "create_cmd_job.json")  # noqa: E501
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_create_credentials():
    path = os.path.join(os.path.dirname(__file__), "data", "create_credentials.json")  # noqa: E501
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_create_job():
    path = os.path.join(os.path.dirname(__file__), "data", "create_job.json")
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_create_job_webhook(test_create_job):
    path = os.path.join(os.path.dirname(__file__), "data", "create_job_webhook.json")  # noqa: E501
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_sql_job_fixture():
    path = os.path.join(os.path.dirname(__file__), "data", "sql_job.json")  # noqa: E501
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_create_tag():
    path = os.path.join(os.path.dirname(__file__), "data", "create_tag.json")
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_get_about():
    path = os.path.join(os.path.dirname(__file__), "data", "get_about.json")
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_get_about_messages():
    path = os.path.join(os.path.dirname(__file__), "data", "get_about_messages.json")  # noqa: E501
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_get_conf_info(test_create_job):
    path = os.path.join(os.path.dirname(__file__), "data", "get_conf_info.json")  # noqa: E501
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_get_credentials(test_create_credentials):
    path = os.path.join(os.path.dirname(__file__), "data", "get_credentials.json")  # noqa: E501
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_get_databases():
    path = os.path.join(os.path.dirname(__file__), "data", "get_databases.json")  # noqa: E501
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_get_job_by_name(test_create_bulk_job):
    path = os.path.join(os.path.dirname(__file__), "data", "get_job_by_name.json")  # noqa: E501
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_get_job(test_create_job):
    path = os.path.join(os.path.dirname(__file__), "data", "get_job.json")
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_get_jobs(test_create_job):
    path = os.path.join(os.path.dirname(__file__), "data", "get_jobs.json")
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_get_metrics():
    path = os.path.join(os.path.dirname(__file__), "data", "get_metrics.json")
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_get_pkg():
    path = os.path.join(os.path.dirname(__file__), "data", "get_pkg.json")
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_get_single_job_status(test_create_job, test_start_job):
    path = os.path.join(os.path.dirname(__file__), "data", "get_single_job_status.json")  # noqa: E501
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_get_single_job_webhook_conf_info(test_create_job_webhook):
    path = os.path.join(os.path.dirname(__file__), "data", "get_single_job_webhook_conf_info.json")  # noqa: E501
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_get_tags():
    path = os.path.join(os.path.dirname(__file__), "data", "get_tags.json")
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_get_webhooks(test_create_job_webhook):
    path = os.path.join(os.path.dirname(__file__), "data", "get_webhooks.json")
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_start_job(test_create_job):
    path = os.path.join(os.path.dirname(__file__), "data", "start_job.json")
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_update_job_credentials(test_create_job):
    path = os.path.join(os.path.dirname(__file__), "data", "update_job_credentials.json")  # noqa: E501
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_update_job(test_create_job):
    path = os.path.join(os.path.dirname(__file__), "data", "update_job.json")
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_update_job_schedule(test_get_job_schedule):
    path = os.path.join(os.path.dirname(__file__), "data", "update_job_schedule.json")  # noqa: E501
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_update_pkg():
    path = os.path.join(os.path.dirname(__file__), "data", "update_pkg.json")
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_delete_job(test_create_job):
    path = os.path.join(os.path.dirname(__file__), "data", "delete_job.json")
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_delete_job_webhook(test_create_job, test_create_job_webhook):
    path = os.path.join(os.path.dirname(__file__), "data", "delete_job_webhook.json")  # noqa: E501
    return os.path.abspath(path)


@pytest.fixture(scope="session")
def test_dbo_update_sql_job(test_create_sql_job):
    path = os.path.join(os.path.dirname(__file__), "data", "dbo_update_sql_job.json")  # noqa: E501
    return os.path.abspath(path)
