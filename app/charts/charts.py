import base64
import io
import matplotlib.pyplot as plt


def generate_histogram_chart(data):
    """
    Generates a histogram plot from the data provided.
    """

    plt.hist(data, bins=10, color='blue', edgecolor='black')
    plt.title('Berry Data Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    chart_image = generate_image_bytes()
    plt.close()

    return chart_image


def generate_image_bytes():
    """
    Converts the Matplotlib plot to a byte representation.
    """
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image = base64.b64encode(buffer.read()).decode("utf-8")
    return image
