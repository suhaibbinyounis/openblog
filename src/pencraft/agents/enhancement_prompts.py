"""Enhancement prompts for improving existing blog posts."""

from __future__ import annotations

# Prompt to analyze an existing blog post for improvement opportunities
CONTENT_ANALYSIS_PROMPT = """Analyze this existing blog post and identify improvement opportunities.

**Blog Title:** {title}
**Current Word Count:** {word_count}
**Target Word Count:** {target_word_count}

**Current Content:**
{content}

**Google Trends Data (if available):**
{trends_data}

Provide a structured analysis in the following format:

## SEO Analysis
- Meta description quality (1-10)
- Heading structure issues
- Missing keywords that should be included
- Title optimization suggestions

## Content Analysis
- Sections that are too short/thin (list section names and current word counts)
- Areas lacking depth or examples
- Missing topics that should be covered based on trends data
- Factual claims that need citations

## Quality Issues
- Grammar/spelling errors (list specific issues)
- Awkward phrasing or unclear sentences
- LLM artifacts to remove (meta-commentary, "In conclusion", etc.)
- Repetitive content

## Frontmatter Issues
- Missing required fields
- Formatting problems
- Incorrect date format

## AdSense Optimization
- Opportunities to naturally include high-CPC terms (Enterprise, Production, API, etc.)
- Sections suitable for monetization hooks

Be specific and actionable. Focus on the most impactful improvements."""

# Prompt to enhance/rewrite blog content
CONTENT_ENHANCEMENT_PROMPT = """You are enhancing an existing blog post to improve its quality, SEO, and reader engagement.

**Original Blog:**
{original_content}

**Analysis Results:**
{analysis_results}

**Google Trends Data:**
{trends_data}

**Enhancement Requirements:**
- Target word count: {target_word_count} (current: {current_word_count})
- Naturally integrate these trending keywords: {trending_keywords}
- Address these specific issues: {specific_issues}
- Maintain the author's voice and existing good content
- Preserve all working code examples and improve them if needed

**High-CPC Keywords to Integrate Naturally:**
- Enterprise, Production, API, Architecture
- Cost analysis, Pricing, ROI
- Security, Compliance, Scalability
- Implementation, Integration, Deployment

**Style Guidelines:**
1. Start directly with value - no "In today's digital world" or similar fluff
2. Use "we" and "I" for a personal, authoritative tone
3. Include specific numbers, benchmarks, or data where possible
4. Break up long paragraphs (max 3-4 sentences)
5. Use subheadings (H2, H3) to improve scannability
6. Include code examples with proper formatting
7. End sections with actionable takeaways

**Output Format:**
Return ONLY the enhanced blog content in Markdown format.
- Do NOT include frontmatter (it will be handled separately)
- Do NOT include the title as an H1 (it's in frontmatter)
- Start directly with the introduction
- Preserve existing good content while expanding thin sections
- Fix all grammar and style issues identified
- Remove any LLM artifacts or meta-commentary"""

# Prompt to generate/improve meta description
META_DESCRIPTION_PROMPT = """Generate an SEO-optimized meta description for this blog post.

**Title:** {title}
**Content Summary:** {content_summary}
**Primary Keywords:** {keywords}

Requirements:
- 150-160 characters maximum
- Include primary keyword near the beginning
- Be compelling and encourage clicks
- No quotes or special characters that break HTML

Return ONLY the meta description text, nothing else."""

# Prompt to suggest improved tags/categories
TAGS_SUGGESTION_PROMPT = """Suggest optimized tags and categories for this blog post.

**Title:** {title}
**Content Topics:** {topics}
**Google Trends Rising Keywords:** {rising_keywords}
**Current Tags:** {current_tags}
**Current Categories:** {current_categories}

Return a JSON object with:
{{
    "tags": ["tag1", "tag2", ...],  // 5-8 tags, kebab-case
    "categories": ["Category1", "Category2"]  // 1-3 categories
}}

Focus on:
- High-search-volume terms
- Specific technical terms (not generic like "technology")
- Rising/trending keywords from Google Trends
- Keep existing good tags"""
