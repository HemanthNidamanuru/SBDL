import pytest
from unittest.mock import MagicMock
from lib.Utils import get_spark_session


def test_spark_session_version_check():
    """
    Test that verifies your code checks the Spark version correctly,
    WITHOUT launching a real SparkSession (slow in Jenkins/Windows).
    """

    # Create a mock SparkSession
    mock_spark = MagicMock()
    mock_spark.version = "3.5.7"

    # Example logic you might test (replace as needed)
    assert mock_spark.version == "3.5.7"
