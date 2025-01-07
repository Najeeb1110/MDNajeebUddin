import unittest
from unittest.mock import Mock

# A simple class to demonstrate mocking
class ExternalService:
    def fetch_data(self):
        """Simulate fetching data from an external source."""
        raise NotImplementedError("This method should connect to an external API.")

# Function that uses the ExternalService class
def process_data(service):
    data = service.fetch_data()
    return f"Processed {data}"

# Unit test using mocking
class TestProcessData(unittest.TestCase):
    def test_process_data_with_mock(self):
        # Create a mock object for ExternalService
        mock_service = Mock()
        
        # Define what the mock should return when fetch_data is called
        mock_service.fetch_data.return_value = "mocked data"
        
        # Call the function with the mock
        result = process_data(mock_service)
        
        # Assertions
        self.assertEqual(result, "Processed mocked data")
        mock_service.fetch_data.assert_called_once()  # Ensure fetch_data was called once

# Run the tests
if __name__ == "__main__":
    unittest.main()
