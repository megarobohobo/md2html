import markdown2
import sys
import os

# Uses a direct link for CSS but also forces local style override to guarantee the column layout
WRAPPER = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MD Viewer</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css@5/github-markdown-dark.css">
    <style>
        /* Force a layout that allows for a sticky TOC sidebar */
        html, body {{
            background-color: #0d1117 !important;
            margin: 0 !important;
            padding: 0 !important;
            display: flex !important;
            justify-content: center;
            align-items: flex-start;
            color: #c9d1d9 !important;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
        }}
        
        /* Table of Contents sidebar */
        .toc {{
            position: sticky;
            top: 0;
            max-height: 100vh;
            overflow-y: auto;
            width: 250px;
            padding: 45px 20px;
            box-sizing: border-box;
            border-right: 1px solid #30363d;
            background-color: #0d1117;
            font-size: 14px;
        }}

        .toc h2 {{
            font-size: 16px;
            margin-top: 0;
            color: #f0f6fc;
        }}

        .toc ul {{
            list-style: none;
            padding-left: 0;
            margin: 0;
        }}

        .toc ul ul {{
            padding-left: 15px;
        }}

        .toc a {{
            color: #8b949e;
            text-decoration: none;
            display: block;
            padding: 4px 0;
            line-height: 1.2;
        }}

        .toc a:hover {{
            color: #58a6ff;
            text-decoration: underline;
        }}

        .markdown-body {{
            box-sizing: border-box !important;
            max-width: 900px !important; /* Adjusted slightly to fit with TOC */
            width: 100%;
            margin: 0 !important;
            padding: 45px !important;
            min-height: 100vh;
            background-color: #0d1117 !important;
            color: #c9d1d9 !important;
        }}

        /* Responsive: hide TOC on small screens */
        @media (max-width: 1200px) {{
            .toc {{ display: none; }}
            .markdown-body {{ margin: 0 auto !important; }}
        }}

        /* Ensure images don't overflow the column */
        img {{ max-width: 100%; }}

        /* Add scroll margin to headers so they don't get hidden under top padding when jumping */
        .markdown-body h1, .markdown-body h2, .markdown-body h3, 
        .markdown-body h4, .markdown-body h5, .markdown-body h6 {{
            scroll-margin-top: 45px;
        }}
    </style>
</head>
<body>
    {toc_sidebar}
    <div class="markdown-body">
        {content}
    </div>
</body>
</html>"""

def convert(file_path):
    if not os.path.isfile(file_path) or not file_path.lower().endswith('.md'):
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Using 'toc' extra to generate a table of contents
    # markdown2 returns a 'UnicodeWithAttributes' object which has a 'toc_html' attribute
    html_output = markdown2.markdown(text, extras=["fenced-code-blocks", "tables", "gfm", "task_list", "toc"])
    
    toc_html = html_output.toc_html
    if toc_html:
        toc_sidebar = f'<nav class="toc"><h2>Contents</h2>{toc_html}</nav>'
    else:
        toc_sidebar = ''
        
    full_html = WRAPPER.format(content=html_output, toc_sidebar=toc_sidebar)
    
    output_path = file_path.replace('.md', '.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"Created vertical layout: {os.path.basename(output_path)}")
    os.startfile(output_path) 

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        convert(arg)