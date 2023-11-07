import matplotlib.pyplot as plt
from app.charts.charts import generate_image_bytes


def test_generate_image_bytes():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

    image = generate_image_bytes()
    assert isinstance(image, str)
    assert len(image) > 0
