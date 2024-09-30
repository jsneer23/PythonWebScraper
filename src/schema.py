QUAL = {
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

ELIM = {}