import re
import subprocess as sb

def replace_url_in_html(file_path, new_url):
    # HTMLファイルを読み込み
    with open(file_path, 'r') as file:
        html_content = file.read()

    # URLを置き換え
    #new_html_content = re.sub(r'https://[a-zA-Z0-9\-\.]+', new_url, html_content)
    #new_html_content = re.sub(r'https[^"]+', new_url, html_content)
    new_html_content = re.sub(r'(?<=URL=)([^"]+)', new_url, html_content)

    #print(new_url)

    # 置き換えたHTMLを書き込み
    #print(new_html_content)
    with open(file_path, 'w') as file:
        file.write(new_html_content)

if __name__ == "__main__":
    # 置き換えたいURL
    command = "curl -s localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url'"
    response = sb.run(command, shell=True, capture_output=True, text=True)
    new_url = response.stdout.split()[0]
    #new_url = "https://example.com"

    # 置き換えたいHTMLファイルのパス
    html_file_path = "index.html"

    # URLをHTMLファイル内で置き換える
    replace_url_in_html(html_file_path, new_url)

