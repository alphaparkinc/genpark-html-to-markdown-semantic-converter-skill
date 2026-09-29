"""HTML to Markdown Semantic Converter.
100% Python Standard Library.
"""

import re

class HTMLToMarkdownConverter:
    """Converts HTML markup into clean structured Markdown for LLM agent context."""
    @staticmethod
    def convert(html_str):
        text = re.sub(r'<(script|style)\b[^>]*>.*?</\1>', '', html_str, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<h1\b[^>]*>(.*?)</h1>', r'\n# \1\n', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<h2\b[^>]*>(.*?)</h2>', r'\n## \1\n', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<h3\b[^>]*>(.*?)</h3>', r'\n### \1\n', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<strong\b[^>]*>(.*?)</strong>|<b\b[^>]*>(.*?)</b>', r'**\1\2**', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<em\b[^>]*>(.*?)</em>|<i\b[^>]*>(.*?)</i>', r'*\1\2*', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<a\b[^>]*href=["']([^"']*)["'][^>]*>(.*?)</a>', r'[\2](\1)', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<li\b[^>]*>(.*?)</li>', r'\n- \1', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<p\b[^>]*>(.*?)</p>', r'\n\1\n', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<code\b[^>]*>(.*?)</code>', r'`\1`', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<[^>]+>', '', text)
        lines = [line.strip() for line in text.split('\n')]
        return '\n'.join([line for line in lines if line])
