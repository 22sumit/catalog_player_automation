from libs import config


class CatalogPageData:

    hotLaunchSourceId = config.get_default("hotLaunchSourceId")
    hotLaunchSourceIds = config.get_default("hotLaunchSourceIds")
    test_catalogPage_data=[{"hlsId":hotLaunchSourceId}, {"hlsId":hotLaunchSourceIds}]
    test_catalogPage_data_1 = [{"hlsId": hotLaunchSourceId}]