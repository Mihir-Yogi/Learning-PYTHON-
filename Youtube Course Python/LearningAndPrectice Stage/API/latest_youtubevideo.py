import requests
import json
import re

def api_handling():
    url = "https://api.freeapi.app/api/v1/public/youtube/videos?page=1&limit=10&query=javascript&sortBy=keep%20one%3A%20mostLiked%20%7C%20mostViewed%20%7C%20latest%20%7C%20oldest"
    response = requests.get(url)
    super_data = response.json()
    if super_data["success"]:
        data = super_data["data"]
        youtube_details = data["data"]
        latest_video_details = youtube_details[0]
        title = latest_video_details["items"]["snippet"]["title"]
        duration = latest_video_details["items"]["contentDetails"]["duration"]
        views = latest_video_details["items"]["statistics"]["viewCount"]
        formatted_duration = duration_format(duration)
        return title,views,formatted_duration
    else:
        raise Exception("Data is not Fetched!")

def duration_format(duration):
    pattern = re.compile(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d)S)?')
    match = pattern.match(duration)

    hours = int(match.group(1)) if match.group(1) else 0
    minutes = int(match.group(2)) if match.group(2) else 0
    seconds = int(match.group(3)) if match.group(3) else 0

    formatted_duration = f"{hours}h {minutes}m {seconds}s".strip()
    return formatted_duration.replace("0h ", "").replace(" 0m", "").replace(" 0s", "")

def main():
    try:
        title,views,formatted_duration = api_handling()
        print("*" * 50)
        print(f"Title: {title} \nViews: {views} \nDuration: {formatted_duration}")
        print("*" * 50)
    except:
        print("Error!")

if __name__ == "__main__":
    main()