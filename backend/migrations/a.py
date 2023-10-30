import orjson
import translators as ts

tags = set()

with open("animeSeries.json", "rb") as f:
    animeseries = orjson.loads(f.read())["data"]

    for anime in animeseries:
        for tag in anime["tags"]:
            tags.add(tag)

print("\n".join(tags))

# for tag in tags:
#     translated_tag = ts.translate_text(tag, translator="google", to_language="pl")
#     print(translated_tag)
