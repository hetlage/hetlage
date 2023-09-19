import requests
from marshmallow import ValidationError

from api.schemas.MediumArticle import MediumArticle

# RSS to JSON conversion endpoint
RSS2JSON_URL = "https://api.rss2json.com/v1/api.json"
RSS_FEED_URL = "https://medium.com/feed/@jhetlage"


def fetch_medium_articles():
    """
    Fetches the latest articles from Medium's RSS feed and converts them to JSON.
    """
    params = {"rss_url": RSS_FEED_URL}

    response = requests.get(RSS2JSON_URL, params=params)

    if response.status_code != 200:
        raise Exception("Unable to fetch Medium articles.")

    return response.json()


def validate_articles(data):
    """
    Validates the articles returned by the RSS to JSON conversion endpoint.
    """
    articles = data.get("items", [])

    results = []
    for article in articles:
        try:
            validated_article = MediumArticle().load(article)
            results.append(validated_article)
        except ValidationError as err:
            print(err.messages)

    return results


def convert_rss_to_json():
    """
    Fetches the latest Medium articles and converts them to JSON.
    """
    data = fetch_medium_articles()
    return validate_articles(data)
