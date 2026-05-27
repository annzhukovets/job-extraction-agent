# job-extraction-agent

Extracts structured data from raw job posting text using Claude and [Instructor](https://python.useinstructor.com/).

## What it does

Parses unstructured job descriptions and returns a typed `JobPosting` object with fields like title, company, location, salary range, work arrangement, required skills, and benefits.

## Tech stack

- **Claude Haiku** (`claude-haiku-4-5`) — LLM for extraction
- **Instructor** — structured output enforcement via tool use
- **Pydantic** — schema definition and validation

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install anthropic instructor pydantic
```

Set your Anthropic API key:

```bash
export ANTHROPIC_API_KEY=your_key_here
```

## Usage

```python
from src.extractor import extract_job_posting

raw = """
Senior ML Engineer at Acme Corp
Location: Amsterdam, Netherlands (Hybrid)
Salary: €80,000 - €110,000
...
"""

job = extract_job_posting(raw)
print(job.model_dump_json(indent=2))
```

Or run the manual test:

```bash
python test_manual.py
```

## Schema

| Field | Type | Notes |
|---|---|---|
| `title` | `str` | Job title |
| `company` | `str` | Company name |
| `location` | `str` | Office location |
| `work_arrangement` | `remote \| hybrid \| onsite` | Work model |
| `salary_min` | `int?` | Minimum salary |
| `salary_max` | `int?` | Maximum salary |
| `employment_type` | `int?` | Employment type |
| `years_experience_min` | `int?` | Minimum years of experience |
| `seniority_level` | `str?` | e.g. Senior, Mid, Junior |
| `requirements` | `list[str]` | Must-have requirements |
| `skills` | `list[str]` | Technical skills |
| `benefits` | `list[str]?` | Perks and benefits |
