from webdriver_manager.download_manager import DefaultDownloadManager
from webdriver_manager.driver_cache import DriverCache
from webdriver_manager.logger import log


class DriverManager(object):
    def __init__(self, root_dir=None, cache_valid_range=1, download_manager=None):
        self.driver_cache = DriverCache(root_dir, cache_valid_range)
        self.download_manager = download_manager
        if download_manager is None:
            self.download_manager = DefaultDownloadManager()
        print()  # this is just to make log output a better
        log("====== WebDriver manager ======")

    def install(self):
        raise NotImplementedError("Please Implement this method")

    def _get_driver_path(self, driver):
        binary_path = self.driver_cache.find_driver(driver)
        if binary_path:
            return binary_path

        file = self.download_manager.download_file(driver.get_url(), driver.ssl_verify)
        binary_path = self.driver_cache.save_file_to_cache(driver, file)
        return binary_path
