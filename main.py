from script import DN_API

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/search')
def search():
    qs = request.args.get('q')
    search_result = DN_API.search(qs)
    return jsonify({
        "status": 200,
        "data": search_result,
        "length": len(search_result)
    }), 200


if __name__ == "__main__":
    app.run(debug=True)