from datetime import datetime

from jinja2 import Environment, FileSystemLoader

# Get the current timestamp in UTC and format it
updated_at = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

# Sample data (in a real-world scenario, you'd fetch this dynamically)
articles_data = [
    {"title": "My First Blog Post", "url": "https://myblog.com/first-post"},
    {"title": "Understanding Jinja2", "url": "https://myblog.com/jinja2"}
]

weather_data = [
    {"date": "2023-09-15", "forecast": "Sunny"},
    {"date": "2023-09-16", "forecast": "Cloudy"}
]

# Interests
interests = {  
    "trading": "## Trading"
}

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('README.md.j2')

# Render and merge templates
rendered_readme = template.render(articles=articles_data, weathers=weather_data, interests=interests, updated_at=updated_at)

# Save to README.md
with open("README.md", "w") as f:
    f.write(rendered_readme)
