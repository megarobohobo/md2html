import markdown2
import sys
import os

# We'll use a direct link but also force a local style override to guarantee the column layout
WRAPPER = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MD Viewer</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css@5/github-markdown-dark.css">
    <style>
        /* Force a vertical document layout */
        html, body {{
            background-color: #0d1117 !important;
            margin: 0 !important;
            padding: 0 !important;
            display: block !important; /* Prevents flex-box stretching if things get weird */
        }}
        
        .markdown-body {{
            box-sizing: border-box !important;
            max-width: 1000px !important; /* Tight column */
            margin: 0 auto !important;   /* Centers the column */
            padding: 45px !important;
            min-height: 100vh;
            border-left: 1px solid #30363d;
            border-right: 1px solid #30363d;
            background-color: #0d1117 !important;
            color: #c9d1d9 !important;
        }}

        /* Ensure images don't overflow the column */
        img {{ max-width: 100%; }}
    </style>
</head>
<body>
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
    
    # Using 'gfm' (GitHub Flavored Markdown) extra for the best compatibility
    html_content = markdown2.markdown(text, extras=["fenced-code-blocks", "tables", "gfm", "task_list"])
    full_html = WRAPPER.format(content=html_content)
    
    output_path = file_path.replace('.md', '.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"Created vertical layout: {os.path.basename(output_path)}")
    os.startfile(output_path) 

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        convert(arg)