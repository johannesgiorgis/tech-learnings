import flask

from pypi_org.infrastructure import cookie_auth
from pypi_org.infrastructure.view_modifiers import response
import pypi_org.services.package_service as package_service
from pypi_org.viewmodels.packages.pagedetails_viewmodel import PackageDetailsViewModel

blueprint = flask.Blueprint("packages", __name__, template_folder="templates")


@blueprint.route("/project/<package_name>")
@response(template_file="packages/details.html")
def package_details(package_name: str):
    vm = PackageDetailsViewModel()
    if not vm.package:
        return flask.abort(status=404)

    return vm.to_dict()


@blueprint.route("/<int:rank>")
def popular(rank: int):
    return f"The details for the {rank}th most popular package"
