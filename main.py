import re
import xml.etree.ElementTree as ET


def remove_clip_path_attributes(svg_path: str, output_path: str):
    # 名前空間の処理
    ET.register_namespace("", "http://www.w3.org/2000/svg")

    tree = ET.parse(svg_path)
    root = tree.getroot()

    clip_path_pattern = re.compile(r"url\(#clipPath\d+\)")

    for elem in root.iter():
        clip_path = elem.attrib.get("clip-path")
        if clip_path and clip_path_pattern.fullmatch(clip_path):
            del elem.attrib["clip-path"]

    tree.write(output_path, encoding="utf-8", xml_declaration=True)


# 使用例
remove_clip_path_attributes("山口県.svg", "山口県_no_clip.svg")
