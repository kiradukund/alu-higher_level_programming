#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements
print(sorted(common_elements({"Python","C","Javascript"}, {"Bash","C","Ruby","Perl"})))
