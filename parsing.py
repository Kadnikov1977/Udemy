from bs4 import BeautifulSoup
html_string = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Web Development Page</title>
        <style type="text/css">
            
            h1{
                color: white;
                background: red;
            }
    
            li{
                color: red;
            }
    
            #css-li{
                color: blue;
            }
    
            .green{
                color: green;
            }
    
        </style>
    </head>
    <body>
        <h1>Web Development</h1>
        <h1 class="green">Web</h1>
        <h3>Programming Languages</h3>
    
        <ol>
            <li>HTML</li>
            <li id="css-li">CSS</li>
            <li class="green">JavaScript</li>
            <li class="green">Python</li>
        </ol>
    
    </body>
    </html>
"""
parsed_html = BeautifulSoup(html_string, 'html.parser') # html.parser - указываем что будем парсить html, также можно парсить xml
# print(parsed_html) # текс превратился в объект
# print(type(parsed_html))
# print(parsed_html.body.h1)
# print(parsed_html.body.ol.li)
list = parsed_html.find_all('li')
for i in list:
    print(i.get_text())
print(parsed_html.select('.green'))