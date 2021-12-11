import logging

from flask import Flask, jsonify, request
from factorial import factorial as factorial_func


logger = logging.getLogger('api')

logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('logfile.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


app = Flask(__name__)
# maths = MathsFunc()

# Just a health check
@app.route("/")
def url_root():
    return "OK"

# Just a health check
@app.route("/_health")
def url_health():
    return "OK"

# # e.g. http://127.0.0.1:5000/factorial?value=10
@app.route("/factorial")
def url_factorial():
    try:
        val = request.args.get("value")
        factorial = factorial_func(int(val))
    except Exception as e:
        logger.error(str(e))
        res = {
            "function": "factorial",
            "input": val,
            "output": "error occured",
        }
        return jsonify(res), 400
    else:
        logger.info("Succesfully ran the factorial function")
        res = {
            "function": "factorial",
            "input": val,
            "output": factorial,
            }
        return jsonify(res), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)