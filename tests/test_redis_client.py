from app.redis.redis_client import set_berry_stats, save_berry_stats, check_berry_stats
from fakeredis import FakeStrictRedis

fake_redis = FakeStrictRedis()


def test_set_berry_stats():
    example_data = [
        {
            "growth_time": 3,
            "id": 1,
            "name": "cheri",
            "max_harvest": 5,
            "size": 20,
            "smoothness": 25,
            "soil_dryness": 15,
            "natural_gift_power": 60
        },
        {
            "growth_time": 4,
            "id": 2,
            "name": "chesto",
            "max_harvest": 5,
            "size": 80,
            "smoothness": 25,
            "soil_dryness": 15,
            "natural_gift_power": 60
        },
    ]

    berry_stats = set_berry_stats(example_data)

    assert isinstance(berry_stats, dict)
    assert "berries_names" in berry_stats
    assert "min_growth_time" in berry_stats
    assert "median_growth_time" in berry_stats
    assert "max_growth_time" in berry_stats
    assert "variance_growth_time" in berry_stats
    assert "mean_growth_time" in berry_stats
    assert "frequency_growth_time" in berry_stats

    assert isinstance(berry_stats["berries_names"], list)
    assert isinstance(berry_stats["min_growth_time"], int)
    assert isinstance(berry_stats["median_growth_time"], float)
    assert isinstance(berry_stats["max_growth_time"], int)
    assert isinstance(berry_stats["variance_growth_time"], float)
    assert isinstance(berry_stats["mean_growth_time"], float)
    assert isinstance(berry_stats["frequency_growth_time"], dict)

    fake_redis.flushall()
