# tests/test_main.py

from typer.testing import CliRunner
from unittest.mock import patch, MagicMock
import pytest

from engine.main import app, update_local_tags

runner = CliRunner()


@patch("engine.main.save_tags_locally")
@patch("engine.main.download_tags")
def test_update_local_tags(download_tags_mock, save_tags_locally_mock):
    fake_tags = [{"name": "4.4.1-stable"}]
    download_tags_mock.return_value = fake_tags

    update_local_tags()

    download_tags_mock.assert_called_once_with(
        "https://api.github.com/repos/godotengine/godot/tags"
    )
    save_tags_locally_mock.assert_called_once_with(fake_tags)


@patch("engine.main.print_to_user")
@patch("engine.main.load_tags")
@patch("engine.main.update_local_tags")
def test_versions_command(
    update_local_tags_mock,
    load_tags_mock,
    print_to_user_mock
):
    fake_tags = [MagicMock(name="4.4.1-stable")]
    load_tags_mock.return_value = fake_tags

    result = runner.invoke(app, ["versions"])

    assert result.exit_code == 0
    assert "Listing available versions..." in result.stdout
    assert "Available versions to download are:" in result.stdout

    update_local_tags_mock.assert_called_once()
    load_tags_mock.assert_called_once()
    print_to_user_mock.assert_called_once_with(fake_tags)


@patch("engine.main.download_godot_version")
@patch("engine.main.load_tags")
@patch("engine.main.update_local_tags")
def test_download_command_without_tag(
    update_local_tags_mock,
    load_tags_mock,
    download_godot_version_mock
):
    latest_tag = MagicMock()
    latest_tag.name = "4.4.1-stable"

    load_tags_mock.return_value = [latest_tag]

    result = runner.invoke(app, ["download"])

    assert result.exit_code == 0
    assert (
        "No godot version were given for donwload. "
        "Download the latest version: 4.4.1-stable"
    ) in result.stdout

    download_godot_version_mock.assert_called_once_with("4.4.1-stable")


@patch("engine.main.download_godot_version")
@patch("engine.main.tag_exists")
@patch("engine.main.load_tags")
@patch("engine.main.update_local_tags")
def test_download_command_with_valid_tag(
    update_local_tags_mock,
    load_tags_mock,
    tag_exists_mock,
    download_godot_version_mock
):
    tag_exists_mock.return_value = True

    result = runner.invoke(
        app,
        ["download", "--tag", "4.4.1-stable"]
    )

    assert result.exit_code == 0

    tag_exists_mock.assert_called_once_with("4.4.1-stable")
    download_godot_version_mock.assert_called_once_with("4.4.1-stable")


@patch("engine.main.tag_exists")
@patch("engine.main.load_tags")
@patch("engine.main.update_local_tags")
def test_download_command_with_invalid_tag(
    update_local_tags_mock,
    load_tags_mock,
    tag_exists_mock
):
    tag_exists_mock.return_value = False

    result = runner.invoke(
        app,
        ["download", "--tag", "invalid-tag"]
    )

    assert result.exit_code == 1
    assert "Tag does not exists." in result.stdout

    tag_exists_mock.assert_called_once_with("invalid-tag")