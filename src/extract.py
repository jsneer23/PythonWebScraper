import json
from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

from schema import QUAL
from schema import ELIM

async def extract_matches(year: str, event_code: str, match_type: str):

    print("\n--- Extracting", match_type, "Matches for", year, event_code, " --- \n")

    # Select Schema
    schema = QUAL
    if match_type != "Qualifications":
        schema = ELIM

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

