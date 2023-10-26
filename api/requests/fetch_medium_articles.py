import logging

import requests
from requests.exceptions import RequestException
from marshmallow import ValidationError

from api.schemas.MediumArticle import MediumArticle

# Initialize logging
logging.basicConfig(level=logging.INFO)

# RSS to JSON conversion endpoint
RSS2JSON_URL = "https://api.rss2json.com/v1/api.json"
RSS_FEED_URL = "https://medium.com/feed/@jhetlage"


def fetch_medium_articles():
    """
    Fetches the latest articles from Medium's RSS feed and converts
    them to JSON.

    Returns:
        dict: A dictionary containing the latest articles from Medium's
        RSS feed in JSON format.
    """
    params = {"rss_url": RSS_FEED_URL}

    try:
        response = requests.get(RSS2JSON_URL, params=params)
        response.raise_for_status()
        return response.json()
    except RequestException as err:
        logging.error(f"Unable to fetch Medium articles: {err}")
        return {}


def validate_articles(data):
    """
    Validates the articles returned by the RSS to JSON conversion endpoint.

    Args:
        data (dict): A dictionary containing the latest articles from Medium's
        RSS feed in JSON format.

    Returns:
        list: A list of validated MediumArticle objects.
    """
    articles = data.get("items", [])
    try:
        validated_articles = MediumArticle(many=True).load(articles)
        return validated_articles
    except ValidationError as err:
        logging.error(f"Validation error: {err.messages}")
        return []


def convert_rss_to_json():
    """
    Fetches the latest Medium articles and converts them to JSON.

    Returns:
        list: A list of validated MediumArticle objects.
    """
    try:
        data = fetch_medium_articles()
        return validate_articles(data)
    except Exception as err:
        logging.error(f"Failed to convert RSS to JSON: {err}")
        return []
