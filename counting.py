from collections import Counter

urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]

def get_file_name(urls):
    if not urls:
        return None
    filenames = []
    for url in urls:
        filenames.append(url.split('/')[-1])
    return filenames

def get_count(names_list):
    c = Counter(names_list)
    commons = c.most_common(3)
    for common in commons:
        print(common[0] + ' ' + str(common[1]))

if __name__ == "__main__":
    names_list = get_file_name(urls)
    get_count(names_list)
