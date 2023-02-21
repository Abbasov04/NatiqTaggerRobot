# @AylinRobot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə Oğlum

# @TheXWarn - < https://t.me/TheXWarn >
# Copyright (C) 2022
#
# Bu fayl, < https://github.com/TheXWarn/LuksTagBot >'un parçasıdır.
# Zəhmət olmasa, GNU Affero Ümumi İctimai Lisenziyasını oxuyun;
# < https://www.github.com/TheXWarn/LuksTagBot/blob/master/LICENSE/ >
#
#  Repodan nəsə əkib başqasına verən kimliyindən aslı olmayaraq peysərdi. # 

from client import *

def __list_all_modules():
    from os.path import dirname, basename, isfile
    import glob

    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [
        basename(f)[:-3] for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    return all_modules


ALL_MODULES = sorted(__list_all_modules())
print("Yüklənəcək modullar: ", str(ALL_MODULES))
__all__ = ALL_MODULES + ["ALL_MODULES"]
