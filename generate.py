import sys
import os
import re
import zipfile
import json

import urllib.request as request


def main(argv):
    getFileFromServer()
    foo = getFileList()
    filepath = "cache/extract/base16-shell-master/scripts"
    colorInfo = []
    for fileName in getFileList():
        with open(filepath + "/" + fileName) as f:
            content = f.readlines()
            dic = dict()
            dic["name"] = fileName[:-3]
            dic.update(getColorInfo(content))
            colorInfo.append(dic)
    jsonString = json.dumps(colorInfo, indent=4, separators=(',', ':'))
    schemesFile = open("schemes.json", "w")
    schemesFile.write(jsonString)
    schemesFile.close()
    print("🎉 Compelete!")


def getFileFromServer(force=False, url="https://github.com/chriskempson/base16-shell/archive/master.zip"):
    if not os.path.exists("cache"):
        os.mkdir("cache")
    if not os.path.exists("cache/master.zip") or force:
        print("🚀 Downloading implementation from remote server...")
        request.urlretrieve(url, "cache/master.zip")
        print("🎉 Download compeleted.")
    unZipFile()


def unZipFile():
    zipFile = zipfile.ZipFile("cache/master.zip")
    if os.path.isdir("cache/extract"):
        pass
    else:
        os.mkdir("cache/extract")
    print("🤐 Unzipping implementation...")
    for names in zipFile.namelist():
        zipFile.extract(names, "cache/extract")
    zipFile.close()
    print("🎉 Unzip compeleted.")


def getFileList():
    return os.listdir("cache/extract/base16-shell-master/scripts")


def getColorInfo(l: list):
    # Oh my shit code!!!
    dirtyColorInfo = list(filter(lambda x: re.match(r"color.*=", x), l))
    dirtyColorInfo = dict(map(lambda x: x.split("="), dirtyColorInfo))

    colorNamePrefix = "color"
    for i in range(16):
        if i < 10:
            getColorHex(dirtyColorInfo, colorNamePrefix + "0" + str(i))
        else:
            getColorHex(dirtyColorInfo, colorNamePrefix + str(i))
    getColorHex(dirtyColorInfo, "color_foreground")
    getColorHex(dirtyColorInfo, "color_background")
    for i in range(16):
        if i < 10:
            getColorRef(dirtyColorInfo, colorNamePrefix + "0" + str(i))
        else:
            getColorRef(dirtyColorInfo, colorNamePrefix + str(i))
    getColorRef(dirtyColorInfo, "color_foreground")
    getColorRef(dirtyColorInfo, "color_background")

    cleanColorInfo = dict()
    cleanColorInfo["black"] = dirtyColorInfo["color00"]
    cleanColorInfo["red"] = dirtyColorInfo["color01"]
    cleanColorInfo["green"] = dirtyColorInfo["color02"]
    cleanColorInfo["yellow"] = dirtyColorInfo["color03"]
    cleanColorInfo["blue"] = dirtyColorInfo["color04"]
    cleanColorInfo["magenta"] = dirtyColorInfo["color05"]
    cleanColorInfo["cyan"] = dirtyColorInfo["color06"]
    cleanColorInfo["white"] = dirtyColorInfo["color07"]
    cleanColorInfo["brightBlack"] = dirtyColorInfo["color08"]
    cleanColorInfo["brightRed"] = dirtyColorInfo["color09"]
    cleanColorInfo["brightGreen"] = dirtyColorInfo["color10"]
    cleanColorInfo["btightYellow"] = dirtyColorInfo["color11"]
    cleanColorInfo["brightBlue"] = dirtyColorInfo["color12"]
    cleanColorInfo["brightMagenta"] = dirtyColorInfo["color13"]
    cleanColorInfo["brightCyan"] = dirtyColorInfo["color14"]
    cleanColorInfo["brightWhite"] = dirtyColorInfo["color15"]
    cleanColorInfo["background"] = dirtyColorInfo["color_background"]
    cleanColorInfo["foreground"] = dirtyColorInfo["color_foreground"]
    cleanColorInfo["selectionBackground"] = dirtyColorInfo["color_foreground"]
    return cleanColorInfo


def getColorHex(dic, name):
    if re.match(r"\$.*", dic[name]):
        pass
    else:
        hex = dic[name].split("\"")[1].split("/")
        dic[name] = "#" + hex[0] + hex[1] + hex[2]


def getColorRef(dic, name):
    if re.match(r"\$.*", dic[name]):
        dic[name] = dic[dic[name][1:8]]


if __name__ == "__main__":
    main(sys.argv)
