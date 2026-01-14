def highlight_python(code):
    """
    Returns HTML with basic Python syntax highlighting using <span> tags.
    Very basic: keywords, strings, comments.
    """
    import html
    code = html.escape(code)
    
    # Basic keyword highlighting
    keywords = ["def", "return", "if", "else", "elif", "for", "while", "import", "from", "as", "try", "except", "class"]
    for kw in keywords:
        code = code.replace(kw, f'<span class="keyword">{kw}</span>')

    # Strings
    import re
    code = re.sub(r'(\".*?\"|\'.*?\')', r'<span class="string">\1</span>', code)

    # Comments
    code = re.sub(r'(#.*?$)', r'<span class="comment">\1</span>', code, flags=re.MULTILINE)

    return code
