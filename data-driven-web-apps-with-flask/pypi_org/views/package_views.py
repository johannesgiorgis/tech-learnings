import flask

from pypi_org.infrastructure.view_modifiers import response
import pypi_org.services.package_service as package_service

blueprint = flask.Blueprint("packages", __name__, template_folder="templates")


@blueprint.route("/project/<package_name>")
# @response(template_file="home/index.html")
def package_details(package_name: str):
    return f"Package details for {package_name}"


@blueprint.route("/<int:rank>")
def popular(rank: int):
    return f"The details for the {rank}th most popular package"
