from lxml import etree


def all_children(context):
    path = []
    for event, elem in context:
        if event == "start":
            path.append(elem.tag)
        else:
            print_keyval(path, elem)
            elem.clear()

            while elem.getprevious() is not None:
                if elem.getparent() is not None:
                    del elem.getparent()[0]
                else:
                    break
    del context


def print_keyval(path, elem):
    if elem is not None and elem.text is not None and elem.text.strip() != "":
        print(".".join(path) + "==" + elem.text.strip())
    try:
        path.pop()
    except IndexError:
        pass


if __name__ == "__main__":
    source = "./en.xml"

    # iterable context
    context = etree.iterparse(source, events=("start", "end",))
    # converted to iterator
    context = iter(context)
    event, root = next(context)  # to skip the parent tag

    all_children(context)
