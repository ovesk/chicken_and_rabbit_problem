from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <h1>This app solves the Chinese chicken and rabbit problem</h1>
        <p>Please hit the URL to get solution.</p>
        URL: <a href="/chicken_and_rabbit/">chicken_and_rabbit</a>
        <p><b>params:</b> <i>head_count</i> & <i>leg_count</i> <br> head_count & leg_count default is 0</p>
        <p><b>Note:</b>For invalid conditions the api returns <i>null</i> for both rabbits and chickens.</p>
    </html>
    """


@app.get("/chicken_and_rabbit/")
def read_head_and_legs(head_count: int = 0, leg_count: int = 0):
    no_of_rabbits = None
    no_of_chicken = None
    if leg_count % 2 == 0 and head_count != 0 and head_count < leg_count:
        no_of_rabbits = int((leg_count + (-2 * head_count)) / 2)
        no_of_chicken = int(head_count - no_of_rabbits)
    return {"rabbits": no_of_rabbits, "chicken": no_of_chicken}
