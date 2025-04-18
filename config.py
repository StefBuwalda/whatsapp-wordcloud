from wordcloud import WordCloud  # type: ignore

wordcloud = WordCloud(
    width=1920,
    height=1080,
    background_color="black",  # or 'black', or any HTML color
    colormap="viridis",  # matplotlib colormap ('plasma', 'cool', 'inferno')
    # font_path="path/to/font.ttf",  # Use a custom font
    max_words=100,  # Max number of words to include
    min_font_size=10,
    max_font_size=200,
    prefer_horizontal=1,  # Between 0 (all vertical) and 1 (all horizontal)
    scale=4,  # Higher = better resolution
    contour_color="steelblue",  # Outline color (when using contour_width)
    contour_width=1,  # For consistent layout between runs
)
