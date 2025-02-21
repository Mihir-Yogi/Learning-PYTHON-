import json

file_name = "youtubevids.txt"
def load_data():
    try:
        with open(file_name,'r') as file:
            result = json.load(file)
            return result
    except FileNotFoundError:
        return []

def file_helper(videos):
    with open(file_name,'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("*" * 50)
    for index, video in enumerate(videos,start=1):
        print(f"{index}, name : {video['name']} , duration: {video['time']}")
    print("*" * 50)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video duration: ")
    videos.append({'name': name , 'time': time})
    file_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter Your Index: "))
    if 1 <= index <= len(videos):
        name = input("Enter your video name: ")
        time = input("Enter video duration: ")
        videos[index-1] = {'name' : name , 'time' : time}
        file_helper(videos)
        print("*" * 50)
        print("Data updated Successfully!")
    else:
        print("--> Wrong Index, Please try again!")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter a index: "))
    if 1 <= index <= len(videos):
        del(videos[index-1])
        print("*" * 50)
        print("video detail has been deleated successfully!")
    else:
        print("--> Wrong Index, Please try again!")

def main():
    videos = load_data()
    while True:
        print("\nYoutube Manager")
        print("1. Listout Favourite Videos")
        print("2. Add a Youtube Video")
        print("3. Update a Youtube video details")
        print("4. Delete a Youtube Video")
        print("5. Exit")
        choice = int(input("Enter Your Choice: "))
        match choice:
            case 1:
                list_all_videos(videos)
            case 2:
                add_video(videos)
            case 3:
                update_video(videos)
            case 4:
                delete_video(videos)
            case 5:
                break
            case __:
                print("Invalid Input!")


if __name__ == "__main__":
    main()