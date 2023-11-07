import base64
import io
import matplotlib.pyplot as plt


def generate_histogram_chart(data):
    """
    Generates a histogram plot from the provided data.

    Args:
        data (dict): A dictionary containing data for generating the histogram.

    Returns:
        str: A base64-encoded image of the histogram plot.
    """
    growth_times = list(data["frequency_growth_time"].keys())
    frequencies = list(data["frequency_growth_time"].values())

    plt.bar(growth_times, frequencies, align='center', alpha=0.5)
    plt.xlabel("Growth Time")
    plt.ylabel("Frequency")
    plt.title('Berry Growth Time Histogram')

    chart_image = generate_image_bytes()
    plt.close()

    return chart_image


def generate_image_bytes():
    """
    Converts the Matplotlib plot to a byte representation and returns it as a base64-encoded string.

    Returns:
        str: A base64-encoded image of the Matplotlib plot.
    """
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image = base64.b64encode(buffer.read()).decode("utf-8")
    return image
