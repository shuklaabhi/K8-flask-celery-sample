from flask import jsonify

from katana import app

import katana.tasks.math as math

@app.route("/api/v1/accounts")
def get_accounts():
    summedup_value = math.add.delay(2,4).wait()
    return jsonify(dict(code="account_success", data=[{"name":"aal", "status":"lla"}, {"name" : "kali", "status" :  "aaa"}], sum=summedup_value))