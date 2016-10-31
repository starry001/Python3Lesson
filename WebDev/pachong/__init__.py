import re
import sys
import time
import threading
import requests


class Archives(object):
    def save_links(self, url):
        try:
            data = requests.get(url, timeout=3)
            'response'
            content = data.text
            link_pat = '"(ed2k://\|file\|[^"]+?\.(S\d+)(E\d+)[^"]+?1024X\d{3}[^"]+?)"'
            name_pat = re.compile(r'<h2 class="entry_title">(.*?)</h2>', re.S)

            links = set(re.findall(link_pat, content))
            name = re.findall(name_pat, content)

            links_dict = {}
            count = len(links)
        except Exception as  e:
            print('e1:', e)
            pass

        for i in links:
            print(i)
            # print(int(i[1][1:3]))
            links_dict[int(i[1][1:3]) * 100 + int(i[2][1:3])] = i  # 把剧集按s和e提取编号

        try:
            with open(name[0].replace('/', ' ') + '.txt', 'w') as f:
                for i in sorted(list(links_dict.keys())):  # 按季数+集数排序顺序写入
                    f.write(links_dict[i][0] + '\n')
                    # print('Get links ... ', name[0], count)
        except Exception:
            print('e2:', e)
            pass

    def get_url(self):
        try:
            for i in range(2025, 2050):
                base_url = 'http://cn163.net/archives/'
                url = base_url + str(i) + '/'

                if requests.get(url).status_code == 404:
                    continue
                else:
                    self.save_links(url)
        except Exception:
            pass

    def main(self):
        thread1 = threading.Thread(target=self.get_url())
        thread1.start()
        thread1.join()


if __name__ == '__main__':
    start = time.time()
    a = Archives()
    a.main()
    end = time.time()
    print('total time :', end - start, 's')
