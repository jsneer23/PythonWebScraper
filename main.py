from src.extract import extract_matches
import asyncio

# Type desired event info here
year = "2024"
event_code = "CASF"
match_type = "Qualifications" #Playoffs not yet supported

# Extract Matches
asyncio.run(extract_matches(year, event_code, match_type))