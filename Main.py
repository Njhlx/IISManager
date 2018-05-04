import IISManager
import ConstSettings
ConstSettings.define()


def main():
    print("Begin")
    print("--------------------------------------------------------")
    site_name = "yxs test site"
    IISManager.create_app_pool(site_name)
    IISManager.set_app_pool_recycling_periodic_restart_schedule(site_name, '03:00:00')
    IISManager.create_site(site_name, 1234, "C:\TestSite")
    IISManager.set_site_app_pool(site_name, site_name)
    IISManager.set_site_auto_start(site_name)
    print("--------------------------------------------------------")
    print("End")
    input("\n\nPress the enter key to exit.")


if __name__ == "__main__":
    main()
