import functools

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.exceptions import abort

from my_app.database.actions import fetch_contract
from my_app.database.adapter import contract_from_db
from my_app.database.app_integration import get_db

bp = Blueprint("contract", __name__, url_prefix="/contract")


@bp.route("/<int:id>", methods=(["GET"]))
def view(id: int):
    contract = fetch_contract(get_db(), id)

    if contract is None:
        abort(404, f"Contract id {id} does not exist.")

    contract = contract_from_db(contract)
    return render_template("contract.html", contract=contract)
