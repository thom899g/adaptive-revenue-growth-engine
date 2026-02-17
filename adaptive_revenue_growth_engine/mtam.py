import logging
from typing import Dict, Any
import requests

class MarketTrendAnalyzer:
    """
    Analyzes market trends from external data sources.
    Implements error handling and logging for robust operation.
    """

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.logger = logging.getLogger(__name__)

    def fetch_market_data(self, endpoint: str) -> Dict[str, Any]:
        """
        Fetches market data from a specified API endpoint.
        Includes error handling and logging for reliability.
        """
        try:
            response = requests.get(endpoint, headers={'Authorization': f'Bearer {self.api_key}'})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to fetch market data from {endpoint}. Error: {str(e)}")
            raise

    def process_trends(self, data: Dict[str, Any]) -> Dict[str, float]:
        """
        Processes raw market data to extract relevant trends.
        Implements type hints for clarity and robustness.
        """
        processed_data = {}
        try:
            # Example processing: extracting average growth rate
            if 'growth_rates' in data:
                processed_data['average_growth'] = sum(data['growth_rates']) / len(data['growth_rates'])
            else:
                self.logger.warning("No growth rates found in market data.")
                processed_data['average_growth'] = 0.0
        except KeyError as e:
            self.logger.error(f"Key {e} not found in market data.")
            raise

        return processed_data