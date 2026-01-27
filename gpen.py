



#json filelist with link

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, FileResponse
import os
from urllib.parse import quote

app = FastAPI(title="Video Folder API")

BASE_URL = "https://10.176.17.178:8000"

# Folder containing video files
FOLDER_PATH = input("enter path") # Change to your folder path

@app.get("/")
def read_root():
    return {"message": "Video Folder API is running!"}

@app.get("/videos")
def list_videos():
    try:
        if not os.path.exists(FOLDER_PATH):
            raise HTTPException(status_code=404, detail="Folder not found")
        
        files = os.listdir(FOLDER_PATH)
        # Make sure this is a list, not a set
        video_files = [f for f in files if f.lower().endswith((".mp4", ".mov", ".avi", ".mkv"))]

        video_list = []
        for f in video_files:
            display_name = f.replace("_", " ")
            link = f"{BASE_URL}/videos/{quote(f)}"
            video_list.append({ display_name : link})
        
        return {"videos": video_list}  # ✅ JSON-serializable

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/videos/{filename}")
def get_video(filename: str):
    file_path = os.path.join(FOLDER_PATH, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(file_path, media_type="video/mp4", filename=filename)

if __name__ == "__main__":
    import uvicorn
    #uvicorn.run(app, host="10.176.17.178", port=8000)            # uvicorn filename:app --host 127.0.0.1 --port 8000
    uvicorn.run(
        app,                 
        port=8000,
        host="10.176.17.178",
        ssl_keyfile="key.pem",
        ssl_certfile="cert.pem"
    )



