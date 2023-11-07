import fastapi
from fastapi.responses import HTMLResponse
from app.redis.redis_client import check_berry_stats, set_berry_stats, save_berry_stats
from app.charts.charts import generate_histogram_chart
from app.api.external_api import call_external_api

router = fastapi.APIRouter()


@router.get('/allBerryStats')
async def get_berry_stats():
    """
    Gets the statistics of the berries.

    If berry statistics are available in Redis, retrieves them.
    If they are not available in Redis, it queries an external API, stores the statistics in Redis
    and returns them.

    Returns:
        dict: A dictionary containing a message and the berry statistics.
    """
    berry_stats = check_berry_stats()

    if berry_stats:
        return {"message": "Berry data retrieved from Redis", "stats": berry_stats}
    else:
        new_berry_data = call_external_api()
        stats = set_berry_stats(new_berry_data)
        save_berry_stats(stats)

        return {"message": "Berry data retrieved from external API and stored in Redis", "stats": stats}


@router.get('/berryHistogram')
async def get_berry_histogram():
    """
    Gets a histogram plot of the berry statistics.

    If berry statistics are available in Redis, generates a histogram plot from that data.
    If they are not available in Redis, queries an external API, stores the statistics in Redis, generates a histogram
    plot and displays it in Redis.

    histogram chart and displays it in an HTML page.

    Returns:
        HTMLResponse: An HTML response that displays the histogram plot of the berry statistics.
    """
    berry_stats = check_berry_stats()

    if berry_stats:
        chart_image = generate_histogram_chart(berry_stats)
    else:
        new_berry_data = call_external_api()

        stats = set_berry_stats(new_berry_data)
        save_berry_stats(stats)
        chart_image = generate_histogram_chart(stats)

    html_content = f"""
        <!html>
        <head>
            <title>Berry Histogram</title>
        </head>
        <body>
            <h1>Berry Histogram</h1>
            <img src="data:image/png;base64,{chart_image}" alt="Berry Histogram">
        </body>
        </html>
        """

    return HTMLResponse(content=html_content)
