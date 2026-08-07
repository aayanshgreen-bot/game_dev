import os

def split_file(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract CSS
    style_start = content.find('<style>')
    style_end = content.find('</style>')
    if style_start != -1 and style_end != -1:
        css_content = content[style_start + 7:style_end].strip()
        html_without_css = content[:style_start] + '<link rel="stylesheet" href="{{ url_for(\'static\', filename=\'css/style.css\') }}">\n' + content[style_end + 8:]
    else:
        css_content = ''
        html_without_css = content

    # Extract JS
    script_start = html_without_css.find('<script>')
    script_end = html_without_css.rfind('</script>')
    if script_start != -1 and script_end != -1:
        js_content = html_without_css[script_start + 8:script_end].strip()
        html_final = html_without_css[:script_start] + '<script src="{{ url_for(\'static\', filename=\'js/app.js\') }}"></script>\n' + html_without_css[script_end + 9:]
    else:
        js_content = ''
        html_final = html_without_css

    # Create directories
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    os.makedirs('templates', exist_ok=True)

    # Write CSS
    with open('static/css/style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)

    # Write JS
    with open('static/js/app.js', 'w', encoding='utf-8') as f:
        f.write(js_content)

    # Write HTML
    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write(html_final.strip())

    print("Splitting completed.")

if __name__ == '__main__':
    split_file('cryptix-games (1).html')
