# Maintainer Note
# @xLexip 2021

def FullOTA_Assertions(info):
    OTA_MaintainerSection(info)
    return

def IncrementalOTA_Assertions(info):
    OTA_MaintainerSection(info)
    return

def OTA_MaintainerSection(info):
    info.script.AppendExtra('ui_print("            LIGMA           -");')
