from app import create_app

app = create_app()

@app.route('/')
def health_check():
    return {"status": "online", "message": "Taskapp Backend API is running"}, 200
 
