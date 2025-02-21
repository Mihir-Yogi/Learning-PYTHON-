from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.5vovg.mongodb.net/", tlsAllowInvalidCertificates=True)

db = client["Ytmanager"]
video_collection = db["Ytmanager"]

def list_all_videos():
    for video in video_collection.find():
        print("*" * 30)
        print(f"Id: {video["_id"]} \nName: {video["name"]} \nDuration: {video["time"]}")
        print("*" * 30)

def add_video():
    print("=" * 50)
    name = input("Enter Your video name: ")
    time = input("Enter Your video Duration: ")
    video_collection.insert_one({"name": name, "time": time})
    print("=" * 50)

def update_video():
    list_all_videos()
    print("=" * 50)
    id = ObjectId(input("Enter Id to Update: "))
    new_name = input("Enter New name: ")
    new_time = input("Enter New duration: ")
    video_collection.update_one({"_id": id},{"$set": {"name": new_name, "time": new_time}})
    print("=" * 50)

def delete_video():
    list_all_videos()
    print("=" * 50)
    id = ObjectId(input("Enter Id to Delete: "))
    video_collection.delete_one({"_id": id})
    print("=" * 50)

def main():
    while True:
        print("=" * 50) 
        print("Youtube Manager")
        print("1. List all Videos Details")
        print("2. Save video")
        print("3. Update video")
        print("4. Delete video")
        choice = input("Enter your choice: ")
        print("=" * 50) 

        match choice:
            case "1":
                list_all_videos()
            case "2":
                add_video()
            case "3":
                update_video()
            case "4":
                delete_video()
            case "5":
                break
            case __:
                print("Invalid choice!")

if __name__ == "__main__":
    main()