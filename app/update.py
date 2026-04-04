import zoneinfo

import jinja2
from datetime import datetime
from pathlib import Path

wd = Path(__file__).parent
docs = Path("/docs")
docs.mkdir(parents=True, exist_ok=True)

# Load template
env = jinja2.Environment(loader=jinja2.FileSystemLoader(wd / "templates"))
template = env.get_template("index.jinja")

# Get current date and time
current_dt = datetime.now(tz=zoneinfo.ZoneInfo("Europe/Amsterdam")).strftime("%Y-%m-%d %H:%M:%S")

# Render
output = template.render(current_date_time=current_dt)

# Write to docs/index.html
with open(docs / "index.html", "w") as f:
    f.write(output)
