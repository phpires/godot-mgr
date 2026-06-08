# tests/test_main.py

from typer.testing import CliRunner
from unittest.mock import patch, MagicMock
import pytest
import unittest

from src.main import app, update_local_tags

runner = CliRunner()

class TestMain(unittest.TestCase):

    @patch("src.main.download_tags")
    @patch("src.main.save_tags_locally")
    def test_update_local_tags(save_tags_locally_mock, download_tags_mock):
        fake_tags = ['''{
    GodotRemoteTags(name=4.6.3-stable, zipball_url=https://api.github.com/repos/godotengine/godot/zipball/refs/tags/4.6.3-stable, tarball_url=https://api.github.com/repos/godotengine/godot/tarball/refs/tags/4.6.3-stable, commit_sha=35e80b3a8822a9df9be390814b62f44c0a9c69e8, node_id=MDM6UmVmMTU2MzQ5ODE6cmVmcy90YWdzLzQuNi4zLXN0YWJsZQ==)
    }''']
        fake_url = "https://api.github.com/repos/godotengine/godot/tags"
        download_tags_mock.return_value = fake_tags

        update_local_tags()

        download_tags_mock.assert_called_once_with(fake_url)
        save_tags_locally_mock.assert_called_once_with(fake_tags)

    @patch("src.main.update_local_tags")
    @patch("src.main.print_to_user")
    @patch("src.main.load_tags")
    @patch("src.main.save_tags_locally")
    def test_versions_command(
        save_tags_locally_mock,
        load_tags_mock,
        print_to_user_mock,
        update_local_tags_mock
    ):
        fake_tags = [MagicMock(name="4.4.1-stable")]
        load_tags_mock.return_value = fake_tags

        result = runner.invoke(app, ["versions"])

        assert result.exit_code == 0
        assert "Listing available versions..." in result.stdout
        assert "Available versions to download are:" in result.stdout

        load_tags_mock.assert_called_once()
        print_to_user_mock.assert_called_once_with(fake_tags)

    @patch("src.main.update_local_tags")
    @patch("src.main.load_tags")
    @patch("src.main.download_godot_version")
    def test_download_command_without_tag(
        download_godot_version_mock,
        load_tags_mock,
        update_local_tags_mock
    ):
        latest_tag = MagicMock()
        latest_tag.name = "4.4.1-stable" 
        load_tags_mock.return_value = [latest_tag]

        result = runner.invoke(app, ["download"])

        assert result.exit_code == 0
        assert (
            f"No godot version were given for donwload. Download the latest version: {latest_tag.name}"
        ) in result.stdout

        download_godot_version_mock.assert_called_once_with("4.4.1-stable")

    @patch("src.main.update_local_tags")
    @patch("src.main.save_tags_locally")
    @patch("src.main.tag_exists")
    @patch("src.main.load_tags")
    @patch("src.main.download_godot_version")
    def test_download_command_with_valid_tag(
        download_godot_version_mock,
        load_tags_mock,
        tag_exists_mock,
        save_tags_locally_mock,
        update_local_tags_mock
    ):
        latest_tag = MagicMock()
        latest_tag.name = "4.4.1-stable" 
        load_tags_mock.return_value = [latest_tag]

        tag_exists_mock.return_value = True

        result = runner.invoke(
            app,
            ["download", "--tag", "4.4.1-stable"]
        )

        assert result.exit_code == 0

        tag_exists_mock.assert_called_once_with("4.4.1-stable")
        download_godot_version_mock.assert_called_once_with("4.4.1-stable")
        load_tags_mock.assert_called_once_with()


    @patch("src.main.update_local_tags")
    @patch("src.main.save_tags_locally")
    @patch("src.main.load_tags")
    @patch("src.main.tag_exists")
    def test_download_command_with_invalid_tag(
        tag_exists_mock,
        load_tags_mock,
        save_tags_locally_mock,
        update_local_tags_mock,
    ):
        load_tags_mock.return_value = None
        tag_exists_mock.return_value = False

        result = runner.invoke(app, ["download", "--tag", "invalid-tag"])

        assert result.exit_code == 1
        tag_exists_mock.assert_called_once_with("invalid-tag")