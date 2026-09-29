from client import HTMLToMarkdownConverter

html = "<h1>Release Notes</h1><p>Version 2.0 adds <b>fast</b> <a href='https://alphapark.org'>tools</a>.</p>"
print("Converted Markdown:\n" + HTMLToMarkdownConverter.convert(html))
