from datetime import datetime

from jinja2 import Environment, FileSystemLoader

from api.requests.fetch_medium_articles import convert_rss_to_json
from api.requests.fetch_weather_data import convert_weather_data_to_dict


# Your personal information in a dictionary
personal_info = {
    "name": "John Hetlage",  # 'Your Name'
    "job_title": "Full Stack Developer",  # 'Your Job Title'
    "city": "Kansas City",  # 'Your City
    "state": "MO",  # 'Your State Abbreviation'
    "twitter_handle": "j_hetlage",  # 'YourTwitterHandle',
    "linkedin_username": "john-hetlage",  # 'YourLinkedInUsername',
    "medium_username": "jhetlage",  # 'YourMediumUsername',
    "passions": ["Open Source", "Sustainable Tech", "AI Ethics"],
    "interests": ["Running", "Trading", "Writing"],
    "tech_stack": ["Python", "JavaScript", "React"],
}


def main():
    # Get the current timestamp in UTC and format it
    updated_at = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Articles data
    articles_data = convert_rss_to_json()

    # Weather data
    weather_data = convert_weather_data_to_dict()
    location, current, forecast, alerts = (
        weather_data.get("location", {}),
        weather_data.get("current", {}),
        weather_data.get("forecast", {}),
        weather_data.get("alerts", {}),
    )

    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("README.md.j2")

    # Render and merge templates
    rendered_readme = template.render(
        articles=articles_data,
        location=location,
        current=current,
        forecast=forecast,
        alerts=alerts,
        updated_at=updated_at,
        personal_info=personal_info,
    )

    # Save to README.md
    with open("README.md", "w") as f:
        f.write(rendered_readme)


if __name__ == "__main__":
    main()
