import unicodedata

TEXT1 = (
    "Denominada en Euskera como Donostia, está "
    "situada en el Golfo de Vizcaya en la provincia "
    "de Guipúzcoa. San Sebastián no es solo conocida "
    "por su afamado festival de cine, sino también "
    "por la belleza de sus calles, las cuales tienen "
    "un corte francés y aburguesado que atraen cada "
    "año a centenares de turistas."
)


def filter_accents(text):
    """Return a sequence of accented characters found in
    the passed in lowercased text string
    """

    text = unicodedata.normalize("NFKC", text).lower()
    # Completely kludgy solution later in this comment
    # This article explains Unicode decomposition
    # https://towardsdatascience.com/what-on-earth-is-unicode-normalization-56c005c55ad0
    #
    # return list({c for c in text if "WITH" in unicodedata.name(c)})
    return {c for c in text if unicodedata.decomposition(c)}


if __name__ == "__main__":
    print(filter_accents(TEXT1))
