import argparse
import uvicorn

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--host", default="0.0.0.0")
    p.add_argument("--port", type=int, default=8000)
    p.add_argument("--card-url", default=None)
    args = p.parse_args()

    uvicorn.run("app.server:app", host=args.host, port=args.port)

if __name__ == "__main__":
    main()