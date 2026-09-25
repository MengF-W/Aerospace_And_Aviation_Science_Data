# def
import requests
import re
from typing import List
from nasaApp.serializers import APODSerializer


class ApodServices:
    @staticmethod
    def get_apod_basic() -> List:
        result = requests.get("https://science.nasa.gov/wp-json/wp/v2/apod-basic")
        result_item_list = []

        for item in result.json():

            match item["media_type"]:
                case "image":
                    item["media_location"] =  re.findall('<IMG SRC=.*.jpg\"', item["basic_html"])[0] + "alt="+ item["alt"] + " width=\"200\" height=\"300\">"
                case "video":
                    item["media_location"] = re.findall('<source src=.*.mp4', item["basic_html"])[0] + "\">"

            serializer = APODSerializer(data=item)
            if serializer.is_valid():
                serializer.save()
            apod = serializer.data

            result_item_list.append(apod)

        return result_item_list