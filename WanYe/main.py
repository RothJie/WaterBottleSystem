from SelfDefineTool import *
import webbrowser


def run():
    web_page = decorator()
    p_label = p()
    all_p = ""
    for uni in open("Contents.txt", mode="r", encoding="utf-8").readlines():
        all_p += p_label(uni)
    content = web_page(all_p)
    with open("沉浸翻译.html", mode="w", encoding="utf-8") as f:
        f.write(content)


if __name__ == '__main__':
    run()
    webbrowser.open("沉浸翻译.html")