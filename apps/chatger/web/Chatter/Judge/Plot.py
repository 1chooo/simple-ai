import altair as alt
import pandas as pd


def make_plot(*args):
    # source = data.stocks()

    score = [0, 100, 100, 200, 200, 300, 400, 500]
    science_scores = [0, 100, 100, 200, 200, 300, 400, 500]
    times = [1, 2, 3, 4, 5, 6, 7, 8]
    symbol = ["Score", "Score", "Score", "Score", "Score", "Score", "Score", "Score"]
    science_symbols = ["S", "S", "S", "S", "S", "S", "S", "S"]

    # 創建 DataFrame
    data = {
        "score": score,
        "science_score": science_scores,
        "times": times,
        "symbol": symbol,
        "science_symbol": science_symbols,
    }

    source = pd.DataFrame(data)

    highlight = alt.selection(type="single", on="mouseover", fields=["symbol"], nearest=True)

    base = alt.Chart(source).encode(x="times:Q", y="score:Q", color="symbol:N")

    points = (
        base.mark_circle()
        .encode(opacity=alt.value(0))
        .add_selection(highlight)
        .properties(
            # width=300,
            height=200
        )
    )

    lines = base.mark_line().encode(size=alt.condition(~highlight, alt.value(1), alt.value(3)))

    return points + lines
