import json
from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

async def extract_matches(year: str, event_code: str, match_type: str):

    # Define the extraction schema
    schema = {
        "name": "Qualification Matches",
        "baseSelector": "tr[role=\"row\"]",
        "fields": [
            {
                "name": "match type",
                "selector": "td.col-2>a",
                "type": "text",
            },
            {
                "name": "match number",
                "selector": "td.col-2>a",
                "type": "text",
            },
            {
                "name": "red 1",
                "selector": "td.danger[id*=\"team4\"]>a",
                "type": "text",
            },
            {
                "name": "red 2",
                "selector": "td.danger[id*=\"team5\"]>a",
                "type": "text",
            },
            {
                "name": "red 3",
                "selector": "td.danger[id*=\"team6\"]>a",
                "type": "text",
            },
            {
                "name": "blue 1",
                "selector": "td.info[id*=\"team1\"]>a",
                "type": "text",
            },
            {
                "name": "blue 2",
                "selector": "td.info[id*=\"team2\"]>a",
                "type": "text",
            },
            {
                "name": "blue 3",
                "selector": "td.info[id*=\"team3\"]>a",
                "type": "text",
            },
            {
                "name": "red score",
                "selector": "td.text-danger",
                "type": "text",
            },
            {
                "name": "blue score",
                "selector": "td.text-primary",
                "type": "text",
            },
        ],
    }

    print("\n--- Extracting", match_type, "Matches for", year, event_code, " --- \n")

    # Create the extraction strategy
    extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)

    # Generate url and savefile
    url="https://frc-events.firstinspires.org/" + year + "/" + event_code + "/" + match_type
    filename = year + event_code + match_type + ".json"
    file = "./json/" + filename

    # Use the AsyncWebCrawler with the extraction strategy
    async with AsyncWebCrawler(verbose=False) as crawler:
        result = await crawler.arun(
            url=url,
            extraction_strategy=extraction_strategy,
            bypass_cache=True,
        )

        assert result.success, "Failed"

        # Print Number of Matches Extracted
        matches = json.loads(result.extracted_content)
        print(f"\n--- Successfully extracted {len(matches)} Matches ---")

        # Parse out the type and number since they used the same CSS input
        for item in matches:
            item['match type'] = item['match type'].split(" ")[0]
            item['match number'] = item['match number'].split(" ")[1]

        # Save to File
        with open(file, "w") as outfile:
            json.dump(matches, outfile)

        print(f"--- Saved to file {filename} ---\n")

