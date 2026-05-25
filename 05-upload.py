from fastapi import FastAPI, File, UploadFile
import uvicorn

app = FastAPI()

@app.post("/uploadfile")
def create_upload_file(file: bytes= File(description="以字节形式读取的文件")):
    return {"file_size": len(file)}

@app.post("/uploadfile1")
async def create_upload_file(file: UploadFile = File(description="作为UploadFile读取的文件")):
    return {"filename": file.filename, "content_type": file.content_type}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)