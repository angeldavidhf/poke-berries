from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.redis.redis_client import check_berry_stats, set_berry_stats, save_berry_stats
from app.charts.charts import generate_histogram_chart
from app.api.external_api import call_external_api

router = APIRouter()


@router.get("/allBerryStats")
async def get_berry_stats():
    """
    """
    berry_stats = check_berry_stats()

    if berry_stats:
        return {"message": "Berry data retrieved from Redis", "stats": berry_stats}
    else:
        new_berry_data = call_external_api()
        stats = set_berry_stats(new_berry_data)
        save_berry_stats(stats)

        return {"message": "Berry data retrieved from external API and stored in Redis", "stats": stats}


@router.get("/berryHistogram")
async def get_berry_histogram():
    """
    """
    berry_stats = check_berry_stats()

    if berry_stats:
        chart = generate_histogram_chart(berry_stats)
        return {"message": "Berry data retrieved from Redis", "chart": chart}
    else:
        new_berry_data = call_external_api()

        stats = set_berry_stats(new_berry_data)
        save_berry_stats(stats)
        chart_image = generate_histogram_chart(stats)

        # return {"message": "Berry data retrieved from external API and stored in Redis", "chart": chart}

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
