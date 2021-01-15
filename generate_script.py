#!/usr/bin/python3
import re
import csv
import sys


def main():
    script = 'urlMatch = "https?:\/\/(.*\.)?('
    file_name = sys.argv[1]
    with open(file_name, "r", encoding="latin1") as csvfile:
        try:
            reader = csv.reader(csvfile, delimiter=";")
            row_list = list(reader)
        except UnicodeError:
            reader = csv.reader(csvfile, delimiter=";")
            row_list = list(reader)
        index = 0
        while not "Firmanavn" in row_list[index][0]:
            index += 1
        first = True
        while True:
            index += 1
            try:
                website = clean_website(row_list[index][2])
                if website:
                    if not first:
                        script += "|"
                    script += website
                    # print(website)
                if first:
                    first = False
            except IndexError:
                break
    script += ')(\/.*)?"; browser.tabs.onUpdated.addListener(function(tabId,changeInfo,tab){if(tab.url.match(urlMatch)){browser.pageAction.show(tabId);}});'
    print(script)


def clean_website(string):
    # Some lines have trailing slashes, other not
    string = string.strip("/").strip(".")
    # Some lines have an email address instead of web site address
    if "@" in string:
        return False
    # Some lines are just not valid addresses
    if not "." in string:
        return False
    return re.escape(string)


if __name__ == "__main__":
    main()
