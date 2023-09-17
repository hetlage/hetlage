import sys
from datetime import datetime

from jinja2 import Environment, FileSystemLoader

from api.requests.fetch_medium_articles import convert_rss_to_json

def main(): 
    # Get the current timestamp in UTC and format it
    updated_at = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Articles data
    articles_data = convert_rss_to_json()

    weather_data = [
        {"date": "2023-09-15", "forecast": "Sunny"},
        {"date": "2023-09-16", "forecast": "Cloudy"}
    ]

    # Interests
    interests = {  
        "trading": "### Trading"
    }

    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('README.md.j2')

    # Render and merge templates
    rendered_readme = template.render(articles=articles_data, weathers=weather_data, interests=interests, updated_at=updated_at)

    # Save to README.md
    with open("README.md", "w") as f:
        f.write(rendered_readme)


if __name__ == "__main__":
    main()