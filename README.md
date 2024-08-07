Conda activate base
uvicorn main:app --host 0.0.0.0 --port 8000
Nohup uvicorn main:app --host 0.0.0.0 --port 8000(백그라운드 실행)

새로운 쉘: ps -ef | grep uvicorn

code nohup.out: 


http://127.0.0.1:8000/redoc

http://127.0.0.1:8000/docs
