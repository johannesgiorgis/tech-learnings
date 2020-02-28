from pypi_org.services import package_service
from pypi_org.viewmodels.shared.viewmodelbase import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()

        self.releases = package_service.get_latest_releases()
        self.package_count = package_service.get_latest_releases()
        self.release_count = package_service.get_latest_releases()
        self.user_count = package_service.get_latest_releases()
