import sqlite3

conn = sqlite3.connect("Youtubedb.db")

cursor = conn.cursor()

cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS videos (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
                )
''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for videos in cursor.fetchall():
        print(f"{videos[0]} : name: {videos[1]}, Duration: {videos[2]} ")
    conn.commit()

def add_video(video, time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?, ?) ", (video, time))
    conn.commit()
    print("*" * 50)
    print("Video Details has been added successfully!")

def update_video(video_id, new_video, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_video, new_time, video_id))
    conn.commit()
    print("*" * 50)
    print("Video Details has been Updated successfully!")

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id, ))
    print("*" * 50)
    print("Video Details has been Deleted successfully!")
    conn.commit() 

def main():
    while True:
        print("\n")
        print("*" * 50)
        print("Youtube Management App with DB")
        print("1. List all videos detail")
        print("2. Add video")
        print("3. update video")
        print("4. delete video")
        print("5. Exit")
        option = int(input("Enter Your choice: "))

        if option == 1:
            list_all_videos()
        elif option == 2:
            video = input("Enter video name: ")
            time = input("Enter video duration: ")
            add_video(video, time)
        elif option == 3:
            list_all_videos()
            video_id = input("Enter index of video that you want to update: ")
            video = input("Enter video name: ")
            time = input("Enter video duration: ")
            update_video(video_id, video, time)
        elif option == 4:
            print("*" * 50)
            list_all_videos()
            print("*" * 50)
            video_id = input("Enter video index you want to delete: ")
            delete_video(video_id)
        elif option == 5:
            break
        else:
            print("Invalid option, Please try again!")
            
    conn.close()

if __name__ == "__main__":
    main()

