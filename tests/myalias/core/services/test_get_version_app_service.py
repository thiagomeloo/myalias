import pytest

from myalias.core.services.get_version_app_service import GetVersionAppService


@pytest.fixture
def get_version_app_service():
    return GetVersionAppService().execute()


def test_check_version(get_version_app_service):

    # Act
    version = get_version_app_service.split('.')

    # Assert
    assert len(version) == 3
    assert version[0].isdigit()
    assert version[1].isdigit()
    assert version[2].isdigit()
