import instructor
import anthropic
from src.schema import JobPosting

client = instructor.from_provider(
    "anthropic/claude-haiku-4-5-20251001",
    mode=instructor.Mode.ANTHROPIC_TOOLS
)

def extract_job_posting(raw_text: str) -> JobPosting:
    return client.chat.completions.create(
                response_model=JobPosting,
        messages=[
            {
                "role": "user",
                "content": f"""Extract structured information from this job posting.

                                Job posting:
                                {raw_text}

                                Extract all available fields. If a field is not mentioned, leave it as None."""
            }
        ]
    )
    