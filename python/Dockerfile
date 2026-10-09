# Start from the image of the python container
FROM astral/uv:python3.14-trixie-slim
 
# Install Linux programs
RUN apt-get update && apt-get install -y \
    git \
    cron
 
# Install Python packages
RUN uv pip install --system \
    pandas \
    "psycopg[binary]" \
    sqlalchemy \
    statsmodels
