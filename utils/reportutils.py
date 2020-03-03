import subprocess

def test_report():
    subprocess.Popen("cd C://mdms//git//catalog_player_automation//reports && C:/Personal/Softwares/allure-2.13.1/bin/allure generate C://mdms//git//catalog_player_automation//reports --clean && allure open allure-report",shell=True)


# def test_report_MR90():
#     subprocess.Popen("cd C://mdms//git//catalog_player_automation//reports/MR90 && C:/Personal/Softwares/allure-2.13.1/bin/allure generate C://mdms//git//catalog_player_automation//reports/MR90 --clean && allure open allure-report",shell=True)


# def test_report_general():
#     date = datetime.now()
#     dt = date.strftime("%Y%m%d%H%M%S")
#     report = "Report" + dt
#     print(report)
#     reportpath="..//reports//"+report
#
#     if not os.path.exists(reportpath):
#         os.mkdir(reportpath)
#         print("Directory ", reportpath, " Created ")
#     else:
#         print("Directory ", reportpath, " already exists")
#
#     command="cd C://mdms//git//catalog_player_automation//reports//"+report+ " && C:/Personal/Softwares/allure-2.13.1/bin/allure generate C://mdms//git//catalog_player_automation//reports//"+report+" --clean && allure open allure-report"
#     print("Command:",command)
#     subprocess.Popen(command, shell=True)
#
# test_report()
