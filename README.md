# GEO Web Crawler

A modular web crawler designed to extract content

## Features

- **JavaScript Execution**: Full JavaScript rendering with crawl4ai
- **Structured Data Extraction**: Schema.org, OpenGraph, Twitter Cards
- **GEO Data Normalization**: Specialized extraction for geo content
- **Meta Data Parsing**: Title, description, canonical URLs, language info
- **Link & Image Analysis**: Internal/external link classification
- **DOM Diff Analysis**: Track JavaScript-induced changes
- **Content Statistics**: Word count, link analysis, image metrics

## Architecture

The crawler follows a modular architecture with single responsibilities:

- **`core_crawler.py`**: Web crawling and JavaScript execution
- **`html_parser.py`**: HTML parsing and structured data extraction  
- **`data_normalizer.py`**: Normalize structured data for GEO models
- **`output_handler.py`**: Format and save output data
- **`utils.py`**: Utility functions

## Installation

```bash
pip install crawl4ai aiohttp beautifulsoup4
```

## Usage

### Simple API Usage

```python
from geo.crawler import crawl_url

# Crawl a single URL and get JSON output
result = await crawl_url("https://example.com")
print(result["meta"]["title"])
print(result["structured_data_normalized"]["geo"])
```

### Command Line Usage

```bash
# Interactive mode
python -m geo.crawler.modular_geo_crawler

# Command line argument
python -m geo.crawler.modular_geo_crawler https://example.com
```

### Advanced Usage

```python
from geo.crawler import GEOCrawlerOrchestrator

orchestrator = GEOCrawlerOrchestrator()
output_data = await orchestrator.crawl_url("https://example.com")

# Access different data types
print(output_data["clean_text"])  # LLM-ready text
print(output_data["structured_data"])  # Raw structured data
print(output_data["structured_data_normalized"])  # GEO-optimized data
print(output_data["meta"])  # Meta tags
print(output_data["links"])  # All links found
print(output_data["images"])  # All images found
```

## Output Format

The crawler outputs comprehensive JSON data including:

- **Raw Content**: Original HTML, rendered HTML, clean text
- **Structured Data**: Schema.org, microdata extraction
- **Normalized Data**: GEO-optimized structured data
- **Meta Data**: Title, description, OpenGraph, Twitter cards
- **Links & Images**: Classified and analyzed
- **Language Info**: HTML lang, hreflang alternatives
- **Crawl Metadata**: Timing, JavaScript execution status
- **DOM Analysis**: Changes between original and rendered HTML

## GEO-Specific Features

The crawler is optimized for geographic content extraction:

- Location coordinates from Schema.org
- Address information normalization
- Place and business data extraction
- Breadcrumb navigation analysis
- FAQ extraction for location-based queries
- Contact information parsing

## Configuration

Key configuration options in `GEOCrawler`:

- `timeout`: Page load timeout (default: 60 seconds)
- `delay_before_return`: Wait time after page load (default: 3 seconds)
- `js_code`: Custom JavaScript execution for dynamic content

## Requirements

- Python 3.7+
- crawl4ai
- aiohttp
- beautifulsoup4


