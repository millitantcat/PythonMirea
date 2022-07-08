import re


def main(source):
    a1 = []
    s1 = []
    source = source.replace('#', "")
    source = source.replace('||', "")
    source = source.replace('.', "")
    source = source.replace('==>', "")
    source = source.replace("global", "")

    p = r"[-+]?\w+"
    matches = re.findall(pattern=p, string=source)
    response = {}
    matches.reverse()

    for i in range(len(matches)):
        arr = []
        if re.match(r"[-+]?\d+", matches[i]) is None:
            j = i + 1
            while j < len(matches) and re.match(r"[-+]?\d+",
                                                matches[j]) is not None:
                arr.append(int(matches[j]))
                j += 1
            arr.reverse()
            response[matches[i]] = arr
    return dict(reversed(list(response.items())))


print(main('|| (global #1105 ==>q(qube) ). ( global #-6421==> q(esaten) ).(global #-268 ==> q(adier)). ( global #-6362 ==> q(raarce_69)). ||'))

"""
import re


def main(source):
    source = source.replace(".do", "")
    source = source.replace(".end", "")
    source = source.replace("variable", "")
    p = r"[-+]?\w+"
    matches = re.findall(pattern=p, string=source)
    response = {}
    for i in range(len(matches)):
        if re.match(r"[-+]?\d+", matches[i]) is not None:
            continue
        response[matches[i]] = int(matches[i-1])
    return response


print(main(".do <% variable 775 -> `ususus; %>; <% variable 752 ->`isan_379;%>;"
           "<% variable -9498 ->`inar; %>;<% variable -4052 -> `isquor; %>; .end"))
"""
"""
import re


def main(source):
    source = source.replace("{", "")
    source = source.replace("}", "")
    source = source.replace("<<", "")
    source = source.replace(">>", "")
    source = source.replace("make", "")
    p = r"[-+]?\w+"
    matches = re.findall(pattern=p, string=source)
    response = {}
    for i in range(len(matches)):
        j = i + 1
        arr = []
        if re.match(r"[-+]?\d+", matches[i]) is not None:
            continue
        while j < len(matches) and re.match(r"[-+]?\d+", matches[j]) is not None:
            arr.append(int(matches[j]))
            j += 1
        response[matches[i]] = arr
    return response


print(main("{ <<make bece_692 :{ -1623 -1202 }>>, << make erzaat_509 :{7029 1646-841 } >>, "
           "<<make onus: { -3357 -9883 -5039}>>, }"))"""